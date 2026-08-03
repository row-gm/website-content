"""Build the five Our Development Plan pages.

    python3 build_development_plan.py

  Our Development Plan   the section hub
  The ROW Way            four dimensions, twelve markers, the four-step scale
  From Plan to Pool Deck belief on the left, what was built on the right
  The Growth Spurt       maturation, with two generated diagrams
  The Birthday Gap       relative age

All five are for swimmers, families and coaches in the same words, which is the
one deliberate exception to the coach and family split. One vocabulary
throughout.

The two Growth Spurt diagrams are generated here rather than pasted as fixed
images, so their spacing can be checked. The original had the university row's
heads running through its own caption.
"""

import base64

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, numbered_row, data_table, lede,
)

from row_diagrams import ladder_diagram, as_img as diagram_img

from layers_common import (
    BASE, AGE_BANDS, URL_OUR_DEVELOPMENT_PLAN, URL_HOW_WE_DEVELOP_SWIMMERS,
    URL_THE_GROWTH_SPURT, URL_THE_BIRTHDAY_GAP, URL_FOR_SWIMMERS,
)

DISP = "'Arial Black', Arial, Helvetica, sans-serif"
SANS = "Arial, Helvetica, sans-serif"
GM = "gm@rowswimming.ca"

URL_PLAN_TO_DECK = f"{URL_OUR_DEVELOPMENT_PLAN}/from-plan-to-pool-deck"
URL_TRAINING_YEAR = f"{URL_OUR_DEVELOPMENT_PLAN}/the-training-year"
URL_WHAT_TO_EXPECT = f"{URL_OUR_DEVELOPMENT_PLAN}/what-to-expect"
URL_ROLE_OF_PARENTS = f"{URL_OUR_DEVELOPMENT_PLAN}/the-role-of-parents"
URL_GOAL_TOOL = f"{URL_FOR_SWIMMERS}/goal-setting-tool"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def mail(a):
    return f'<strong class="row-link">{a}</strong>'


def ask_coach():
    return note("Questions about your swimmer&rsquo;s development? Talk to your coach before or "
                "after a practice, or email " + mail(GM) + ".")


# ---------------------------------------------------------------------------
# The two Growth Spurt diagrams, generated so the spacing can be checked
# ---------------------------------------------------------------------------

def figure(cx, base_y, height, colour, w=22):
    """A stick figure: a head, and a body standing on base_y."""
    head_r = 10
    body_h = height - head_r * 2 - 4
    top = base_y - body_h
    return (f'<rect x="{cx - w // 2}" y="{top}" width="{w}" height="{body_h}" rx="{w // 2}" '
            f'fill="{colour}"/>'
            f'<circle cx="{cx}" cy="{top - head_r - 2}" r="{head_r}" fill="{colour}"/>')


def row_of_figures(base_y, heights, colour):
    step = 46
    x0 = 60
    return "".join(figure(x0 + i * step, base_y, h, colour)
                   for i, h in enumerate(heights))


def class_diagram():
    """Same class, three points in time. Captions sit clear of the tallest head:
    the original overlapped by 6px."""
    ROWS = [
        ("GRADE 6", "Same birth year. Some have started their growth spurt, most have not.",
         [52, 72, 44, 104, 56, 68, 40, 100, 58, 64, 46, 88], RED),
        ("GRADE 12", "Most have been through it. A few are still finishing.",
         [96, 112, 100, 124, 92, 116, 84, 122, 104, 110, 98, 120], TEAL),
        ("UNIVERSITY", "Everyone has finished. The gap has closed.",
         [116, 122, 118, 124, 114, 120, 116, 124, 118, 122, 116, 124], NAVY),
    ]
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 700">'
             '<rect width="620" height="700" fill="#FFFFFF"/>']
    y = 40
    for label, caption, heights, colour in ROWS:
        tallest = max(heights)
        base = y + 30 + tallest          # caption, gap, then the figures
        parts.append(f'<text x="30" y="{y}" font-family="{DISP}" font-size="15" '
                     f'fill="{NAVY}">{label}</text>')
        parts.append(f'<text x="30" y="{y + 20}" font-family="{SANS}" font-size="13" '
                     f'fill="{INK_SOFT}">{caption}</text>')
        parts.append(row_of_figures(base, heights, colour))
        parts.append(f'<line x1="30" y1="{base}" x2="590" y2="{base}" stroke="{LINE}" '
                     f'stroke-width="1.5"/>')
        y = base + 62
    parts.append('</svg>')
    return "".join(parts)


