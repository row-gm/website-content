"""Build Newsletters, Club Records, ROW Equipment List, FPP Reporting and
How to Get Involved.

    python3 build_swimmers_and_parents_pages.py

Five pure-markup pages on the stylesheet.

The equipment list is rewritten against the 2026-27 groups. RSA Age Group and
RSA Competitive are retired, so their lists are gone. TOPS is one list for both
2x and 3x, and AGD covers both age versions, because kit does not change with
session count.
"""

from row_page_helpers import (
    NAVY, TEAL, RED, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede,
)

from layers_common import BASE, URL_FOR_SWIMMERS

URL_HOSTED_MEETS = f"{BASE}/page/events/row-hosted-meets"
URL_OFFICIATING = f"{BASE}/page/for-parents/officiating"
URL_FPP_GUIDE = f"{BASE}/page/for-parents/fpp-guide-2026-update"
URL_LY = "https://www.lysports.com/team/row/"
URL_SO_OFFICIALS = "https://www.swimontario.com/officials/certification/"
URL_RECORDS_SHEET = ("https://docs.google.com/spreadsheets/d/e/2PACX-1vQCvOvawHevkW7azfC0rlJ2d2"
                     "mrY8GFc6l1x-nMMKw9ubYYOSsYzVyb6qGrEpy_MZwkh7xLHP2duZ_8/pubhtml")
URL_FPP_FORM = "https://forms.gle/Ld3qqUA9sNuPdoGc9"
GM = "gm@rowswimming.ca"
OFFICIALS = "officials@rowswimming.ca"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def mail(addr):
    return f'<strong class="row-link">{addr}</strong>'


def nothing_yet(headers, message):
    ths = "".join(f"<th>{h}</th>" for h in headers)
    return (f'<div class="row-scroll"><table class="row-table"><tbody><tr>{ths}</tr>'
            f'</tbody></table></div>' + note(message))


# ---------------------------------------------------------------------------
# Newsletters
# ---------------------------------------------------------------------------

BASE_PDF = f"{BASE}/canrwsc/UserFiles/Image/QuickUpload"

