"""AIVITA content-architecture generator.

Каждая страница описывается как Page(...) с уникальным контентом.
Общий каркас (шапка, футер, хлебные крошки, hreflang, JSON-LD, sitemap, llms)
собирается автоматически, чтобы гарантировать консистентность и FAQ schema = HTML 1:1.

Запуск:  python3 tools/gen/build.py
Выход:   статические <slug>/index.html в корне репозитория + sitemap.xml + llms.txt
"""
from __future__ import annotations
import html
import json
import os
import re
from dataclasses import dataclass, field
from datetime import date

DOMAIN = "https://aivita.uz"
BRAND = "AIVITA"
ORG_EMAIL = "hello@aivita.uz"
TODAY = "2026-07-11"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

LANG_NAMES = {"ru": "Русский", "uz": "O‘zbekcha", "en": "English"}
LANG_HOME = {"ru": "/", "uz": "/uz/", "en": "/en/"}

# Главная навигация по языкам (label, url-suffix относительно языкового корня)
NAV = {
    "ru": [
        ("Возможности", "/features/"),
        ("Блог", "/blog/"),
        ("Регионы", "/regions/"),
        ("Врачи", "/doctors/"),
        ("Медтуризм", "/medical-tourism/"),
        ("MedSoft", "/medsoft/"),
        ("О нас", "/about/"),
    ],
    "uz": [
        ("Imkoniyatlar", "/uz/features/"),
        ("Blog", "/uz/blog/"),
        ("Hududlar", "/uz/regions/"),
        ("Shifokorlar", "/uz/doctors/"),
        ("MedSoft", "/uz/medsoft/"),
        ("Biz haqimizda", "/uz/about/"),
    ],
    "en": [
        ("Features", "/en/features/"),
        ("Medical tourism", "/en/medical-tourism/"),
        ("About", "/en/about/"),
    ],
}

FOOTER = {
    "ru": [
        ("Возможности", [
            ("AI-чекап", "/features/ai-checkup/"),
            ("Проверка лекарств", "/features/drug-checker/"),
            ("Медкарта", "/features/medcard/"),
            ("Мониторинг здоровья", "/features/monitoring/"),
            ("SOS-помощь", "/features/sos/"),
        ]),
        ("Разделы", [
            ("Блог о здоровье", "/blog/"),
            ("Здоровый образ жизни", "/health/"),
            ("Врачи по специальностям", "/doctors/"),
            ("Регионы Узбекистана", "/regions/"),
            ("Медицинский туризм", "/medical-tourism/"),
        ]),
        ("Для кого", [
            ("Для мам", "/for/moms/"),
            ("Для всей семьи", "/for/family/"),
            ("Для врачей", "/for/doctors/"),
        ]),
        ("Бизнесу", [
            ("MedSoft для клиник", "/medsoft/"),
            ("Малым клиникам", "/medsoft/small/"),
            ("Сетям клиник", "/medsoft/network/"),
            ("О компании", "/about/"),
        ]),
    ],
    "uz": [
        ("Imkoniyatlar", [
            ("AI-checkup", "/uz/features/ai-checkup/"),
            ("Dori mosligini tekshirish", "/uz/features/drug-checker/"),
            ("Tibbiy karta", "/uz/features/medcard/"),
        ]),
        ("Bo‘limlar", [
            ("Blog", "/uz/blog/"),
            ("Shifokorlar", "/uz/doctors/"),
            ("Hududlar", "/uz/regions/"),
        ]),
        ("Biznes", [
            ("MedSoft", "/uz/medsoft/"),
            ("Biz haqimizda", "/uz/about/"),
        ]),
    ],
    "en": [
        ("Product", [
            ("Features", "/en/features/"),
            ("Medical tourism", "/en/medical-tourism/"),
        ]),
        ("Company", [
            ("About AIVITA", "/en/about/"),
        ]),
    ],
}

DISCLAIMER = {
    "ru": ("Информация на сайте носит справочный характер и не заменяет очную "
           "консультацию врача. AIVITA не ставит диагнозы и не назначает лечение — "
           "решения о вашем здоровье принимает врач."),
    "uz": ("Saytdagi ma’lumot ma’lumot uchun bo‘lib, shifokor bilan yuzma-yuz "
           "maslahatning o‘rnini bosmaydi. AIVITA tashxis qo‘ymaydi va davolashni "
           "tayinlamaydi — sog‘lig‘ingiz haqidagi qarorlarni shifokor qabul qiladi."),
    "en": ("This information is for reference only and does not replace an in-person "
           "consultation with a doctor. AIVITA does not diagnose or prescribe treatment — "
           "decisions about your health are made by a physician."),
}

