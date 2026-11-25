# Data Centre Signpost Tracker

A static website that tracks 54 signposts behind eight calls on how power, water and
land constrain the build-out of artificial intelligence (AI) data centres.

## How it works

- `index.html` is the whole site. It has no libraries and no server.
- `data/signposts.json` holds the six calls, their signposts, readings and history.
- `data/calendar.json` holds the dated catalysts.
- `data/heatmap.json` holds the eight-region severity ratings.
- `scripts/` holds the tools that build and refresh the data.

The page reads the data files when it loads. Changing a data file changes the site.

## Rules the data follows

- Every reading carries a primary source link and a retrieval date. A reading
  without one is shown as "Press-reported; to be verified against primary source".
- New readings publish automatically. A change of signpost status, or of a severity
  rating, is made only by the owner.
- No keys or credentials are stored in this repository.

## Viewing it locally

Browsers do not let a page read data files straight from a folder. Either serve the
folder (`python -m http.server`, then open http://localhost:8000) or run
`python scripts/build_preview.py` and open the `preview.html` it writes.
