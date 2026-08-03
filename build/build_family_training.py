"""Build the two family-facing training pages for the Development Plan section.

    python3 build_family_training.py

WHY TWO PAGES AND NOT FIVE. The decisions record says every coach page gets a
family counterpart. That was written before the goal was stated plainly: families
should understand the approach, not be equipped to assess a coach from the stands.
A one-for-one mirror hands a parent the session template and the weekly zone
percentages, which is exactly an audit checklist. So these two are organized
around what a parent wonders, not around the coach's four layers.

  The Training Year  why training looks the way it does through the year
  What to Expect  the racing season, the flat patches, and what actually helps

FAMILY PAGES. Run the audience check before delivering:

    python3 -c "import row_vocabulary as V; \
      print(V.check_audience(open('<file>').read(), 'family'))"

One vocabulary. The phase names and the LOAD / UNLOAD / ENTRY words are the same
as the coaches use, so a swimmer and a parent are talking about the same thing.
No coach-only lines.
Nothing that sets this season against the future: a family is paying for this one.
"""

from row_page_helpers import (
    NAVY, TEAL, RED, FOAM, INK, INK_SOFT, LINE, DISPLAY_FONT, BODY_FONT, MONO_FONT,
    body, note, h2, card, callout, hero, lanes_divider, wrap_page, data_table, lede,
)

from layers_common import (
    URL_OUR_DEVELOPMENT_PLAN, URL_HOW_WE_DEVELOP_SWIMMERS,
    URL_THE_GROWTH_SPURT, URL_THE_BIRTHDAY_GAP, URL_ASSESSMENT,
)


def link(url, text):
    return f'<a href="{url}" target="_blank" class="row-link">{text}</a>'


def badge(word):
    """LOAD, UNLOAD, ENTRY. The same words the coaches use, deliberately.
    An earlier version used BUILDING, EASING and STARTING for families. That
    was dropped: a swimmer comes home saying the group is in Accumulation, and
    a parent reading a different word for it is worse off, not better."""
    bg = {"LOAD": RED, "UNLOAD": TEAL, "ENTRY": NAVY}[word]
    return (f'<span style="display:inline-block;font-family:{MONO_FONT};font-weight:700;'
            f'font-size:10px;letter-spacing:0.08em;background:{bg};color:{FOAM};'
            f'border-radius:4px;padding:3px 8px;">{word}</span>')


READ_NEXT = [
    (URL_OUR_DEVELOPMENT_PLAN, "Our Development Plan",
     "What we are trying to build, and the four things we develop in every swimmer."),
    (URL_HOW_WE_DEVELOP_SWIMMERS, "The ROW Way",
     "The twelve things we are developing, written in the swimmer's own words."),
    (URL_THE_GROWTH_SPURT, "The Growth Spurt",
     "Why times can stall for months while a swimmer grows, and what helps."),
    (URL_THE_BIRTHDAY_GAP, "The Birthday Gap",
     "Why the fastest twelve year olds are often not the fastest eighteen year olds."),
]


def read_next(skip=""):
    rows = [[link(u, t), d] for u, t, d in READ_NEXT if t != skip]
    return card(h2("Read next")
                + lede("These four pages are the rest of the picture.")
                + data_table(["Page", "What it covers"], rows))


# ---------------------------------------------------------------------------
# Page one: How We Train
# ---------------------------------------------------------------------------

PHASES = [
    ("Introduction", "ENTRY", "2 to 4 weeks, after a summer or a month away",
     "Back into the habit. Technique, skills, and gentle swimming while the body remembers "
     "what it is doing."),
    ("Accumulation", "LOAD", "The longest stretch of the year",
     "The heavy weeks. A lot of swimming at a steady effort. <strong>Race times often get "
     "slower here, and that is the plan working, not failing.</strong>"),
    ("Consolidation", "UNLOAD", "4 to 7 days, after every hard stretch",
     "A lighter week so the last block of work can sink in. Swimmers improve while recovering "
     "from hard training, not during it."),
    ("Intensification", "LOAD", "3 to 5 weeks before a big meet",
     "Less swimming, faster swimming. Race speed, starts, turns and race plans. Your swimmer "
     "will be tired in a different way."),
    ("Peaking", "UNLOAD", "1 to 3 weeks, twice a year",
     "The taper. Training drops right down so the racing can come up. Only for the two meets "
     "a year the season is built around."),
    ("Transition", "UNLOAD", "1 to 2 weeks at the end of a cycle",
     "Rest, other sports, and a proper look back at the season. Scheduled on purpose, not "
     "whatever time is left over."),
]

ZONES = [
    ("Zone 1", "Very easy. Could chat the whole way."),
    ("Zone 2", "Steady and comfortable. Could keep going a long time."),
    ("Zone 3", "Working. Talking gets short."),
    ("Zone 4", "Race speed. Hard, and needs real rest afterwards."),
    ("Zone 5", "Flat out, over in seconds, then a long rest."),
]

