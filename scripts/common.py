"""Shared helpers for the refresh scripts. Standard library only, so the scripts run
anywhere Python 3.10 or later is installed."""
import datetime
import html
import json
import pathlib
import re
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
USER_AGENT = "dc-signpost-tracker (public-interest research; automated daily check)"


class Skip(Exception):
    """Raised by a feed that cannot run yet, for example because a setting is missing."""


def today():
    return datetime.datetime.now(datetime.timezone.utc).date()


def get_json(url, headers=None, timeout=30, missing_ok=False):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json", **(headers or {})})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        if missing_ok and error.code == 404:
            return None
        raise


def get_text(url, timeout=30):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def passages(text, terms, limit=10, span=1500):
    """The parts of a document's plain text that mention any of the terms, word for word.

    A regulator's combined notice lists many unrelated filings, each starting with
    "Docket Numbers"; where a mention sits inside such an entry the whole entry is kept.
    Otherwise the paragraph around the mention is kept. Runs of spaces and line breaks
    are collapsed; nothing else is altered."""
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).replace("\r", "")
    found, covered = [], []
    for term in terms:
        pattern = r"\s+".join(re.escape(word) for word in term.split())
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            if any(start <= match.start() < end for start, end in covered):
                continue
            entry = text.rfind("Docket Numbers", max(0, match.start() - span), match.start())
            if entry >= 0 and "\n\n" in text[entry:match.start()]:
                entry = -1  # that entry ended before this mention
            reach = span if entry >= 0 else span // 2
            if entry >= 0:
                start = entry
            else:
                start = text.rfind("\n\n", max(0, match.start() - reach), match.start())
                start = max(0, match.start() - reach) if start < 0 else start
            stops = [text.find(mark, match.end(), match.end() + reach) for mark in ("Docket Numbers", "\n\n")]
            end = min([stop for stop in stops if stop >= 0] or [min(len(text), match.end() + reach)])
            covered.append((start, end))
            found.append(" ".join(text[start:end].split()))
            if len(found) >= limit:
                return found
    return found


def load(name, default=None):
    path = DATA / name
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save(name, obj):
    (DATA / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
