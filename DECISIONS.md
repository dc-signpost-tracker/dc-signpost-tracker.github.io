# Owner's decisions log

Every session that works on this repository reads this file first and follows it.
When the owner decides something that affects how the tracker works, how the site
looks, or how he wants to be worked with, add a dated line here in the same session,
commit and push. Signpost statuses are not logged here; they live in
`data/signposts.json`. Rules about what may change unattended are in
`OPERATING_RULES.md`.

## How the owner wants to be worked with

- Spell out every acronym at first use, on the site and in messages.
- When asked for options or recommendations, give a comprehensive list.
- Put decision points as multiple-choice cards where a question tool is available.
- One step at a time; do not ask for several things at once.
- Show the site as a link in the chat, not as a file in a folder.
- Do a refresh in one pass with one digest. Ask only when recommending a status change
  or when the call is close; list everything else for information.

## Decisions (20 Nov 2026)

- **Audience:** public website, anyone with the link.
- **No attribution:** the site names no author, employer, office, source note or note
  date. The six calls are presented as the tracker's own framework.
- **Screen:** designed for a typical computer screen. Mobile is not a target.
- **Design:** sleek, not dense, easy for any reader. Severity colours are pale red
  (Severe), pale amber (Moderate), pale teal (Minor). Signal colours are navy for
  "Supports call" and red for "Challenges call". Headline stays "Where power, water and
  land redirect the data centre build-out". First screen is the six-calls board. No
  compact summary grid. Signpost cards show status, reading, next date and gauge, with
  trigger and sources behind a tap.
- **Review flag:** a call shows "Rating under review" as soon as one signpost
  challenges it, including a single event signpost the owner has approved.
- **Ratings:** never change automatically. Only the owner changes a rating.
- **Refresh:** feeds run daily on GitHub's scheduler, with an owner-only manual trigger.
  No public refresh button.
- **Morning digest:** a scheduled task sweeps all 24 signposts every morning. Unattended,
  it may update a reading only when the status is unchanged and it read the primary
  document itself. Phone notification only.
- **Paid sources:** listed, switched off.
- **Johor reserve margin:** lead with the official statewide 14.4%; mention the 12.8%
  brokerage estimate.
- **Address:** the site will be served from a neutral GitHub organisation,
  `dc-signpost-tracker`, at `dc-signpost-tracker.github.io`. Move pending.
- **Go-live:** on hold until the owner's design changes are made and he says so.

## Open

- The owner has design comments to give on making the site more intuitive.
- Seven readings still need checking at their primary source (`data/followups.json`).
- History charts, the rules file and feeds for most signposts are not built.
