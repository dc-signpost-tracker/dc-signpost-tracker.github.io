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

- **Signpost cards:** all white, lifted off the grey page by a soft shadow, with a rule
  under the title in the banner's tint (not navy). No grey header band (it blurred into the page background).

## Design changes (20 Nov 2026, evening)

- **Title** runs across the full page width on one line.
- **"Last refreshed"** is small, italic and muted.
- **Signpost key** (supports / challenges / no signal yet) sits inside the banner, in
  small type under the signpost squares, not above the tabs.
- **Calendar rail:** the countdown ("in 19 days") is italic and not bold, to separate it
  from the date. Each event ends with an italic line "Relevant for: Signpost A1 Capacity
  auctions" (several signposts are listed with semicolons) in place of a bare label.
- **Tagline** under the title, in the owner's own wording: "The outlook for physical
  constraint severity in select regions till 2030 and beyond, tested against 24 signposts".
- **Next catalyst in the banner:** a tear-off calendar tile (month band in the call's
  direction colour, day, year) to the right of the countdown and the event text. Built on the
  recommended option because the owner left that card unanswered; he may still change it.

- **Tab order** is grouped by region: North America Power, North America Land, Europe
  Power, Europe Water, North Asia ex-China Power, South & Southeast Asia Water.
- **Signposts relettered on 20 Nov 2026 (evening)** so the letters follow the tab order.
  Old to new: D (North America Land) became B; E (Europe Water) became D; B (North Asia
  ex-China Power) became E. A, C and F are unchanged. Numbers are unchanged (old D3 is
  B3). Entries in this file written before that time use the old letters.
- **Calendar notes** sit on their own "Note:" line, not after "Relevant for".

- **Banner key** is 10px. **"Watch for" and "What the call depends on":** each statement
  sits on its own line with a round bullet in the call's direction colour (vertical bars
  were tried and the owner found them confusing).

- **A3 Turbine supply** (revised 21 Nov 2026, replacing the earlier "GE Vernova only"
  wording): tracks large gas turbines (215 megawatts and above) used by US utilities.
  Headline in plain English: "Turbine waiting list still growing" (or "shrinking" once
  deliveries outpace orders), with the numbers in the sentence below (orders taken against
  turbines delivered). No ratios or jargon in the headline. Beside it, the earliest delivery slot on sale ("sold out to
  2029–30"). The US order count by maker is context, not the headline (the owner noted a
  count alone says nothing about easing). Makers: GE Vernova, Mitsubishi Heavy Industries and Doosan
  Enerbility; Siemens Energy is noted only while its US share stays small. Small turbines
  and other on-site power are out of scope. Trigger: positive if large-turbine orders
  fall below shipments, so backlogs stop rising, and delivery slots before 2030 reappear.

