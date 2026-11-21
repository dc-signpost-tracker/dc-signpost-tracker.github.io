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

Some signposts turn mainly on politics. For A4 (Texas connections) the developments
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

## How the owner's rule on review flags works

A call shows "Rating under review" as soon as one of its signposts challenges it. For
Easing calls a `neg` status challenges; for Persisting and Intensifying calls a `pos`
status challenges. The site computes this; do not set it by hand.

## The daily cycle

1. `.github/workflows/refresh.yml` runs `scripts/refresh.py` every day. It files new
   documents in `data/inbox.json` with `"state": "new"`. It changes no reading.
2. The morning digest (an AI task) then, every Wednesday (weekly since 21 Nov 2026; it was
   daily before), covering everything since the last run:
   - **Feeds:** reads every inbox item with `"state": "new"`;
   - **Catalysts:** checks the dated events in `data/calendar.json` that have passed
     without an `outcome`;
   - **Sweep of all 24 signposts:** runs at least one web search for every signpost,
     A1 to F2, for developments since its `last_checked_on` date, and reads further
     only where something is new relative to its current `latest` reading. No signpost
     is skipped because it has no feed. `last_checked_on` is set to the day's date on
     every signpost searched, whether or not anything was found;
   - **Follow-ups:** works through at most two items in `data/followups.json`;
   - opens the primary document for each finding where it can;
   - sorts each finding into one of three groups (below);
   - marks each inbox item it handled `"state": "reviewed"` with `"reviewed_on"`.
     Routine notices that say nothing about a signpost are marked reviewed too; an
     item is left `"new"` only if it could not be opened, and the digest says so.

### The three groups

| Group | When | What the task may do unattended |
|---|---|---|
| A. Needs the owner's decision | The finding could change a status, or it is a close call | Nothing on the site except `last_checked_on`. Present the evidence, the source links and a recommendation. Wait. |
| B. For information, verified | Status unchanged, and the primary document was read directly | Update `latest`, `latestDate`, `source_url`, `retrieved_on`, `verify`, `next`, `history`, and calendar `outcome`. Never `status`. |
| C. For information, press-only | Status unchanged, but only press reports were found | Nothing on the site except `last_checked_on`. List it in the digest. |

If in doubt between A and B, choose A.

### The digest

One message to the owner, in this order: (1) "Needs your decision", each item with what
happened, sources, what the trigger says and a recommendation; (2) "For information",
listing what was updated on the site and what is press-only; (3) one closing line saying how many of the 24 signposts were
searched and how many had nothing new, naming any that could not be searched. Use plain English, spell out acronyms at first use, and keep
it short. When the owner replies with decisions, apply them, commit and push.

## Committing

Commit to `main` with a message that says which signposts changed and why. After any
change to `data/`, the site updates by itself once pushed.
