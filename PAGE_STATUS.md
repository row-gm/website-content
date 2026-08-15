# Page status: live vs repo

Which pages are known to match the live site, and which have never been checked.
Kept because the repo has no useful history, so nothing else can tell you.

A row is only VERIFIED if someone has actually compared the two.

File names follow section 19 of the decisions record: `row_<section>_<h1>_embed.html`.

| Status | Meaning |
|---|---|
| **VERIFIED** | Live source pulled and compared. Repo matches the site. |
| **UNVERIFIED** | Never compared. The repo copy may be stale, missing or wrong. |
| **NOT IN REPO** | Live page, or planned page, with no file in this repo. |

Counts: **25 verified**, **32 unverified**, **3 not in repo**, 60 rows.

| Section | Page URL | Repo file | Build script | Status | Checked | Notes |
|---|---|---|---|---|---|---|
| Programs | `programs/row-swim-academy` | `row_programs_swim_academy_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/tops-2` | `row_programs_tops_2_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/tops-1` | `row_programs_tops_1_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/junior-development-2` | `row_programs_junior_development_2_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/junior-development-1` | `row_programs_junior_development_1_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/recreation-groups` | `row_programs_recreation_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/age-group-development-2` | `row_programs_age_group_development_2_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/age-group-development-1` | `row_programs_age_group_development_1_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/senior-development` | `row_programs_senior_development_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/provincial-development-3` | `row_programs_provincial_development_3_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/provincial-development-2` | `row_programs_provincial_development_2_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/provincial-development-1` | `row_programs_provincial_development_1_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs/national-development` | `row_programs_national_development_embed.html` | `build_program_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Programs | `programs` | `row_programs_programs_embed.html` | `build_programs_overview.py` | **UNVERIFIED** | — |  |
| Programs | `programs/row-camps--summer-team` | `row_programs_row_camps_summer_team_embed.html` | `build_program_pages.py  STALE` | **UNVERIFIED** | — |  |
| Development plan | `our-development-plan` | `row_devplan_our_development_plan_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 | Index row for How Swimmer Movement Works added |
| Development plan | `our-development-plan/how-we-develop-swimmers` | `row_devplan_the_row_way_embed.html` | `(other Claude account)` | **VERIFIED** | 15 Aug 2026 | Slug kept as how-we-develop-swimmers, decided 15 Aug. Carries the twelve markers, section 18 |
| Development plan | `our-development-plan/from-plan-to-pool-deck` | `row_devplan_from_plan_to_pool_deck_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/the-growth-spurt` | `row_devplan_the_growth_spurt_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 | trousers changed to pants |
| Development plan | `our-development-plan/the-birthday-gap` | `row_devplan_the_birthday_gap_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/the-role-of-parents` | `row_devplan_the_role_of_parents_embed.html` | `build_the_role_of_parents.py  STALE` | **VERIFIED** | 15 Aug 2026 | Goal statement, apostrophe typo and CMS paste residue fixed |
| Development plan | `our-development-plan/the-training-year` | `row_devplan_the_training_year_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 | Numbered zones are correct. Source of the six phase names |
| Development plan | `our-development-plan/how-swimmer-movement-works` | `row_devplan_how_swimmer_movement_works_embed.html` | `(none)` | **VERIFIED** | 15 Aug 2026 | Converted from 119 inline styles to 104 classes on 15 Aug. Was the last page not using the stylesheet |
| Development plan | `our-development-plan/what-to-expect` | `row_devplan_what_to_expect_at_meets_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 | Meet table rewritten to the tag system. Slug being updated by the GM |
| Meets and events | `events/meet-schedule` | `row_meets_meets_and_events_overview_embed.html` | `build_meets_and_policies.py  STALE` | **VERIFIED** | 15 Aug 2026 | Retitled from Meet and Event Schedule. SportsEngine help link removed |
| Meets and events | `events/confirm-and-decline` | `row_meets_confirm_or_decline_embed.html` | `(none)` | **VERIFIED** | 15 Aug 2026 | Was in no repo until 15 Aug. Seven CSS classes it uses were undefined. SportsEngine help block removed |
| Meets and events | `events/row-hosted-meets` | `row_meets_hosted_meets_embed.html` | `build_meets_and_policies.py` | **UNVERIFIED** | — | Link text updated 15 Aug, but the page is not diffed against live |
| About | `about/olympians` | `row_about_our_olympians_and_paralympians_embed.html` | `build_photo_pages.py` | **VERIFIED** | 15 Aug 2026 | Live diffed, four bios folded into the script, CMS drift removed, new Fratesi photo |
| About | `about/coaches--operations-team` | `row_about_coaches_and_operations_team_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — | Do NOT run the script until live is diffed. Needs the current stylesheet |
| For parents | `for-parents/officiating` | `row_parents_officiating_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — | Link text updated 15 Aug. Needs the current stylesheet. Not diffed against live |
| For swimmers | `for-swimmers/uniforms-and-row-gear` | `row_swimmers_clothing_and_equipment_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/time-standards` | `row_swimmers_time_standards_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — |  |
| For coaches | `coaching-at-row` | `row_coaches_coaching_at_row_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py. Zone colours were retired in favour of numbers |
| For coaches | `coaching-at-row/how-we-plan-training` | `row_coaches_how_we_plan_training_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py. Zone colours were retired in favour of numbers |
| For coaches | `coaching-at-row/how-we-design-training` | `row_coaches_how_we_design_training_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py. Zone colours were retired in favour of numbers |
| For coaches | `coaching-at-row/the-training-week` | `row_coaches_the_training_week_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py. Zone colours were retired in favour of numbers |
| For coaches | `coaching-at-row/the-practice-session` | `row_coaches_the_practice_session_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py. Zone colours were retired in favour of numbers |
| For coaches | `coaching-at-row/the-individual-swimmer` | `row_coaches_the_individual_swimmer_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py. Zone colours were retired in favour of numbers |
| For coaches | `coaching-at-row/the-row-way-in-detail` | `(other Claude account)` | `(other Claude account)` | **NOT IN REPO** | — | Never created in the CMS. Do not paste as it stands: retired vocabulary, and the rejected marker revision |
| Home | `home` | `row_home_embed.html` | `various` | **UNVERIFIED** | — |  |
| Home | `home` | `row_home_main_body_embed.html` | `various` | **UNVERIFIED** | — |  |
| Home | `home` | `row_home_footer_embed.html` | `various` | **UNVERIFIED** | — |  |
| News | `news` | `row_news_news_embed.html` | `various` | **UNVERIFIED** | — |  |
| News | `news/monthly-newsletters` | `row_news_club_newsletters_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about` | `row_about_about_us_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/board-of-directors` | `row_about_board_of_directors_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/board-sub-committees` | `row_about_board_committees_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/club-info` | `row_about_club_info_and_policies_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/club-info` | `row_about_withdrawal_policy_embed.html` | `various` | **UNVERIFIED** | — | h1 reads Club Info and Policies. Two files, one page? |
| About | `programs/row-pool-locations` | `row_about_pool_locations_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `programs/row-pool-locations` | `row_about_pool_locations_source.html` | `various` | **UNVERIFIED** | — | No row- classes and no row-wrap. A source scrape, not a built page |
| For swimmers | `for-swimmers` | `row_swimmers_for_swimmers_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/all-row-records` | `row_swimmers_club_records_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/row-equipment-list` | `row_swimmers_equipment_list_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/goal-setting-tool` | `(row-gm/row-swimming-math)` | `various` | **NOT IN REPO** | — | Separate repo |
| For parents | `for-parents` | `row_parents_for_parents_embed.html` | `various` | **UNVERIFIED** | — |  |
| For parents | `for-parents/parent-guide` | `row_parents_how_to_get_involved_embed.html` | `various` | **UNVERIFIED** | — |  |
| For parents | `for-parents/fpp-guide` | `row_parents_fpp_reporting_and_tracking_embed.html` | `various` | **UNVERIFIED** | — |  |
| For parents | `for-parents/registration-fees` | `(not in repo)` | `various` | **NOT IN REPO** | — | Linked from every program page Fees chip |
| Top level | `sport-safety` | `row_sport_safety_embed.html` | `various` | **UNVERIFIED** | — | Top level in the nav, so it takes no section prefix |

---

## Done on 15 August 2026

**13 program pages.** Pulled from live, edited, pasted, committed. Applied: the
goal statement per section 15, Canadian spelling, `taper` to Peaking, `AGD1` to
`AGD 1`, phone table labels corrected, the Fees chip, new group sizes and
descriptions, and CMS paste residue removed from Senior Development. Later, the
age band phrasing and the six phase names were aligned to the development plan,
per section 20.

**9 development plan pages.** The twelve markers were confirmed against live and
recorded in section 18; the proposed revision 2 was never adopted and is dropped.
How Swimmer Movement Works was converted from 119 inline styles to 104 classes,
which was the last page on the site not using the shared stylesheet.

**3 meets and events pages.** Meets and Events Overview retitled. Confirm or
Decline found live and in no repo. Every SportsEngine help link removed, since
Confirm or Decline now explains the same thing in ROW's own words.

**Our Olympians and Paralympians.** Rebuilt after CMS drift: 34 heading blocks
where the build makes 16, 17 of them empty.

## The stylesheet grew from 34 classes to 59

Every page pulled from live turned up classes the stylesheet had never defined,
so those parts of those pages had never rendered correctly:

| Added | For |
|---|---|
| `row-stage-*`, 6 | coach and official names on three pages |
| `row-faq-*`, `row-pill`, 5 | the FAQ blocks and meet tag badges |
| `row-step-*`, `row-btn-*`, 7 | numbered walkthroughs and buttons |
| `row-grid-*`, `row-chip-l/v`, `row-framed`, `row-bar*`, 8 | the twelve markers grid |

It also gained vertical rhythm. Block spacing used to come from
`<div style="margin:24px 0 0;">` wrappers that build scripts emitted, so pages
written in the CMS had none and everything stacked flush. `.row-wrap > *` now
carries it. **Do not add spacer divs back**; they would double the gap.

Expect more missing classes as the remaining pages are pulled. Run
`row_css_check.py` on every page that comes in from the CMS.

## Still open on verified pages

- Two slugs no longer match their page. `how-we-develop-swimmers` is The ROW Way,
  and that slug is being kept deliberately. `what-to-expect` is being updated.
- `row_about_withdrawal_policy_embed.html` and `row_about_club_info_and_policies_embed.html`
  may be the same page twice. Not yet checked.
- `row_about_pool_locations_source.html` is not a built page. It has no classes and
  no wrapper. Decide whether to convert it or drop it.

## How to verify a page

1. Open the page in the CMS, click **Source**, copy everything.
2. Save it as `row_<section>_<h1 in lower snake case>_embed.html`.
3. Diff it against the repo copy. If they differ, **the live page wins** — fold the
   difference into the build script, not the other way round.
4. Run `row_vocabulary.py`, `row_style_check.py` and `row_css_check.py`.
5. Paste the current stylesheet into the page's custom CSS field.
6. Mark the row VERIFIED with today's date.

## Do not run these build scripts

- `build_program_pages.py` — behind the site.
- `build_development_plan.py` and `build_the_role_of_parents.py` — behind the site.
- `build_meets_and_policies.py` — behind the site.
- `build_photo_pages.py` — current for Olympians only. It also builds four pages
  that have never been diffed against live.

## Not on this list

- `ROW_Coaching_Framework_Decisions.md` — deliberately kept out of this public repo;
  it holds contested numbers and notes on coach pushback. It is versioned nowhere.
- The build guide, the IM tool design spec, the project instructions and the
  handover file. None are in any repo.
