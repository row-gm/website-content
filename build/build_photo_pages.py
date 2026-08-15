"""Build the five pages that carry photographs.

    python3 build_photo_pages.py

  Coaches & Operations Team    six staff photos
  Our Olympians & Paralympians sixteen archive photos
  Officiating                  eight meet photos
  ROW Clothing & Equipment     two partner logos
  Time Standards               two governing body logos

Images live in build/images, named after who or what they show, and are embedded
as data URIs at build time. That way a photo can be replaced by dropping in a
new file with the same name; no page markup changes.

The Andrew Moss photo arrived as a 1.8 MB PNG at 1122x1402, which was 84% of
that page on its own. Resized to 700px wide and saved as JPEG, per the build
guide's 700px cap: 65 KB, and it looks the same on screen.

Group assignments come from the 2026-27 Executive Summary, not from the old
page, which still listed RSA Age Group and RSA Competitive.
"""

import base64
import os

from row_page_helpers import (
    NAVY, TEAL, RED, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede,
)

from layers_common import BASE, URL_FOR_SWIMMERS

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
MIME = {".jpg": "jpeg", ".jpeg": "jpeg", ".png": "png", ".webp": "webp"}

URL_EQUIPMENT_LIST = f"{URL_FOR_SWIMMERS}/row-equipment-list"
URL_HOSTED_MEETS = f"{BASE}/page/events/row-hosted-meets"
URL_MEET_SCHEDULE = f"{BASE}/page/events/meet-schedule"
URL_PROGRAMS = f"{BASE}/page/programs"
URL_SO_POSITIONS = "https://www.swimontario.com/officials/positions/"
URL_SO_CERT = "https://www.swimontario.com/officials/certification/"
URL_SO_STANDARDS = "https://www.swimontario.com/swimming/time-standards/"
URL_SC_STANDARDS = "https://www.swimming.ca/en/events-results/time-standards/"
URL_GMP = "https://www.gmpsportswear.com/"
URL_LY = "https://www.lysports.com/team/row/"
URL_GEEK = "https://geekswimmers.com"
GM = "gm@rowswimming.ca"
OFFICIALS = "officials@rowswimming.ca"
MEETMGR = "meetmanager@rowswimming.ca"
CLOTHING = "clothing@rowswimming.ca"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def mail(a):
    return f'<strong class="row-link">{a}</strong>'


def img(name, alt, cls="row-photo"):
    """Embed an image from build/images as a data URI."""
    path = os.path.join(IMG_DIR, name)
    ext = os.path.splitext(name)[1].lower()
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return (f'<img src="data:image/{MIME[ext]};base64,{b64}" alt="{alt}" class="{cls}" />')


def person(photo, name, role, bio, note_=""):
    return (f'<div class="row-person">'
            f'<div class="row-person-pic">{img(photo, name)}</div>'
            f'<div class="row-person-text">'
            f'<div class="row-stage-head">{name}</div>'
            f'<div class="row-stage-lead">{role}</div>'
            f'{body(bio, margin="0")}'
            + (note(note_) if note_ else "")
            + '</div></div>')


# ---------------------------------------------------------------------------
# Coaches & Operations Team
# ---------------------------------------------------------------------------