UI = {
    "ru": {"read_also": "Читайте также", "home": "Главная", "faq": "Частые вопросы",
           "menu": "Меню", "updated": "Обновлено", "disclaimer_h": "Важно"},
    "uz": {"read_also": "Shuningdek o‘qing", "home": "Bosh sahifa", "faq": "Ko‘p beriladigan savollar",
           "menu": "Menyu", "updated": "Yangilangan", "disclaimer_h": "Muhim"},
    "en": {"read_also": "Read also", "home": "Home", "faq": "Frequently asked questions",
           "menu": "Menu", "updated": "Updated", "disclaimer_h": "Important"},
}


@dataclass
class Page:
    path: str                      # 'features/ai-checkup' — без начального/конечного слэша; '' = язык-корень
    lang: str                      # ru | uz | en
    title: str                     # <title> / og:title
    description: str               # meta description
    h1: str
    body: str                      # уникальный HTML контента (без h1, без FAQ, без related)
    crumbs: list = field(default_factory=list)   # [(label, url|None)], последний обычно None (текущая)
    faq: list = field(default_factory=list)       # [(вопрос, ответ_текст)] — рендер + FAQPage schema из одного источника
    related: list = field(default_factory=list)   # [(label, url)]
    schema: list = field(default_factory=list)    # доп. JSON-LD объекты (Article/Service/...)
    section: str = ""              # ключ для подсветки навигации
    hreflang: dict = field(default_factory=dict)  # {'ru':'/path/','uz':'/uz/path/','en':'/en/path/'}; пусто = без hreflang
    cta: tuple = None              # (заголовок, текст, кнопка_label, кнопка_href) или None → дефолт
    disclaimer: bool = False       # медицинский дисклеймер YMYL
    updated: str = None            # дата для Article
    og_type: str = "website"

    def url(self):
        base = "/" + self.path if self.path else ""
        return (base + "/").replace("//", "/") if self.path else "/"

    def loc(self):
        # для языковых корней path может быть 'uz' или 'en'
        return DOMAIN + self.url()


def _t(lang, key):
    return UI.get(lang, UI["ru"])[key]


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", " ", s)


def word_count(page: "Page") -> int:
    txt = strip_tags(page.body)
    for q, a in page.faq:
        txt += " " + q + " " + a
    words = re.findall(r"[\wа-яёА-ЯЎўҚқҒғҲҳ’ʼ']+", txt, flags=re.UNICODE)
    return len(words)


def _canonical(page: "Page") -> str:
    return DOMAIN + page.url()


def _hreflang_tags(page: "Page") -> str:
    if not page.hreflang or len(page.hreflang) < 2:
        return ""
    out = []
    for lang, path in page.hreflang.items():
        out.append(f'<link rel="alternate" hreflang="{lang}" href="{DOMAIN}{path}">')
    # x-default = ru
    if "ru" in page.hreflang:
        out.append(f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}{page.hreflang["ru"]}">')
    return "\n".join(out)


def _jsonld(page: "Page") -> str:
    graph = []
    # BreadcrumbList
    if page.crumbs:
        items = []
        pos = 1
        for label, href in page.crumbs:
            item = {"@type": "ListItem", "position": pos, "name": label}
            if href:
                item["item"] = DOMAIN + href
            items.append(item)
            pos += 1
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    # FAQPage из того же источника, что и видимый HTML
    if page.faq:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q,
                 "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a).strip()}}
                for q, a in page.faq
            ],
        })
    # Пользовательские объекты (Article/Service/WebPage/MedicalBusiness...)
    for obj in page.schema:
        graph.append(obj)
    if not graph:
        return ""
    doc = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(doc, ensure_ascii=False) + '</script>')


def _nav(page: "Page") -> str:
    items = NAV.get(page.lang, NAV["ru"])
    out = []
    for label, href in items:
        cur = ' aria-current="page"' if page.section and href.rstrip("/").endswith(page.section) else ""
        out.append(f'<a href="{href}"{cur}>{html.escape(label)}</a>')
    return "".join(out)


def _langswitch(page: "Page") -> str:
    out = []
    for lang in ("ru", "uz", "en"):
        target = page.hreflang.get(lang) if page.hreflang else LANG_HOME[lang]
        if not target:
            target = LANG_HOME[lang]
        cur = ' aria-current="true"' if lang == page.lang else ""
        out.append(f'<a href="{target}"{cur} hreflang="{lang}">{lang}</a>')
    return "".join(out)