NEWSLETTERS = [
    ("2026", [
        ("June", "row-june-newsletter-2026-1-_030793.pdf",
         "Meet highlights: AGI International, BAD Outdoor Invite, WOSA 2026 &middot; End of "
         "season picnic &middot; Beyond the Blocks",
         [("Part I", "row-june-newsletter-2026-1-_030793.pdf"),
          ("Part II", "row-june-newsletter-2026-2-_018121.pdf")]),
        ("May", "row-may-newsletter-5-_038742.pdf",
         "Meet highlights: Amanda Reason, Top Cup, Jack McCormick, GMAC and Dash", []),
        ("April", "row-april-newsletter-2-_074988.pdf",
         "Meet highlights: Cunningham Classic &middot; Swimathon &middot; 50th anniversary gala "
         "&middot; Beyond the Blocks", []),
        ("March", "row-march-2026-newsletter-2-_035674.pdf",
         "Meet highlights: OAG 2026, GHAC Winter Invitational, Club Championship #3 &middot; "
         "Swimathon &middot; ROW annual survey", []),
        ("February", "row-february-newsletter-2-_000990.pdf",
         "Meet highlights: WOSA 2026, GTA Skins &middot; Summer program", []),
        ("January", "row-january-newsletter-7-_095639.pdf",
         "Meet highlights: Markham Winter Invitational, Dean Boles, David Lawson Invitational "
         "&middot; Celebrate Our Olympians, part IV", []),
    ]),
    ("2025", [
        ("December", "row-december-newsletter-7-_073699.pdf",
         "Meet highlights: AGI short course, OJI, GMAC Dash 4 Cash, Team Showdown &middot; Club "
         "Championship #1 &middot; Celebrate Our Olympians, part III", []),
        ("November", "november-2025-newsletter-4-_014973.pdf",
         "Meet highlights: BAC Fall Invitational, Aces Invitational, NYAC Cup, "
         "Nother&rsquo;s Invitational &middot; Celebrate Our Olympians, part II", []),
        ("October", "row-october-newsletter-2025-5-_009193.pdf",
         "Meet highlights: Fall First Try &middot; Celebrate Our Olympians, part I &middot; New "
         "parent handbook", []),
        ("September", "row-sept-2025-newsletter-19-_000364.pdf",
         "ROW 50th anniversary gala &middot; YMCA camp and Terry Fox run &middot; New parent "
         "information &middot; Open Water Championships", []),
        ("Summer", "summer-newsletter-2025_096158.pdf",
         "OSC, AGI, WOSA, Trials &middot; Swimmer&rsquo;s corner &middot; ROW picnic", []),
        ("May", "may-newsletter-2025_029702.pdf",
         "Amanda Reason, GMAC, Top Cup &middot; Coaches&rsquo; spotlight: Russ Franklin "
         "&middot; Swimmer&rsquo;s corner", []),
        ("April", "april-newsletter-2025_079470.pdf",
         "Cunningham Classic &middot; Coaches&rsquo; spotlight: Ron Forrest &middot; "
         "Swimmer&rsquo;s corner", []),
        ("March", "march-newsletter-2025-1-_086686.pdf",
         "OAG &middot; Coaches&rsquo; spotlight: Chloe Hughes &middot; Swimmer&rsquo;s corner",
         []),
        ("February", "febuary-2025-newsletter-1-_033985.pdf",
         "WOSA &middot; Coaches&rsquo; spotlight: Kaitlyn Schultz &middot; Swimmer&rsquo;s "
         "corner &middot; Food and nutrition, part II", []),
        ("January", "2025-january-newsletter_059279.pdf",
         "New Year Cup Scarborough Invite &middot; Coaches&rsquo; spotlight: Tyson MacDonald "
         "&middot; Swimmer&rsquo;s corner &middot; Food and nutrition", []),
    ]),
    ("2024", [
        ("December", "row-december-newsletter_077875.pdf",
         "Meet highlights: Team Showdown &middot; Coaches&rsquo; spotlights &middot; "
         "Swimmer&rsquo;s corner &middot; ROW banquet", []),
        ("November", "2024-november-newsletter-final2-_017068.pdf",
         "Meet highlights: Fall First Try, NYAC Cup &middot; Program structure &middot; "
         "Financial assistance", []),
        ("October", "row-newsletter-october-2024-1-_081228.pdf",
         "Club Championships &middot; Swim meet 101 &middot; New time standard", []),
        ("September", "row-newsletter-september-2024_061261.pdf",
         "New coaches &middot; YMCA camp and Terry Fox run &middot; New parent information", []),
    ]),
]


def newsletter_rows(issues):
    out = []
    for month, pdf, summary, parts in issues:
        title = link(f"{BASE_PDF}/{pdf}", month)
        if parts:
            title += " &middot; " + " ".join(link(f"{BASE_PDF}/{p}", lbl) for lbl, p in parts)
        out.append([title, summary])
    return out


newsletters = wrap_page(
    hero("ROW Swim Club", "Club Newsletters",
         "Every ROW newsletter, most recent first. Click a month to open the issue."),
    lanes_divider(),
    *[f'<div style="margin:{"0" if i == 0 else "24px"} 0 0;">' + card(
        h2(year) + data_table(["Issue", "In this one"], newsletter_rows(issues))) + '</div>'
      for i, (year, issues) in enumerate(NEWSLETTERS)],
)


# ---------------------------------------------------------------------------
# Club Records
# ---------------------------------------------------------------------------

