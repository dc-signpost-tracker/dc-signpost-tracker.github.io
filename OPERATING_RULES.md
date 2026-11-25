# Operating rules for the signpost tracker

These rules bind anyone, human or AI, who updates this repository. The owner of the
repository is the only person who decides statuses and ratings.

## What must never happen

1. **Never invent data.** Every reading needs a source, a link and a retrieval date.
2. **Never change a signpost's `status` without the owner's explicit approval** in the
   conversation. `status` is `none` (Not yet), `pos` (Turned positive) or `neg` (Turned
   negative).
3. **Never change a severity rating** (`from` / `to` on a call, or `data/heatmap.json`).
   Only the owner does that, and only when he says so.
4. **Never add attribution.** The site names no author, employer, office or source note
   for the six calls. Do not add any.
5. **Never commit keys, tokens or email addresses.** Secrets live in the repository's
   secret store.
6. **Paid sources stay switched off** in `data/sources.json` unless the owner says otherwise.

## The baseline date: 12 Nov 2026

The ratings were set on 12 Nov 2026 with everything known up to that date already
taken into account. **A signpost's status changes only on a development after
12 Nov 2026.** A fact that was known on or before that date is baseline: show it as
context in the reading, but never recommend a status change because of it, however
adverse it looks. When recommending a change, state the date of the development.