STAFF = [
    ("coach-ron-forrest.jpg", "Ron Forrest", "Lead coach &middot; ND and PD1",
     "Ron began as an age group swimmer with ROW before a 25-year coaching career that included "
     "two decades as Head Coach and Program Director of the Fort Worth Area Swim Team. His "
     "athletes have included an Olympic gold medallist, an Olympic qualifier and world record "
     "holder, a Para-swimming world record holder, and numerous Pan-American, Commonwealth and "
     "NCAA competitors. He was named Texas Swimming Senior Coach of the Year in 2002 and 2004."),
    ("coach-tyson-macdonald.jpg", "Tyson MacDonald", "Lead coach &middot; PD2 and SD",
     "A recently retired competitive swimmer who represented Canada internationally, most "
     "recently earning three medals at the 2023 Para Pan American Games in Santiago. Tyson swam "
     "at Wilfrid Laurier University from 2015 to 2020 and brings that experience onto the deck."),
    ("coach-kaitlyn-schultz.jpg", "Kaitlyn Schultz", "Lead coach &middot; JD1, JD2 and TOPS",
     "With ROW since 2009 and more than 30 years in Ontario swimming, Kaitlyn coached at Champion "
     "Swim Club before becoming Head Coach of Variety Village Flames in 2008, working with both "
     "able-bodied and Paralympic swimmers. One of her athletes qualified for two consecutive "
     "Paralympic World Championship teams. She holds a Speedo Award of Excellence and a CSTCA "
     "national coaching award, and is NCCP Level 2 certified."),
    ("coach-chloe-hughes.jpg", "Chloe Hughes", "Lead coach &middot; ROW Swim Academy",
     "In her fourth season on full-time staff, Chloe&rsquo;s connection to ROW goes back to 2011 "
     "as a competitive swimmer. She joined the coaching team in 2016 and now works with athletes "
     "aged four to sixteen. She holds a degree in English from the University of Guelph and is an "
     "Ontario Certified Teacher completing a Master&rsquo;s in Professional Education at Western."),
    ("coach-russ-franklin.jpg", "Russ Franklin", "Mentor coach &middot; every group",
     "Now in his 51st year of coaching, roughly 30 of them as a head coach, Russ has guided "
     "provincial and national medallists and athletes who went on to represent Canada "
     "internationally, including at the Olympics. He works across every competitive group, at "
     "training and at meets, so what he knows is passed on while he is here to pass it on."),
    ("coach-andrew-moss.jpg", "Andrew Moss", "General Manager",
     "Andrew brings 15 years of coaching experience, from age group swimmers through to "
     "Olympic-calibre athletes, along with another 15 years in senior leadership at Swim BC, "
     "Swimming Canada, the Canadian Sport Institute Ontario and Golf Ontario. Since 2018 he has "
     "focused on executive and life coaching, and recently completed the 11-month Clipper Round "
     "the World Yacht Race."),
]

coaches = wrap_page(
    hero("ROW Swim Club", "Coaches &amp; Operations Team",
         "The people behind ROW &mdash; the coaches guiding swimmers at every level, and the team "
         "supporting the club."),
    lanes_divider(),
    card(h2("Our staff")
         + lede("Group assignments for the 2026-27 season. A lead coach for AGD 1, AGD 2 and the "
                "Recreation groups is currently being recruited.")
         + "".join(person(*s) for s in STAFF)),
    '<div style="margin:24px 0 0;">' + card(
        h2("How we develop coaches")
        + body("A club cannot promise long-term development to swimmers and treat its coaches as "
               "interchangeable. Every ROW coach has a development plan: certification, time on "
               "deck with a mentor, and support to take on more as they are ready. Assistant "
               "roles are a route into the job, not a holding pattern.")
        + body("ROW alumni coach here too. SD swimmers take the ROW Swim Academy on Saturday "
               "mornings, fifteen minutes after finishing their own session.", margin="0")) + '</div>',
)


# ---------------------------------------------------------------------------
# Our Olympians & Paralympians
# ---------------------------------------------------------------------------