club_records = wrap_page(
    hero("ROW Swim Club", "Club Records",
         "The fastest swims in club history, by age group and event."),
    lanes_divider(),
    card(h2("The records")
         + body("The full record sheet opens in a new tab. Use the tabs along the bottom to move "
                "between age groups.")
         + body(link(URL_RECORDS_SHEET, "Open the club records &rarr;"), margin="0")
         + callout("Records are best read on a laptop &mdash; there are a lot of columns. "
                   "Spotted something wrong? Email " + mail(GM) + " and we will check it.")),
    '<div style="margin:24px 0 0;">' + card(
        h2("Chasing one?")
        + body("A club record is a long way from most swimmers, and that is the point of having "
               "them. A more useful target is the next one up from where you are now.")
        + body("The " + link(f"{URL_FOR_SWIMMERS}/goal-setting-tool", "Goal Setting Tool")
               + " builds you a goal for every distance from a single best time, and the "
               + link(f"{URL_FOR_SWIMMERS}/time-standards", "Time Standards")
               + " page shows the qualifying times for each meet level.", margin="0")) + '</div>',
)


# ---------------------------------------------------------------------------
# ROW Equipment List
# ---------------------------------------------------------------------------

EQUIPMENT = [
    ("ROW Swim Academy", "All ROW Swim Academy classes",
     ["Kickboard", "Goggles", "ROW swim cap"]),
    ("TOPS", "TOPS 2 and TOPS 1",
     ["Short blade fins", "Kickboard", "ROW swim cap", "Water bottle",
      "Racing or practice suit: Speedo Endurance level, black", "ROW t-shirt for meets"]),
    ("Junior Development 2", "JD2",
     ["Fins", "Snorkel", "Kickboard", "Small junior pull buoy", "ROW swim cap", "Water bottle",
      "Yoga mat for dryland", "Racing or practice suit: Speedo Endurance level, black",
      "ROW t-shirt for meets"]),
    ("Junior Development 1", "JD1",
     ["Short blade fins", "Snorkel, Finis junior", "Kickboard", "Small junior pull buoy",
      "ROW swim cap", "Water bottle", "Yoga mat for dryland",
      "Racing or practice suit: Speedo Endurance level, black", "ROW t-shirt for meets",
      "ROW pants, jacket or sweater to keep warm"]),
    ("Age Group Development", "AGD 2 and AGD 1",
     ["Short blade fins", "Kickboard", "Snorkel, Finis junior", "Small junior pull buoy",
      "ROW swim cap", "Water bottle", "Yoga mat for dryland",
      "Racing or practice suit: Speedo Endurance level, black", "ROW t-shirt for meets",
      "ROW pants, jacket or sweater to keep warm"]),
    ("Recreation", "REC AM and REC PM",
     ["Fins", "Kickboard", "ROW swim cap", "Water bottle",
      "Racing or practice suit: Speedo Endurance level, black", "ROW t-shirt for meets"]),
    ("Provincial Development 3", "PD3",
     ["Short blade fins", "Snorkel, Finis junior", "Kickboard", "Small junior pull buoy",
      "ROW swim cap", "Water bottle", "Yoga mat for dryland",
      "Racing or practice suit: Speedo Endurance level, black", "ROW t-shirt for meets",
      "ROW pants, jacket or sweater to keep warm"]),
    ("Provincial Development 2", "PD2",
     ["Fins", "Snorkel", "Kickboard", "Pull buoy", "Drag suits for boys", "ROW swim cap",
      "Water bottle", "Yoga mat for dryland", "Practice suit, black",
      "Racing suit: Power Plus, blue or black", "ROW t-shirt for meets",
      "ROW pants, jacket or sweater to keep warm"]),
    ("Senior Development", "SD",
     ["Fins", "Snorkel", "Kickboard", "Pull buoy", "Pulling band for ankles", "Paddles, Finis",
      "Drag suits for boys", "ROW swim cap", "Water bottle", "Yoga mat for dryland",
      "Practice suit, black",
      "Racing suit: Power Plus or LZR Racer, check with your coach, blue or black",
      "ROW t-shirt for meets", "ROW pants, jacket or sweater to keep warm"]),
    ("Provincial Development 1", "PD1",
     ["Fins", "Snorkel", "Kickboard", "Pull buoy", "Pulling band for ankles",
      "Paddles, Strokemaker preferred", "Drag suits for boys", "ROW swim cap", "Water bottle",
      "Yoga mat for dryland", "Skipping rope", "Practice suit, black",
      "Racing suit: Power Plus or LZR Racer, check with your coach, blue or black",
      "ROW t-shirt for meets", "ROW pants, jacket or sweater to keep warm"]),
    ("National Development", "ND",
     ["Fins", "Snorkel", "Kickboard", "Pull buoy", "Pulling band for ankles",
      "Small parachute", "Paddles, Finis", "Water shoes", "Drag suits for boys", "ROW swim cap",
      "Water bottle", "Yoga mat for dryland", "Skipping rope", "Practice suit, black",
      "Racing suit: LZR Racer Pro for regional, Valor for provincial, your choice for Swimming "
      "Canada meets. Black, blue or grey",
      "ROW t-shirt for meets", "ROW pants, jacket or sweater to keep warm"]),
]

