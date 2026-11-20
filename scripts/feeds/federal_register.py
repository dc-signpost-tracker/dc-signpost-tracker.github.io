"""US Federal Register: documents matching a search. No key needed.
API notes: https://www.federalregister.gov/developers/documentation/api/v1"""
import urllib.parse

from common import get_json


def fetch(source):
    p = source["params"]
    query = [("per_page", "50"), ("order", "newest"),
             ("conditions[term]", p["term"]),
             ("conditions[publication_date][gte]", p["since"])]
    query += [("conditions[agencies][]", a) for a in p.get("agencies", [])]
    query += [("conditions[type][]", t) for t in p.get("types", [])]
    query += [("fields[]", f) for f in ("title", "abstract", "type", "html_url", "publication_date", "raw_text_url")]
    url = "https://www.federalregister.gov/api/v1/documents.json?" + urllib.parse.urlencode(query)
    results = (get_json(url) or {}).get("results") or []
    must = [m.lower() for m in p.get("must_mention", [])]
    if must:  # the search is full-text, so keep only documents that are about the subject
        results = [r for r in results
                   if any(m in ((r.get("title") or "") + " " + (r.get("abstract") or "")).lower() for m in must)]
    # The web pages refuse automated readers, so the morning digest cannot open them.
    # Hand back the address of each document's plain text and the words to look for;
    # refresh.py saves the matching passages with the inbox item.
    terms = p.get("must_mention") or [p["term"].strip('"')]
    return [{"title": r["title"], "url": r["html_url"], "published": r["publication_date"], "kind": r.get("type") or "Document",
             "text_url": r.get("raw_text_url"), "terms": terms}
            for r in results]