def early_late_diagram():
    """Two swimmers, one early and one late. At 12 they look different; by 18 not."""
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 340">'
             '<rect width="620" height="340" fill="#FFFFFF"/>']
    for i, (title, pairs) in enumerate([
            ("AT 12", [("early", 116, RED), ("late", 62, TEAL)]),
            ("AT 18", [("early", 128, RED), ("late", 126, TEAL)])]):
        x0 = 70 + i * 300
        base = 268
        parts.append(f'<text x="{x0 + 60}" y="42" font-family="{DISP}" font-size="15" '
                     f'fill="{NAVY}" text-anchor="middle">{title}</text>')
        for j, (who, h, colour) in enumerate(pairs):
            cx = x0 + j * 120
            parts.append(figure(cx, base, h, colour, w=30))
            parts.append(f'<text x="{cx}" y="{base + 26}" font-family="{SANS}" '
                         f'font-size="13" fill="{INK_SOFT}" text-anchor="middle">'
                         f'{who} spurt</text>')
        parts.append(f'<line x1="{x0 - 40}" y1="{base}" x2="{x0 + 160}" y2="{base}" '
                     f'stroke="{LINE}" stroke-width="1.5"/>')
    parts.append('</svg>')
    return "".join(parts)


def as_img(svg, alt):
    b = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return (f'<img src="data:image/svg+xml;base64,{b}" alt="{alt}" '
            f'style="width:100%;height:auto;display:block;border-radius:10px;'
            f'border:1px solid {LINE};background:#FFFFFF;" />')


# ---------------------------------------------------------------------------
# Our Development Plan
# ---------------------------------------------------------------------------

DIMENSIONS = [
    ("Physical", "What my body can do",
     "Endurance, speed, strength, and the ability to repeat hard work. The engine."),
    ("Technical", "What I can do in the water",
     "Stroke, starts, turns, underwaters and pacing. The skills that hold up when you are tired."),
    ("Mental", "How I think and race",
     "Focus, resilience, handling pressure and racing your own race. Trained on deck, not taught "
     "in a speech."),
    ("Character", "How I show up",
     "Effort, reliability, honesty, and how you treat the people around you. The part that "
     "outlasts the swimming."),
]

SYSTEM = [
    "<strong>The season is organized in phases.</strong> Blocks of training with different jobs: "
    "building, sharpening, recovering, racing. Each one is chosen, not inherited from last year.",
    "<strong>The week has a shape.</strong> Hard days and easy days sit in a deliberate order, "
    "and load builds across weeks rather than randomly.",
    "<strong>Every practice is built the same way.</strong> So the same set means the same thing "
    "on every deck, in every group.",
    "<strong>The prescription fits the swimmer.</strong> Same set, same purpose, different "
    "interval, distance or target.",
]

SECTION_PAGES = [
    (URL_HOW_WE_DEVELOP_SWIMMERS, "The ROW Way",
     "The twelve things we develop in every swimmer, in the swimmer&rsquo;s own words, and the "
     "four steps from learning something to owning it. The backbone of this whole section."),
    (URL_PLAN_TO_DECK, "From Plan to Pool Deck",
     "How each belief shows up in the 2026-27 program: the training ladder, group placement, how "
     "progress is measured, and what each coach is asked to do."),
    (URL_TRAINING_YEAR, "The Training Year",
     "Why training changes through the year, why times can go slower during a hard block, and "
     "what the five zones mean."),
    (URL_WHAT_TO_EXPECT, "What to Expect",
     "The shape of a racing season, the three kinds of meet, and the four things that help most "
     "&mdash; none of which happen at the pool."),
    (URL_ROLE_OF_PARENTS, "The Role of Parents",
     "The triangle of swimmer, coach and parent, and how the lead moves between the three as a "
     "swimmer grows."),
    (URL_THE_GROWTH_SPURT, "The Growth Spurt",
     "Every swimmer grows at their own time and it changes their swimming for a while. Why times "
     "stall, and why results at 12 do not predict results at 18."),
    (URL_THE_BIRTHDAY_GAP, "The Birthday Gap",
     "Age groups run January to December, so two swimmers in one group can be almost a year "
     "apart. What that is worth in seconds, and why it fades."),
    (URL_GOAL_TOOL, "Goal Setting Tool",
     "Turn one best time into a goal for every other distance, plus the splits to swim it."),
]

PLAN_FAQ = [
    ("Is this section for swimmers or for parents?",
     "Both, and for coaches too. These pages are deliberately written once, in words everyone "
     "can use, so a swimmer and a parent are reading the same thing."),
    ("Where is the detailed coaching framework?",
     "In the coaches&rsquo; area of the site. It covers training phases, zones, week structure "
     "and session design. It is written for staff and needs coach access."),
    ("Does this replace talking to my coach?",
     "No. It gives you the shared language for a better conversation. Your coach knows your "
     "swimmer; a web page does not."),
    ("My swimmer is young. Does any of this apply yet?",
     "Yes, in a lighter form. All four areas start on day one. What changes as a swimmer grows "
     "is how much of each, and how much they run themselves."),
]