equipment_list = wrap_page(
    hero("ROW Swim Club", "ROW Equipment List",
         "What to have in your bag, group by group. Check here before you buy anything."),
    lanes_divider(),
    card(h2("Before you buy")
         + body("Ask your coach before or after a practice if you are unsure about anything on "
                "this list. Brands are named only where they matter.")
         + body("The club gets a discount at " + link(URL_LY, "Ly Sports") + ", so start there.",
                margin="0")
         + callout("No jammer-style suits for boys in practice. Racing suits are listed by group "
                   "because the rules differ by meet level.")),
    *[f'<div style="margin:24px 0 0;">' + card(
        h2(name) + lede(short)
        + data_table([""], [[i] for i in items])) + '</div>'
      for name, short, items in EQUIPMENT],
)


# ---------------------------------------------------------------------------
# FPP Reporting
# ---------------------------------------------------------------------------

AUTO_TRACKED = [
    "<strong>ROW-hosted meets</strong> &mdash; Fall First Try, ROW Novice, Dean Boles and the "
    "Cunningham Classic. Tracked automatically, nothing to submit.",
    "<strong>Swimming Canada officials training</strong> &mdash; also tracked automatically and "
    "assigned to you.",
    f"<strong>A non-ROW meet</strong> &mdash; email {mail(OFFICIALS)} directly. Do not use the "
    f"self-reporting form for meet roles.",
]

SELF_REPORT = [
    "<strong>Everything that is not a meet role</strong> &mdash; committee work, chaperoning, "
    "merchandise help, the Off the Blocks meeting, the AGM, club socials and similar. Use the "
    "form below.",
    "<strong>Include your family name and the email you use for the ROW website</strong>, so the "
    "points reach the right account.",
    "<strong>Submit soon after the activity.</strong> Do not save them up for the end of the "
    "season; late submissions may not be accepted.",
]

UPDATES = [
    ("December", "Mid-season check-in, so you know where you stand going into the new year."),
    ("March", "Third-quarter update, with enough season left to earn any remaining points."),
    ("June", "Final balance before reporting closes in mid-July."),
]

