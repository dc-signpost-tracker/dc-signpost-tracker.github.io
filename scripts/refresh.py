"""Refresh signposts: run every enabled feed in data/sources.json and file what it finds.

What this does
- Runs each source that is enabled and has a fetcher.
- Adds any document not seen before to data/inbox.json, marked "new", with its link,
  publication date and retrieval date.
- Where a feed supplies the document's plain text (the US Federal Register does), saves
  the passages that mention the subject with the inbox item, as "excerpt", word for
  word, so the item can be reviewed without opening the web page.
- Records how each feed went in data/refresh_status.json.
- Stamps data/signposts.json with the date of the run ("Last refreshed" on the site).

What this never does
- It never changes a signpost's status or a severity rating. Those are the owner's
  decisions. Documents wait in the inbox until the owner has reviewed them.

Run from the repository root:  python scripts/refresh.py
"""
import sys

from common import Skip, get_text, load, passages, save, today
from feeds import boe, federal_register, sec_edgar

FETCHERS = {"federal_register": federal_register.fetch, "sec_edgar": sec_edgar.fetch, "boe": boe.fetch}


def add_excerpt(item, text_url, terms):
    """Save the passages of the official text that mention the subject. Never fatal."""
    try:
        item["excerpt"] = passages(get_text(text_url), terms)
        item["excerpt_from"] = text_url
        item.pop("excerpt_error", None)
    except Exception as error:
        item["excerpt_error"] = f"{type(error).__name__}: {str(error)[:200]}"


def main():
    run_on = today().isoformat()
    sources = load("sources.json")["sources"]
    inbox = load("inbox.json", {"items": []})
    seen = {item["url"] for item in inbox["items"]}
    by_url = {item["url"]: item for item in inbox["items"]}
    feeds, any_ok, any_failed = {}, False, False

    for source in sources:
        if not (source.get("enabled") and source.get("fetcher")):
            continue
        try:
            found = FETCHERS[source["fetcher"]](source)
        except Skip as reason:
            feeds[source["id"]] = {"state": "skipped", "detail": str(reason)}
            continue
        except Exception as error:  # one broken feed must not stop the others
            feeds[source["id"]] = {"state": "failed", "detail": f"{type(error).__name__}: {str(error)[:200]}"}
            any_failed = True
            continue
        new = 0
        for item in found:
            text_url, terms = item.pop("text_url", None), item.pop("terms", None)
            if item["url"] in seen:
                waiting = by_url.get(item["url"])  # filed earlier, not yet reviewed, no passages saved
                if text_url and waiting and waiting["state"] == "new" and "excerpt" not in waiting:
                    add_excerpt(waiting, text_url, terms)
                continue
            seen.add(item["url"])
            entry = {**item, "source": source["id"], "signposts": source["signposts"],
                     "retrieved_on": run_on, "state": "new"}
            if text_url:
                add_excerpt(entry, text_url, terms)
            inbox["items"].append(entry)
            by_url[entry["url"]] = entry
            new += 1
        feeds[source["id"]] = {"state": "ok", "found": len(found), "new": new}
        any_ok = True

    inbox["items"].sort(key=lambda item: (item["published"], item["url"]), reverse=True)
    save("inbox.json", inbox)
    save("refresh_status.json", {"run_on": run_on, "feeds": feeds})
    # "Last refreshed" on the site is the date of the last digest, which reviews the
    # signposts; this feed check only files documents, so it leaves that date alone.
    # The date of this run is kept in refresh_status.json.

    for name, result in feeds.items():
        print(f"{name}: {result}")
    return 1 if any_failed else 0


if __name__ == "__main__":
    sys.exit(main())
