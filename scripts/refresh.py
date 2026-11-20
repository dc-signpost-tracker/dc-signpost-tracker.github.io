"""Refresh signposts: run every enabled feed in data/sources.json and file what it finds.

What this does
- Runs each source that is enabled and has a fetcher.
- Adds any document not seen before to data/inbox.json, marked "new", with its link,
  publication date and retrieval date.
- Records how each feed went in data/refresh_status.json.
- Stamps data/signposts.json with the date of the run ("Last refreshed" on the site).

What this never does
- It never changes a signpost's status or a severity rating. Those are the owner's
  decisions. Documents wait in the inbox until the owner has reviewed them.

Run from the repository root:  python scripts/refresh.py
"""
import sys

from common import Skip, load, save, today
from feeds import boe, federal_register, sec_edgar

FETCHERS = {"federal_register": federal_register.fetch, "sec_edgar": sec_edgar.fetch, "boe": boe.fetch}


def main():
    run_on = today().isoformat()
    sources = load("sources.json")["sources"]
    inbox = load("inbox.json", {"items": []})
    seen = {item["url"] for item in inbox["items"]}
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
            if item["url"] in seen:
                continue
            seen.add(item["url"])
            inbox["items"].append({**item, "source": source["id"], "signposts": source["signposts"],
                                   "retrieved_on": run_on, "state": "new"})
            new += 1
        feeds[source["id"]] = {"state": "ok", "found": len(found), "new": new}
        any_ok = True

    inbox["items"].sort(key=lambda item: (item["published"], item["url"]), reverse=True)
    save("inbox.json", inbox)
    save("refresh_status.json", {"run_on": run_on, "feeds": feeds})
    if any_ok:
        signposts = load("signposts.json")
        signposts["last_refreshed"] = run_on
        save("signposts.json", signposts)

    for name, result in feeds.items():
        print(f"{name}: {result}")
    return 1 if any_failed else 0


if __name__ == "__main__":
    sys.exit(main())