fpp_reporting = wrap_page(
    hero("ROW Swim Club", "FPP Reporting and Tracking",
         "How Family Participation Program activities get recorded, and when you will hear about "
         "your balance."),
    lanes_divider(),
    card(h2("Your part: report what you have done")
         + body("You are responsible for submitting your completed FPP activities. Some things "
                "are tracked for you; everything else needs the form.")
         + lede("Tracked automatically")
         + list_shell("".join(numbered_row(i + 1, t, i=i)
                              for i, t in enumerate(AUTO_TRACKED)))
         + lede("You report these yourself")
         + list_shell("".join(numbered_row(i + 1, t, i=i)
                              for i, t in enumerate(SELF_REPORT)))
         + body(link(URL_FPP_FORM, "Open the FPP self-reporting form &rarr;"),
                margin="20px 0 0")
         + note(f"Meet questions go to {mail(OFFICIALS)}. Everything else to {mail(GM)}.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Our part: track it and report back")
        + body("ROW tracks FPP points centrally, so you do not need to keep your own tally. "
               "Balance updates go to every member at least three times a season.")
        + data_table(["Update", "What it covers"], [[a, b] for a, b in UPDATES])) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("If you fall short")
        + body("Families who do not meet their requirement by the end of the season are charged "
               "for every point short, applied to the account after reporting closes. The "
               "current rate is $50 a point.")
        + callout("<strong>For example.</strong> A family with a 12-point requirement finishes "
                  "with 8 points, so 4 short. Four times $50 is <strong>$200 charged to the "
                  "account</strong>.", warn=True)
        + note("The policy and the rate are reviewed by the Board of Directors each season. The "
               + link(URL_FPP_GUIDE, "FPP Guide") + " has the full requirement and how points "
               "are earned.")) + '</div>',
)


# ---------------------------------------------------------------------------
# How to Get Involved
# ---------------------------------------------------------------------------

WAYS = [
    ("Volunteer at a meet", "On deck",
     "ROW hosts several meets a season and relies on family volunteers to run them. Timers, "
     "marshals, hospitality &mdash; every role matters.",
     URL_HOSTED_MEETS, "See our hosted meets"),
    ("Become an official", "Certified",
     "Certified officials are essential to every competitive meet. Swim Ontario runs training "
     "clinics that qualify you to work meets across the region.",
     URL_SO_OFFICIALS, "Swim Ontario officials"),
    ("Join a committee", "Ongoing",
     "Fundraising, communications, social media, finance and clothing all run on parent "
     "volunteers, and all of them welcome more.",
     f"{BASE}/page/about/board-committees", "Board committees"),
]

REQUESTS = [
    ("Volunteer Roles", ["Role", "Contact", "Status"],
     "No open volunteer roles posted yet."),
    ("Equipment", ["Item", "Details", "Status"],
     "No equipment requests posted yet."),
    ("Merchandise", ["Item", "Details", "Status"],
     "No merchandise requests posted yet."),
    ("Services and Sponsorship", ["What", "Details", "Status"],
     "No service or sponsorship requests posted yet."),
]

get_involved = wrap_page(
    hero("ROW Swim Club", "How to Get Involved",
         "ROW is built by the people who show up. A great swim club is not built from the "
         "sidelines."),
    lanes_divider(),
    card(h2("Where to start")
         + body("There are many ways to contribute, from timing a lane at one of our meets to "
                "leading a social for your swimmer&rsquo;s group, to connecting the club with "
                "merchandise or sponsored services. Most of them also earn Family Participation "
                "Program points.")
         + data_table(["Way in", "", "What it involves", ""],
                      [[w, tag, d, link(u, lbl)] for w, tag, d, u, lbl in WAYS])
         + note("The " + link(URL_OFFICIATING, "Officiating") + " page lists every volunteer "
                "role at a meet and what each one involves.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("What the club needs right now")
        + lede("Specific things ROW could use. If you can provide or source any of it, or you "
               "know a business that might sponsor the club, we would love to hear from you.")) + '</div>',

    *[f'<div style="margin:16px 0 0;">' + card(
        h2(title) + nothing_yet(headers, f"{msg} Check back soon, or email {mail(GM)} to say "
                                         f"what you can offer.")) + '</div>'
      for title, headers, msg in REQUESTS],
)


PAGES = [("club-newsletters", newsletters),
         ("club-records", club_records),
         ("row-equipment-list", equipment_list),
         ("fpp-reporting-and-tracking", fpp_reporting),
         ("how-to-get-involved", get_involved)]

if __name__ == "__main__":
    for slug, page in PAGES:
        stem = slug.replace("-", "_")
        stem = stem[4:] if stem.startswith("row_") else stem
        out = f"/mnt/user-data/outputs/row_{stem}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<46}{len(page) // 1024:>4} KB")