- **Source link on each card** is an "i" in a circle (hover text "Open the primary
  source"), not the words "Primary source". Cards without a verified source still show
  "Not yet verified" in words, as the rules require.

- **"How to read this"** keeps two boxes only: Ratings and Signpost status. "How the data
  refreshes" and "Open data issues" were removed at the owner's request.

## Go-live (20 Nov 2026, evening)

- The owner said "go live". The repository moved to the organisation
  `dc-signpost-tracker` and was renamed `dc-signpost-tracker.github.io`. It is public and
  served by GitHub Pages from branch `main` at https://dc-signpost-tracker.github.io/
- Every push to `main` now publishes to the public site within a minute or two.
- The morning digest task points at the new repository name.

## Decisions (21 Nov 2026)

- **How a status change is written up:** when a signpost's status changes, the reading
  gives the facts in a balanced way: what happened and why it supports the change, and
  equally what is not yet settled (for Spain's decree: not yet in the official gazette, a
  planned court challenge, the opposition's pledge to repeal, and which sites the water
  rule covers and from when). "Next" names the next critical date (there, the general
  election of 29 Nov 2026).
- **A catalyst that arrives early** is recorded on the date it happened, with its
  outcome, and the next critical date becomes the catalyst shown.
- **Digest runs weekly (decided 21 Nov 2026, evening):** the signpost digest runs every
  Wednesday morning, not every day, to save usage while the tracker is still a work in
  progress. The feeds still refresh daily on GitHub's scheduler. Each run covers
  everything since each signpost's `last_checked_on` date. This supersedes "every
  morning" in the entries above.

## Redesign (21 Nov 2026)

The owner reviewed the site as a first-time reader would and approved:

- **Landing page:** the site opens on an overview. "The picture today" paragraph; a grid
  of all eight regions by power, water and land, with the six tracked pairs solid and
  clickable and the rest faded; "What changed"; and "Why these six". Each pair opens its
  region page, which keeps the six tabs and has "← All regions" at the top. The owner
  chose the grid over a map-style layout and a table-first layout.
- **Signals, not stances:** cards say "Constraint tightening" (red, status `neg`) or
  "Constraint easing" (green, status `pos`) instead of "Supports / Challenges call".
  The "Rating under review" rule is unchanged.
- **Bottom line** sentence at the top of each region page; **trigger line** on each card;
  **delta** beside the headline figure only where the earlier figure is in the data;
  **verified count** in each banner ("2 of 3 readings verified at the primary source").
- **Calendar:** next six weeks shown; later and passed dates folded away; each
  "Relevant for" jumps to its card.
- Card colour follows the owner-approved status only; no good-or-bad colouring of
  readings that have no status.
- **Signpost order:** ranked once by materiality and renumbered on 21 Nov 2026 (14:23),
  so the first card in each call is the most material. The order stays fixed; it is not
  tied to the next catalyst date. Old to new: A4 to A2 and A2 to A4; B3 to B2 and B2 to
  B3; C3 to C1, C1 to C2, C2 to C3; D5 to D3 and D3 to D5; E2 to E1, E4 to E2, E5 to E3,
  E1 to E4, E3 to E5. A1, A3, A5, A6, B1, D1, D2, D4, F1 and F2 are unchanged. Entries
  in this file written before then use the old numbers.

- **Shapes:** signposts are circles everywhere (banner, legends, overview), matching the
  numbered circles on the cards; rectangles are kept for severity ratings only, so the two
  are not confused (owner, 21 Nov 2026).

- **Landing page look (21 Nov 2026):** full-width navy-to-teal header behind the title and
  "The picture today", on the landing page only; no row of key numbers; grid heading "What
  we currently track"; every grid cell the same size as a tracked pair, untracked ones
  faded. The owner looked at a constraint-colour version and a full heatmap and chose this.

- **Landing page refinements (21 Nov 2026, 15:17):** the line under "What we currently
  track" is the coverage note in the owner's wording, and the separate "Why these six" box
  is gone. "What changed" is a timeline on a beige panel (changed from navy at the owner's request, as navy clashed with the header) with signpost labels in circles. Tracked cells
  show a round arrow button instead of "Open →", and "Next catalyst: <full date>" in
  italics at the bottom left. "How to read this" is quiet grey notes below a rule, not
  boxed cards.

- **Grid legend** sits on one line, in small type, above the grid rather than below it (21 Nov 2026).
- **Header art (21 Nov 2026):** a faint line drawing of a data centre campus (halls with
  rooftop cooling, a substation, pylons and a water tank) fades in on the right of the
  landing-page header. It was drawn for the site; no stock photo is used.

- **Phones (21 Nov 2026):** the owner now wants the site to work on phones as well as
  computers (this replaces the earlier "computer screen only" rule). On narrow screens the
  landing grid becomes full-width cards grouped by region, untracked pairs are listed
  under each region or folded into "Regions not tracked", and the legend wraps. Region
  pages stack into one column and the selected tab scrolls into view. The computer layout
  is unchanged.

- **Digest schedule (confirmed 23 Nov 2026):** the morning digest runs weekly, on
  Wednesdays at 07:08 Singapore time. The GitHub feed check still runs every day and only
  collects documents into the inbox; the Wednesday digest reads everything that arrived
  during the week.

- **"Last refreshed" (23 Nov 2026):** shows the date of the last digest, when the
  signposts were reviewed. The daily feed check no longer changes it.

## Two calls added (23 Nov 2026)

- **Coverage widened to eight calls and 38 signposts.** At the owner's request the
  tracker now also follows North America Water and Europe Land, both Moderate in both
  periods, to complete power, water and land for North America and Europe. The question
  on each is whether Moderate eases to Minor or intensifies to Severe. Each has seven
  signposts taken from the owner's analysis pages.
- **Relettered again so letters follow the tab order.** Tabs: A North America Power,
  B North America Water (new), C North America Land, D Europe Power, E Europe Water,
  F Europe Land (new), G North Asia ex-China Power, H South & Southeast Asia Water.
  Old to new: B to C, C to D, D to E, E to G, F to H; numbers unchanged (old C3, Spain's
  final rules, is now D3). Entries above this point use the older letters.
- **Baseline for B and F is 23 Nov 2026.** Their readings are baseline readings from the
  owner's analysis, shown as "Not yet verified" until a primary source is read.
- **Review flag on holding calls:** a signal in either direction flags B or F.
- The tagline now says 38 signposts and the coverage note under "What we currently
  track" was reworded for eight pairs (wording to be confirmed by the owner, along with
  the two new bottom lines).

- **Charts on cards (23 Nov 2026):** five signposts (A1, A2, A3, A6, G3) show their time
  series as an interactive chart or table on the card, from `data/series.json`, using the
  figures in the owner's analysis pages. The digest appends new points as they are
  published and read at source. A2's approved-to-energise and observed-peak lines were
  added from the owner's figures. The PJM reserve margin chart shows data labels.

## Nineteen signposts added (23 Nov 2026)

- After a source sweep of 23 proposed signposts, the owner approved 19: the 15 with a
  dependable source and 4 that can only be followed through news (A10 on-site power, E7
  water company objections, G7 Japan's siting shift, H6 India's hubs). Four were dropped
  or merged: water used by power plants, flexible connections, low-water cooling uptake,
  and the share of the pipeline in water-stressed areas. Taiwan was excluded earlier.
- Added at the end of each tab so the new ones are easy to see: A7 Texas high-voltage
  lines, A8 New generation connecting, A9 Who pays for the grid, A10 On-site power, A11
  Build-out plans (all regions); C4 Local pauses and bans, C5 State tax incentives, C6
  Federal sites; D4 Britain's connection-queue reform, D5 Ireland's connection policy; E6
  Reported water use, E7 Water company objections; F8 Ireland's planning decisions; G6
  Tokyo-area grid upgrades, G7 Japan's siting shift; H3 Thailand's water-reuse rule, H4
  Johor reclaimed water and tariffs, H5 Johor reservoir levels, H6 India's hubs.
- All start at "No signal yet" and "Not yet verified", with a "New" tag. Baseline 23 Nov
  2026. Names, trigger wording and headlines were drafted by Claude and await the owner's
  confirmation. Relabelling and ordering by urgency are deferred at the owner's request.
- The site now has 57 signposts; the tagline says so.

- **"News, no signal" (23 Nov 2026):** at the owner's request, a signpost where new
  developments were reviewed but did not cross the trigger now shows "News, no signal"
  instead of "No signal yet", in the same grey. It applies when the history holds a
  reviewed development (kind "reading"). Wording chosen by Claude; alternatives offered.

- **Verified-readings counter removed (24 Nov 2026):** the "X of N readings verified at
  the primary source" line on each call's banner was deleted at the owner's request. Each
  card still shows "Not yet verified" where that applies.

- **Card layout (25 Nov 2026):** on computer screens a card with charts takes two rows, so
  the two plain cards next to it stack and share its height instead of each stretching to
  the full height (e.g. A3 beside A4 and A5; A6 beside A7 and A8). Phones are unchanged.

- **Two signposts dropped, two relettered (25 Nov 2026):** the owner dropped A8 New
  generation connecting (it overlaps with A1, and both are about PJM: keep A1 only) and A11
  Build-out plans (it measures demand across all regions, not a constraint). A9 Who pays for
  the grid stays, to be ranked low when signposts are reordered by urgency. To avoid gaps,
  the old A9 Who pays for the grid became A8 and the old A10 On-site power became A9. The
  site now has 55 signposts.

- **North America Water reordered by criticality (25 Nov 2026):** the owner approved this
  order, most critical first, and the signposts were relettered: B1 Hard limits in law
  (was B6), B2 Colorado River shortage (was B5), B3 Drought curtailments (was B7), B4
  Closed-loop becomes standard (was B1), B5 Water planning catches up (was B3), B6 Reclaimed
  water at scale (was B2), B7 Growth shifts to water-rich basins (was B4). Earlier entries
  in this file use the old letters.
- **B4 rescoped (25 Nov 2026):** Closed-loop becomes standard now tracks the whole US, with
  Microsoft kept as one example; headline "17 billion gallons" (on-site use in 2023, national
  laboratory estimate). The owner approved correcting the 2028 range in the trigger, but the
  primary report shows 16 to 33 billion gallons is right for hyperscale sites, so the trigger
  was then reworded with the owner's approval to say it covers the largest cloud sites.

- **B2 and B3 swapped (25 Nov 2026):** Drought curtailments is now B2 and Colorado River
  shortage is B3. The owner noted the Colorado River mainly affects Phoenix (plus Las Vegas
  and Tucson), not the largest hubs, and mostly indirectly, while a drought curtailment is a
  direct hard stop that can hit any hub.

- **North America Land reordered by criticality (25 Nov 2026):** owner approved, most
  critical first: C1 Projects disrupted (unchanged), C2 Local pauses and bans (was C4), C3
  State or federal override (was C2), C4 State tax incentives (was C5), C5 Community benefit
  deals (was C3), C6 Federal sites (unchanged). Community deals stays above Federal sites
  because it is named in the call's "Eases if" line.

- **"Eases if" points follow signpost order (25 Nov 2026):** at the owner's request each
  call's "Eases if" (or "Stays contained if") points are now listed in the order of the
  signposts that track them. Wording unchanged; points reordered on A, B, C, D, E and H
  (F and G already matched).

- **C2 tracker chosen (25 Nov 2026):** Local pauses and bans uses the US Data Center
  Moratorium Tracker (approved moratoria and bans, with active and permanent shown
  separately); the National League of Cities tracker is a cross-check. The trigger now uses
  the active count, so expiring pauses can show: "Positive if the number of active pauses and
  bans stops rising and pauses expire without being renewed." Headline "320+ localities"
  (11 Oct 2026, press-reported until the tracker is opened).

- **Bottom lines updated for the new signposts (25 Nov 2026):** the owner approved new
  bottom lines on all eight calls, drafted by Claude to reflect the signposts added on 23
  Nov 2026 and the reorders of 25 Nov 2026, plus changes to "What the call depends on" on B
  (Severe list reordered), C (tax incentives added) and G (Inzai grid upgrades added).
- **Banners kept in step (25 Nov 2026):** the owner asked that the weekly digest check the
  banner text against the signposts after any change and draft updates for his approval.
  Open gaps noted for later: "avoid water-stressed areas" has no signpost on calls E and H;
  E1 and E6 both show 0.58 litres; "The picture today" does not mention calls B and F.

- **B1 and B2 readings corrected (25 Nov 2026):** with the owner's approval, B1 no longer
  says Chandler caps data centre water use (its rules cover siting and noise; Mesa, Avondale
  and Phoenix cap industrial water use) and says no Arizona statewide pause bill has been
  found. B2's headline became "Georgia utilities balking", cited to Bloomberg Law (June
  2026). Both stay "Not yet verified" until the original documents are read.

