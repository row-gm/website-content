"""Build About Us and the two home page content blocks.

    python3 build_about_and_home.py

The home page is TWO separate content blocks in the CMS, Main Body and Footer.
The stylesheet is scoped per block, so each one needs its own copy of
row_stylesheet.css in its CSS field.

The promise and the mission come from layers_common.py. Do not retype either:
four versions were in circulation before they were settled.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import BASE, PROMISE, MISSION, FOUNDED, URL_ASSESSMENT, URL_OUR_DEVELOPMENT_PLAN

URL_SPORT_SAFETY = f"{BASE}/page/sport-safety"
URL_POOLS = f"{BASE}/page/about/row-pool-locations"
GM = "gm@rowswimming.ca"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def promise_block():
    """The club's promise, on the dark card. Same on About Us and the home page,
    from one constant, so the two can never say different things again."""
    return (f'<div class="row-quote"><b>&ldquo;</b><p>{PROMISE}</p>'
            f'<span></span></div>')


MISSION_POINTS = [
    "Provides instruction, training and competition for every swimmer, novice to champion, "
    "building skills and confidence that last well beyond their competitive years",
    "Gives families a community built on shared commitment and shared effort, with "
    "relationships that outlast a single season",
    "Gives coaches the chance to grow as mentors and leaders, and to see their work carried "
    "forward by the swimmers and families they have guided",
    "Builds sportsmanship, team spirit and mutual respect among swimmers, families and "
    "coaches alike",
]


def bullets(items):
    li = "".join(f'<li class="row-li">{x}</li>' for x in items)
    return f'<ul class="row-ul">{li}</ul>'


# ---------------------------------------------------------------------------
# About Us
# ---------------------------------------------------------------------------

about_us = wrap_page(
    hero("ROW Swim Club", "About Us",
         f"Welcome to the Region of Waterloo Swim Club &mdash; since {FOUNDED}."),
    lanes_divider(),
    promise_block(),

    '<div style="margin:18px 0 0;">' + card(
        h2("About")
        + body(f"ROW has developed swimmers from age five through to adult since {FOUNDED}. From "
               "stroke development and fitness to world competition, ROW swimmers have "
               "represented Canada with medal performances at the Olympics, World "
               "Championships, Commonwealth Games, Pan Am Games and World Cups, as well as "
               "representing the community at the International Children&rsquo;s Games, "
               "Provincial and Regional Championships, and local meets.")
        + body("As Kitchener-Waterloo&rsquo;s premiere competitive swim club, ROW provides "
               "nationally certified coaches to work with its swimmers. We run full season "
               "programs, summer camps and community involvement programs through the year, and "
               "operate as a not-for-profit organization under the Ontario Not-for-Profit "
               "Corporations Act.")
        + body("If you would like to join us, book a "
               + link(URL_ASSESSMENT, "new swimmer assessment") + ".", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Mission statement")
        + body(MISSION + " To this end, the club:")
        + bullets(MISSION_POINTS)
        + body(f"The club was founded in {FOUNDED}, and over its history ROW swimmers have "
               "qualified for the Olympics, World Championships, Pan American Games and "
               "Commonwealth Games. ROW coaches have been selected for the Far Western Tour "
               "Team, the Ontario Tour Team, the 8 Nations International Meet team and Canada "
               "Games teams.", margin="18px 0 0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Our commitment to safe sport")
        + body("ROW&rsquo;s commitment to safe sport aligns with the national framework set by "
               "the Government of Canada, Swimming Canada and Swim Ontario. We are the local "
               "stakeholders responsible for creating environments true to that commitment, and "
               "for protecting our members from anything that is not.")
        + body("See the " + link(URL_SPORT_SAFETY, "Sport Safety") + " page for how to report a "
               "concern, Rowan&rsquo;s Law requirements, and safe sport resources.",
               margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("How we develop swimmers")
        + body("What we are building, how training is designed, and why a swimmer&rsquo;s "
               "progress does not run in a straight line, are all set out in "
               + link(URL_OUR_DEVELOPMENT_PLAN, "Our Development Plan") + ".",
               margin="0")) + '</div>',
)


# ---------------------------------------------------------------------------
# Home page, main body
# ---------------------------------------------------------------------------

COMMITMENTS = [
    "We provide expert instruction, training and competition support for every swimmer, from "
    "first-time competitors to champions, building skills and confidence that carry forward long "
    "after the season ends.",
    "We build a family community rooted in shared effort and mutual support, with connections "
    "that outlast any single season.",
    "We treat our coaches as mentors, leaders and real people, so they too feel the impact of "
    "being with ROW long after their time with us.",
    "We hold ourselves to the highest standard of care, for every swimmer, every family and "
    "every coach who puts their trust in us.",
]

home_main = wrap_page(
    promise_block(),

    '<div style="margin:18px 0 0;">' + card(
        h2("Our commitment")
        + body("At ROW, the pool is just the beginning. Everything we do is designed to create "
               "positive experiences that last, for swimmers, families and coaches alike.")
        + bullets(COMMITMENTS)
        + body(f"ROW was founded in {FOUNDED}, and over the club&rsquo;s history our swimmers "
               "have represented Canada at the Olympics, World Championships, Pan American "
               "Games and Commonwealth Games, earning seven Olympic medals along the way.",
               margin="18px 0 14px")
        + body("We are equally proud of what happens after the pool. ROW alumni have gone on to "
               "build careers, businesses and lives of service in communities around the world. "
               "The discipline, relationships and experiences they gained here have carried them "
               "further than any split could measure.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">'
    + f'<a href="{URL_ASSESSMENT}" target="_blank" class="row-cta">'
      f'<b>Ready to be part of the ROW family?</b>'
      f'<span>Book a new swimmer assessment and we will place your swimmer in the right group '
      f'from day one.</span><em>Book an assessment &rarr;</em></a>' + '</div>',
)


# ---------------------------------------------------------------------------
# Home page, footer
# ---------------------------------------------------------------------------

POOLS = [
    ("Wilfrid Laurier University Athletic Complex", "75 University Ave West, Waterloo, Ontario "
     "N2L 3C5", "",
     "https://www.google.com/maps/place/Laurier+Athletic+Complex/@43.4752429,-80.5282663,17z"),
    ("Cameron Heights", "301 Charles Street East, Kitchener, Ontario N2G 2P8", "",
     "https://goo.gl/maps/LUiUWMJva6ywkYfe8"),
    ("Waterloo Recreation Complex", "101 Father David Bauer Dr, Waterloo, Ontario N2J 4A8", "",
     "https://www.google.ca/maps/place/101+Father+David+Bauer+Dr,+Waterloo,+ON+N2J+4A8"),
    ("Cowan Recreation Centre", "1664 Huron Rd, Kitchener, Ontario N2R 1R6", "Coming soon",
     "https://www.google.com/maps/place/1664+Huron+Rd,+Kitchener,+ON+N2R+1R6"),
    ("Harry Class Pool", "45 Woodside Ave, Kitchener, Ontario N2M 1A1", "Summer training",
     "https://www.google.com/maps/place/45+Woodside+Ave,+Kitchener,+ON+N2M+1A1"),
]


def pool_rows():
    rows = []
    for name, addr, tag, url in POOLS:
        label = name + (f' <span class="row-tag">{tag}</span>' if tag else "")
        rows.append([label, addr, link(url, "Get directions &rarr;")])
    return rows


home_footer = wrap_page(
    lanes_divider(),
    f'<div class="row-quote"><b></b><p class="row-address">Region of Waterloo Swim Club<br />'
    f'75 University Ave W, Waterloo, Ontario N2L 3C5<br /><strong>{GM}</strong></p>'
    f'<span></span></div>',
    '<div style="margin:18px 0 0;">' + card(
        h2("Where we train")
        + lede("We train in some great facilities across the Kitchener-Waterloo region.")
        + data_table(["Pool", "Address", ""], pool_rows())
        + note("Full details, parking and access notes are on the "
               + link(URL_POOLS, "ROW Pool Locations") + " page.")) + '</div>',
)


PAGES = [("about-us", about_us), ("home-main-body", home_main), ("home-footer", home_footer)]

if __name__ == "__main__":
    for slug, page in PAGES:
        out = f"/mnt/user-data/outputs/row_{slug.replace('-', '_')}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<40}{len(page) // 1024:>4} KB")
