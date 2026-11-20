"""Shared helpers for the refresh scripts. Standard library only, so the scripts run
anywhere Python 3.10 or later is installed."""
import datetime
import json
import pathlib
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


def load(name, default=None):
    path = DATA / name
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save(name, obj):
    (DATA / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
