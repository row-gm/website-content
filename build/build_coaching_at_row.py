"""Build the coach hub, Coaching at ROW.

    python3 build_coaching_at_row.py

The one page that carries the layer map and the build status labels. Every other
coach page dropped both, deliberately: status in one place means publishing a
document does not force a rebuild of its siblings.

Coach page. /page/coaching-at-row, permissioned. The nav label is For Coaches,
which is fine: the nav is wayfinding, the slug is stable. See the naming note in
layers_common.py.
"""

from row_page_helpers import (
    NAVY, TEAL, CYAN, RED, SAND, FOAM, INK, INK_SOFT, LINE,
    DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page,
    list_shell, layer_row, parent_row, numbered_row, data_table, lede,
)

from layers_common import (
    LAYERS, PARENT, PUBLISHED, STATE, URL_HOW_WE_DESIGN_TRAINING,
    URL_HOW_WE_DEVELOP_SWIMMERS,
)

STATUS = {"LIVE": TEAL, "IN DRAFT": RED, "PLANNED": NAVY}


def status_tag(s):
    return (f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;'
            f'font-size:10px;letter-spacing:0.08em;background:{STATUS[s]};color:{FOAM};'
            f'border-radius:4px;padding:3px 8px;margin-right:10px;'
            f'vertical-align:middle;">{s}</span>')


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def area(status, title, what, ask_label, ask, links=None):
    inner = (f'<div style="margin:0 0 10px;">{status_tag(status)}'
             f'<span style="font-family:{DISPLAY_FONT};text-transform:uppercase;'
             f'letter-spacing:0.01em;color:{NAVY};font-size:18px;">{title}</span></div>'
             + body(what)
             + f'<div style="font-family:{MONO_FONT};font-weight:700;font-size:10.5px;'
               f'letter-spacing:0.08em;text-transform:uppercase;color:{INK_SOFT};'
               f'margin:0 0 4px;">{ask_label}</div>'
             + body(ask, margin="0"))
    if links:
        inner += ('<div style="margin:14px 0 0;">'
                  + "".join(f'<div style="margin:0 0 6px;">{l}</div>' for l in links)
                  + '</div>')
    return card(inner)


# ---------------------------------------------------------------------------
# The nine areas. Status lives here and nowhere else.
# ---------------------------------------------------------------------------

FRAMEWORK_LINKS = [
    link(URL_HOW_WE_DESIGN_TRAINING, "How We Design Training") + " &middot; philosophy and zones",
] + [
    f'{link(STATE[k][1], t)} &middot; Layer {n}'
    for n, t, q, b, k in LAYERS if k in PUBLISHED
]

AREAS = [
    ("LIVE", "How We Design Training",
     "Our training philosophy and the vocabulary behind it. Eight principles, five training "
     "zones, and the age guidance for each. Four layer documents sit underneath it: the season, "
     "the block, the practice, and the swimmer.",
     "Use it now",
     "Label every block in your plan with a phase name. Write every set with a zone number.",
     FRAMEWORK_LINKS),

    ("LIVE", "The ROW Way",
     "Our athlete development model, and the answer to why we do this at all. Four things we "
     "develop, twelve markers written in the swimmer&rsquo;s words, and a four-step scale "
     "showing how far a swimmer has taken each one. One page for swimmers, families and coaches.",
     "Use it now",
     "The basis for swimmer reviews and for the language used in group move conversations.",
     [link(URL_HOW_WE_DEVELOP_SWIMMERS, "The ROW Way") + " &middot; open to all members"]),

    ("IN DRAFT", "Season Planning",
     "How the year is built. Peak meets named before the season starts, phases mapped week by "
     "week, and each pathway clear on which meets it peaks for. Built from the club event "
     "planner.",
     "Coming to you", "You will map your own group using a shared template."),

    ("PLANNED", "Testing and Progress",
     "A standard test battery every group runs at set points in the season. Same tests, same "
     "conditions, same reporting, so progress follows a swimmer as they move up. It also owns "
     "how a result becomes a training target.",
     "Coming to you", "Test results will also set individual targets inside a shared set."),

    ("PLANNED", "Dryland Programming",
     "Age-appropriate strength and movement, stage by stage. What each group does on land, when "
     "external loading is introduced, and how dryland tracks the phase the group is in.",
     "Your input needed", "Flag your current dryland content so we build from what works."),

    ("PLANNED", "Skill Progressions",
     "Technical standards by group. Strokes, starts, turns, finishes, breathing, underwater "
     "work. What a swimmer must own before they move up, written down instead of assumed.",
     "Your input needed", "Lead coaches will set the standards for their own group."),

    ("PLANNED", "Group Pathway",
     "How swimmers move through the club. What each group is for, what is expected in and out "
     "of the water, and how advancement decisions are made and communicated.",
     "Use it now", "Until this is published, route advancement questions to the Head Coach."),

    ("PLANNED", "Racing and Meet Strategy",
     "How we prepare for and review races. Warm-up routines, pacing, race plans by event, and "
     "what a swimmer takes from a meet that was not a peak.",
     "Coming to you", "A shared race review sheet is the first piece."),

    ("PLANNED", "Recovery and Athlete Habits",
     "Sleep, fuelling, hydration, and load away from the pool. The habits that decide whether "
     "training turns into improvement, plus the messaging families get.",
     "Coming to you", "A family-facing version will follow once the coach side is settled."),
]