def _crumbs_html(page: "Page") -> str:
    if not page.crumbs:
        return ""
    parts = []
    for i, (label, href) in enumerate(page.crumbs):
        if i:
            parts.append('<span class="sep">/</span>')
        if href:
            parts.append(f'<a href="{href}">{html.escape(label)}</a>')
        else:
            parts.append(f'<span aria-current="page">{html.escape(label)}</span>')
    return f'<nav class="crumbs wrap" aria-label="breadcrumb">{"".join(parts)}</nav>'


def _faq_html(page: "Page") -> str:
    if not page.faq:
        return ""
    rows = []
    for q, a in page.faq:
        rows.append(
            f'<details><summary>{html.escape(q)}</summary><div>{a}</div></details>'
        )
    return (f'<section class="faq"><h2>{_t(page.lang, "faq")}</h2>'
            + "".join(rows) + "</section>")


def _related_html(page: "Page") -> str:
    if not page.related:
        return ""
    cards = []
    for label, href in page.related:
        cards.append(f'<a class="card" href="{href}"><h3>{html.escape(label)}</h3>'
                     f'<span class="more">Открыть →</span></a>')
    return (f'<section class="related"><h2>{_t(page.lang, "read_also")}</h2>'
            f'<div class="grid grid-3">{"".join(cards)}</div></section>')


def _disclaimer_html(page: "Page") -> str:
    if not page.disclaimer:
        return ""
    return (f'<div class="callout disclaimer"><strong>{_t(page.lang, "disclaimer_h")}.</strong> '
            f'{html.escape(DISCLAIMER[page.lang])}</div>')


def _cta_html(page: "Page") -> str:
    if page.cta is None:
        if page.lang == "uz":
            title, text, blabel, bhref = ("Sog‘lig‘ingizni AIVITA’ga ishoning",
                "60 soniyada AI-checkupdan o‘ting, tibbiy kartangizni yuriting va onlayn shifokorga yoziling — bitta ilovada.",
                "AIVITA’ni ochish", "/uz/")
        elif page.lang == "en":
            title, text, blabel, bhref = ("Take care of your health with AIVITA",
                "Run an AI check-up in 60 seconds, keep your medical card and book a doctor online — in one app.",
                "Open AIVITA", "/en/")
        else:
            title, text, blabel, bhref = ("Позаботьтесь о здоровье вместе с AIVITA",
                "Пройдите AI-чекап за 60 секунд, ведите электронную медкарту и запишитесь к врачу онлайн — в одном приложении.",
                "Открыть AIVITA", "/")
    else:
        title, text, blabel, bhref = page.cta
    return (f'<section class="cta-band"><div class="inner">'
            f'<h2>{html.escape(title)}</h2><p>{html.escape(text)}</p>'
            f'<div class="cta-row"><a class="btn btn-primary" href="{bhref}">{html.escape(blabel)}</a></div>'
            f'</div></section>')


def _footer(page: "Page") -> str:
    cols = FOOTER.get(page.lang, FOOTER["ru"])
    colhtml = []
    for h4, links in cols:
        ls = "".join(f'<a href="{href}">{html.escape(l)}</a>' for l, href in links)
        colhtml.append(f'<div><h4>{html.escape(h4)}</h4>{ls}</div>')
    about = {
        "ru": "AIVITA — цифровая экосистема заботы о здоровье в Узбекистане: AI-чекап, "
              "электронная медкарта, проверка совместимости лекарств и врачи онлайн на 3 языках.",
        "uz": "AIVITA — O‘zbekistonda sog‘liqni saqlash bo‘yicha raqamli ekotizim: AI-checkup, "
              "elektron tibbiy karta, dori mosligini tekshirish va onlayn shifokorlar 3 tilda.",
        "en": "AIVITA is a digital health ecosystem in Uzbekistan: AI check-up, electronic "
              "medical card, drug-interaction checker and online doctors in 3 languages.",
    }[page.lang]
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{LANG_HOME[page.lang]}"><span class="brand-mark">{_logo_svg()}</span>{BRAND}<span class="tld">.uz</span></a>
<p class="foot-about">{html.escape(about)}</p></div>
{''.join(colhtml)}
</div>
<p class="foot-disclaimer">{html.escape(DISCLAIMER[page.lang])}</p>
<div class="foot-bottom"><span>© 2026 {BRAND} · Узбекистан · <a href="mailto:{ORG_EMAIL}">{ORG_EMAIL}</a></span>
<span>{" · ".join(f'<a href="{LANG_HOME[l]}" hreflang="{l}">{LANG_NAMES[l]}</a>' for l in ("ru","uz","en"))}</span></div>
</div></footer>'''


def _logo_svg():
    return ('<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            '<path d="M12 21s-7-4.35-9.33-9.02C1.1 8.9 2.7 5.5 6 5.5c1.8 0 3.1 1 3.9 2.3C10.7 6.5 12 5.5 13.8 5.5'
            'c3.3 0 4.9 3.4 3.33 6.48C19 16.65 12 21 12 21z" fill="#4f9384"/></svg>')


def render(page: "Page") -> str:
    canonical = _canonical(page)
    hreflang = _hreflang_tags(page)
    jsonld = _jsonld(page)
    og_img = DOMAIN + "/assets/og-image.svg"
    lede_block = ""
    header = f'''<header class="site-header"><div class="wrap">
