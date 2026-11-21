"""Build preview.html: index.html with the data files inlined, so it opens by double-click.
Run from the repository root:  python scripts/build_preview.py"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
data = {k: json.loads((root / "data" / f"{k}.json").read_text(encoding="utf-8")) for k in ("signposts", "calendar", "heatmap")}
html = (root / "index.html").read_text(encoding="utf-8")
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
marker = "<script>\n/* Data lives in"
assert marker in html
html = html.replace(marker, "<script>window.__DATA__ = " + blob + ";</script>\n" + marker, 1)
(root / "preview.html").write_text(html, encoding="utf-8")
print("preview.html written")