- **Unverified caveat softened (25 Nov 2026):** the red "Not yet verified" label became a
  small grey italic caveat, "Press-reported; to be verified against primary source", at the
  owner's request, because the red label read as a credibility problem.
- **Headline style (25 Nov 2026):** the owner found headlines whose summary continued the
  sentence (e.g. "Georgia utilities balking" / "At large data centre water requests...")
  unintuitive. All such cards were rewritten so the summary is a complete sentence: A6, A8,
  A9, B2, B3, B6, B7, C1, C2, C4, D1, D2, D4, E1, E3, E5, E6, F8, G2, G3, G4, G6, G7, H1, H2,
  H4, H5, H6. Headlines changed on B2 ("Pushback in Georgia"), B3 ("1.25 million acre-feet
  cut a year") and C1 ("Over half disrupted"). The rule is in OPERATING_RULES.md.

- **Legacy analysis retired as a source (25 Nov 2026):** the owner said his analysis pages
  are stale and the website is what lives on. Readings that rested on them (C1, F3, F4, G1,
  and the timing view on F1) were re-sourced from web sources. G1's headline became "About
  60% around Seoul" (Korea had no reading before); F4 drops Cologno Monzese and Pyhäjoki,
  which could not be sourced; F3 now uses the economy ministry's site counts and the July
  2026 rulings at Alixan and Le Bourget.

- **Gauge redrawn (25 Nov 2026):** the owner found C1's gauge confusing ("over 50%" and
  "trigger 25%" on one line). Now the label sits alone above the bar, "Now: ..." is written
  over the dot, the trigger is written under its own tick (C1: "Eases below 25%"), and the
  easing zone is shaded green where there is one (A1, C1). Applies to A1, C1, E1 and G2.