SWIMMERS = [
    ("oly-jim-hett.jpg", "Jim Hett", "1976 Montreal",
     "Born and raised in Waterloo, Hett swam for the Kitchener-Waterloo YMCA Aquatic Club, "
     "ROW&rsquo;s predecessor. He qualified for the Montreal Games at 18, placing 22nd in the "
     "200 m freestyle, then coached with ROW for three years before moving on to clubs in "
     "Sudbury, Peterborough and Oshawa.",
     "Pictured with Prime Minister Pierre Trudeau."),
    ("oly-dave-heinbuch.webp", "Dave Heinbuch", "1976 Montreal",
     "Kitchener-born, Heinbuch trained at the Laurier pool and Simon Fraser University before "
     "competing in the 200 m breaststroke in Montreal, finishing 15th. He coached the University "
     "of Waterloo varsity teams for nine years, then spent two decades as head coach of the "
     "Nepean Kanata Barracudas. He most recently coached at the University of Ottawa, retiring "
     "in 2026.", ""),
    ("oly-kevin-auger.jpg", "Kevin Auger", "1980 Moscow",
     "A Guelph native, Auger joined ROW in 1980 to train under coach Cliff Barry and qualified "
     "for the Moscow Games, but never competed after Canada joined the boycott. He went on to a "
     "long coaching career, most recently leading the Wildkit Swimming Organization near "
     "Chicago.", ""),
    ("oly-victor-davis.jpg", "Victor Davis", "1984 Los Angeles &middot; 1988 Seoul",
     "One of ROW&rsquo;s most celebrated swimmers, Davis won Olympic gold in the 200 m "
     "breaststroke at Los Angeles in 1984 in a world record time, plus three silver medals "
     "across two Games. A three-time Swimming Canada Athlete of the Year and Member of the Order "
     "of Canada, he is remembered as one of the country&rsquo;s greatest swimmers. Davis died in "
     "1989, aged 25.", ""),
    ("oly-mike-west.jpg", "Mike West", "1984 Los Angeles",
     "Born and raised in Waterloo, West joined ROW at 13 and became a backstroke specialist, "
     "setting a world record in the 200 m backstroke. At the 1984 Games he won silver in the "
     "medley relay and bronze in the 100 m backstroke alongside teammate Victor Davis. He later "
     "became a family physician.", ""),
    ("oly-laura-nicholls.jpg", "Laura Nicholls", "1996 Atlanta &middot; 2000 Sydney",
     "A Kitchener native who joined ROW at five, Nicholls became one of Canada&rsquo;s fastest "
     "freestyle sprinters, competing at two Olympics and setting a Canadian record in the 50 m "
     "freestyle. She went on to become head coach of the Oakville Aquatic Club, and now the "
     "Guelph Marlins Aquatic Club.", ""),
    ("oly-jennifer-button.jpg", "Jennifer Button", "2000 Sydney",
     "Button moved to Waterloo at 13 and trained under coach Dean Boles, becoming one of the "
     "country&rsquo;s top butterfly swimmers. At the Sydney Games she competed in four events, "
     "reaching the final in the 4x200 m freestyle relay. She later worked in marketing for the "
     "Canadian Olympic Committee.", ""),
    ("oly-takashi-yamamoto.jpg", "Takashi Yamamoto", "2000 Sydney &middot; 2004 Athens",
     "A Japanese swimmer who trained with ROW for six years under coach Bud McAllister, Yamamoto "
     "won Olympic silver in the 200 m butterfly at Athens 2004, a fraction of a second behind "
     "Michael Phelps, plus bronze in the 4x100 m medley relay.", ""),
    ("oly-jessica-tuomela.jpg", "Jessica Tuomela",
     "Paralympian &middot; 2000 Sydney &middot; 2004 Athens &middot; 2008 Beijing",
     "Blind since early childhood, Tuomela trained under coach Bud McAllister at Wilfrid Laurier "
     "as a freestyle "
     "sprint specialist, guided in the pool by a tapper who signalled when she neared the wall. "
     "She won Paralympic silver in the 50 m freestyle at Sydney 2000 and competed at three "
     "consecutive Games.", ""),
    ("oly-jennifer-fratesi.jpg", "Jennifer Fratesi", "2004 Athens",
     "Fratesi moved to ROW at 15 to train under Dean Boles and set a Canadian record in the 200 m "
     "backstroke at the 2001 World Championships. At the Athens Games she missed the final by two "
     "hundredths of a second. She later became a medical student at the University of Ottawa.",
     ""),
    ("oly-keith-beavers.jpg", "Keith Beavers", "2004 Athens &middot; 2008 Beijing",
     "Orangeville-born, Beavers trained under Bud McAllister and Dean Boles at ROW&rsquo;s "
     "national training centre. He competed at two Olympics, placing seventh in the 200 m "
     "individual medley at Beijing 2008 in a race that included Michael Phelps. He later coached "
     "varsity swimming at Simon Fraser University.", ""),
    ("oly-alec-elliot.jpg", "Alec Elliot", "Paralympian &middot; 2016 Rio",
     "Born with a hand and foot condition called syndactyly, Elliot began swimming with ROW as a "
     "child and returned to the sport at 12 after a stint in football. Training at Laurier under "
     "coach Hans Witolla, he qualified for the 2016 Rio Paralympics, competing in six events with "
     "a best finish of fourth in the 100 m butterfly, and went on to three Paralympic Games.",
     "Photo by Paige Bush / The Cord."),
]

