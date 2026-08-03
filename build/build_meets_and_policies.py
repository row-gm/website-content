"""Build the Meets pages and Club Info & Policies.

    python3 build_meets_and_policies.py

Three pure-markup pages, converted to the stylesheet. Public pages, so the
family audience check applies.

The document tables on these pages are placeholders on the live site: the
categories are set, the documents are not posted yet. That structure is kept
rather than invented over.
"""

from row_page_helpers import (
    TEAL, INK_SOFT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import BASE

URL_PARENT_GUIDE = f"{BASE}/page/for-parents/parent-guide"
URL_FPP_GUIDE = f"{BASE}/page/for-parents/fpp-guide-2026-update"
URL_SPORT_SAFETY = f"{BASE}/page/sport-safety"
URL_OFFICIATING = f"{BASE}/page/for-parents/officiating"
URL_MEET_SCHEDULE = f"{BASE}/page/events/meet-schedule"
URL_MEET_ENTRIES = f"{BASE}/page/events/meet-entry-policy"
URL_POOLS = f"{BASE}/page/about/row-pool-locations"
URL_RESULTS = "http://results.teamunify.com/canrwsc/"
URL_CALENDAR = ("https://calendar.google.com/calendar/embed?src=d51570905fd67365ad89db415067"
                "8658fa7c2da00a6282e420ede6bb26afd99c%40group.calendar.google.com"
                "&ctz=America%2FToronto")
URL_ICAL = ("https://calendar.google.com/calendar/ical/d51570905fd67365ad89db4150678658fa7c2da"
            "00a6282e420ede6bb26afd99c%40group.calendar.google.com/public/basic.ics")

GM = "gm@rowswimming.ca"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def under_review(what):
    return callout(f"<strong>This page is under review.</strong> {what}")


def empty_table(headers, message):
    """A category with nothing posted in it yet. The headings show a family what
    will live here, and the message sits underneath.

    No colspan: only style and class are safe attributes on a td. The sanitizer
    rejected data-label for the same reason.
    """
    ths = "".join(f"<th>{h}</th>" for h in headers)
    return (f'<div class="row-scroll"><table class="row-table"><tbody><tr>{ths}</tr>'
            f'</tbody></table></div>' + note(message))


# ---------------------------------------------------------------------------
# Club Info & Policies
# ---------------------------------------------------------------------------

DOC_CATEGORIES = [
    ("Governance",
     "The club&rsquo;s foundational records: bylaws, AGM minutes, board policies and "
     "strategic planning documents.",
     "No governance documents posted yet."),
    ("Financial Policies",
     "Fee schedules, the refund and withdrawal policy, and payment policies.",
     "No financial policy documents posted yet."),
    ("Privacy &amp; Consent",
     "The club&rsquo;s privacy policy, and the photo, video and media consent policies.",
     "No privacy or consent documents posted yet."),
    ("Other Club Documents",
     "Anything outside the categories above &mdash; annual reports, historical records and "
     "similar reference material.",
     "No other documents posted yet."),
]

club_info = wrap_page(
    hero("ROW Swim Club", "Club Info &amp; Policies",
         "Governance records, formal policies, and official club documents in one place."),
    lanes_divider(),
    under_review("We are building out the club&rsquo;s document library. The categories below "
                 "are what belongs here going forward, and documents are added as they are "
                 "confirmed."),
    f'<div style="margin:24px 0 0;">' + card(
        h2("Looking for something else?")
        + body("The " + link(URL_PARENT_GUIDE, "Parent Guide") + ", "
               + link(URL_FPP_GUIDE, "FPP Guide") + " and "
               + link(URL_SPORT_SAFETY, "Sport Safety") + " pages cover the day to day "
                 "questions most families have. This page is for the club&rsquo;s formal "
                 "governance records and policy documents.", margin="0")) + '</div>',
    *[f'<div style="margin:24px 0 0;">' + card(
        h2(title) + lede(desc)
        + empty_table(["Document", "Details", "Status"],
                      f"{msg} Check back soon, or email <strong>{GM}</strong>.")) + '</div>'
      for title, desc, msg in DOC_CATEGORIES],
)


# ---------------------------------------------------------------------------
# Meet and Event Schedule
# ---------------------------------------------------------------------------

SCHEDULE_CATEGORIES = [
    ("Meets", "The season&rsquo;s competitive meet schedule.",
     ["Meet", "Date", "Host Club", "Location", "Attending"],
     "Season schedule not yet posted."),
    ("Novice Meets", "Meets for TOPS, Recreation and other novice-level swimmers.",
     ["Meet", "Date", "Host Club", "Location", "Attending"],
     "Season schedule not yet posted."),
    ("Club Events", "Off the Blocks, team socials, banquets, the Swim-A-Thon and other "
                    "club-wide events.",
     ["Club Event", "Date", "Location", "Notes"],
     "Season events not yet posted."),
    ("Holiday &amp; Off Days", "Statutory holidays, school breaks and other scheduled "
                               "training closures.",
     ["Holiday or Off Day", "Date", "Notes"],
     "Season closures not yet posted."),
]

meet_schedule = wrap_page(
    hero("ROW Swim Club", "Meet and Event Schedule",
         "Competitive meets, novice meets, club events, and holiday closures for the season, "
         "in one place."),
    lanes_divider(),
    under_review("The categories below are the schedule&rsquo;s structure going forward. "
                 "Season dates are added once confirmed."),
    f'<div style="margin:24px 0 0;">' + card(
        h2("Put it in your own calendar")
        + body("Add " + link(URL_CALENDAR, "this Google Calendar") + " to your family calendar. "
               "Open the link, then click the plus sign at the bottom right. There is an "
               + link(URL_ICAL, "iCal version") + " too if you need it.", margin="0")) + '</div>',
    *[f'<div style="margin:24px 0 0;">' + card(
        h2(title) + lede(desc)
        + empty_table(headers, f"{msg} Check back soon, or email <strong>{GM}</strong>.")) + '</div>'
      for title, desc, headers, msg in SCHEDULE_CATEGORIES],
    f'<div style="margin:24px 0 0;">' + callout(
        "This schedule is tentative until posted. Tentative entries are marked, and a change to "
        "one can affect other parts of the schedule.") + '</div>',
)


# ---------------------------------------------------------------------------
# ROW Hosted Meets
# ---------------------------------------------------------------------------

HOSTED = [
    ("Fall First Try", "All groups", "Season opener, held early in the fall."),
    ("ROW Novice #1", "Novice", "Early-season novice meet, held in early winter."),
    ("Dean Boles", "All groups", "The club&rsquo;s first competition after Winter Break."),
    ("Cunningham Classic", "All groups", "A multi-session, multi-day meet held in the spring."),
    ("ROW Novice #2", "Novice", "Late-season novice meet, held in the spring."),
    ("Club Championships", "Closed", "In-club competition series, held across the season."),
]

hosted_meets = wrap_page(
    hero("ROW Swim Club", "ROW Hosted Meets",
         "Waterloo&rsquo;s home for competitive swimming &mdash; meets run by our community, "
         "for our community."),
    lanes_divider(),
    under_review("Meet dates, packages and heat sheets are added as each meet is confirmed."),
    f'<div style="margin:24px 0 0;">' + card(
        h2("Our hosted meets")
        + lede("Our lineup runs from an early fall opener through to late-spring novice meets. "
               "Dates are confirmed each season on the "
               + link(URL_MEET_SCHEDULE, "Meet and Event Schedule") + " page.")
        + data_table(["Meet", "Who it is for", "When"], [[a, b, c] for a, b, c in HOSTED])
        + note("Meet packages, heat sheets and results are posted as each meet "
               "approaches.")) + '</div>',
    f'<div style="margin:24px 0 0;">' + card(
        h2("Live results")
        + body("Live results from ROW-hosted meets go to Meet Mobile and "
               + link(URL_RESULTS, "results.teamunify.com/canrwsc") + ".", margin="0")) + '</div>',
    f'<div style="margin:24px 0 0;">' + card(
        h2("Help us host")
        + body("Every ROW-hosted meet runs on volunteers &mdash; timers, marshals, the admin "
               "desk and more. No experience is needed, training is provided, and your hours "
               "count towards your family&rsquo;s Family Participation Program points.")
        + body("See the " + link(URL_OFFICIATING, "Officiating") + " page for the full list of "
               "roles and how to get started.", margin="0")) + '</div>',
    f'<div style="margin:24px 0 0;">' + card(
        h2("Coming to a meet")
        + data_table(["Page", "What it covers"], [
            [link(URL_MEET_SCHEDULE, "Meet and Event Schedule"),
             "Confirmed dates for the season&rsquo;s meets, including ours."],
            [link(URL_MEET_ENTRIES, "Meet Entries"),
             "Meet packages and entry lists as they are posted."],
            [link(URL_POOLS, "ROW Pool Locations"),
             "Directions and details for our training and meet venues."]])) + '</div>',
)


PAGES = [("club-info-and-policies", club_info),
         ("meet-and-event-schedule", meet_schedule),
         ("row-hosted-meets", hosted_meets)]

if __name__ == "__main__":
    for slug, page in PAGES:
        stem = slug.replace("-", "_")
        stem = stem[4:] if stem.startswith("row_") else stem
        out = f"/mnt/user-data/outputs/row_{stem}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<44}{len(page) // 1024:>4} KB")