training_year = wrap_page(
    hero("Our Development Plan", "The Training Year",
         "Why training looks the way it does, and why it changes as the year goes on."),
    lanes_divider(),

    card(h2("Training is not the same all year")
         + body("If you watched one practice a month for a season, you would see very "
                "different things. That is deliberate. Training moves through phases, each "
                "with a different job, and your swimmer's coach chooses which one the group "
                "is in.")
         + body("Every ROW coach uses the same six names for these, and so does this page. "
                "When your swimmer says the group is in Accumulation, this is what they "
                "mean.", margin="0")),

    '<div style="margin:24px 0 0;">' + card(
        h2("The six phases")
        + lede("What each one is for, and what you will notice at home.")
        + data_table(["Phase", "", "How long", "What it looks like"],
                     [[n, badge(b), w, d] for n, b, w, d in PHASES])
        + callout("<strong>Slower times during a building phase are normal.</strong> Swimmers "
                  "are training through fatigue on purpose. The speed shows up after the "
                  "lighter weeks that follow, not during the heavy ones.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Effort, not speed")
        + body("Coaches ask for an effort rather than a time. That is what lets one set work "
               "for a whole lane of different swimmers at once. A faster swimmer and a slower "
               "swimmer can be doing exactly the same training, and both be right.")
        + body("Swimmers talk about zones at home, so here is what they mean.")
        + data_table(["Zone", "What it feels like"], [[z, d] for z, d in ZONES])
        + note("Your swimmer's coach decides which zones a group uses and how much. Younger "
               "swimmers spend almost all their time in the easier ones, and that is on "
               "purpose.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("Hard days and easy days")
        + body("A good week is not a week of hard sessions. It has hard days, easy days and at "
               "least one day off, in a deliberate order.")
        + body("The easy session is not a wasted one. It is the session that lets the hard ones "
               "work. If your swimmer says practice was easy today, that is usually the plan "
               "rather than a coach going easy on them.", margin="0")
        + callout("<strong>One thing that surprises people.</strong> Swimmers in the same lane, "
                  "on the same set, are often given different intervals, distances or targets. "
                  "They are doing the same training, fitted to them. Nobody is being given less.")) + '</div>',

    '<div style="margin:24px 0 0;">' + read_next("") + '</div>',
)


# ---------------------------------------------------------------------------
# Page two: What to Expect
# ---------------------------------------------------------------------------

MEETS = [
    ("Peak meets", "Two a year",
     "The meets the season is built around. Training drops right down beforehand so your "
     "swimmer arrives fresh and fast. Your coach names these at the start of the season."),
    ("Tune-up meets", "A few a year",
     "Raced in the middle of hard training, on purpose. Your swimmer will be tired. These are "
     "for practising pacing, starts and race plans, not for chasing a best time."),
    ("Meets we race through", "Most of the calendar",
     "Raced without changing anything about training that week. Good racing experience, and "
     "best times still happen, but they are not what the meet is for."),
]

HELPS = [
    ("Sleep", "The single biggest one, and it costs nothing. Growing bodies training hard need "
              "more sleep than they think."),
    ("Food", "Regular meals, and something to eat soon after practice. A swimmer who trains "
             "hungry does not adapt to the training."),
    ("Turning up", "Consistency beats intensity at every age. A swimmer who trains most weeks "
                   "for years beats one who trains brilliantly in bursts."),
    ("What you say after a race", "Ask what went well and what they would change. Those two "
                                  "questions do more than any amount of analysis, and they hand "
                                  "the thinking back to the swimmer, which is the point."),
]

what_to_expect = wrap_page(
    hero("Our Development Plan", "What to Expect",
         "The shape of a racing season, the patches that worry people, and what genuinely helps."),
    lanes_divider(),

    card(h2("Not every meet is a big meet")
         + body("A season has more meets than peak meets, and they are not all for the same "
                "thing. Knowing which is which explains a lot of what you see on the day.")
         + data_table(["Kind of meet", "How often", "What it is for"],
                      [[a, b, c] for a, b, c in MEETS])
         + callout("<strong>A swimmer can race well without a taper.</strong> If your swimmer is "
                   "racing tired at a tune-up meet, that is the plan. Judge that weekend on how "
                   "they swam it, not on the clock.")),

    '<div style="margin:24px 0 0;">' + card(
        h2("Flat patches are part of it")
        + body("Almost every swimmer has stretches with no best times. Some of that is training "
               "phase. Some of it is growth. Very little of it means anything is wrong.")
        + body("Two pages here go into this properly: "
               + link(URL_THE_GROWTH_SPURT, "The Growth Spurt")
               + " on what happens while a swimmer is growing, and "
               + link(URL_THE_BIRTHDAY_GAP, "The Birthday Gap")
               + " on why the fastest twelve year olds are often not the fastest eighteen year "
                 "olds.", margin="0")
        + callout("Every season adds a layer to the foundation. A season with few best times is "
                  "not a wasted one, and this year and the long run are not in competition.")) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("What actually helps")
        + lede("Four things, and none of them happen at the pool.")
        + data_table(["", "Why it matters"], [[a, b] for a, b in HELPS])) + '</div>',

    '<div style="margin:24px 0 0;">' + card(
        h2("How to ask about your swimmer")
        + body("You will get two proper conversations a year with your swimmer's coach, about "
               "the objectives set for that phase. Those are the ones for the bigger questions.")
        + body("In between, catch your swimmer&rsquo;s coach before or after a practice. What "
               "works less well is a "
               "conversation about training in front of your swimmer, because it puts them in "
               "the middle of it.")
        + body("Coaches are working from a written plan for the group, and are happy to explain "
               "what their swimmer is working on and why. That is a different conversation from "
               "one about the plan itself, and it is usually the more useful one.", margin="0")) + '</div>',

    '<div style="margin:24px 0 0;">' + read_next("") + '</div>',
)


PAGES = [("the-training-year", training_year), ("what-to-expect", what_to_expect)]

if __name__ == "__main__":
    for slug, page in PAGES:
        out = f"/mnt/user-data/outputs/row_{slug.replace('-', '_')}_embed.html"
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"  {out.split('/')[-1]:<40}{len(page) // 1024:>4} KB")