OLY_COACHES = [
    ("oly-clifford-barry.jpg", "Clifford Barry", "1980&ndash;1984 &middot; Head Coach",
     "A two-time Olympian himself, Barry represented Canada in water polo at Munich 1972 and "
     "Montreal 1976 before turning to coaching. He guided Victor Davis to Olympic gold and Mike "
     "West to two medals at Los Angeles 1984, and served as an official coach with Canadian "
     "national teams at the Olympics, Pan Am, Commonwealth and World Championships from 1981 to "
     "1991. A three-time Canadian Coach of the Year, he was inducted into the Canadian Swimming "
     "Coaches Hall of Fame. Barry died in 2021.", ""),
    ("oly-bud-mcallister.jpg", "Bud McAllister", "National team coach &middot; USA and Canada",
     "An internationally renowned coach who has led national programs for both the United States "
     "and Canada, McAllister headed ROW&rsquo;s national training centre, where he coached "
     "Takashi Yamamoto, Jessica Tuomela and Keith Beavers. His swimmers have combined for five "
     "Olympic medals and "
     "two Olympic records. He was named Canadian Coach of the Year in 2002.", ""),
    ("oly-dean-boles.jpg", "Dean Boles", "Now CEO and CTO &middot; Swim Ontario",
     "Boles joined ROW in 1980 as a national-level swimmer before turning to coaching a year "
     "later. Over 22 years as Wilfrid Laurier&rsquo;s head coach he guided swimmers to four "
     "consecutive Olympic Games, including Laura Nicholls, Jennifer Button, Jennifer Fratesi and "
     "Keith Beavers. He served as National Coach of the Danish Swimming Federation, and has been "
     "CEO and Chief Technical Officer of Swim Ontario since 2019.", ""),
    ("oly-hans-witolla.jpg", "Hans Witolla",
     "Now Lead Age Group Coach &middot; Richmond Hill Aquatic Club",
     "Witolla has had a long coaching career, starting in Brantford, Ontario. He coached at the "
     "Guelph Marlins and as an assistant with the University of Guelph "
     "Gryphons before moving to the Waterloo region, where he served as Wilfrid Laurier&rsquo;s "
     "head coach and a senior coach with ROW. He coached Alec Elliot from age 12 through "
     "Elliot&rsquo;s Rio 2016 Paralympic debut and the 2018 Pan Pacific Para Swimming "
     "Championships. He later headed the Barrie Trojan Swim Club before joining Richmond Hill in "
     "2023.", ""),
]

