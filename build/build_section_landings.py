"""Build the For Swimmers and For Parents landing pages.

    python3 build_section_landings.py

Both were empty on the live site. A landing page's job is to say what the
section is for and list what is in it, nothing more.

LINKS. Five slugs are confirmed, taken from links on live pages:
    for-swimmers/goal-setting-tool
    for-swimmers/row-equipment-list
    for-parents/parent-guide
    for-parents/fpp-guide-2026-update
    for-parents/officiating
The rest follow the naming rule, lower-cased with hyphens. Marked below with
GUESS so they can be checked in one pass.
"""

from row_page_helpers import (
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import (
    BASE, URL_ASSESSMENT, URL_FOR_SWIMMERS, URL_OUR_DEVELOPMENT_PLAN,
    URL_HOW_WE_DEVELOP_SWIMMERS,
)

FOR_PARENTS = f"{BASE}/page/for-parents"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


# (nav label, slug, description, confirmed?)
SWIMMER_PAGES = [
    ("Goal Setting Tool", "goal-setting-tool",
     "Work out a goal time for every distance from one best time, and the splits to swim it. "
     "There is a calculator that does the whole thing for you.", True),
    ("Time Standards", "time-standards",
     "The qualifying times for every meet level, so you can see what you are chasing.", False),
    ("ROW Club Records", "row-club-records",
     "The fastest swims in club history, by age group and event.", False),
    ("ROW Equipment List", "row-equipment-list",
     "What to have in your bag, by group. Check this before you buy anything.", True),
    ("ROW Clothing &amp; Equipment", "row-clothing-and-equipment",
     "Club suits, caps, parkas and team wear, and how to order.", False),
    ("GeekSwimmers App", "geekswimmers-app",
     "An app for tracking your own times and progress.", False),
]

PARENT_PAGES = [
    ("New Swimmer Assessment", None,
     "Book an assessment. We will place your swimmer in the right group from day one.", True),
    ("Parent Guide", "parent-guide",
     "The practical handbook. How a meet works, what to bring, what the season looks like.", True),
    ("FPP Guide", "fpp-guide-2026-update",
     "The Family Participation Program explained: what the requirement is and how to meet it.",
     True),
    ("FPP Reporting", "fpp-reporting",
     "How to submit what you have done, and when your balance is updated.", False),
    ("FPP How to Get Involved", "fpp-how-to-get-involved",
     "Every role available, and what each one involves.", False),
    ("Officiating", "officiating",
     "Becoming a swim official. No experience needed and the training is provided.", True),
]

# Two pages live under For Swimmers and are listed here too. The navigation shows
# them under different names because SportsEngine will not allow a duplicate nav
# entry; the names below are the pages' real ones, which is what their headings
# say and what a link to them should read.
SHARED_PAGES = [
    ("ROW Equipment List", f"{URL_FOR_SWIMMERS}/row-equipment-list",
     "What your swimmer needs in their bag, by group. Check before you buy anything."),
    ("ROW Clothing &amp; Equipment", f"{URL_FOR_SWIMMERS}/row-clothing-and-equipment",
     "Club suits, caps, parkas and team wear, and how to order."),
]


def rows(pages, tree):
    out = []
    for label, slug, desc, _ in pages:
        url = URL_ASSESSMENT if slug is None else f"{tree}/{slug}"
        out.append([link(url, label), desc])
    return out


# ---------------------------------------------------------------------------

for_swimmers = wrap_page(
    hero("ROW Swim Club", "For Swimmers",
         "Everything a ROW swimmer needs in one place: what to aim at, what to bring, and where "
         "you sit against the standards."),
    lanes_divider(),

    card(h2("What is in here")
         + lede("Six pages, and the first two are the ones swimmers use most.")
         + data_table(["Page", "What it is for"], rows(SWIMMER_PAGES, URL_FOR_SWIMMERS))),

    '<div style="margin:24px 0 0;">' + card(
        h2("Setting a goal that is worth chasing")
        + body("A goal is worth having when it is close enough to reach in one training block "
               "and specific enough to swim. The " + link(f"{URL_FOR_SWIMMERS}/goal-setting-tool",
                                                          "Goal Setting Tool")
        + " turns one best time into a target for every other distance, and gives you the splits "
          "to get there.")
        + body("Bring your numbers to your coach before or after a practice. Their target always "
               "wins &mdash; they can see your training, your stroke and your race plan, and the "
               "tool cannot.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("What we are developing in you")
        + body("Twelve things, written in your own words, across four parts of being a swimmer. "
               "Read " + link(URL_HOW_WE_DEVELOP_SWIMMERS, "The ROW Way")
        + ", and the rest of " + link(URL_OUR_DEVELOPMENT_PLAN, "Our Development Plan")
        + " if you want to know why training changes through the year.", margin="0")) + '</div>',
)


for_parents = wrap_page(
    hero("ROW Swim Club", "For Parents",
         "The practical side of being a ROW family: joining, volunteering, and getting through "
         "your first meets."),
    lanes_divider(),

    card(h2("What is in here")
         + lede("Start with the Parent Guide. Everything else answers a narrower question.")
         + data_table(["Page", "What it is for"],
                      rows(PARENT_PAGES, FOR_PARENTS)
                      + [[link(u, n), d] for n, u, d in SHARED_PAGES])
         + note("FPP Reporting and FPP How to Get Involved need you to be signed in. The last "
                "two pages are shared with the For Swimmers section, so the menu lists them "
                "under slightly different names.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("New to the club?")
        + body("Book a " + link(URL_ASSESSMENT, "new swimmer assessment") + " and we will place "
               "your swimmer in the right group from day one. After that, the "
               + link(f"{FOR_PARENTS}/parent-guide", "Parent Guide")
        + " covers your first few months: how a meet runs, what to pack, and what the season "
          "looks like.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Understanding what your swimmer is doing")
        + body("Our Development Plan section explains the approach rather than the timetable: "
               "what we are developing, why training changes through the year, why times stall "
               "for months at a time, and how your own role shifts as your swimmer grows.")
        + body("Start with " + link(URL_OUR_DEVELOPMENT_PLAN, "Our Development Plan") + ".",
               margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("The Family Participation Program")
        + body("Every ROW family contributes hours through the season, and the club could not "
               "host a meet without it. No experience is needed for any role and training is "
               "provided.")
        + body("The " + link(f"{FOR_PARENTS}/fpp-guide-2026-update", "FPP Guide")
        + " explains the requirement, and "
        + link(f"{FOR_PARENTS}/fpp-how-to-get-involved", "How to Get Involved")
        + " lists every role.", margin="0")) + '</div>',
)


PAGES = [("for-swimmers", for_swimmers), ("for-parents", for_parents)]

if __name__ == "__main__":
    for slug, page in PAGES:
        out = f"/mnt/user-data/outputs/row_{slug.replace('-', '_')}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<40}{len(page) // 1024:>4} KB")
    print()
    for name, pages in [("For Swimmers", SWIMMER_PAGES), ("For Parents", PARENT_PAGES)]:
        unconfirmed = [p[0] for p in pages if not p[3]]
        print(f"  {name}: {len(unconfirmed)} slugs to confirm -> "
              + (", ".join(unconfirmed) if unconfirmed else "none"))