plan_main = wrap_page(
    hero("ROW Swim Club", "Our Development Plan",
         "How we use swimming to build fast swimmers and capable young adults. Written for "
         "swimmers, coaches and families, in the same words."),
    lanes_divider(),

    card(h2("What we are trying to do")
         + body("Our goal is to <strong>graduate athletes who are experts in their own "
                "performance</strong>. Swimmers who know how they train, why it works, and what "
                "to do when it does not.")
         + body("Almost none of our swimmers will make a career of this sport. All of them will "
                "carry what it taught them. So we train the swimmer and the person at the same "
                "time, on purpose rather than by accident.", margin="0")
         + callout("<strong>Swimming is the vehicle, not the point.</strong> A swim club is a good "
                   "place to learn things that are hard to teach anywhere else: how to work at "
                   "something for years, how to lose and come back, how to be honest about your "
                   "own performance, how to be part of a group that depends on you. This is not a "
                   "softer version of competing. The swimmers who develop these habits are the "
                   "ones who end up fastest.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("The four things we develop")
        + lede("Everything we coach falls into one of four areas. A swimmer is not finished when "
               "they are fit. They are finished when all four are in place.")
        + data_table(["Area", "The question", "What sits inside it"],
                     [[a, b, c] for a, b, c in DIMENSIONS])) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("A system, not a collection of sessions")
        + body("Behind every practice is a plan that runs from the season down to a single set. "
               "Coaches share one vocabulary, so a swimmer moving between groups is not starting "
               "over.")
        + list_shell("".join(numbered_row(i + 1, t, i=i) for i, t in enumerate(SYSTEM)))
        + note("The full coaching framework is written for our coaching staff and lives in the "
               "coaches&rsquo; area. What matters to a swimmer or a family is that it exists, "
               "that it is written down, and that every coach works from the same one.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("In this section")
        + lede("Eight pages, written once for everyone. Start with The ROW Way.")
        + data_table(["Page", "What it covers"],
                     [[link(u, t), d] for u, t, d in SECTION_PAGES])) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Common questions")
        + data_table(["", ""], [[f"<strong>{q}</strong>", a] for q, a in PLAN_FAQ])
        + ask_coach()) + '</div>',
)


# ---------------------------------------------------------------------------
# The ROW Way
# ---------------------------------------------------------------------------

STEPS = [
    ("Learning it", "Someone has shown me. I can do it with help.", "The coach"),
    ("With reminders", "I can do it on my own when the coach reminds me.", "The coach, prompting"),
    ("On my own", "I do it every practice without being told.", "The swimmer"),
    ("When it&rsquo;s hard", "I do it tired, at speed, and when I race.",
     "The swimmer, under pressure"),
]

MARKERS = [
    ("Physical", [
        "I can keep going. I finish the session and hold the effort through a long set.",
        "I can go fast. Every short sprint is full speed, not just the first one.",
        "I look after myself. Sleep, food after practice, water, arriving ready."]),
    ("Technical", [
        "I hold my streamline and underwaters off every wall.",
        "I keep my stroke together when I get tired.",
        "I can swim my race, not just swim fast. Starts, turns, finishes, pacing."]),
    ("Mental", [
        "I know what I am working on today and why. I stay with it.",
        "I bounce forward from a bad swim or a hard set. I learn and adapt.",
        "I know what I am aiming at and what steps are required."]),
    ("Character", [
        "I am ready to train. On time, kit packed, mindset focused.",
        "I am coachable. I listen, I try the change, I ask when I do not understand.",
        "I am part of the team. I cheer, I include people, I leave the deck better."]),
]

L, W, O, H, DASH = "Learning it", "With reminders", "On my own", "When it&rsquo;s hard", "&mdash;"
GRID = [
    ("Keep going", L, W, O, H),
    ("Go fast", W, O, O, H),
    ("Look after myself", L, L, W, O),
    ("Streamline and underwaters", L, W, O, H),
    ("Stroke when tired", DASH, L, W, H),
    ("Swim my race", DASH, L, W, O),
    ("Stay with the focus", L, W, O, H),
    ("Come back from a setback", L, L, W, O),
    ("Know what I&rsquo;m aiming at", DASH, L, W, O),
    ("Ready to train", W, O, O, H),
    ("Coachable", L, W, O, H),
    ("Part of the team", L, W, O, O),
]

