"""US Securities and Exchange Commission filing system (EDGAR): a company's recent filings.
No key needed, but every request must identify the requester with a contact email.
Set it as the CONTACT_EMAIL environment variable (a repository secret on GitHub)."""
import os

from common import Skip, get_json


def fetch(source):
    contact = os.environ.get("CONTACT_EMAIL", "").strip()
    if not contact:
        raise Skip("CONTACT_EMAIL is not set; the filing system requires a contact address")
    p = source["params"]
    cik = str(p["cik"]).zfill(10)
    data = get_json(f"https://data.sec.gov/submissions/CIK{cik}.json",
                    headers={"User-Agent": f"dc-signpost-tracker {contact}"})
    recent = data["filings"]["recent"]
    items = []
    for form, date, accession, document, described, sections in zip(
            recent["form"], recent["filingDate"], recent["accessionNumber"],
            recent["primaryDocument"], recent["primaryDocDescription"], recent["items"]):
        if form not in p["forms"] or date < p["since"]:
            continue
        if form == "8-K" and p.get("items_include") and not any(i in sections for i in p["items_include"]):
            continue
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/{document}"
        items.append({"title": f"{data['name']} {form}" + (f": {described}" if described else ""),
                      "url": url, "published": date, "kind": form})
    return items