<a class="brand" href="{LANG_HOME[page.lang]}"><span class="brand-mark">{_logo_svg()}</span>{BRAND}<span class="tld">.uz</span></a>
<button class="menu-toggle" aria-label="{_t(page.lang,'menu')}" onclick="document.querySelector('.nav').classList.toggle('open')">☰</button>
<nav class="nav" aria-label="main">{_nav(page)}</nav>
<div class="langs">{_langswitch(page)}</div>
</div></header>'''

    article_open = '<article class="article">' if page.section in ("blog",) or page.updated else '<div class="article">'
    article_close = '</article>' if page.section in ("blog",) or page.updated else '</div>'

    meta_line = ""
    if page.updated:
        meta_line = f'<p class="meta"><time datetime="{page.updated}">{_t(page.lang,"updated")}: {page.updated}</time></p>'

    doc = f'''<!DOCTYPE html>
<html lang="{page.lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(page.title)}</title>
<meta name="description" content="{html.escape(page.description)}">
<link rel="canonical" href="{canonical}">
{hreflang}
<meta property="og:type" content="{page.og_type}">
<meta property="og:title" content="{html.escape(page.title)}">
<meta property="og:description" content="{html.escape(page.description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:site_name" content="{BRAND}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ece7df">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{jsonld}
</head>
<body>
{header}
{_crumbs_html(page)}
<main><div class="wrap">
{article_open}
<div class="hero"><h1>{html.escape(page.h1)}</h1></div>
{meta_line}
{_disclaimer_html(page)}
{page.body}
{_faq_html(page)}
{_related_html(page)}
{article_close}
{_cta_html(page)}
</div></main>
{_footer(page)}
</body>
</html>'''
    return doc


# ----------------------------------------------------------------------------
# Сборка
# ----------------------------------------------------------------------------
_REGISTRY: list = []


def add(pages):
    if isinstance(pages, Page):
        _REGISTRY.append(pages)
    else:
        _REGISTRY.extend(pages)


def write_all(verbose=True):
    warnings = []
    seen = set()
    for p in _REGISTRY:
        if p.url() in seen:
            warnings.append(f"DUP URL: {p.url()}")
        seen.add(p.url())
        # запись
        rel = p.path
        outdir = ROOT if rel == "" else os.path.join(ROOT, rel)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(render(p))
        wc = word_count(p)
        thin = ""
        if p.section not in ("hub-index",) and wc < 350 and p.path not in ("",):
            thin = "  ⚠ THIN (<350)"
            warnings.append(f"THIN {wc}w: {p.url()}")
        if verbose:
            print(f"  {p.lang}  {wc:4d}w  {p.url()}{thin}")
    return warnings


def build_sitemap():
    # группируем по каноническому URL, добавляя xhtml:link alternates
    urls = []
    for p in _REGISTRY:
        alts = ""
        if p.hreflang and len(p.hreflang) >= 2:
            for lang, path in p.hreflang.items():
                alts += f'\n    <xhtml:link rel="alternate" hreflang="{lang}" href="{DOMAIN}{path}"/>'
            if "ru" in p.hreflang:
                alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}{p.hreflang["ru"]}"/>'
        lastmod = p.updated or TODAY
        urls.append(
            f'  <url>\n    <loc>{p.loc()}</loc>\n    <lastmod>{lastmod}</lastmod>{alts}\n  </url>'
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    return len(urls)


def all_urls():
    return [p.loc() for p in _REGISTRY]
