#!/usr/bin/env python3
"""IndexNow — уведомление поисковиков (Bing, Яндекс) о новых/изменённых URL.

Запускать ПОСЛЕ деплоя, когда страницы уже доступны на https://aivita.uz/.
Ключ IndexNow должен быть доступен по адресу
  https://aivita.uz/026149e5d1435297bad1ac0ccfe6fbc1.txt
(файл лежит в корне репозитория и деплоится вместе с сайтом).

Использование:
  python3 tools/indexnow.py                # пингануть все URL из sitemap.xml
  python3 tools/indexnow.py /features/ /blog/...   # только указанные пути
"""
import json
import os
import re
import sys
import urllib.request

HOST = "aivita.uz"
KEY = "026149e5d1435297bad1ac0ccfe6fbc1"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def urls_from_sitemap():
    path = os.path.join(ROOT, "sitemap.xml")
    xml = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", xml)


def main():
    if len(sys.argv) > 1:
        urls = [f"https://{HOST}{p}" if p.startswith("/") else p for p in sys.argv[1:]]
    else:
        urls = urls_from_sitemap()
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=data,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    print(f"IndexNow: отправляю {len(urls)} URL на {ENDPOINT} …")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"HTTP {resp.status} — {resp.reason}")
            print("Готово. Bing/Яндекс получили список URL для переобхода.")
    except Exception as e:  # noqa: BLE001
        print(f"Ошибка отправки: {e}")
        print("Проверьте, что сайт задеплоен и ключ доступен по", KEY_LOCATION)
        sys.exit(1)


if __name__ == "__main__":
    main()
