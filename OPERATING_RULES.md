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

## What a reading is

Each signpost in `data/signposts.json` has `latest` (plain-language reading),
`latestDate`, `source_url`, `retrieved_on`, `verify` (a visible caveat), `next`,
`status`, `status_reviewed_on` and `history`.

- `source_url` is set **only** when the linked document was opened and read directly.
  A fact known only from press reports gets no `source_url`; say so in `verify`.
- Write readings in plain English. Spell out every acronym at first use.

## How the owner's rule on review flags works

A call shows "Rating under review" as soon as one of its signposts challenges it. For
Easing calls a `neg` status challenges; for Persisting and Intensifying calls a `pos`
status challenges. The site computes this; do not set it by hand.

## The daily cycle

1. `.github/workflows/refresh.yml` runs `scripts/refresh.py` every day. It files new
   documents in `data/inbox.json` with `"state": "new"`. It changes no reading.
2. The morning digest (an AI task) then:
   - reads every inbox item with `"state": "new"`, and checks the dated catalysts in
     `data/calendar.json` that have passed without an `outcome`;
   - opens the primary document for each where it can;
   - sorts each finding into one of three groups (below);
   - works through at most two items in `data/followups.json`;
   - marks each inbox item it handled `"state": "reviewed"` with `"reviewed_on"`.

### The three groups

| Group | When | What the task may do unattended |
|---|---|---|
| A. Needs the owner's decision | The finding could change a status, or it is a close call | Nothing on the site. Present the evidence, the source links and a recommendation. Wait. |
| B. For information, verified | Status unchanged, and the primary document was read directly | Update `latest`, `latestDate`, `source_url`, `retrieved_on`, `verify`, `next`, `history`, and calendar `outcome`. Never `status`. |
| C. For information, press-only | Status unchanged, but only press reports were found | Nothing on the site. List it in the digest. |

If in doubt between A and B, choose A.

### The digest

One message to the owner, in this order: (1) "Needs your decision", each item with what
happened, sources, what the trigger says and a recommendation; (2) "For information",
listing what was updated on the site and what is press-only; (3) "Nothing new" if that
is the case, in one line. Use plain English, spell out acronyms at first use, and keep
it short. When the owner replies with decisions, apply them, commit and push.

## Committing

Commit to `main` with a message that says which signposts changed and why. After any
change to `data/`, the site updates by itself once pushed.
