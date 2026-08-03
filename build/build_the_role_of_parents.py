"""Build The Role of Parents, for the Development Plan section.

    python3 build_the_role_of_parents.py

A family page. One vocabulary with the coach pages. No coach-only lines. Never
points a family at a coach on deck: before or after a practice.

The triangle is drawn as an SVG data URI because the CMS allowlist has no svg
tag. Same approach as The Growth Spurt.
"""

import base64

from row_page_helpers import (
    NAVY, TEAL, RED, SAND, FOAM, INK, INK_SOFT, LINE,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import (
    URL_OUR_DEVELOPMENT_PLAN, URL_HOW_WE_DEVELOP_SWIMMERS,
    URL_THE_GROWTH_SPURT, URL_THE_BIRTHDAY_GAP,
)

DISP = "'Arial Black', Arial, Helvetica, sans-serif"
SANS = "Arial, Helvetica, sans-serif"


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


# ---------------------------------------------------------------------------
# The triangle
# ---------------------------------------------------------------------------

MUTED = "#C9CFD1"


def corner(cx, cy, colour, label, job, job_y):
    """A corner of the big triangle. The job label sits outside the triangle,
    never across the lines: that was the mistake in the first version."""
    return (
        f'<circle cx="{cx}" cy="{cy}" r="48" fill="{colour}"/>'
        f'<text x="{cx}" y="{cy + 6}" font-family="{DISP}" font-size="15" fill="#FFFFFF" '
        f'text-anchor="middle">{label}</text>'
        f'<text x="{cx}" y="{job_y}" font-family="{SANS}" font-size="13.5" fill="#4B5B60" '
        f'text-anchor="middle">{job}</text>'
    )


def triangle_svg():
    s = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 450">'
        f'<rect width="680" height="450" fill="#FFFFFF"/>'
        f'<line x1="306" y1="138" x2="152" y2="288" stroke="{LINE}" stroke-width="2"/>'
        f'<line x1="374" y1="138" x2="528" y2="288" stroke="{LINE}" stroke-width="2"/>'
        f'<line x1="166" y1="322" x2="514" y2="322" stroke="{LINE}" stroke-width="2"/>'
        f'<text x="196" y="196" font-family="{SANS}" font-size="12.5" fill="{INK_SOFT}" '
        f'text-anchor="middle" transform="rotate(-44 196 196)">swimmer and coach</text>'
        f'<text x="484" y="196" font-family="{SANS}" font-size="12.5" fill="{INK_SOFT}" '
        f'text-anchor="middle" transform="rotate(44 484 196)">parent and coach</text>'
        f'<text x="340" y="310" font-family="{SANS}" font-size="12.5" fill="{INK_SOFT}" '
        f'text-anchor="middle">parent and swimmer</text>'
        + corner(340, 104, NAVY, "SWIMMER", "does the work", 40)
        + corner(118, 322, TEAL, "COACH", "decides the training", 396)
        + corner(562, 322, RED, "PARENT", "makes it all possible", 396)
        + f'</svg>'
    )
    b = base64.b64encode(s.encode("utf-8")).decode("ascii")
    return (f'<img src="data:image/svg+xml;base64,{b}" alt="A triangle with the swimmer, the '
            f'coach and the parent at its corners" style="width:100%;height:auto;display:block;'
            f'border-radius:10px;border:1px solid {LINE};background:#FFFFFF;" />')


def small_triangle(leader):
    """The same triangle at stage size. The corner that leads is full colour and
    larger; the other two are muted. No labels along the sides: at this size they
    would be unreadable, and the big triangle above has already explained them.

    Labels sit outside the circles, so nothing overlaps at any size.
    """
    PTS = [("swimmer", 130, 74, NAVY, "SWIMMER", 26),
           ("coach", 54, 176, TEAL, "COACH", 224),
           ("parent", 206, 176, RED, "PARENT", 224)]
    out = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 240">'
           '<rect width="260" height="240" fill="#FFFFFF"/>')
    for a, b_ in [(0, 1), (0, 2), (1, 2)]:
        out += (f'<line x1="{PTS[a][1]}" y1="{PTS[a][2]}" x2="{PTS[b_][1]}" '
                f'y2="{PTS[b_][2]}" stroke="{LINE}" stroke-width="1.5"/>')
    for key, cx, cy, colour, label, ly in PTS:
        lead = key == leader
        out += (f'<circle cx="{cx}" cy="{cy}" r="{34 if lead else 24}" '
                f'fill="{colour if lead else MUTED}"/>'
                f'<text x="{cx}" y="{ly}" font-family="{DISP}" '
                f'font-size="{11.5 if lead else 10.5}" '
                f'fill="{"#152225" if lead else INK_SOFT}" '
                f'text-anchor="middle">{label}</text>')
    out += '</svg>'
    b = base64.b64encode(out.encode("utf-8")).decode("ascii")
    return (f'<img src="data:image/svg+xml;base64,{b}" alt="The triangle with the {leader} '
            f'leading" style="width:100%;max-width:220px;height:auto;display:block;'
            f'margin:0 auto;" />')


# ---------------------------------------------------------------------------
# Content
# ---------------------------------------------------------------------------