- **C1 trigger changed (25 Nov 2026):** the owner replaced the 25% threshold, which had no
  basis, with "Positive if the share of large projects blocked or delayed falls consistently
  for several quarters." The measure is the share, not the count (the count already fell
  from 75 to 45 between the first and second quarters of 2026 while the share stayed above
  half). The gauge now shows only the current reading.

- **Europe Power order kept; D1 renamed (25 Nov 2026):** the owner kept the order D1 to D5
  (D4 Britain and D5 Ireland stay last as country-specific). D1 was renamed from "Earlier
  grid expansions" to "Grid fixes: Amsterdam, Frankfurt, London" so the header says
  which hubs it covers.

- **Europe Water reordered; pipeline signpost dropped (25 Nov 2026):** the owner dropped
  Pipeline in water-stressed areas (was E4: no source publishes the figure before August
  2027) and approved this order: E1 European Union minimum standards (unchanged), E2
  Reported water use (was E6), E3 Spain's final rules on water (was E2), E4 Drought (was
  E3), E5 French permit refusals (unchanged), E6 Water company objections (was E7). E1's
  headline became "No limit set yet" and the 0.58 against 0.4 litres bar moved to E2, so
  the two cards no longer share a headline. "Data centres avoid water-stressed areas" was
  cut from "Stays contained if" as nothing tracks it. The site now has 54 signposts.