olympians = wrap_page(
    hero("ROW Swim Club", "Our Olympians &amp; Paralympians",
         "Since 1977, ROW swimmers have represented Canada and other nations at the Olympic and "
         "Paralympic Games &mdash; from the same Laurier pool our swimmers train in today."),
    lanes_divider(),
    card(h2("Club of the Year, 1998")
         + body("In 1998 ROW was named Club of the Year by Swimming Canada and chosen as a "
                "national swim centre. That reputation drew swimmers from around the world to "
                "train here, and sent ROW-trained swimmers on to the biggest stages in the sport. "
                "Here are their stories.", margin="0")),
    '<div style="margin:24px 0 0;">' + card(
        h2("The swimmers")
        + "".join(person(*s) for s in SWIMMERS)) + '</div>',
    '<div style="margin:24px 0 0;">' + card(
        h2("The coaches behind them")
        + lede("Every swimmer above trained under one of these four: three Olympic coaches and "
               "one of Canada&rsquo;s most experienced Para-swimming coaches.")
        + "".join(person(*c) for c in OLY_COACHES)) + '</div>',
    '<div style="margin:24px 0 0;">' + callout(
        "Know a ROW alum we should add, or spotted a correction? Email " + mail(GM) + ".") + '</div>',
)


# ---------------------------------------------------------------------------
# Officiating
# ---------------------------------------------------------------------------

INTRO_ROLES = [
    ("off-timekeeper.jpg", "Timekeeper",
     "Operate a stopwatch and assist with the electronic timing system for one lane.",
     "Your role is what makes an accurate swim time possible."),
    ("off-marshal.jpg", "Safety Marshal",
     "Keep swimmers safe during warm-up, following the Swimming Canada warm-up safety "
     "procedures. Reports to the Referee.",
     "Sets the tone for the session and keeps everyone safe."),
    ("", "Marshal",
     "Help the admin desk keep swimmers organized on deck.",
     "Getting swimmers to their heats stops anyone missing a race, and an orderly walk to the "
     "blocks lets them focus on the swim."),
    ("off-turns.jpg", "Inspector of Turns",
     "Watch swimmers at the start and through their turns to check the rules for their stroke.",
     "You are what makes the race fair and consistent for everyone in it."),
]

SENIOR_ROLES = [
    ("Judge of Stroke", "Watch swimmers through the race to check the rules for their stroke.",
     "Consistent stroke judging protects fairness for every swimmer in the race."),
    ("Starter", "With the Referee, start the race and judge the fairness of the start.",
     "A fair, consistent start is the foundation of a fair race."),
    ("Admin Desk", "Organize swimmers on deck and keep all the information current.",
     "Keeps the meet on schedule and swimmers where they need to be."),
    ("Chief Timekeeper", "Lead the timekeepers and support them through the session.",
     "Accurate timing across every lane, every race."),
    ("Chief Judge Electronics",
     "Supervise the inspectors of turns and judges of stroke, so the rules are applied the same "
     "way all meet.", "Keeps stroke and turn judging consistent across the whole competition."),
    ("Referee", "The highest authority at a meet, responsible for its overall operation and "
                "integrity.", "Every decision on deck ultimately runs through the Referee."),
]

EXPECTATIONS = [
    "Register as an official.",
    "Attend the officiating clinics for the roles you will work.",
    "Officiate at ROW meets when your swimmer is in the meet.",
]

MUST = [
    "Be 14 or older.",
    "Register each swim season, September 1 to August 31, to be an active official.",
    "Complete the training for the positions you will work at a competition.",
]

STEPS = [
    "<strong>Register.</strong> Complete the form shared with the ROW membership each season. "
    f"Re-registration is required every year; if you did not get the link, email {mail(OFFICIALS)}.",
    "<strong>Training.</strong> First time out, complete one or two short online courses from "
    "Swim Ontario. We send you everything you need.",
    "<strong>Tell us you are available.</strong> Watch your inbox about four weeks before each "
    "meet. Registered officials are contacted first.",
    "<strong>On the day.</strong> Wear a red or white shirt and black pants, shorts or a skirt. "
    "Your team gives you your assignment and any equipment.",
    "<strong>Enjoy it.</strong> You are now part of the group that makes every meet possible.",
]

