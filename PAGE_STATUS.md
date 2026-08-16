# Page status: live vs repo

Which pages are known to match the live site, and which have never been checked.
A row is only VERIFIED if someone has compared the two.

File names follow section 19 of the decisions record: `row_<section>_<h1>_embed.html`.

| Status | Meaning |
|---|---|
| **VERIFIED** | Live source pulled and compared. Repo matches the site. |
| **UNVERIFIED** | Never compared. The repo copy may be stale, missing or wrong. |
| **NOT IN REPO** | Live or planned page with no file here. |

Counts: **33 verified**, **26 unverified**, **4 not in repo**, 64 rows.

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
| Programs | `programs` | `row_programs_programs_overview_embed.html` | `build_programs_overview.py` | **UNVERIFIED** | — | Uses RSA once |
| Programs | `programs/row-camps--summer-team` | `row_programs_row_camps_summer_team_embed.html` | `build_program_pages.py  STALE` | **UNVERIFIED** | — |  |
| Development plan | `our-development-plan` | `row_devplan_our_development_plan_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/how-we-develop-swimmers` | `row_devplan_the_row_way_embed.html` | `(other Claude account)` | **VERIFIED** | 15 Aug 2026 | Slug kept deliberately. Twelve markers, section 18 |
| Development plan | `our-development-plan/from-plan-to-pool-deck` | `row_devplan_from_plan_to_pool_deck_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/the-growth-spurt` | `row_devplan_the_growth_spurt_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/the-birthday-gap` | `row_devplan_the_birthday_gap_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/the-role-of-parents` | `row_devplan_the_role_of_parents_embed.html` | `build_the_role_of_parents.py  STALE` | **VERIFIED** | 15 Aug 2026 |  |
| Development plan | `our-development-plan/the-training-year` | `row_devplan_the_training_year_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 | Source of the six phase names |
| Development plan | `our-development-plan/how-swimmer-movement-works` | `row_devplan_how_swimmer_movement_works_embed.html` | `(none)` | **VERIFIED** | 15 Aug 2026 | Converted from 119 inline styles to classes |
| Development plan | `our-development-plan/what-to-expect-at-meets` | `row_devplan_what_to_expect_at_meets_embed.html` | `build_development_plan.py  STALE` | **VERIFIED** | 15 Aug 2026 | Uses the meet tag system |
| Meets and events | `events/meet-schedule` | `row_meets_meets_and_events_overview_embed.html` | `build_meets_and_policies.py  STALE` | **VERIFIED** | 15 Aug 2026 | Authority for meet type tags |
| Meets and events | `events/confirm-and-decline` | `row_meets_confirm_or_decline_embed.html` | `(none)` | **VERIFIED** | 15 Aug 2026 | Was in no repo until 15 Aug |
| Meets and events | `events/row-hosted-meets` | `row_meets_hosted_meets_embed.html` | `build_meets_and_policies.py  STALE` | **VERIFIED** | 15 Aug 2026 | Live matched the repo exactly. Link text already updated |
| About | `about/olympians` | `row_about_our_olympians_and_paralympians_embed.html` | `build_photo_pages.py` | **VERIFIED** | 15 Aug 2026 | 711 KB to 413 KB, photos resized |
| About | `about/coaches--operations-team` | `row_about_coaches_and_operations_team_embed.html` | `build_photo_pages.py` | **VERIFIED** | 15 Aug 2026 | Chloe removed, Connor added, titles and bios rewritten, Join our team block |
| For swimmers | `for-swimmers/uniforms-and-row-gear` | `row_swimmers_clothing_and_equipment_embed.html` | `build_photo_pages.py` | **VERIFIED** | 15 Aug 2026 | 137 KB. Two partner logos are oversized |
| For swimmers | `for-swimmers/row-equipment-list` | `row_swimmers_equipment_list_embed.html` | `build_swimmers_and_parents_pages.py  STALE` | **VERIFIED** | 15 Aug 2026 | Recreation kit added, RSA label retired |
| For swimmers | `for-swimmers/time-standards` | `row_swimmers_time_standards_embed.html` | `build_photo_pages.py` | **UNVERIFIED** | — | Same script as Olympians. Not diffed |
| For parents | `for-parents/officiating` | `row_parents_officiating_embed.html` | `build_photo_pages.py` | **VERIFIED** | 15 Aug 2026 | Two graphics moved to row-figure, Marshal merged with Safety Marshal, entries link corrected |
| For coaches | `coaching-at-row` | `row_coaches_coaching_at_row_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py |
| For coaches | `coaching-at-row/how-we-plan-training` | `row_coaches_how_we_plan_training_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py |
| For coaches | `coaching-at-row/how-we-design-training` | `row_coaches_how_we_design_training_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py |
| For coaches | `coaching-at-row/the-training-week` | `row_coaches_the_training_week_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py |
| For coaches | `coaching-at-row/the-practice-session` | `row_coaches_the_practice_session_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py |
| For coaches | `coaching-at-row/the-individual-swimmer` | `row_coaches_the_individual_swimmer_embed.html` | `(other Claude account)` | **UNVERIFIED** | — | Fails row_vocabulary.py |
| For coaches | `coaching-at-row/the-row-way-in-detail` | `(other Claude account)` | `(other Claude account)` | **NOT IN REPO** | — | Never created in the CMS. Retired vocabulary |
| Home | `home` | `row_home_embed.html` | `various` | **UNVERIFIED** | — |  |
| Home | `home` | `row_home_main_body_embed.html` | `various` | **UNVERIFIED** | — |  |
| Home | `home` | `row_home_footer_embed.html` | `various` | **UNVERIFIED** | — |  |
| News | `news` | `row_news_news_embed.html` | `various` | **UNVERIFIED** | — |  |
| News | `news/monthly-newsletters` | `row_news_club_newsletters_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about` | `row_about_about_us_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/board-of-directors` | `row_about_board_of_directors_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/board-sub-committees` | `row_about_board_committees_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `about/club-info` | `row_about_club_info_and_policies_embed.html` | `various` | **UNVERIFIED** | — | Near duplicate of the withdrawal policy file |
| About | `about/club-info` | `row_about_withdrawal_policy_embed.html` | `various` | **UNVERIFIED** | — | Same h1 as club_info_and_policies. Only one can be live |
| About | `programs/row-pool-locations` | `row_about_pool_locations_embed.html` | `various` | **UNVERIFIED** | — |  |
| About | `programs/row-pool-locations` | `row_about_pool_locations_source.html` | `various` | **UNVERIFIED** | — | No classes, no wrapper. A scrape, not a page |
| About | `about/row-careers` | `(not in repo)` | `various` | **NOT IN REPO** | — | Linked from the coaches page Join our team block |
| For swimmers | `for-swimmers` | `row_swimmers_for_swimmers_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/all-row-records` | `row_swimmers_club_records_embed.html` | `various` | **UNVERIFIED** | — |  |
| For swimmers | `for-swimmers/goal-setting-tool` | `(row-gm/row-swimming-math)` | `various` | **NOT IN REPO** | — | Separate repo |
| For parents | `for-parents` | `row_parents_for_parents_embed.html` | various | **VERIFIED** | 15 Aug 2026 | Live matched the repo exactly |
| For parents | `for-parents/parent-guide` | `row_parents_parent_guide_embed.html` | `(none)` | **VERIFIED** | 15 Aug 2026 | Converted from 326 inline styles to classes. 58 KB to 37 KB. Two dead links repointed |
| For parents | `for-parents/fpp-guide` | `row_parents_family_partnership_program_embed.html` | `(none)` | **VERIFIED** | 15 Aug 2026 | Converted from 383 inline styles to classes. 61 KB to 27 KB |
| For parents | `for-parents/how-to-get-involved` | `row_parents_how_to_get_involved_embed.html` | `various` | **UNVERIFIED** | — | Target of the two repointed links. Live URL now confirmed |
| For parents | `(url unknown)` | `row_parents_fpp_reporting_and_tracking_embed.html` | `various` | **UNVERIFIED** | — | A 7 KB page, not the same as the FPP Guide. Its live URL is not known |
| For parents | `for-parents/registration-fees` | `(not in repo)` | `various` | **NOT IN REPO** | — | Linked from every program page Fees chip |
| Top level | `sport-safety` | `row_sport_safety_embed.html` | `various` | **UNVERIFIED** | — |  |