ASKS = [
    "<strong>Use the six phase names and the five zones.</strong> Phases in your season plan, "
    "zone numbers on your whiteboard, both in anything you send to families. This is the one "
    "change that has to happen everywhere at once for the rest to work.",
    "<strong>Name your peak meets before the season starts.</strong> Two or three per group. "
    "Share them with families in September, not in November when someone asks why their swimmer "
    "swam slow.",
    "<strong>Bring your season plan to lead coach meetings.</strong> Mapped against the six "
    "phases. That is where the gaps in this framework will show up.",
    "<strong>Say when something does not fit your group.</strong> A framework that only works "
    "for 18&U swimmers has failed. If a rule breaks down at 12&U, that is information we need, "
    "not a problem with your coaching.",
]


page = wrap_page(
    hero("ROW Swim Club", "Coaching at ROW",
         "One shared approach to training across every competitive group. This hub holds the "
         "standards, the vocabulary, and the documents we all work from. Session content stays "
         "yours."),
    lanes_divider(),

    card(h2("Why we built this")
         + body("ROW has strong coaches. What we have not had is a shared way of describing what "
                "we do. The same training week could be explained four different ways depending "
                "on which coach you asked. That makes swimmers harder to move between groups, "
                "handovers harder to run, and family questions harder to answer well.")
         + body("This framework fixes the language and the standards, not the coaching. Every "
                "group uses the same words for the same things. What happens inside those words "
                "is still built by you, for the age, stage and events of the swimmers in front "
                "of you.")
         + callout("<strong>What this is not.</strong> It is not one session for every group and "
                   "it is not a script. You keep control of session content. What is shared is "
                   "the structure, the vocabulary, and the standards a swimmer must meet to "
                   "move up.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Where each document sits")
        + lede("Five pages. The parent sets the vocabulary; each layer below it answers a "
               "smaller question than the one above.")
        + list_shell(
            parent_row(*PARENT[:3])
            + "".join(layer_row(n, t, q, b, i=i)
                      for i, (n, t, q, b, k) in enumerate(LAYERS)))) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("The framework")
        + lede("Nine areas. Each gets its own document as it is finished, and the status labels "
               "below are the only place that status is recorded.")) + '</div>',

    *[f'<div style="margin:16px 0 0;">{area(*a)}</div>' for a in AREAS],

    '<div style="margin:28px 0 0;">' + card(
        h2("What we are asking of you")
        + lede("Four things. Everything else is your call as lead coach.")
        + list_shell("".join(numbered_row(n + 1, t, i=n) for n, t in enumerate(ASKS)))
        + callout("Nothing here changes what you write on the whiteboard tomorrow. It changes "
                  "what we call it, and whether the coach after you can pick it up.")) + '</div>',
)


if __name__ == "__main__":
    OUT = "/mnt/user-data/outputs/row_coaching_at_row_embed.html"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote", OUT, len(page) // 1024, "KB")