officiating = wrap_page(
    hero("ROW Swim Club", "Officiating",
         "An essential role at every swim meet. No experience needed, and every hour counts "
         "towards your family&rsquo;s FPP points."),
    lanes_divider(),

    card(h2("Why officiating matters")
         + body("Swim meets are the milestones where swimmers test their training, build "
                "resilience and gain confidence. They are run almost entirely by volunteers, most "
                "of them ROW parents.")
         + img("off-meet-1.jpg", "Officials on deck at a ROW meet")
         + body("Volunteering does not just make the meet possible. It is the fastest way to "
                "learn how the sport works and how to support your own swimmer. We welcome "
                "volunteers at every level of experience and provide all the training.",
                margin="16px 0 0")
         + data_table(["Who runs our meets", "Contact"],
                      [["<strong>Meet Management</strong> organizes and runs ROW-hosted meets.",
                        mail(MEETMGR)],
                       ["<strong>Officials Development &amp; Administration</strong>, part of Meet "
                        "Management, makes sure there is a trained pool of officials available.",
                        mail(OFFICIALS)]])),

    '<div style="margin:24px 0 0;">' + card(
        h2("Where to start")
        + lede("No prior experience is needed for any of these four.")
        + "".join(
            (person(p, r, w, why) if p else
             f'<div class="row-person"><div class="row-person-text">'
             f'<div class="row-stage-head">{r}</div>'
             f'<div class="row-stage-lead">{w}</div>{body(why, margin="0")}</div></div>')
            for p, r, w, why in INTRO_ROLES)
        + note("More detail on any position is on the "
               + link(URL_SO_POSITIONS, "Swim Ontario positions page") + ".")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Senior positions")
        + lede("Senior officials mentor and supervise other volunteers. All of them need deck "
               "experience first, and some, like Referee, need certification in several other "
               "roles.")
        + img("off-referee.jpg", "A senior official on deck")
        + data_table(["Position", "What you do", "Why it matters"],
                     [[a, b, c] for a, b, c in SENIOR_ROLES])
        + note("Interested in a senior position? Get familiar with the "
               + link(URL_SO_CERT, "certification pathway") + " and email " + mail(OFFICIALS)
               + " so we can support you.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("What is expected")
        + body("Membership of any swim club in Canada comes with the expectation that families "
               "help run meets. At ROW that means three things.")
        + list_shell("".join(numbered_row(i + 1, t, i=i) for i, t in enumerate(EXPECTATIONS)))
        + img("off-registration.jpg", "Officials at the admin desk")
        + lede("To work on deck you must also:")
        + list_shell("".join(numbered_row(i + 1, t, i=i) for i, t in enumerate(MUST)))
        + callout("Time spent helping run meets earns Family Participation Program points. Our "
                  "officials administrators will walk any new volunteer through the process "
                  "&mdash; email " + mail(OFFICIALS) + " to start.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("How to get started")
        + list_shell("".join(numbered_row(i + 1, t, i=i)
                             for i, t in enumerate(STEPS)))) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("ROW hosted meets")
        + img("off-meet-3.jpg", "A ROW hosted meet in progress")
        + data_table(["", ""],
                     [["Meets a season", "Five or more"],
                      ["Volunteers needed a meet", "35 to 85"]])
        + body("Volunteering at a home meet supports the club and saves you the travel. The "
               "current schedule is on " + link(URL_HOSTED_MEETS, "ROW Hosted Meets")
               + ", and whether your swimmer is entered is on the "
               + link(URL_MEET_SCHEDULE, "Meet and Event Schedule") + ".", margin="16px 0 0")
        + callout("<strong>Want to do more?</strong> If you have helped for a season or more, "
                  "consider joining Meet Management, the group behind the scenes that makes "
                  "hosting possible. Email " + mail(MEETMGR) + ".")) + '</div>',
)


# ---------------------------------------------------------------------------
# ROW Clothing & Equipment
# ---------------------------------------------------------------------------

clothing = wrap_page(
    hero("ROW Swim Club", "ROW Clothing &amp; Equipment",
         "Where to get ROW team wear and swim equipment. For what your group specifically needs, "
         "see the ROW Equipment List."),
    lanes_divider(),

    card(h2("Team clothing")
         + img("logo-gmp-sportswear.png", "GMP Sportswear", cls="row-logo")
         + body("ROW has partnered with GMP Sportswear on Victoria Street in Kitchener. A "
                "family-owned business for over 30 years, Gus and the team at GMP look after our "
                "team wear.")
         + body("<strong>Open for 2026-27 purchases.</strong> After a short summer reset, we are "
                "ready for your ROW team clothing orders.")
         + body(link(URL_GMP, "Shop ROW team wear &rarr;"), margin="0")
         + note("Thank our volunteer Team Clothing Manager, Kristen Baskerville, when you see "
                "her.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Swim equipment and gear")
        + img("logo-ly-sports.png", "LY Sports", cls="row-logo")
        + body("ROW is partnered with LY Sports for suits, fins, kickboards and the rest, with a "
               "club discount. Our team page gives 20% off regular-priced items, plus another 2% "
               "at checkout with the code <strong>ROWSWIM</strong>. You can order online any "
               "time, all year.")
        + body(link(URL_LY, "Shop LY Sports, ROW team page &rarr;"), margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("What does my swimmer need?")
        + body("The " + link(URL_EQUIPMENT_LIST, "ROW Equipment List")
               + " has it group by group. Your swimmer&rsquo;s "
               + link(URL_PROGRAMS, "program page")
               + " also lists it, and a coach will confirm before or after a practice.")
        + note("Questions about team wear or gear? Email " + mail(CLOTHING) + ".")) + '</div>',
)


# ---------------------------------------------------------------------------
# Time Standards
# ---------------------------------------------------------------------------

time_standards = wrap_page(
    hero("ROW Swim Club", "Time Standards",
         "Standards change every season, so rather than keep our own copies this page links "
         "straight to the two organizations that set them."),
    lanes_divider(),

    card(h2("Where to find them")
         + body("Swim Ontario and Swimming Canada keep their own standards pages current, so "
                "those are always the best source.")
         + data_table(["Who", "What they cover", ""],
                      [[img("logo-swim-ontario.png", "Swim Ontario", cls="row-logo-sm"),
                        "Ontario provincial standards, including OSC, OAG, WOSA and OJI.",
                        link(URL_SO_STANDARDS, "View standards &rarr;")],
                       [img("logo-swimming-canada.png", "Swimming Canada", cls="row-logo-sm"),
                        "National standards, including Canadian Championships and preliminary "
                        "competition information.",
                        link(URL_SC_STANDARDS, "View standards &rarr;")]])
         + note("The 2025-26 standards that used to be listed here have been retired.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Compare your own times")
        + body(link(URL_GEEK, "geekswimmers.com")
               + " lets you compare your times against regional, provincial and national "
                 "standards. It is a free web app, built by a ROW parent.")
        + body("For a target that is closer than a standard, the "
               + link(f"{URL_FOR_SWIMMERS}/goal-setting-tool", "Goal Setting Tool")
               + " turns one best time into a goal for every other distance, with the splits to "
                 "swim it.", margin="0")) + '</div>',
)


PAGES = [("coaches-and-operations-team", coaches),
         ("our-olympians-and-paralympians", olympians),
         ("officiating", officiating),
         ("row-clothing-and-equipment", clothing),
         ("time-standards", time_standards)]

if __name__ == "__main__":
    for slug, page in PAGES:
        stem = slug.replace("-", "_")
        stem = stem[4:] if stem.startswith("row_") else stem
        out = f"/mnt/user-data/outputs/row_{stem}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<48}{len(page) // 1024:>5} KB")
