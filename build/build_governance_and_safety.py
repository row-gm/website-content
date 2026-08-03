"""Build Board of Directors, Board Committees and Sport Safety.

    python3 build_governance_and_safety.py

Three pure-markup pages on the stylesheet.

The board and committee rosters are people's names and club email addresses,
carried across exactly as they were published. Anything that changes with an
election gets edited in the lists below, not in the markup.
"""

from row_page_helpers import (
    NAVY, TEAL, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede, circular_badge,
)

from layers_common import BASE

URL_PARENT_GUIDE = f"{BASE}/page/for-parents/parent-guide"
URL_OFFICIATING = f"{BASE}/page/for-parents/officiating"
SEASON = "2025&ndash;26"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def mail(addr):
    """House style: emails as bold plain text, not links."""
    return f'<strong class="row-link">{addr}</strong>'


# ---------------------------------------------------------------------------
# Board of Directors
# ---------------------------------------------------------------------------

BOARD = [
    ("Lydia Fischer", "Club President",
     "Chairs the board, sets meeting agendas with fellow directors, and makes sure the board "
     "meets its governance and fiduciary responsibilities to the club."),
    ("Liz Akeroyd", "Past President",
     "Provides continuity and historical context to support sound board decisions through the "
     "leadership transition."),
    ("Brent Hutzal", "Treasurer",
     "Oversees the club&rsquo;s financial governance, including budget approval, financial "
     "policy, and reporting the club&rsquo;s position to the board and membership."),
    ("Jason Whalen", "Secretary, Apparel",
     "Keeps accurate board meeting records, and oversees team apparel and uniform sourcing."),
    ("Kate Hano", "Fundraising &amp; Sponsorships",
     "Sets fundraising and sponsorship strategy, and oversees the policy governing the "
     "club&rsquo;s external funding relationships."),
    ("Peter Shannon", "External Relations",
     "Board-level oversight of the club&rsquo;s relationships with Swim Ontario, Swimming "
     "Canada and other outside organizations."),
    ("Brad Hickey", "Social Media",
     "Oversees governance of the club&rsquo;s social media policy and public-facing "
     "communications standards."),
    ("Wing Chan", "Communications",
     "Sets policy for how the club communicates with its membership, and oversees adherence to "
     "those standards."),
    ("Pratheek Harish", "FPP &amp; Member Liaison",
     "Governance oversight of the Family Participation Program policy, and the board&rsquo;s "
     "point of contact for member concerns."),
    ("Todd Snyder", "Technology",
     "Oversees governance of the club&rsquo;s technology policy, including data privacy and "
     "platform decisions."),
]

GOVERNANCE = [
    "Board members are elected to three-year terms, with a maximum of two consecutive terms.",
    "Elections happen at the Annual General Meeting, usually held in January. Openings are "
    "advertised in advance.",
    "Board meetings are open to every ROW member in good standing, usually on the first "
    "Wednesday of the month.",
    "Want an item on the agenda? Send it to the president at least two days before the meeting.",
]

CONCERN_PATH = [
    "Start with your swimmer&rsquo;s coach, before or after a practice, and try to resolve it "
    "directly.",
    "Not satisfied with the outcome? Bring it to the Head Coach.",
    f"Still unresolved? Contact the Member Liaison at {mail('memberliaison@rowswimming.ca')}.",
]


def initials(name):
    return "".join(p[0] for p in name.split()[:2]).upper()


board_page = wrap_page(
    hero("ROW Swim Club", "Board of Directors",
         "ROW is governed by a board of parent volunteers, elected to three-year terms."),
    lanes_divider(),

    card(h2("The current board")
         + lede("Ten parent volunteers serve on the board. Board meetings are open to every ROW "
                "member in good standing.")
         + data_table(["Director", "Role", "What the role covers"],
                      [[n, r, d] for n, r, d in BOARD])),

    '<div style="margin:24px 0 0;">' + card(
        h2("How the board works")
        + list_shell("".join(numbered_row(i + 1, t, i=i)
                             for i, t in enumerate(GOVERNANCE)))) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Have a concern?")
        + body("Things around the pool go wrong sometimes. This is the path we ask you to follow, "
               "and each step usually resolves it.")
        + list_shell("".join(numbered_row(i + 1, t, i=i)
                             for i, t in enumerate(CONCERN_PATH)))
        + callout("<strong>Operational concerns</strong> go to Andrew Moss, General Manager, at "
                  + mail("gm@rowswimming.ca") + ". To reach all ten directors, use "
                  + mail("board@rowswimming.ca") + ".")) + '</div>',
)


# ---------------------------------------------------------------------------
# Board Committees
# ---------------------------------------------------------------------------

COMMITTEES = [
    ("Fundraising and Sponsorship", "Kate Hano", "",
     "Organize fundraising through the season.", "fundraising@rowswimming.ca"),
    ("Club Communications", "Wing Chan",
     "Horatiu Rus, Hildeberto Mendonca, Feng Guo, Xiuwei (Angela) Wang",
     "Improve how the club communicates: email, news, the website and more.",
     "communications@rowswimming.ca"),
    ("Social Media", "Brad Hickey",
     "Sujin Lee and Angie Alegre, content. Ted Lin and Dake Yu, photography.",
     "Maintain the club&rsquo;s social media presence and outreach to families.",
     "social@rowswimming.ca"),
    ("Finance", "Brent Hutzal", "",
     "Support the Treasurer with budget planning, expense tracking and financial reporting.",
     "finance@rowswimming.ca"),
    ("Clothing", "Jason Whalen", "Kristen Baskerville, Rebecca Wang",
     "Manage relationships with equipment and apparel suppliers.",
     "clothing@rowswimming.ca"),
]

