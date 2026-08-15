# Page status: live vs repo

Which pages are known to match the live site, and which have never been checked.
Kept because the repo has one commit and no history, so nothing else can tell you.

Update a row whenever you pull a live page or paste a new one. A row is only
VERIFIED if someone has actually compared the two.

| Status | Meaning |
|---|---|
| **VERIFIED** | Live source pulled and compared. Repo matches the site. |
| **PENDING PASTE** | A newer file exists. Paste it, then mark VERIFIED. |
| **UNVERIFIED** | Never compared. The repo copy may be stale, missing or wrong. |
| **NOT IN REPO** | Live page with no file and no build script anywhere. |

Counts: **1 verified**, **13 pending paste**, **34 unverified**, **8 not in repo**, 56 pages total.

| Section | Page URL | Repo file | Build script | Status | Checked | Notes |
|---|---|---|---|---|---|---|
| Programs | `programs/row-swim-academy` | `row_swim_academy_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/tops-2` | `row_tops_2_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/tops-1` | `row_tops_1_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/junior-development-2` | `row_junior_development_2_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/junior-development-1` | `row_junior_development_1_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/recreation-groups` | `row_recreation_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/age-group-development-2` | `row_age_group_development_2_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/age-group-development-1` | `row_age_group_development_1_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/senior-development` | `row_senior_development_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 | SD also had CMS paste junk removed |
| Programs | `programs/provincial-development-3` | `row_provincial_development_3_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/provincial-development-2` | `row_provincial_development_2_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/provincial-development-1` | `row_provincial_development_1_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs/national-development` | `row_national_development_embed.html` | `build_program_pages.py  STALE` | **PENDING PASTE** | 15 Aug 2026 |  |
| Programs | `programs` | `row_programs_embed.html` | `build_programs_overview.py` | **UNVERIFIED** | — |  |
| Programs | `programs/row-pool-locations` | `row_row_pool_locations_embed.html` | `build_about_and_home.py` | **UNVERIFIED** | — |  |
| Programs | `programs/row-camps--summer-team` | `row_row_camps_summer_team_embed.html` | `build_program_pages.py` | **UNVERIFIED** | — |  |
| About | `about/olympians` | `row_our_olympians_and_paralympians_embed.html` | `build_photo_pages.py` | **VERIFIED** | 15 Aug 2026 | Live diffed, 4 bios folded into script, CMS drift removed, new Fratesi photo |
| About | `about/coaches--operations-team` | `row_coaches_and_operations_team_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — | Same script as Olympians. Do NOT run it until live is diffed |
| For parents | `for-parents/officiating` | `row_officiating_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — | Same script as Olympians. Do NOT run it until live is diffed |
| For swimmers | `for-swimmers/uniforms-and-row-gear` | `row_clothing_and_equipment_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/time-standards` | `row_time_standards_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — |  |
| Development plan | `our-development-plan` | `row_our_development_plan_embed.html` | `build_development_plan.py` | **UNVERIFIED** | — | Index omits How Swimmer Movement Works; lists Goal Setting Tool from another tree |
| Development plan | `our-development-plan/how-we-develop-swimmers` | `row_how_we_develop_swimmers_embed.html` | `(other account)` | **UNVERIFIED** | — | The ROW Way. Revision 2 of the twelve markers |
| Development plan | `our-development-plan/from-plan-to-pool-deck` | `row_from_plan_to_pool_deck_embed.html` | `build_development_plan.py` | **UNVERIFIED** | — | Goal statement wording |
| Development plan | `our-development-plan/the-growth-spurt` | `row_the_growth_spurt_embed.html` | `build_development_plan.py` | **UNVERIFIED** | — | 'trousers' is not Canadian |
| Development plan | `our-development-plan/the-birthday-gap` | `row_the_birthday_gap_embed.html` | `build_development_plan.py` | **UNVERIFIED** | — |  |
| Development plan | `our-development-plan/the-role-of-parents` | `row_the_role_of_parents_embed.html` | `build_the_role_of_parents.py` | **UNVERIFIED** | — | Goal statement wording; 'Parent's run almost everything' |
| Development plan | `our-development-plan/the-training-year` | `row_the_training_year_embed.html` | `build_development_plan.py` | **UNVERIFIED** | — | Peak meet promised to every family |
| Development plan | `our-development-plan/how-swimmer-movement-works` | `—` | `—` | **NOT IN REPO** | — | LIVE AND UNOWNED. No file, no script, in either repo. Carries revision 1 of the twelve markers |
| Development plan | `our-development-plan/what-to-expect` | `row_what_to_expect_embed.html` | `build_development_plan.py` | **UNVERIFIED** | — | Named four ways. Peak meet promised to every family |
| Coaching (coach only) | `coaching-at-row` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | 7 of 8 fail row_vocabulary.py |
| Coaching (coach only) | `coaching-at-row/how-we-plan-training` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | 7 of 8 fail row_vocabulary.py |
| Coaching (coach only) | `coaching-at-row/how-we-design-training` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | 7 of 8 fail row_vocabulary.py |
| Coaching (coach only) | `coaching-at-row/the-training-week` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | 7 of 8 fail row_vocabulary.py |
| Coaching (coach only) | `coaching-at-row/the-practice-session` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | 7 of 8 fail row_vocabulary.py |
| Coaching (coach only) | `coaching-at-row/the-individual-swimmer` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | 7 of 8 fail row_vocabulary.py |
| Coaching (coach only) | `coaching-at-row/the-row-way-in-detail` | `(other Claude account)` | `(other account)` | **NOT IN REPO** | — | Not created in the CMS yet |
| Home | `home` | `row_home_embed.html` | `various` | **UNVERIFIED** | — |  |
| News | `news` | `row_news_embed.html` | `various` | **UNVERIFIED** | — |  |
| News | `news/monthly-newsletters` | `row_monthly_newsletters_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about` | `row_about_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/board-of-directors` | `row_board_of_directors_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/board-sub-committees` | `row_board_sub_committees_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/club-info` | `row_club_info_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/row-careers` | `row_row_careers_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers` | `row_for_swimmers_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/all-row-records` | `row_all_row_records_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/row-equipment-list` | `row_row_equipment_list_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/goal-setting-tool` | `(row-gm/row-swimming-math)` | `various` | **UNVERIFIED** | — | Separate repo |
| For parents | `for-parents` | `row_for_parents_embed.html` | `various` | **UNVERIFIED** | — |  |
| For parents | `for-parents/parent-guide` | `row_parent_guide_embed.html` | `various` | **UNVERIFIED** | — |  |
| For parents | `for-parents/fpp-guide` | `row_fpp_guide_embed.html` | `various` | **UNVERIFIED** | — |  |
| For parents | `for-parents/registration-fees` | `row_registration_fees_embed.html` | `various` | **UNVERIFIED** | — |  |
| Events | `events` | `row_events_embed.html` | `various` | **UNVERIFIED** | — |  |
| Events | `events/row-hosted-meets` | `row_row_hosted_meets_embed.html` | `various` | **UNVERIFIED** | — |  |
| Safety | `sport-safety` | `row_sport_safety_embed.html` | `various` | **UNVERIFIED** | — |  |

---

## How to verify a page

1. Open the page in the CMS, click **Source**, copy everything.
2. Save it as `pages/row_<h1-in-lower-snake-case>_embed.html`.
3. Diff it against the repo copy. If they differ, **the live page wins** —
   fold the difference into the build script, not the other way round.
4. Run the three checks: `row_vocabulary.py`, `row_style_check.py`,
   `row_css_check.py`.
5. Mark the row VERIFIED with today's date.

## Do not run these build scripts yet

- `build_program_pages.py` — behind the site. The 13 program pages committed on
  15 August are the source of truth; the script has not caught up.
- `build_photo_pages.py` — current for Olympians only. It also builds Coaches
  and Operations Team, Officiating, Clothing and Equipment, and Time Standards,
  none of which have been diffed against live. Running it could overwrite real
  edits.

## Not on this list

- `ROW_Coaching_Framework_Decisions.md` — deliberately kept out of this public
  repo; it holds contested numbers and notes on coach pushback. It is versioned
  nowhere. That is a gap.
- The build guide, the IM tool design spec, the project instructions and the
  handover file. None are in any repo.
