"""Spain's official gazette (Boletín Oficial del Estado): the daily summary, searched
for keywords in item titles. No key needed.
API notes: https://www.boe.es/datosabiertos/"""
import datetime

from common import get_json, today


def _items(node):
    if isinstance(node, dict):
        if "titulo" in node and "url_html" in node:
            yield node
        for value in node.values():
            yield from _items(value)
    elif isinstance(node, list):
        for value in node:
            yield from _items(value)


def fetch(source):
    p = source["params"]
    keywords = [k.lower() for k in p["keywords"]]
    found = []
    for back in range(p.get("days_back", 7)):
        date = today() - datetime.timedelta(days=back)
        data = get_json(f"https://www.boe.es/datosabiertos/api/boe/sumario/{date:%Y%m%d}", missing_ok=True)
        if not data:
            continue  # no gazette that day
        for item in _items(data):
            title = item["titulo"]
            if any(k in title.lower() for k in keywords):
                found.append({"title": title, "url": item["url_html"], "published": date.isoformat(), "kind": "Gazette item"})
    return found