HOW_TO_READ = [
    "<strong>For swimmers.</strong> Where you are now is not a grade and not a ranking. Find "
    "your stage, read down the column, and pick one thing to move up a step. One. Then tell your "
    "coach which one you picked.",
    "<strong>For families.</strong> &ldquo;With reminders&rdquo; means your swimmer can do it and "
    "still needs prompting. That is normal and it is not a complaint. The most useful thing you "
    "can do is ask what they are working on, then leave the coaching to the coach.",
    "<strong>For coaches.</strong> This is descriptive. Use it in conversation, in season "
    "reviews, and when explaining a group move. Do not turn it into a checklist a swimmer has to "
    "pass. If a marker does not fit your group, say so.",
]

USES = [
    ("Swimmer reviews", "Twice a season",
     "Coach and swimmer go through the twelve markers together. The swimmer says where they think "
     "they are first. They leave with one or two things to work on, not twelve."),
    ("Season planning", "Start of a cycle",
     "A group&rsquo;s weak markers shape what the coach emphasizes in the next block. If half a "
     "group cannot hold stroke when tired, that is a training decision, not a talk."),
    ("Group assessments", "When a move is being considered",
     "One input among several, alongside times, attendance, training history and readiness. It is "
     "not a pass mark, and no single marker decides a move."),
]

row_way = wrap_page(
    hero("For swimmers, families and coaches", "The ROW Way",
         "Our approach to using swimming to develop great human beings. Four things we develop, "
         "twelve things we watch for, and one scale showing how far a swimmer has taken each."),
    lanes_divider(),

    card(h2("What we are working towards")
         + body("Our goal is to graduate athletes who are experts in themselves and their own "
                "performance. Whether they go on to university swimming, another sport, or none "
                "of it, they will know how to look after themselves.")
         + body("That means every year a swimmer should need our direct coaching a little less. "
                "They should know what a hard set feels like, what their body needs afterwards, "
                "and what they are trying to fix.")
         + body("Swimming is how we do it, not why we do it. A handful of ROW swimmers will make "
                "a career of this sport; all of them will carry what it taught them.", margin="0")
         + callout("This page is not a checklist and it is not a ranking. It describes what we "
                   "are developing, and how we talk about a swimmer&rsquo;s progress at each "
                   "stage.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Four things we develop")
        + lede("They carry equal weight. A swimmer strong in one and absent in another is not "
               "further ahead.")
        + data_table(["Area", "The question", "What sits inside it"],
                     [[a, b, c] for a, b, c in DIMENSIONS])) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("How far along: four steps")
        + lede("Every marker moves through the same four steps. The steps are a handover: each "
               "one moves a little more of the responsibility from the coach to the swimmer.")
        + data_table(["Step", "What it means", "Who is driving"],
                     [[a, b, c] for a, b, c in STEPS])
        + callout("<strong>The last step is the real test.</strong> A swimmer who only holds a "
                  "skill when fresh has not finished learning it. Races, and most of life, happen "
                  "when we are not at our best.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Twelve things we watch for")
        + lede("Written the way a swimmer would say them, because they are for the swimmer first.")
        + "".join(
            f'<div class="row-stage-head" style="margin:22px 0 8px;">{area}</div>'
            + data_table([""], [[m] for m in items])
            for area, items in MARKERS)) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("The whole model")
        + lede("What we would usually expect at each stage. A dash means we are not working on "
               "it yet.")
        + data_table(["Marker"] + [f"{b}<br /><span class=\"row-lbl-in\">{g}</span>"
                                   for b, g in AGE_BANDS],
                     [list(r) for r in GRID])
        + callout("<strong>&Under is a stage, not a birthday.</strong> Swimmers move when they "
                  "are ready by training and maturity. Some 13 year olds belong in the 12&U "
                  "column and some 11 year olds do not.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("How to read this")
        + list_shell("".join(numbered_row(i + 1, t, i=i)
                             for i, t in enumerate(HOW_TO_READ)))) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("How we use it through the year")
        + lede("The model is not a document to read once. It is what our conversations about a "
               "swimmer are built on.")
        + data_table(["Where", "When", "What happens"], [[a, b, c] for a, b, c in USES])
        + note("Group moves are about readiness &mdash; a coaching judgement about when a swimmer "
               "has got everything they can from their current group. This page makes sure that "
               "conversation uses the same words every time.")) + '</div>',
)


# ---------------------------------------------------------------------------
# From Plan to Pool Deck
# ---------------------------------------------------------------------------

