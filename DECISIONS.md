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
- **Federal Register passages:** the refresh script saves the passages of each Federal
  Register document that mention the subject with its inbox item. A passage saved this
  way counts as reading the primary document directly.
- **Decision cards:** put each decision as a card with several options, the
  recommended option first, and room for a free-text answer.
- **Paid sources:** listed, switched off.
- **Johor reserve margin:** lead with the official statewide 14.4%; mention the 12.8%
  brokerage estimate.
- **Address:** the site will be served from a neutral GitHub organisation,
  `dc-signpost-tracker`, at `dc-signpost-tracker.github.io`. Move pending.
- **Go-live:** on hold until the owner's design changes are made and he says so.

- **Baseline date:** a signpost's status changes only on developments after
  12 Nov 2026. Anything known on or before that date is baseline context.
- **A4 (Texas connections):** reverted to "Not yet" on 20 Nov; the earlier "Turned
  negative" rested on a pause that predates the baseline. The card leads with the
  political track: the Governor-elect's pledged moratorium, her powers from
  19 Jan 2027 and the new Legislature.

## Design changes (20 Nov 2026, afternoon)

- Removed from the top of the page: the introductory sentence under the headline, the
  "24 signposts across 6 calls" line, the "The six calls" heading, and the severity
  rating legend. Do not add them back.

- Removed the line "Select a call to see its signposts."
- **Tabs, not one long page:** the six region and constraint pairs are six tabs across
  the top. Selecting a tab shows that pair's ratings, signposts and next catalyst.
  Each tab has its own address (for example `#europe-power`).
- **Rating boxes are labelled:** "2026–30" sits above the first box and "Beyond 2030"
  above the second. No caption underneath.

- **Removed "Where the constraints bind":** the eight-region table and its section are
  gone from the page. `data/heatmap.json` stays in the repository as a record but is
  not shown. Do not add the section back.
- **Calendar per tab:** each tab has its own catalyst calendar, listing only the events
  tied to that tab's signposts. There is no page-wide calendar.

- **Signpost labels:** each label (A1, A2…) is a solid navy circle on its card, a
  neutral colour that carries no status meaning. The squares in each tab's summary
  carry the same labels.

- **Layout approved (20 Nov):** a solid navy banner for each call (name, labelled
  rating boxes, labelled signpost squares, next catalyst as a countdown panel), with
  the open tab joined to it in navy. Signposts are cards, two across, each with a grey
  header band and a headline figure in large type; the full reading, trigger and
  sources sit behind a tap. The catalyst calendar is a navy rail down the right side.

- **Region names:** the tabs and the banners read "North Asia ex-China" and "South & Southeast Asia".
  Region names sit on one line across all six tabs, with the constraint and direction
  on one line beneath.

- **Signpost squares in the banner** sit on a white strip, so the navy "supports"
  fill and the red "challenges" fill both show against the navy banner and match the
  legend. The "2026–30" and "Beyond 2030" labels are centred over their rating boxes.

- **Banner colour (supersedes the navy banner):** each banner is tinted in its call's
  direction colour: pale green for Easing, pale grey for Persisting, pale red for
  Intensifying. The open tab takes the same tint. The owner found navy too heavy and
  the same on every tab. The rating boxes and signpost squares sit on white insets.
  The calendar rail stays navy.
- **Banner subtitle:** one line, "Power | Easing after 2030". No separate direction box.

- **No white boxes in the banner:** the rating boxes carry a fine outline in their own
  colour and sit directly on the tint; thin vertical lines divide the banner into its
  four parts. The owner found the white insets jarring.

- **Signpost cards:** all white, lifted off the grey page by a soft shadow, with a navy
  rule under the title. No grey header band (it blurred into the page background).

## Open

- The owner has design comments to give on making the site more intuitive.
- Seven readings still need checking at their primary source (`data/followups.json`).
- History charts, the rules file and feeds for most signposts are not built.
