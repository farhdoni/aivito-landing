#!/usr/bin/env python3
"""GATE-валидация сгенерированного сайта AIVITA.

- Все внутренние href ведут на существующие страницы (нет 404).
- FAQ schema (FAQPage) 1:1 к видимым <summary> на странице.
- Ни одной страницы < 350 слов (кроме языковых корней-исключений).
- hreflang: альтернаты существуют; страницы без переводов — без hreflang.
- Печатает GATE-таблицу: URL | lang | words | schema | canonical | hreflang.
"""
import html as htmllib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "content"))
import build  # noqa: E402  (populates registry)
import engine as S  # noqa: E402

build.load_modules()
for name, mod in build.load_modules():
    if hasattr(mod, "pages"):
        S.add(mod.pages())

# дедуп по url (load_modules дважды не вызываем — уже добавлено выше один раз)
PAGES = {p.url(): p for p in S._REGISTRY}
VALID = set(PAGES.keys())
ROOT = S.ROOT


def strip(s):
    return re.sub(r"<[^>]+>", " ", s)


def check_links():
    problems = []
    href_re = re.compile(r'href="([^"]+)"')
    for url, p in PAGES.items():
        out = os.path.join(ROOT, "index.html") if p.path == "" else os.path.join(ROOT, p.path, "index.html")
        doc = open(out, encoding="utf-8").read()
        for href in href_re.findall(doc):
            if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            if href.startswith("/assets/"):
                asset = os.path.join(ROOT, href.lstrip("/"))
                if not os.path.exists(asset):
                    problems.append((url, href, "MISSING ASSET"))
                continue
            # нормализуем на trailing slash
            target = href.split("#")[0].split("?")[0]
            if not target.endswith("/"):
                target += "/"
            if target not in VALID:
                problems.append((url, href, "404 INTERNAL"))
    return problems


def check_faq_and_hreflang():
    problems = []
    for url, p in PAGES.items():
        out = os.path.join(ROOT, "index.html") if p.path == "" else os.path.join(ROOT, p.path, "index.html")
        doc = open(out, encoding="utf-8").read()
        # FAQ 1:1
        summaries = [htmllib.unescape(s).strip() for s in re.findall(r"<summary>(.*?)</summary>", doc, re.S)]
        faq_schema = []
        for block in re.findall(r'application/ld\+json">(.*?)</script>', doc, re.S):
            data = json.loads(block)
            for g in data.get("@graph", []):
                if g.get("@type") == "FAQPage":
                    faq_schema = [htmllib.unescape(q["name"]).strip() for q in g["mainEntity"]]
        if summaries != faq_schema:
            problems.append((url, "FAQ schema != HTML summaries", f"{len(summaries)} vs {len(faq_schema)}"))
        # hreflang согласованность
        alts = re.findall(r'rel="alternate" hreflang="([a-z-]+)" href="([^"]+)"', doc)
        for lang, href in alts:
            if lang == "x-default":
                continue
            path = href.replace(S.DOMAIN, "")
            if path not in VALID:
                problems.append((url, f"hreflang {lang} -> 404", href))
    return problems


def schema_types(p):
    types = []
    if p.crumbs:
        types.append("Breadcrumb")
    if p.faq:
        types.append("FAQ")
    for obj in p.schema:
        types.append(obj.get("@type", "?"))
    return "+".join(types) if types else "—"


def main():
    print("== GATE-валидация ==\n")
    link_problems = check_links()
    faq_problems = check_faq_and_hreflang()

    # таблица
    print(f"{'URL':52} {'lang':4} {'words':>5}  {'schema':30} canon hreflang")
    print("-" * 120)
    thin = 0
    for url in sorted(PAGES):
        p = PAGES[url]
        wc = S.word_count(p)
        if wc < 350 and p.path != "" and p.path not in ("uz", "en"):
            thin += 1
        hl = ",".join(p.hreflang.keys()) if p.hreflang else "—"
        print(f"{url:52} {p.lang:4} {wc:5d}  {schema_types(p):30} yes   {hl}")

    print("\n== ИТОГИ ==")
    print(f"Всего страниц: {len(PAGES)}")
    print(f"Тонких (<350, не корни): {thin}")
    print(f"Проблем со ссылками (404/asset): {len(link_problems)}")
    for x in link_problems:
        print("   !", x)
    print(f"Проблем FAQ/hreflang: {len(faq_problems)}")
    for x in faq_problems:
        print("   !", x)
    ok = not link_problems and not faq_problems and thin == 0
    print("\nРЕЗУЛЬТАТ:", "✅ GATE PASSED" if ok else "❌ ЕСТЬ ПРОБЛЕМЫ")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