STAGES = [
    ("The early years", "parent", "ROW Swim Academy, TOPS, Junior Development",
     "The parent leads",
     "You run almost everything. Getting there, the kit bag, the food, the sleep, the mood in "
     "the car. Your swimmer&rsquo;s job at this stage is to turn up and enjoy it. The coach is "
     "teaching skills rather than managing a season."),
    ("The middle years", "coach", "Age Group Development, PD3, PD2",
     "The coach leads",
     "The training plan starts driving the week, and the coach is the one holding it. This is "
     "the hardest shift for a parent, because it means stepping back from the content while "
     "staying fully in charge of everything around it. Your swimmer begins owning their own "
     "bag, their own effort, and their own honesty about how a session went."),
    ("The later years", "swimmer", "Senior Development, PD1, National Development",
     "The swimmer leads",
     "Your swimmer talks to their coach directly, sets their own goals, and decides what to do "
     "when something is not working. You become transport, food, and the person who is glad to "
     "see them whatever the clock said. That is not a smaller role. It is the one that lasts."),
]

HANDOVER = [
    ("Packing the kit bag", "Around 10 to 12",
     "Let them forget things. A forgotten pair of goggles teaches more than ten reminders."),
    ("Talking to the coach about a race", "Around 12 to 14",
     "Start with them asking one question themselves. It is a skill, and it is faster to learn "
     "than most parents expect."),
    ("Deciding whether to swim when tired or sore", "Around 14",
     "With the coach, not instead of the coach. Learning to tell the difference between tired "
     "and hurt is part of the sport."),
    ("Setting the goals", "Around 14 to 16",
     "Goals a swimmer chose are the ones they chase. Your job becomes asking about them rather "
     "than setting them."),
]

WHO_TO_ASK = [
    ("How my swimmer is progressing", "Parent to coach",
     "Two proper conversations a year, against the objectives set for the phase. Bigger "
     "questions belong there."),
    ("Why we did that set today", "Swimmer to coach",
     "From about 12 up, this is your swimmer&rsquo;s question to ask. Encourage it rather than "
     "asking it for them."),
    ("Schedules, fees, meet entries", "Parent to the office",
     "Nothing to do with the coach on deck. Email is quicker and it gets a written answer."),
    ("Something that worries you about the group or the environment",
     "Parent to coach, then the General Manager",
     "Raise it directly and early. There is a clear route, and using it works better than "
     "letting it sit."),
]


page = wrap_page(
    hero("Our Development Plan", "The Role of Parents",
         "Three people make a swimmer. The one out in front changes as they grow."),
    lanes_divider(),

    card(h2("Three corners, three jobs")
         + body("A swimmer sits inside a triangle. Each corner has a job that nobody else in "
                "the triangle can do, and the whole thing works when each one sticks to theirs.")
         + triangle_svg()
         + note("The sides matter as much as the corners. Each one is a line of communication, "
                "and each has to stay open for the triangle to hold.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Who leads changes as they grow")
        + lede("The triangle stays the same shape. What moves is which corner is out in front.")
        + "".join(
            f'<div class="row-stage">'
            f'<div class="row-stage-pic">{small_triangle(who)}</div>'
            f'<div class="row-stage-text">'
            f'<div class="row-stage-head">{stage}</div>'
            f'<div class="row-stage-lead">{lead}</div>'
            f'<div class="row-stage-groups">{groups}</div>'
            f'{body(desc, margin="0")}</div></div>'
            for stage, who, groups, lead, desc in STAGES)
        + callout("<strong>The shifts are the point, not a side effect.</strong> Our goal is a "
                  "swimmer who is an expert in their own performance. That cannot happen if the "
                  "parent is still leading at seventeen, and it will not happen by accident at "
                  "any age.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("What to hand over, and roughly when")
        + lede("Ages are a guide, not a rule. Swimmers are ready at different times, and that "
               "is normal.")
        + data_table(["What", "Roughly when", "How"], [[a, b, c] for a, b, c in HANDOVER])
        + note("Handing something over usually means watching it be done badly for a while. "
               "That is the cost, and it is worth paying.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Keeping the lines open")
        + body("Most difficulty in the triangle comes from a question going to the wrong corner, "
               "or from a line going quiet. Neither is hard to fix once you know which is which.")
        + data_table(["What you want to raise", "Who with", "How it works best"],
                     [[a, b, c] for a, b, c in WHO_TO_ASK])
        + callout("<strong>Catch a coach before or after a practice, not during one.</strong> "
                  "A coach on deck is coaching, and a conversation then takes their attention "
                  "off a lane of swimmers.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("The car ride home")
        + body("It is the most-remembered conversation in youth sport, and the one most often "
               "got wrong. A swimmer who has just raced badly already knows. What they need on "
               "the way home is not analysis.")
        + body("<strong>The six words that work: I love watching you swim.</strong> Then let "
               "them lead. If they want to talk about the race they will, and if they do not, "
               "the race will still be there tomorrow when the coach goes through it.")
        + body("If you want a question, make it one of theirs to answer: what went well, and "
               "what would you change. Those two hand the thinking back where it belongs.",
               margin="0")) + '</div>',

)


if __name__ == "__main__":
    OUT = "/mnt/user-data/outputs/row_the_role_of_parents_embed.html"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote", OUT, len(page) // 1024, "KB")