- **Europe Land reordered; Europe headers name their geography (25 Nov 2026):** owner
  approved, most critical first: F1 Europe-wide project rejections (was F4, "Projects rejected or restricted"),
  F2 EU fast-track permitting (was F1), F3 England's national route (was F2, "UK national
  route"), F4 France's fast-track (was F3), F5 Local bans: Netherlands and Scotland (was
  "Local bans spread"), F6 Contested appeals: Scotland and England, F7 Ireland's planning
  decisions (was F8), F8 Powered-land prices: Frankfurt (was F7). On Europe Water: "EU-wide
  reported water use", "Drought: EU and UK", "UK water company objections". The owner asked
  that every Europe signpost header say whether it is EU-wide or country-specific.

- **North Asia ex-China Power: two merges and a reorder (25 Nov 2026):** to manage the
  signpost count the owner merged Korea's exemption threshold (was G4) into Korea's regional
  connections, and Japanese connection times (was G2) into Japan's siting shift, moving
  their readings, sources, history and the Osaka-against-Tokyo bar across. New order, most
  critical first: G1 Japan's siting shift (was G7), G2 Korea's regional connections (was
  G1), G3 Japan's nuclear restarts (unchanged, keeps its chart), G4 Tokyo-area grid upgrades
  (was G6), G5 Korea's transmission build (unchanged). Headers now name the country. The
  site now has 52 signposts.

- **G1 simplified (25 Nov 2026):** the owner pointed out that the Osaka-against-Tokyo
  connection-time bar does not fit a signpost about capacity moving outside both cities.
  The bar was removed and the trigger went back to a single test: "Positive if a meaningful
  share of new capacity is committed outside Tokyo and Osaka." The owner then noted that without connection times the card read like a land
  issue, so the summary keeps the power reason: Tokyo takes 8 to 10 years to connect, and
  policy steers sites to regions with spare grid.

## Open

- Seven readings still need checking at their primary source (`data/followups.json`).
- History charts, the rules file and feeds for most signposts are not built.