BELIEFS = [
    ("We are building for progressive development", [
        ("The ladder has to start somewhere a beginner can reach.",
         "<strong>The ROW Swim Academy.</strong> The first rung. Saturday mornings at Cameron "
         "Heights, three class options of forty minutes, with a coach on every lane. Many of "
         "those coaches are our own SD swimmers, on deck fifteen minutes after finishing "
         "their own session."),
        ("Swimmers are developed as people first, in steps that promote improvement season after "
         "season.",
         "<strong>A ladder with small steps.</strong> Sessions a week rise two, three, three then "
         "four through Junior. Four, five then six through Regional. Five, six then seven through "
         "Provincial. Eight at National. Nobody jumps from four sessions to eight."),
        ("Swimmers should be able to change their choice as their lives change.",
         "<strong>A pathway system.</strong> Six pathways with real choices, so a swimmer can "
         "move without leaving the sport."),
        ("Twelve hours of recovery between an evening session and the next morning.",
         "<strong>A scheduling rule that cannot be broken.</strong> No group finishes in the "
         "evening and starts at 6:00 am. It is met everywhere in the timetable. Growing bodies "
         "need the sleep more than they need the extra session."),
    ]),
    ("A birth year is not a training group", [
        ("Where a swimmer sits close to the top of an age band, we will be flexible.",
         "<strong>Placement by readiness, not birth year.</strong> A swimmer wanting to compete "
         "should be in the group that suits them rather than the one their birth year puts them "
         "in."),
        ("Swimmers at different stages need different amounts, not different sports.",
         "<strong>Age Group Development split in two.</strong> One group of about seventy became "
         "AGD 2 at four sessions and AGD 1 at five, each with its own lead coach. Junior "
         "Development runs as JD1 and JD2, training alongside each other at different volumes."),
    ]),
    ("Times are one measure, not the measure", [
        ("Progress is measured against every part of development, not just times in best events.",
         "<strong>Two formal progress conversations a year</strong>, with the swimmer and the "
         "family, against objectives set at the start of the phase. Not a results printout."),
        ("Families should be able to describe their swimmer&rsquo;s plan.",
         "<strong>A written season plan for every group</strong>, setting out the phases, the "
         "technical priorities and the objectives, shared with families. Every group, including "
         "the two and three session programs."),
    ]),
    ("Skills are taught, not hoped for", [
        ("Technical work should be on a plan, not fitted in when time allows.",
         "<strong>Technical work on a named cycle</strong> for every group, so skills are taught "
         "on a schedule rather than whenever a session runs short."),
        ("A swimmer learns faster when they can see what they are being asked to do.",
         "<strong>Underwater video on a regular cadence</strong>, with the footage shown to the "
         "swimmer, and a GoSwim account for every swimmer outside the Academy and every coach."),
    ]),
    ("The same set, a different prescription", [
        ("Training should fit the swimmer.",
         "<strong>Differentiated work within every session</strong>, so sprint, middle distance "
         "and distance swimmers in the same lane are not doing identical work."),
        ("A coach can only individualize what they can see.",
         "<strong>Swimmers per lane falls as the level rises.</strong> National trains four to a "
         "lane, PD1 at five, and the Recreation groups at four or fewer. In our youngest program "
         "every lane has its own coach."),
    ]),
    ("We develop coaches the way we develop swimmers", [
        ("A club cannot promise long-term development to swimmers and treat its coaches as "
         "interchangeable.",
         "<strong>Every coach has a development plan.</strong> Certification, time on deck with a "
         "mentor, and support to take on more as they are ready. Assistant roles are a route into "
         "the job, not a holding pattern."),
        ("What our most experienced coaches know has to be passed on while they are here to pass "
         "it on.",
         "<strong>Mentor coaches work across every group</strong>, at training and at meets. And "
         "ROW alumni coach here: SD swimmers take the Academy on Saturday mornings, straight "
         "after their own session."),
    ]),
]

DECK_FAQ = [
    ("Does a smaller program get a smaller version of this?",
     "No. A written season plan, differentiated work, a technical cycle, underwater video, a "
     "GoSwim account, dryland with an owner and two progress conversations apply to every group, "
     "including the two and three session programs."),
    ("How do I know which group my swimmer should be in?",
     "Written criteria for moving between groups and pathways are published at the start of the "
     "season. Age band is a guide, and readiness matters more than birth year."),
    ("Why not just train more?",
     "Because more is not the goal; being able to keep going for years is. Session lengths are "
     "capped, recovery between sessions is protected, and only PD1 and ND ever "
     "train twice in a day."),
    ("Is the Recreation pathway a step down?",
     "It is a different choice, not a lower one. It is for swimmers who want technique, fitness "
     "and a group without the competitive commitment. Staying in the sport is a good outcome."),
]

