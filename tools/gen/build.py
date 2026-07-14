#!/usr/bin/env python3
"""Собирает весь сайт AIVITA из content-модулей.

Использование:  python3 tools/gen/build.py
Каждый модуль в tools/gen/content/*.py экспортирует pages() -> list[Page].
"""
import importlib
import os
import pkgutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)                      # чтобы работал `from engine import ...`
sys.path.insert(0, os.path.join(HERE, "content"))

import engine as S  # noqa: E402


# Порядок модулей = порядок этапов (для читаемого вывода)
ORDER = [
    "home", "features", "audiences", "blog", "regions",
    "doctors", "medical_tourism", "medsoft", "health", "about",
    "uz", "en",
]


def load_modules():
    content_dir = os.path.join(HERE, "content")
    available = {name for _, name, _ in pkgutil.iter_modules([content_dir])}
    ordered = [m for m in ORDER if m in available]
    ordered += sorted(available - set(ordered))
    mods = []
    for name in ordered:
        mods.append((name, importlib.import_module(name)))
    return mods


def build_llms():
    from engine import DOMAIN
    txt = f"""# AIVITA — llms.txt
# {DOMAIN}

> AIVITA — цифровая экосистема заботы о здоровье в Узбекистане. Помогает пройти
> AI-чекап организма, вести электронную медкарту, проверять совместимость лекарств,
> отслеживать показатели здоровья с умных часов и записываться к врачам онлайн.
> Интерфейс и контент доступны на трёх языках: русском (/), узбекском (/uz/) и
> английском (/en/). Часть экосистемы: AIVITA (пациенты), MedSoft (МИС для клиник),
> AIVITA Beauty (салоны красоты).

## Языки
- Русский — корень сайта: {DOMAIN}/
- O‘zbekcha (lotin) — {DOMAIN}/uz/
- English — {DOMAIN}/en/

## Возможности (Features)
- AI-чекап организма онлайн: {DOMAIN}/features/ai-checkup/
- Проверка совместимости лекарств: {DOMAIN}/features/drug-checker/
- Электронная медкарта: {DOMAIN}/features/medcard/
- Врачи онлайн (телемедицина): {DOMAIN}/features/doctors/
- SOS-помощь: {DOMAIN}/features/sos/
- Мониторинг здоровья (умные часы, браслеты): {DOMAIN}/features/monitoring/

## Разделы
- Блог о здоровье: {DOMAIN}/blog/
- Здоровый образ жизни (хаб): {DOMAIN}/health/
- Врачи по специальностям: {DOMAIN}/doctors/
- Регионы Узбекистана: {DOMAIN}/regions/
- Для мам / семьи / врачей: {DOMAIN}/for/moms/
- Медицинский туризм в Узбекистане: {DOMAIN}/medical-tourism/ (EN: {DOMAIN}/en/medical-tourism/)

## Для бизнеса
- MedSoft — медицинская информационная система (МИС) для клиник: {DOMAIN}/medsoft/
  (малым клиникам {DOMAIN}/medsoft/small/, сетям {DOMAIN}/medsoft/network/,
  стоматологии {DOMAIN}/medsoft/stomatologiya/, интеграция {DOMAIN}/medsoft/integration/)
- О компании и экосистеме (AIVITA + MedSoft + AIVITA Beauty): {DOMAIN}/about/

## Узбекская версия (O‘zbekcha)
- Bosh sahifa: {DOMAIN}/uz/
- Imkoniyatlar: {DOMAIN}/uz/features/
- Hududlar: {DOMAIN}/uz/regions/
- Blog: {DOMAIN}/uz/blog/
- Biz haqimizda: {DOMAIN}/uz/about/

## English version
- Home: {DOMAIN}/en/
- Features: {DOMAIN}/en/features/
- Medical tourism in Uzbekistan: {DOMAIN}/en/medical-tourism/
- About: {DOMAIN}/en/about/

## Факты
- AI-чекап занимает около 60 секунд и оценивает 5 систем организма.
- Каталог: 250+ врачей, покрытие — 14 регионов Узбекистана.
- Телемедицина: врач из любого региона доступен онлайн.

## Дисклеймер
Контент AIVITA носит справочный характер и не заменяет консультацию врача.
Платформа не ставит диагнозы и не назначает лечение.

## Sitemap
{DOMAIN}/sitemap.xml
"""
    with open(os.path.join(S.ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(txt)


def main():
    mods = load_modules()
    print("== Загружаю content-модули:", ", ".join(n for n, _ in mods))
    for name, mod in mods:
        if hasattr(mod, "pages"):
            S.add(mod.pages())
    print(f"== Всего страниц: {len(S._REGISTRY)}")
    warnings = S.write_all(verbose=True)
    n = S.build_sitemap()
    build_llms()
    print(f"== sitemap.xml: {n} URL")
    print(f"== llms.txt обновлён")
    if warnings:
        print("\n!! ПРЕДУПРЕЖДЕНИЯ:")
        for w in warnings:
            print("  -", w)
    else:
        print("== Предупреждений нет")


if __name__ == "__main__":
    main()