Calls B (North America Water) and F (Europe Land) were added on 23 Nov 2026, so their
baseline date is 23 Nov 2026 (the call's `baseline` field): only developments after that
date can change the status of B1 to B7 and F1 to F8.

Some signposts turn mainly on politics. For A2 (Texas connections) the developments
that matter most are statements and measures from the Governor-elect, other incoming
Democratic office-holders and the Texas Legislature that would extend, widen or lift
the pause on data centre approvals. Search for those by name every time.

## What a reading is

Each signpost in `data/signposts.json` has `latest` (plain-language reading),
`latestDate`, `source_url`, `retrieved_on`, `verify` (a visible caveat), `next`,
`status`, `status_reviewed_on`, `last_checked_on` and `history`.

- `headline` is the figure or two-to-four-word fact the card leads with in large type
  (for example "6,831 megawatts short", "Paused"); `summary` is the one line beneath
  it. Both must say only what `latest` says. **Whenever `latest` changes, update
  `headline` and `summary` in the same commit**, under the same rule that allows the
  change to `latest`.
- `source_url` is set **only** when the linked document was opened and read directly.
  A fact known only from press reports gets no `source_url`; say so in `verify`.
- A US Federal Register document counts as read directly when the refresh script has
  saved its passages with the inbox item (`excerpt`). They are the official text, word
  for word, taken through the site's own programme interface because its web pages
  refuse automated readers. Use the item's `url` as the `source_url`, and claim only
  what the saved passages say.
- Write readings in plain English. Spell out every acronym at first use.
- `threshold` is the one short line on the card that states the trigger ("Trigger:
  shortfall below 6,831 megawatts", or "Watch: ..." where the trigger is a list of terms).
  Leave it unchanged unless the owner changes the trigger.
- `delta` (optional) shows how the headline figure moved since the previous reading of
  the same measure, for example `{"dir": "up", "text": "from 6,516 at the 2027/28
  auction"}`. Set it only when both figures come from sources already recorded on the
  signpost; otherwise leave it out. When a new reading of the same measure arrives,
  move the previous figure into `delta`.
- `history` entries that the overview's "What changed" list should show carry `kind`
  and `brief`. `kind` is `"status"` for a status change the owner approved, `"reading"`
  for a new development recorded in `latest`, and `"note"` for housekeeping that the
  list should not show. `brief` is one plain sentence of no more than about 25 words
  saying what happened. Add one such entry, dated the day the development happened,
  whenever `latest` changes for a new development or a status changes.

## Charts (`data/series.json`)

Five signposts carry a time series shown as a chart or table on the card: A1 (PJM reserve
margin and auction table), A2 (Texas large-load requests), A3 (GE Vernova firm orders,
reserved slots and deliveries), A6 (reliability risk ratings by assessment year) and G3
(Japan's restarted nuclear capacity). Each entry names its `source` and its `next_point`.

When a new data point for one of these series is published (for example the PJM 2029/30
auction results, GE Vernova's next quarterly filing, the Texas audit report, the 2026
reliability assessment, or a reactor restart), the digest:

1. reads the figure at its primary source (the daily feed check files GE Vernova's
   filings in the inbox; the others are found in the weekly sweep and from the calendar);
2. appends the point to the series in `data/series.json`: add the label to `x`, one value
   to every series in that chart (and to `line` and `rows` where present), and update
   `next_point`. Never change or remove an existing point without telling the owner;
3. updates the signpost's reading fields in the same commit, as a group B change.

A figure found only in the press is not added to a chart; list it in the digest as
group C. Never estimate a point or read one off a picture of a chart.

## Owner-approved wording

`insight` (the "The picture today" paragraph), `coverage_note` (the line under "What we currently track") and
each call's `bottom_line` were approved by the owner on 21 Nov 2026. Never change them
on your own. If a development makes one of them inaccurate, put the proposed new
wording in group A of the digest and wait for the owner's answer.

## How the owner's rule on review flags works

A call shows "Rating under review" as soon as one of its signposts challenges it. For
Easing calls a `neg` status challenges; for Persisting and Intensifying calls a `pos`
status challenges. The site computes this; do not set it by hand. Calls B and F hold at
Moderate in both periods and can move either way (to Minor or to Severe), so on those
calls a signal in either direction flags the call.

## The daily cycle

1. `.github/workflows/refresh.yml` runs `scripts/refresh.py` every day. It files new
   documents in `data/inbox.json` with `"state": "new"`. It changes no reading and does
   not touch `last_refreshed`; its own run date is in `data/refresh_status.json`.
2. The morning digest (an AI task) then, every Wednesday (weekly since 21 Nov 2026; it was
   daily before), covering everything since the last run:
   - **Feeds:** reads every inbox item with `"state": "new"`;
   - **Catalysts:** checks the dated events in `data/calendar.json` that have passed
     without an `outcome`;
   - **Sweep of all 54 signposts:** runs at least one web search for every signpost,
     A1 to H6, for developments since its `last_checked_on` date, and reads further
     only where something is new relative to its current `latest` reading. No signpost
     is skipped because it has no feed. `last_checked_on` is set to the day's date on
     every signpost searched, whether or not anything was found;
   - **Follow-ups:** works through at most two items in `data/followups.json`;
   - opens the primary document for each finding where it can;
   - sorts each finding into one of three groups (below);
   - sets `last_refreshed` in `data/signposts.json` to the day's date once the sweep is
     done (the site shows it as "Last refreshed", meaning the signposts were reviewed);
   - marks each inbox item it handled `"state": "reviewed"` with `"reviewed_on"`.
     Routine notices that say nothing about a signpost are marked reviewed too; an
     item is left `"new"` only if it could not be opened, and the digest says so.

### The three groups

| Group | When | What the task may do unattended |
|---|---|---|
| A. Needs the owner's decision | The finding could change a status, or it is a close call | Nothing on the site except `last_checked_on`. Present the evidence, the source links and a recommendation. Wait. |
| B. For information, verified | Status unchanged, and the primary document was read directly | Update `latest`, `latestDate`, `headline`, `summary`, `delta`, `source_url`, `retrieved_on`, `verify`, `next`, `history` (with `kind` and `brief`), and calendar `outcome`. Never `status`, `threshold`, `bottom_line`, `insight` or `coverage_note`. |
| C. For information, press-only | Status unchanged, but only press reports were found | Nothing on the site except `last_checked_on`. List it in the digest. |

If in doubt between A and B, choose A.

### The digest

One message to the owner, in this order: (1) "Needs your decision", each item with what
happened, sources, what the trigger says and a recommendation; (2) "For information",
listing what was updated on the site and what is press-only; (3) one closing line saying how many of the 54 signposts were
searched and how many had nothing new, naming any that could not be searched. Use plain English, spell out acronyms at first use, and keep
it short. When the owner replies with decisions, apply them, commit and push.

## Committing

Commit to `main` with a message that says which signposts changed and why. After any
change to `data/`, the site updates by itself once pushed.

A chart may set `"axis": true` (with `"max"` and `"tick"`) to show numbers down the left
side; A2's line chart does.

## Signposts added on 23 Nov 2026

Nineteen signposts were added at the end of their tabs on 23 Nov 2026; seventeen remain:
A7 to A9, C2, C4, C6, D4, D5, E2, E6, F7, G6, G7, H3 to H6 (the owner dropped the old A8 and
A11 on 25 Nov 2026, and the old A9 and A10 became A8 and A9). Each carries `"added": "2026-11-23"` and shows a "New" tag.

- Their baseline is 23 Nov 2026: only developments after that date can change a status.
- Their trigger wording is a draft until the owner confirms it. Until then, report
  developments in the digest but do not propose a status change on them.
- Their readings came from search results and press and carry the grey "Press-reported; to be verified against primary source" caveat. Verify
  them at the primary source as for any other reading.
- C2 (local pauses and bans) uses the US Data Center Moratorium Tracker, chosen by the owner on
  25 Nov 2026; its trigger uses the count of active pauses and bans, not the running total.

## "News, no signal" label

A signpost with status `none` shows "News, no signal" (same grey as "No signal yet") when
its history holds at least one entry with `"kind": "reading"`, meaning a development was
reviewed and did not cross the trigger. Otherwise it shows "No signal yet". So when a
group B finding is logged, always add the history entry with `"kind": "reading"` and a
`brief`; that entry is what switches the label and lists the item under "What changed".

## Order of the "Eases if" points

Each call's key points (`key.text`, the "Eases if" or "Stays contained if" line) are listed in
the same order as the signposts that track them. When a tab is reordered, reorder these
points to match, without changing their wording.

## Keeping the banners in step with the signposts

Each call's banner text (`bottom_line`, `depends` and `key.text`) is owner-approved wording.
Whenever signposts are added, dropped, reordered or relettered, or a status changes, check
that this text still matches the signposts. Where it no longer does, draft the updated
wording (marking what is new) and put it under "Needs your decision" in the digest. Never
apply it without the owner's approval. Reordering `key.text` points to follow signpost
order needs no approval, as long as the wording is unchanged.

## Headline and summary style

Each card's headline must make sense on its own (a figure with its unit, or a short
plain-English phrase), and the summary under it must be a complete sentence that reads on
its own. Never write a summary that continues the headline's sentence (for example a
headline "Eight states" followed by "Paused or repealed ..."). Repeating the headline's
figure in the summary is fine. A card without a primary source shows a grey caveat,
"Press-reported; to be verified against primary source", not a red label.

## Sources: web only, never the owner's old analysis

The owner's original analysis pages are legacy and are no longer a source. Every reading must
come from something found on the web (official documents first, then trackers and press)
and carry its link. Never describe a reading as coming from "the analysis behind this call".
The site itself is now the live record of the analysis.

## Europe headers name their geography

On the three Europe tabs every signpost name says where it applies: "EU-wide",
"Europe-wide", or the country or city (for example "England's national route",
"Powered-land prices: Frankfurt"). Keep this when adding or renaming signposts.