MEET_TEAM = ("Gavin Bee, Chris Deir, Mike Hui, Tam Nguyen, Kaoru Yajima, Matthew Campbell, "
             "Hildeberto Mendonca, David Tausky")

committees_page = wrap_page(
    hero(f"ROW Swim Club &middot; {SEASON} season", "Board Committees",
         "Committees of parent volunteers support the board. Openings are always worth asking "
         "about."),
    lanes_divider(),

    card(h2("Board committees")
         + lede("Five committees, each led by a director. Every one welcomes more volunteers.")
         + data_table(["Committee", "Director", "Members", "What they do", "Contact"],
                      [[c, d, m or "&mdash;", w, mail(e)]
                       for c, d, m, w, e in COMMITTEES])),

    '<div style="margin:24px 0 0;">' + card(
        h2("Meet management")
        + lede("This team runs independently of the board committees above.")
        + body("The ROW meet management team is a group of club parents who organize and run swim "
               "meets, and develop swimming officials as Swim Ontario requires. The team welcomes "
               "any ROW parent who would like to get involved. No experience is needed and the "
               "training is provided.")
        + data_table(["", ""],
                     [["Members", MEET_TEAM],
                      ["Contact", mail("meetmanager@rowswimming.ca")]])
        + note("The " + link(URL_OFFICIATING, "Officiating") + " page lists every volunteer role "
               "and how to start.")) + '</div>',
)


# ---------------------------------------------------------------------------
# Sport Safety
# ---------------------------------------------------------------------------

CHAIN = [
    ("Government of Canada",
     "Sets the national mandate through the Universal Code of Conduct to Prevent and Address "
     "Maltreatment in Sport, and funds the independent Canadian Safe Sport Program.",
     "https://www.canada.ca/en/canadian-heritage/services/safety-integrity-ethics-sport.html"),
    ("Swimming Canada",
     "Has adopted the Canadian Safe Sport Program nationally, and states plainly that every "
     "athlete, coach, official and volunteer has the right to a training and competitive "
     "environment free of abuse, harassment or discrimination.",
     "https://www.swimming.ca/en/safe-sport/"),
    ("Swim Ontario",
     "Carries that mandate provincially, committed to fun, healthy, inclusive and safe "
     "environments built on fairness, integrity, open communication and mutual respect.",
     "https://www.swimontario.com/sport-safety/"),
    ("ROW Swim Club",
     "We are the local stakeholders. We create the day to day environments aligned with that "
     "commitment, and we protect our members from anything that is not.", None),
]

RESOURCES = [
    ("Kids Help Phone", "https://kidshelpphone.ca/"),
    ("The Canadian Sport Helpline", "http://abuse-free-sport.ca/en/"),
    ("Canadian Centre for Child Protection",
     "https://www.protectchildren.ca/en/programs-and-initiatives/commit-to-kids-children-in-sport/"),
    ("Canadian Red Cross &mdash; violence, bullying and abuse prevention",
     "https://www.redcross.ca/how-we-help/violence-bullying-and-abuse-prevention"),
    ("PREVNet", "https://www.prevnet.ca/resources"),
    ("Swimming Canada &mdash; Safe Sport", "https://www.swimming.ca/safesport/"),
    ("Swimming Canada &mdash; harassment, abuse and anti-bullying",
     "https://www.swimming.ca/en/safe-sport/education/abuse-harassment-anti-bullying/"),
]

safety_page = wrap_page(
    hero("ROW Swim Club", "Sport Safety",
         "How to report a concern, what Rowan&rsquo;s Law requires, and where to find support."),
    lanes_divider(),

    card(h2("A shared commitment")
         + body("Safe sport at ROW is not a standalone club policy. It is the local link in a "
                "chain that runs from the federal government through our national and provincial "
                "bodies, down to every practice and meet we run.")
         + data_table(["Who", "What they do"],
                      [[link(u, w) if u else w, d] for w, d, u in CHAIN])),

    '<div style="margin:24px 0 0;">' + card(
        h2("Reporting a concern")
        + body("If something is wrong, raise it. Start with your swimmer&rsquo;s coach before or "
               "after a practice, then the Head Coach, then the Member Liaison at "
               + mail("memberliaison@rowswimming.ca") + ".")
        + body("For help filing a formal complaint, contact Swim Ontario through their "
               + link("https://www.swimontario.com/sport-safety/discipline-and-complaints-policy-clubs/",
                      "Club Resources") + " page, which also holds the procedures for "
               "complaints, dispute resolution, discipline and appeals.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Rowan&rsquo;s Law")
        + body("Ontario&rsquo;s Rowan&rsquo;s Law concussion regulations came into effect on "
               "1 July 2019 and are mandatory for every sports organization.")
        + body("As part of registration, all swimmers and families under 26, and all coaches and "
               "officials at Level 3 and above, must confirm they have read and agreed to the "
               "Rowan&rsquo;s Law resources and declaration.")
        + body("More is on the "
               + link("https://www.ontario.ca/page/rowans-law-concussion-safety",
                      "Government of Ontario") + " site and on Swim Ontario&rsquo;s "
               + link("https://www.swimontario.com/sport-safety/concussion-safety",
                      "Concussion Safety") + " page.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Where to find support")
        + lede("If you or someone you know needs help, these organizations can provide it.")
        + data_table(["Organization", ""],
                     [[link(u, n), ""] for n, u in RESOURCES])
        + note("Questions about sport safety at ROW go to "
               + mail("office@rowswimming.ca") + ".")) + '</div>',
)


PAGES = [("board-of-directors", board_page),
         ("board-committees", committees_page),
         ("sport-safety", safety_page)]

if __name__ == "__main__":
    for slug, page in PAGES:
        out = f"/mnt/user-data/outputs/row_{slug.replace('-', '_')}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<40}{len(page) // 1024:>4} KB")
