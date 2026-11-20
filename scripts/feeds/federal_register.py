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
    query += [("fields[]", f) for f in ("title", "abstract", "type", "html_url", "publication_date")]
    url = "https://www.federalregister.gov/api/v1/documents.json?" + urllib.parse.urlencode(query)
    results = (get_json(url) or {}).get("results") or []
    must = [m.lower() for m in p.get("must_mention", [])]
    if must:  # the search is full-text, so keep only documents that are about the subject
        results = [r for r in results
                   if any(m in ((r.get("title") or "") + " " + (r.get("abstract") or "")).lower() for m in must)]
    return [{"title": r["title"], "url": r["html_url"], "published": r["publication_date"], "kind": r.get("type") or "Document"}
            for r in results]