plan_to_deck = wrap_page(
    hero("Our Development Plan", "From Plan to Pool Deck",
         "Our philosophy is not a separate document from our program. Here is how each belief "
         "shows up in what actually happens at the pool."),
    lanes_divider(),

    card(h2("Beliefs are easy. Design choices are not.")
         + body("Any club can write down that it develops the whole athlete. What matters is the "
                "timetable, the group structure, the training system, and what each coach is "
                "asked to do.")
         + body("Every program choice at ROW traces back to the best interest of the swimmer. If "
                "we learned something that would help our swimmers, we would change the program.",
                margin="0")),

    '<div style="margin:24px 0 0;">' + card(
        h2("The whole ladder")
        + lede("From forty minutes on a Saturday to fourteen hours a week. The gaps between "
               "rungs are deliberately small: nobody jumps from four sessions to eight.")
        + diagram_img(ladder_diagram(), "Every ROW group as a rung, ordered by hours a week")) + '</div>',

    *[f'<div style="margin:24px 0 0;">' + card(
        h2(theme)
        + data_table(["What we believe", "So we built"], [[b, w] for b, w in pairs])) + '</div>'
      for theme, pairs in BELIEFS],

    '<div style="margin:24px 0 0;">' + card(
        h2("Common questions")
        + data_table(["", ""], [[f"<strong>{q}</strong>", a] for q, a in DECK_FAQ])
        + ask_coach()) + '</div>',
)


# ---------------------------------------------------------------------------
# The Growth Spurt
# ---------------------------------------------------------------------------

SPURT_FACTS = [
    "<strong>It happens at very different ages.</strong> On average around 12 for girls and "
    "around 14 for boys. Average is not a rule: two years either side is completely normal.",
    "<strong>Arms and legs grow first.</strong> Hands, feet and limbs lengthen before the body "
    "catches up. You are suddenly a different shape in the water.",
    "<strong>Strength arrives later.</strong> You get longer before you get stronger. The "
    "strength catches up, but not at the same time.",
]

SPURT_EFFECTS = [
    ("Your feel for the water changes",
     "Longer arms move through the water differently. A stroke that worked last season can feel "
     "clumsy."),
    ("Your timing goes off",
     "Turns, starts and stroke rhythm were tuned to a body you no longer have."),
    ("Your times can stall or go backwards",
     "For a few months you might train well and swim slower. This is normal and it passes."),
]

SPURT_ADVICE = [
    ("If you are a swimmer", [
        "Judge yourself against yourself. Your own times, your own skills, your own effort. Not "
        "the tallest person in your lane.",
        "Work on skills while you grow. Turns, starts, streamline, underwaters and pacing do not "
        "depend on being big. They are what you will still own when everyone catches up.",
        "Tell your coach how you feel. Sore knees, tight backs and heavy legs are common during "
        "a spurt. Say something."]),
    ("If you are a parent", [
        "Expect a flat patch and do not panic. A season with few best times during a growth "
        "spurt is not a wasted season.",
        "Praise the things they control. Attendance, effort, attitude and skills, not the "
        "finishing position.",
        "Watch for growing pains and fatigue. Growing takes energy, so sleep and food matter "
        "more during this period, not less."]),
    ("If you are a coach", [
        "Track height, not just times. A sudden jump explains a lot about a swimmer&rsquo;s "
        "month.",
        "Protect technique through the spurt. This is when a stroke can drift without anyone "
        "noticing.",
        "Do not read early results as potential. Group moves and expectations should account for "
        "where a swimmer is in their growth, not just where they finished."]),
]

SPURT_FAQ = [
    ("How do I know if I am in a growth spurt?",
     "Shoes that stop fitting, trousers getting short quickly, and feeling clumsy or sore. Your "
     "coach may also track your height through the season."),
    ("How long does it last?",
     "The fastest part usually lasts about a year, and the awkward feeling in the water is often "
     "shorter than that. Growth continues more slowly for a few years after."),
    ("Should I train less while I am growing?",
     "No. You keep training. What may change is the emphasis, with more attention to skills while "
     "your body settles. Your coach will guide this."),
    ("My times got worse. Am I doing something wrong?",
     "Probably not. A flat or backwards patch during a growth spurt is one of the most normal "
     "things in swimming. Keep coming and keep working on skills."),
    ("Does growing early mean I will be a better swimmer?",
     "No. It means you got there first. The swimmers around you are still coming."),
]

