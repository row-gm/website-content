# Pull list: pages still to verify

Tick one off at a time. For each page:

1. Open it in the CMS, click **Source**, copy everything, save it as a `.txt`
2. While you are in there, paste `row_stylesheet.css` into that page's **custom CSS** field
3. Upload the `.txt`

Step 2 applies to every page, not only the ones that change. The stylesheet
gained block spacing on 15 August, so any page still on the old copy looks
cramped next to one on the new copy.

## Meets and events

**Start here.** Link text was changed in the repo on 15 August and never checked against live, so the repo and the site disagree right now.

- [ ] `https://www.rowswimming.ca/page/events/row-hosted-meets`  
      → `row_meets_hosted_meets_embed.html`  
      Link text edited 15 Aug but never diffed against live

## For parents

**Start here.** Officiating also needs the new CSS before the official names render at all.

- [ ] `https://www.rowswimming.ca/page/for-parents/officiating`  
      → `row_parents_officiating_embed.html`  
      Link text edited 15 Aug but never diffed. 594 KB
- [ ] `https://www.rowswimming.ca/page/for-parents`  
      → `row_parents_for_parents_embed.html`
- [ ] `https://www.rowswimming.ca/page/for-parents/parent-guide`  
      → `row_parents_how_to_get_involved_embed.html`
- [ ] `https://www.rowswimming.ca/page/for-parents/fpp-guide`  
      → `row_parents_fpp_reporting_and_tracking_embed.html`

## For coaches

All six fail the vocabulary check, mostly zone colours where the framework now uses numbers. They exist only in the other Claude account, so pulling from live is the only way into this repo.

- [ ] `https://www.rowswimming.ca/page/coaching-at-row`  
      → `row_coaches_coaching_at_row_embed.html`  
      Fails row_vocabulary.py
- [ ] `https://www.rowswimming.ca/page/coaching-at-row/how-we-plan-training`  
      → `row_coaches_how_we_plan_training_embed.html`  
      Fails row_vocabulary.py
- [ ] `https://www.rowswimming.ca/page/coaching-at-row/how-we-design-training`  
      → `row_coaches_how_we_design_training_embed.html`  
      Fails row_vocabulary.py
- [ ] `https://www.rowswimming.ca/page/coaching-at-row/the-training-week`  
      → `row_coaches_the_training_week_embed.html`  
      Fails row_vocabulary.py
- [ ] `https://www.rowswimming.ca/page/coaching-at-row/the-practice-session`  
      → `row_coaches_the_practice_session_embed.html`  
      Fails row_vocabulary.py
- [ ] `https://www.rowswimming.ca/page/coaching-at-row/the-individual-swimmer`  
      → `row_coaches_the_individual_swimmer_embed.html`  
      Fails row_vocabulary.py

## About

Two of these may be the same page: `club_info_and_policies` and `withdrawal_policy` share an `<h1>` and only one can be live at `/page/about/club-info`.

- [ ] `https://www.rowswimming.ca/page/about`  
      → `row_about_about_us_embed.html`
- [ ] `https://www.rowswimming.ca/page/about/board-of-directors`  
      → `row_about_board_of_directors_embed.html`
- [ ] `https://www.rowswimming.ca/page/about/board-sub-committees`  
      → `row_about_board_committees_embed.html`
- [ ] `https://www.rowswimming.ca/page/about/club-info`  
      → `row_about_club_info_and_policies_embed.html`  
      Near duplicate of the withdrawal policy file
- [ ] `https://www.rowswimming.ca/page/about/club-info`  
      → `row_about_withdrawal_policy_embed.html`  
      Same h1 as club_info_and_policies. Only one can be live
- [ ] `https://www.rowswimming.ca/page/programs/row-pool-locations`  
      → `row_about_pool_locations_embed.html`
- [ ] `https://www.rowswimming.ca/page/programs/row-pool-locations`  
      → `row_about_pool_locations_source.html`  
      No classes, no wrapper. A scrape, not a page

## Programs

Programs Overview uses RSA once. ROW Swim Academy is the name now.

- [ ] `https://www.rowswimming.ca/page/programs`  
      → `row_programs_programs_overview_embed.html`  
      Uses RSA once
- [ ] `https://www.rowswimming.ca/page/programs/row-camps--summer-team`  
      → `row_programs_row_camps_summer_team_embed.html`

## For swimmers

- [ ] `https://www.rowswimming.ca/page/for-swimmers/time-standards`  
      → `row_swimmers_time_standards_embed.html`  
      Same script as Olympians. Not diffed
- [ ] `https://www.rowswimming.ca/page/for-swimmers`  
      → `row_swimmers_for_swimmers_embed.html`
- [ ] `https://www.rowswimming.ca/page/for-swimmers/all-row-records`  
      → `row_swimmers_club_records_embed.html`

## News

- [ ] `https://www.rowswimming.ca/page/news`  
      → `row_news_news_embed.html`
- [ ] `https://www.rowswimming.ca/page/news/monthly-newsletters`  
      → `row_news_club_newsletters_embed.html`

## Home

- [ ] `https://www.rowswimming.ca/page/home`  
      → `row_home_embed.html`
- [ ] `https://www.rowswimming.ca/page/home`  
      → `row_home_main_body_embed.html`
- [ ] `https://www.rowswimming.ca/page/home`  
      → `row_home_footer_embed.html`

## Top level

- [ ] `https://www.rowswimming.ca/page/sport-safety`  
      → `row_sport_safety_embed.html`

---

**29 pages.** 28 are already verified; `PAGE_STATUS.md` has the full table.

## While you are pasting CSS anyway

The 28 verified pages also need the current stylesheet. They are correct in the
repo, but most are still running an older CSS copy on the site.