growth_spurt = wrap_page(
    hero("Our Development Plan", "The Growth Spurt",
         "Every swimmer grows at their own time. Understanding when, and what it does to "
         "swimming, makes the next few years easier for everyone."),
    lanes_divider(),

    card(h2("How growth happens")
         + body("If you have been to a graduation ceremony for elementary or high school, you "
                "have seen this already. Growth is not steady, and the differences in timing "
                "change what a swimmer can do.")
         + as_img(class_diagram(), "The same class at three points in time, with the height "
                                   "differences closing by university")
         + note("Same class, three points in time. By the last row everyone has finished growing "
                "and the gap has closed. Between the first row and the last, races are being won "
                "and lost by biology.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("What a growth spurt is")
        + body("Somewhere in your teens you grow faster than at any time since you were a baby. "
               "Coaches call the fastest point peak height velocity. We just call it the growth "
               "spurt.")
        + list_shell("".join(numbered_row(i + 1, t, i=i) for i, t in enumerate(SPURT_FACTS)))
        + note("Nobody chooses when it happens. It is not something you earn by training harder, "
               "and it is not something you can hurry along.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("What it does to your swimming")
        + body("A growth spurt can make swimming feel worse for a while. That surprises people, "
               "so it is worth saying plainly.")
        + data_table(["What changes", "Why"], [[a, b] for a, b in SPURT_EFFECTS])
        + callout("If your times stop improving during a growth spurt, that is not a sign you are "
                  "working less hard or that you have hit your limit. It is a sign your body is "
                  "busy.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Why results at 12 can mislead")
        + body("At 12, a swimmer who grew early is racing swimmers who have not started yet. They "
               "are bigger, stronger and further along. They often win.")
        + body("That advantage is real, and it is also temporary. When everyone finishes growing "
               "it disappears. Some swimmers who won everything at 12 are mid-pack at 17. Some "
               "who never made a final at 12 are the fastest in the club at 17.")
        + as_img(early_late_diagram(), "Two swimmers, one who grew early and one late, similar in "
                                       "height by 18")
        + note("Two swimmers, one early and one late. At 12 they look very different. By 18 they "
               "do not.")
        + callout("This cuts both ways. If you are winning now, your speed is real, but some of "
                  "your lead is timing and it will not last, so keep building skills. If you are "
                  "behind now, you are not out of the race. You have not started yours yet.")) + '</div>',

    *[f'<div style="margin:{"24px" if i == 0 else "16px"} 0 0;">' + card(
        h2(who) + data_table([""], [[t] for t in items])) + '</div>'
      for i, (who, items) in enumerate(SPURT_ADVICE)],

    '<div style="margin:24px 0 0;">' + card(
        h2("Common questions")
        + data_table(["", ""], [[f"<strong>{q}</strong>", a] for q, a in SPURT_FAQ])
        + note("This page and " + link(URL_THE_BIRTHDAY_GAP, "The Birthday Gap")
               + " describe two different clocks that stack on top of each other.")
        + ask_coach()) + '</div>',
)


# ---------------------------------------------------------------------------
# The Birthday Gap
# ---------------------------------------------------------------------------

FADE = [
    "<strong>It is strongest at 12 to 15.</strong> One study of elite youth swimmers found the "
    "effect only in 12 year old girls and in boys between 12 and 15. Outside that window it was "
    "not there.",
    "<strong>It shrinks with age.</strong> As swimmers finish growing, eleven months of age stops "
    "meaning very much. A 20 year old born in December is not behind a 20 year old born in "
    "January.",
    "<strong>It can turn around.</strong> Some research finds the pattern reverses among "
    "adult swimmers, with late-year swimmers over-represented. One suggested reason is "
    "that they had to "
    "develop skill and resilience to survive the years when they were the youngest.",
]

GAP_ADVICE = [
    ("If you are a swimmer", [
        "Race the clock, not the lane beside you. Your own best times are the only fair "
        "comparison you have.",
        "If you are one of the youngest, you are not behind. You are younger. Those are different "
        "things, and the difference goes away.",
        "If you are one of the oldest, build skills now. Some of your lead is months, not "
        "ability. Skills are what you keep when the months stop counting."]),
    ("If you are a parent", [
        "Check the birthday before you read the result. A December swimmer mid-pack in their age "
        "group may be well ahead of where a January swimmer was at the same point.",
        "Do not let a slow year at 12 end the story. This is the age where swimmers quit, and "
        "often the ones quitting are the youngest in the group rather than the least able.",
        "Ask about progress, not placings. Best times, skills and attendance say more about a 12 "
        "year old than a finish position does."]),
    ("If you are a coach", [
        "Know the birth months in your group. It changes how you read a result and how you talk "
        "to the swimmer about it.",
        "Do not let selection compound the gap. Attention, lane order and group moves based on "
        "current results will systematically favour early-year swimmers.",
        "Judge on trajectory and skills. Where a swimmer is heading, and what they can do in the "
        "water, beats where they finished on Sunday."]),
]

GAP_FAQ = [
    ("Should age groups be organized differently?",
     "Some sports have tried, moving swimmers up on their birthday rather than on 1 January. It "
     "helps, but competition calendars are built around age groups, so no club can fix this "
     "alone. Understanding it is what we can do."),
    ("My swimmer is born in December. Are they at a disadvantage?",
     "In their age group races at 12, yes, by a small and measurable amount. By 17 or 18 it has "
     "essentially gone. The main risk is not the seconds. It is deciding too early that they are "
     "not good at this."),
    ("My swimmer is born in January and wins a lot. Does that not count?",
     "It counts. They are genuinely swimming those times. Just know that part of the margin is "
     "months rather than ability, and it will not be there forever. The way to keep the lead is "
     "skills."),
    ("Does this apply to every event?",
     "The research finds it more strongly in shorter, more strength-dependent events, and in "
     "butterfly and breaststroke. It shows up almost everywhere at 12, though."),
    ("Is this an excuse for a bad swim?",
     "No. It is context for reading a season, not a reason to train less. Effort, attendance and "
     "skills are still entirely in the swimmer&rsquo;s hands."),
]

birthday_gap = wrap_page(
    hero("Our Development Plan", "The Birthday Gap",
         "Age groups run from January to December. Two swimmers in the same group can be almost a "
         "year apart, and at 12 a year is a lot."),
    lanes_divider(),

    card(h2("Same age group, nearly a year apart")
         + body("A swimmer born on 2 January and a swimmer born on 30 December are both 12. They "
                "train in the same group and race the same events all season. The January "
                "swimmer has had nearly one more year of growing, training and racing.")
         + body("Nobody chose this. It is just where the calendar falls. But it shows up in "
                "results, and it is worth understanding before anyone draws conclusions from "
                "them.", margin="0")),

    '<div style="margin:24px 0 0;">' + card(
        h2("What a few months is worth")
        + body("French researchers looked at more than five million swims by swimmers aged 10 to "
               "18. They found each extra day of age is worth roughly eight thousandths of a "
               "second.")
        + body("Across a full year that adds up to about <strong>three seconds</strong>. In a 12 "
               "year old&rsquo;s race, three seconds is not a small margin. It can be the "
               "difference between a final and the outside lanes.")
        + body("This is not about talent or effort. It is the same reason we do not race 12 year "
               "olds against 14 year olds.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Who ends up in the fast lane")
        + body("If birthdays did not matter, each quarter of the year would produce about a "
               "quarter of the fast swimmers. That is not what happens. Among all 12 year olds "
               "the gap is already there, and among the fastest tenth it is much wider: nearly "
               "five early-year swimmers for every late-year one.")
        + callout("The pattern gets stronger the more selective the group. That matters, because "
                  "the fastest swimmers get the most attention, the most encouragement and often "
                  "the best lanes. A head start turns into a bigger head start.")
        + note("A review of the research across many countries found this uneven pattern in most "
               "of the studies it looked at. It is one of the best documented findings in youth "
               "sport, and it is not unique to swimming.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("And then it fades")
        + body("Here is the part that matters most. The birthday gap is largest in the years "
               "either side of 12, and it shrinks as swimmers get older.")
        + list_shell("".join(numbered_row(i + 1, t, i=i) for i, t in enumerate(FADE)))
        + note("The evidence is not unanimous on whether the gap disappears completely at the "
               "very top. What every study agrees on is that it is far bigger at 12 than at "
               "18.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Two clocks, not one")
        + body("This page and " + link(URL_THE_GROWTH_SPURT, "The Growth Spurt")
               + " describe different things, and they stack on top of each other.")
        + data_table(["Clock", "What it decides"],
                     [["Your birthday", "How many months of life you have had. Fixed, and you can "
                                        "work it out from a calendar."],
                      ["Your growth spurt", "How far through puberty you are. It varies by years "
                                            "and nobody controls it."]])
        + callout("At 12, a January swimmer who grew early and a December swimmer who has not "
                  "started can be three years apart in development while being the same age on "
                  "paper. The race result tells you almost nothing about which one will be faster "
                  "at 18.")) + '</div>',

    *[f'<div style="margin:{"24px" if i == 0 else "16px"} 0 0;">' + card(
        h2(who) + data_table([""], [[t] for t in items])) + '</div>'
      for i, (who, items) in enumerate(GAP_ADVICE)],

    '<div style="margin:24px 0 0;">' + card(
        h2("Common questions")
        + data_table(["", ""], [[f"<strong>{q}</strong>", a] for q, a in GAP_FAQ])
        + ask_coach()) + '</div>',
)


PAGES = [("our-development-plan", plan_main),
         ("the-row-way", row_way),
         ("from-plan-to-pool-deck", plan_to_deck),
         ("the-growth-spurt", growth_spurt),
         ("the-birthday-gap", birthday_gap)]

if __name__ == "__main__":
    for slug, page in PAGES:
        out = f"/mnt/user-data/outputs/row_{slug.replace('-', '_')}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<44}{len(page) // 1024:>4} KB")
