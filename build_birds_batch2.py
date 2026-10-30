"""Pigeons & Doves book, batch 2 (pages 5-8). Run: python3 build-tools/build_birds_batch2.py
Uses shared helpers from birds_common.py. Writes into ../deliverables."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from birds_common import *  # noqa: F401,F403  (build, svg, txt, arrow, pigeon_at, colours, icons)

# ---------- extra icons ----------
ICON_SEED = ("<svg viewBox='0 0 40 40'><ellipse cx='15' cy='22' rx='9' ry='5' fill='%s' stroke='%s' stroke-width='2' transform='rotate(-30 15 22)'/>"
             "<ellipse cx='27' cy='17' rx='9' ry='5' fill='%s' stroke='%s' stroke-width='2' transform='rotate(20 27 17)'/></svg>" % (GOLD, NAVY, GOLD, NAVY))
ICON_HEAT = ("<svg viewBox='0 0 40 40'><path d='M10 34 q6 -10 0 -20 M20 34 q6 -10 0 -20 M30 34 q6 -10 0 -20' fill='none' stroke='%s' stroke-width='3' stroke-linecap='round'/></svg>" % ORANGE)
ICON_LEGPUSH = ("<svg viewBox='0 0 40 40'><line x1='4' y1='34' x2='36' y2='34' stroke='%s' stroke-width='3'/>%s</svg>" % (NAVY, arrow(12, 32, 30, 8, ORANGE, 4, 10)))
ICON_PEAK = ("<svg viewBox='0 0 40 40'><path d='M3 34 Q20 -8 37 34' fill='none' stroke='%s' stroke-width='3'/><circle cx='20' cy='13' r='4' fill='%s' stroke='%s' stroke-width='1.5'/></svg>" % (TEAL, GOLD, NAVY))
ICON_GRAPH_STEEP = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='32' x2='28' y2='8' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, GREEN)
ICON_GRAPH_FLAT = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='18' x2='32' y2='18' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, ORANGE)
ICON_GRAPH_GENTLE = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='32' x2='32' y2='22' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, TEAL)
ICON_SUN = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='8' fill='%s' stroke='%s' stroke-width='2'/>"
            "<path d='M20 4v6 M20 30v6 M4 20h6 M30 20h6 M9 9l4 4 M27 27l4 4 M31 9l-4 4 M13 27l-4 4' stroke='%s' stroke-width='2.5' stroke-linecap='round'/></svg>" % (GOLD, NAVY, GOLD))
ICON_MAGNET = ("<svg viewBox='0 0 40 40'><path d='M10 6 V22 A10 10 0 0 0 30 22 V6' fill='none' stroke='%s' stroke-width='7'/>"
               "<rect x='6.5' y='4' width='7' height='7' fill='%s'/><rect x='26.5' y='4' width='7' height='7' fill='%s'/></svg>" % (ORANGE, SAND, SAND))
ICON_HOUSE = ("<svg viewBox='0 0 40 40'><rect x='9' y='19' width='22' height='15' fill='%s' stroke='%s' stroke-width='2'/>"
              "<polygon points='6,20 20,7 34,20' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (SAND, NAVY, ORANGE, NAVY))
ICON_COMPASS = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='15' fill='#FFFFFF' stroke='%s' stroke-width='2.5'/>"
                "<polygon points='20,7 16,20 24,20' fill='%s'/><polygon points='20,33 16,20 24,20' fill='%s'/></svg>" % (NAVY, ORANGE, PG))


def sun(cx, cy, r=12):
    rays = "".join("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' stroke='%s' stroke-width='2.5' stroke-linecap='round'/>" % (
        cx + (r + 4) * math.cos(a), cy + (r + 4) * math.sin(a), cx + (r + 10) * math.cos(a), cy + (r + 10) * math.sin(a), GOLD)
        for a in [i * math.pi / 4 for i in range(8)])
    return "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='2'/>" % (cx, cy, r, GOLD, NAVY) + rays


def axes(ox, oy, xend, ytop):
    return ("<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2'/>" % (ox, oy, xend, oy, NAVY)
            + "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2'/>" % (ox, oy, ox, ytop, NAVY)
            + tri_right(xend + 4, oy, NAVY, 5)
            + "<polygon points='%g,%g %g,%g %g,%g' fill='%s'/>" % (ox, ytop - 4, ox - 4, ytop + 5, ox + 4, ytop + 5, NAVY))


def poly(points, color, w=4):
    return "<polyline points='%s' fill='none' stroke='%s' stroke-width='%s' stroke-linecap='round' stroke-linejoin='round'/>" % (
        " ".join("%g,%g" % p for p in points), color, w)


# ====================== PAGE 5: FLAP CYCLE & ENERGY ======================
wing_small = "M165 85 Q185 40 215 55 Q200 90 165 85 Z"
c5 = {
  "observe": {
    "svg": svg(300, 170,
      "<ellipse cx='34' cy='66' rx='13' ry='7' fill='%s' stroke='%s' stroke-width='2' transform='rotate(-30 34 66)'/>" % (GOLD, NAVY)
      + "<ellipse cx='48' cy='76' rx='13' ry='7' fill='%s' stroke='%s' stroke-width='2' transform='rotate(25 48 76)'/>" % (GOLD, NAVY)
      + "<ellipse cx='112' cy='70' rx='24' ry='17' fill='%s' stroke='%s' stroke-width='2'/>" % (ORANGE, NAVY)
      + "<path d='M92 70 Q112 56 132 70 M94 77 Q112 64 130 77' fill='none' stroke='%s' stroke-width='2'/>" % NAVY
      + "<path d='%s' fill='%s' stroke='%s' stroke-width='2'/>" % (wing_small, PD, NAVY)
      + "".join("<path d='M%d 90 q6 -12 0 -24 q-6 -12 0 -24' fill='none' stroke='%s' stroke-width='3' stroke-linecap='round'/>" % (x, ORANGE) for x in (248, 262, 276))
      + arrow(62, 70, 84, 70, NAVY, 2.5, 8) + arrow(140, 70, 160, 70, NAVY, 2.5, 8) + arrow(222, 70, 240, 70, NAVY, 2.5, 8)
      + txt(40, 130, "food", 11, NAVY, "middle", "bold") + txt(112, 130, "chest muscle", 11, NAVY, "middle", "bold")
      + txt(190, 130, "flap", 11, NAVY, "middle", "bold") + txt(262, 130, "heat", 11, NAVY, "middle", "bold")
      + txt(40, 146, "stored energy", 9, TEAL, "middle") + txt(112, 146, "converts it", 9, TEAL, "middle")
      + txt(190, 146, "motion", 9, TEAL, "middle") + txt(262, 146, "leaks out", 9, TEAL, "middle"),
      "Energy chain: food, chest muscle, flapping wing, heat"),
    "question": "A pigeon eats seeds, then flaps hard. Where does the energy for flapping come from?",
    "explanation": "Seeds store chemical energy. The chest muscle changes that stored energy into motion. Energy changes form, and some always leaks out as heat.",
    "choices": [
      {"text": "Chemical energy stored in its food 🌾", "correct": True},
      {"text": "Only from the wind 🌬️", "correct": False},
      {"text": "From nothing: wings make energy ✨", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "food", "name": "Seeds", "icon": ICON_SEED, "fact": "🌾 Seeds store chemical energy. That is the pigeon's fuel."},
    {"id": "muscle", "name": "Chest muscle", "icon": ICON_CHEST, "fact": "💪 The muscle changes stored chemical energy into movement (and some heat)."},
    {"id": "heat", "name": "Heat", "icon": ICON_HEAT, "fact": "🔥 Some energy always leaks out as heat. That is why hard exercise makes you warm too."},
  ]},
  "draw": {
    "prompt": "Draw an energy chain: seed, then muscle, then wing, then heat. Put an arrow between each one.",
    "hintSvg": svg(300, 200,
      "".join("<circle cx='%d' cy='90' r='24' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % (x, ORANGE) for x in (40, 115, 190, 265))
      + arrow(66, 90, 88, 90, NAVY, 3, 9) + arrow(141, 90, 163, 90, NAVY, 3, 9) + arrow(216, 90, 238, 90, NAVY, 3, 9)
      + txt(40, 140, "seed", 11, NAVY, "middle") + txt(115, 140, "muscle", 11, NAVY, "middle")
      + txt(190, 140, "wing", 11, NAVY, "middle") + txt(265, 140, "heat", 11, NAVY, "middle"),
      "hint: four circles joined by arrows"),
  },
  "rotate": {
    "prompt": "Rotate the picture and look at the two arrows. The downstroke is the POWER stroke: the wing pushes air down. The upstroke just resets the wing.",
    "svg": "<g transform='translate(8,70) scale(0.95)'>" + pigeon() + "</g>"
           + arrow(120, 122, 120, 84, PD, 4, 11) + txt(120, 74, "up", 12, PD, "middle", "bold")
           + arrow(178, 80, 178, 122, ORANGE, 7, 14) + txt(185, 70, "down: power!", 12, ORANGE, "middle", "bold")
  },
  "compare": {
    "question": "Tap the picture where the pigeon is using MORE energy every second.",
    "explanation": "Taking off needs big, fast flaps, so the chest muscle burns lots of food energy. Cruising needs less. More energy used also means more heat given off.",
    "choices": [
      {"label": "A — cruising", "svg": svg(200, 140,
          pigeon_at(0.35, 100, 38) + "<rect x='20' y='90' width='50' height='18' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY)
          + txt(20, 130, "energy used", 10, NAVY), "short energy bar"), "correct": False},
      {"label": "B — taking off", "svg": svg(200, 140,
          pigeon_at(0.35, 100, 38) + arrow(100, 62, 100, 78, ORANGE, 3, 7)
          + "<rect x='20' y='90' width='160' height='18' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY)
          + txt(20, 130, "energy used", 10, NAVY), "long energy bar"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "The pigeon eats seeds: chemical energy is stored", "icon": ICON_SEED},
    {"text": "The chest muscle changes it into movement", "icon": ICON_CHEST},
    {"text": "The wing moves air, and some energy leaks out as heat", "icon": ICON_HEAT},
    {"text": "🔗 Links to Mario Energy Transformation: Mario's jump swaps energy forms the same way. Energy changes shape but never just vanishes", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "After flapping hard, why does a pigeon's body feel warm, even on a cool day?",
    "visualSvg": svg(200, 100,
      "<ellipse cx='36' cy='50' rx='13' ry='7' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY)
      + arrow(60, 50, 100, 50, NAVY, 3, 9)
      + "".join("<path d='M%d 68 q6 -10 0 -20 q-6 -10 0 -20' fill='none' stroke='%s' stroke-width='3' stroke-linecap='round'/>" % (x, ORANGE) for x in (125, 142, 159)),
      "seed turning into heat"),
    "starters": ["The muscle changes chemical energy into...", "Some energy leaks out as..."],
    "keywords": ["energy", "muscle", "heat", "food"]
  },
  "predict": {
    "question": "A pigeon flaps twice as hard as before. What happens to the heat its body gives off?",
    "explanation": "Harder flapping means the muscle changes more food energy every second. Some of it always leaks out as heat, so more heat is given off.",
    "choices": [
      {"text": "More heat 🔥", "correct": True},
      {"text": "Less heat ❄️", "correct": False},
      {"text": "No heat at all", "correct": False},
    ]
  },
}
build("birds-05-flap-cycle", "Pigeon: Flap Cycle & Energy 💪", c5)

# ====================== PAGE 6: TAKE-OFF ARC ======================
c6 = {
  "observe": {
    "svg": svg(300, 200,
      "<line x1='10' y1='170' x2='290' y2='170' stroke='%s' stroke-width='4'/>" % SAND
      + "<path d='M30 165 Q130 20 230 165' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 5'/>" % NAVY
      + "<path d='M30 165 Q95 70 150 85 Q220 100 280 40' fill='none' stroke='%s' stroke-width='4'/>" % TEAL
      + arrow(268, 50, 282, 38, TEAL, 2, 10)
      + "<circle cx='30' cy='165' r='7' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
      + txt(238, 158, "jump only", 10, NAVY) + txt(112, 52, "jump + flapping", 10, TEAL, "start", "bold"),
      "A jump arc that returns to the ground and a flapping path that keeps climbing"),
    "question": "A pigeon hops off the ground without flapping. What stops it from going up forever?",
    "explanation": "Gravity keeps pulling the pigeon down the whole time. Its upward speed shrinks to zero at the top of the hop, then it falls. That makes a curved arc.",
    "choices": [
      {"text": "Gravity keeps pulling it down 🌍", "correct": True},
      {"text": "The ground pulls it back", "correct": False},
      {"text": "Nothing: jumps go up forever", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "launch", "name": "Launch push", "icon": ICON_LEGPUSH, "fact": "🦵 The legs push off the ground. This gives the pigeon its starting speed."},
    {"id": "peak", "name": "Peak of the arc", "icon": ICON_PEAK, "fact": "⛰️ At the top, the upward speed hits zero for a moment. Gravity is still pulling."},
    {"id": "thrust", "name": "Wing power", "icon": ICON_WING, "fact": "🪶 Flapping adds a new push, so the pigeon does not have to come back down."},
  ]},
  "draw": {
    "prompt": "Draw the path of a hop: a smooth arc up and back down. Then draw a second path where flapping carries the pigeon higher.",
    "hintSvg": svg(300, 200,
      "<line x1='10' y1='170' x2='290' y2='170' stroke='%s' stroke-width='4'/>" % SAND
      + "<path d='M30 165 Q130 20 230 165' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 5'/>" % ORANGE
      + "<path d='M30 165 Q95 70 150 85 Q220 100 280 40' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 5'/>" % TEAL
      + "<circle cx='30' cy='165' r='7' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY),
      "hint: two dotted arcs from the ground"),
  },
  "rotate": {
    "prompt": "Rotate the arc. Turned upside down it looks like a bowl 🥣. A hop follows a smooth curve called a parabola, which is an upside-down bowl.",
    "svg": "<line x1='30' y1='220' x2='270' y2='220' stroke='%s' stroke-width='4'/>" % SAND
           + "<path d='M30 220 Q150 -20 270 220' fill='none' stroke='%s' stroke-width='4'/>" % TEAL
           + "<circle cx='30' cy='220' r='7' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
           + "<circle cx='150' cy='100' r='7' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY)
           + txt(150, 84, "peak", 12, NAVY, "middle", "bold")
  },
  "compare": {
    "question": "Two pigeons hop off the ground. Tap the one that pushed off with MORE speed.",
    "explanation": "A faster launch goes higher and farther before gravity wins. The hop on the right is taller and longer, so that pigeon started with more speed.",
    "choices": [
      {"label": "A — low short hop", "svg": svg(200, 140,
          "<line x1='5' y1='120' x2='195' y2='120' stroke='%s' stroke-width='3'/>" % SAND
          + "<path d='M20 120 Q60 80 100 120' fill='none' stroke='%s' stroke-width='3'/>" % NAVY
          + "<circle cx='20' cy='120' r='5' fill='%s' stroke='%s' stroke-width='1.5'/>" % (PG, NAVY), "small arc"), "correct": False},
      {"label": "B — high long hop", "svg": svg(200, 140,
          "<line x1='5' y1='120' x2='195' y2='120' stroke='%s' stroke-width='3'/>" % SAND
          + "<path d='M20 120 Q100 10 180 120' fill='none' stroke='%s' stroke-width='3'/>" % NAVY
          + "<circle cx='20' cy='120' r='5' fill='%s' stroke='%s' stroke-width='1.5'/>" % (PG, NAVY), "big arc"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "The legs push off the ground: that is the launch speed", "icon": ICON_LEGPUSH},
    {"text": "Gravity pulls the pigeon down while it rises", "icon": ICON_DOWN},
    {"text": "Upward speed shrinks to zero at the peak, then it falls: an arc", "icon": ICON_PEAK},
    {"text": "🔗 Links to Mario Jump Arc: Mario and the pigeon follow the same curve. Flapping is like an extra power-up", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "How do flapping wings change a pigeon's hop path?",
    "visualSvg": svg(200, 100,
      "<path d='M15 85 Q60 10 105 85' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='5 4'/>" % NAVY
      + "<path d='M15 85 Q60 30 105 60 Q150 85 185 20' fill='none' stroke='%s' stroke-width='3'/>" % TEAL
      + "<circle cx='15' cy='85' r='5' fill='%s' stroke='%s' stroke-width='1.5'/>" % (PG, NAVY),
      "plain arc and a flapping path"),
    "starters": ["Without flapping, gravity...", "With flapping, the wings add..."],
    "keywords": ["gravity", "arc", "thrust", "lift"]
  },
  "predict": {
    "question": "A pigeon launches with a faster push from its legs. What happens to its hop arc?",
    "explanation": "More launch speed means the pigeon rises higher and travels farther before gravity pulls it back to the ground.",
    "choices": [
      {"text": "Higher and longer", "correct": True},
      {"text": "Lower and shorter", "correct": False},
      {"text": "The arc stays exactly the same", "correct": False},
    ]
  },
}
build("birds-06-take-off-arc", "Pigeon: Take-off Arc 🛫", c6)

# ====================== PAGE 7: HOMING RACE GRAPH ======================
c7 = {
  "observe": {
    "svg": svg(300, 200,
      axes(40, 160, 280, 20)
      + poly([(40, 160), (100, 100), (160, 100), (250, 40)], TEAL, 4)
      + txt(48, 112, "A", 14, NAVY, "start", "bold") + txt(130, 90, "B", 14, NAVY, "start", "bold") + txt(195, 62, "C", 14, NAVY, "start", "bold")
      + txt(284, 178, "time", 11, NAVY, "end") + txt(46, 16, "distance flown", 11, NAVY),
      "Distance-time graph of a pigeon race with a steep part, a flat part and a gentler part"),
    "question": "This graph shows a pigeon's race. Which part is the pigeon RESTING?",
    "explanation": "On a distance-time graph, a flat line means time keeps passing but the distance does not change. The pigeon is not moving, so it is resting.",
    "choices": [
      {"text": "Part A (steep line)", "correct": False},
      {"text": "Part B (flat line)", "correct": True},
      {"text": "Part C (gentler line)", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "steep", "name": "Steep line", "icon": ICON_GRAPH_STEEP, "fact": "🚀 Fast! A lot of distance in a little time."},
    {"id": "flat", "name": "Flat line", "icon": ICON_GRAPH_FLAT, "fact": "😴 Resting. Time passes but the distance does not change."},
    {"id": "gentle", "name": "Gentler slope", "icon": ICON_GRAPH_GENTLE, "fact": "🌬️ Slower. Maybe a headwind. Less distance each minute."},
  ]},
  "draw": {
    "prompt": "Draw a graph for a pigeon race: fast flying first, then a rest, then slower flying.",
    "hintSvg": svg(300, 200,
      axes(40, 160, 280, 20)
      + "<polyline points='40,160 100,100 160,100 250,40' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 5'/>" % ORANGE
      + txt(284, 178, "time", 11, NAVY, "end") + txt(46, 16, "distance flown", 11, NAVY),
      "hint: axes with a dotted fast, flat, slower line"),
  },
  "rotate": {
    "prompt": "Rotate the graph. It looks different, but the meaning is the same. Slope is still speed, and the steeper part is still the fast part.",
    "svg": axes(50, 250, 270, 40)
           + poly([(50, 250), (110, 190), (170, 190), (250, 130)], TEAL, 5)
           + txt(96, 232, "fast", 12, NAVY, "start", "bold") + txt(124, 180, "rest", 12, NAVY, "start", "bold")
           + txt(205, 175, "slower", 12, NAVY, "start", "bold")
  },
  "compare": {
    "question": "Two pigeons race for the same time. Tap the line of the FASTER pigeon.",
    "explanation": "A steeper line covers more distance in the same time, so the pigeon is faster. Speed = distance ÷ time.",
    "choices": [
      {"label": "A — gentle line", "svg": svg(200, 140,
          axes(30, 115, 185, 15) + poly([(30, 115), (170, 70)], TEAL, 4), "gentle line"), "correct": False},
      {"label": "B — steep line", "svg": svg(200, 140,
          axes(30, 115, 185, 15) + poly([(30, 115), (130, 25)], TEAL, 4), "steep line"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "The pigeon flies some distance in some time", "icon": ICON_BIRD_DOT},
    {"text": "Plot distance against time: the line climbs", "icon": ICON_GRAPH_GENTLE},
    {"text": "A steeper line means more distance each minute: faster (speed = distance ÷ time)", "icon": ICON_GRAPH_STEEP},
    {"text": "🔗 Links to Mario Position vs Time: same graph! Steep = fast and flat = still, for Mario and for a pigeon", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "A tailwind pushes the pigeon from behind. How would the graph line change?",
    "visualSvg": svg(200, 100,
      axes(25, 85, 185, 10) + poly([(25, 85), (80, 60)], GREEN, 3) + poly([(25, 85), (110, 20)], ORANGE, 3)
      + txt(115, 24, "tailwind?", 10, ORANGE),
      "two lines, one steeper"),
    "starters": ["With a tailwind the line gets...", "Because the pigeon covers more..."],
    "keywords": ["steeper", "speed", "distance", "time"]
  },
  "predict": {
    "question": "A pigeon flies into a strong headwind. What happens to the slope of its line?",
    "explanation": "A headwind slows the pigeon, so it covers less distance each minute. The line is still rising, but it gets gentler.",
    "choices": [
      {"text": "It gets gentler", "correct": True},
      {"text": "It gets steeper", "correct": False},
      {"text": "It goes perfectly flat the whole way", "correct": False},
    ]
  },
}
build("birds-07-homing-race-graph", "Pigeon: Homing Race Graph 📈", c7)

# ====================== PAGE 8: SKY COMPASS ======================
def magnet(cx, cy):
    return ("<g transform='translate(%g,%g)'><path d='M-12 -12 V6 A12 12 0 0 0 12 6 V-12' fill='none' stroke='%s' stroke-width='7'/>"
            "<rect x='-15.5' y='-14' width='7' height='7' fill='%s' stroke='%s' stroke-width='1.5'/>"
            "<rect x='8.5' y='-14' width='7' height='7' fill='%s' stroke='%s' stroke-width='1.5'/></g>" % (cx, cy, ORANGE, SAND, NAVY, SAND, NAVY))


def house(cx, cy):
    return ("<rect x='%g' y='%g' width='26' height='18' fill='%s' stroke='%s' stroke-width='2'/>"
            "<polygon points='%g,%g %g,%g %g,%g' fill='%s' stroke='%s' stroke-width='2'/>"
            % (cx - 13, cy - 4, SAND, NAVY, cx - 17, cy - 3, cx, cy - 20, cx + 17, cy - 3, ORANGE, NAVY))


def top_view(sun_x):
    return ("<polygon points='100,50 88,92 112,92' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
            + "<circle cx='%g' cy='72' r='9' fill='%s' stroke='%s' stroke-width='2'/>" % (sun_x, GOLD, NAVY)
            + txt(100, 14, "N", 12, NAVY, "middle", "bold") + txt(190, 76, "E", 12, NAVY, "middle", "bold")
            + txt(100, 134, "S", 12, NAVY, "middle", "bold") + txt(10, 76, "W", 12, NAVY, "middle", "bold"))


c8 = {
  "observe": {
    "svg": svg(300, 200,
      sun(50, 40) + magnet(150, 40) + house(250, 44)
      + txt(50, 88, "sun", 11, NAVY, "middle", "bold") + txt(150, 88, "magnetic field", 11, NAVY, "middle", "bold") + txt(250, 88, "landmarks", 11, NAVY, "middle", "bold")
      + arrow(60, 98, 116, 136, TEAL, 2.5, 9) + arrow(150, 98, 150, 132, TEAL, 2.5, 9) + arrow(240, 98, 184, 136, TEAL, 2.5, 9)
      + pigeon_at(0.4, 150, 160),
      "A pigeon with three clues pointing to it: the sun, Earth's magnetic field, and landmarks"),
    "question": "A homing pigeon is let go far from home. Which clues can it use to find its way?",
    "explanation": "Scientists have found that homing pigeons use the sun, landmarks near home, and probably Earth's magnetic field. How the magnetic sense works is still being studied.",
    "choices": [
      {"text": "The sun, landmarks, and probably Earth's magnetic field", "correct": True},
      {"text": "Only luck 🎲", "correct": False},
      {"text": "GPS satellites 📡", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "sun", "name": "Sun", "icon": ICON_SUN, "fact": "☀️ The sun's angle works like a compass. A pigeon's inner body clock helps it adjust as the sun moves."},
    {"id": "magnet", "name": "Magnetic field", "icon": ICON_MAGNET, "fact": "🧲 Earth is like a giant magnet. Scientists think pigeons sense it, but exactly how is still being studied."},
    {"id": "land", "name": "Landmarks", "icon": ICON_HOUSE, "fact": "🏠 Rivers, roads and hills help a pigeon when it gets close to home."},
  ]},
  "draw": {
    "prompt": "Draw the sun, a hill, and a house. Then draw a dotted arrow showing the pigeon's route home.",
    "hintSvg": svg(300, 200,
      sun(45, 40) + "<path d='M100 150 Q150 70 200 150 Z' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % NAVY
      + "<rect x='238' y='120' width='34' height='26' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % ORANGE
      + "<polygon points='233,121 255,98 277,121' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % ORANGE
      + "<path d='M30 160 Q110 60 235 125' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='4 5'/>" % TEAL
      + arrow(222, 118, 236, 124, TEAL, 2, 9),
      "hint: sun, hill, house and a dotted route"),
  },
  "rotate": {
    "prompt": "Rotate the compass picture. The letters turn with the paper, but a real needle always points north. Turning yourself does not move north.",
    "svg": "<circle cx='150' cy='150' r='105' fill='none' stroke='%s' stroke-width='4'/>" % NAVY
           + txt(150, 66, "N", 22, NAVY, "middle", "bold") + txt(240, 158, "E", 22, NAVY, "middle", "bold")
           + txt(150, 248, "S", 22, NAVY, "middle", "bold") + txt(60, 158, "W", 22, NAVY, "middle", "bold")
           + "<polygon points='150,82 140,150 160,150' fill='%s'/><polygon points='150,218 140,150 160,150' fill='%s'/>" % (ORANGE, PG)
           + "<circle cx='150' cy='150' r='6' fill='%s'/>" % NAVY
  },
  "compare": {
    "question": "At sunrise the sun is in the EAST. Tap the picture where the pigeon is flying NORTH using the sun.",
    "explanation": "If a pigeon flies north, east is on its right-hand side. So the sunrise sun should be on its right.",
    "choices": [
      {"label": "A — sun on its right", "svg": svg(200, 140, top_view(160), "pigeon flying north, sun on the right"), "correct": True},
      {"label": "B — sun on its left", "svg": svg(200, 140, top_view(40), "pigeon flying north, sun on the left"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "The pigeon is released far from home", "icon": ICON_BIRD_DOT},
    {"text": "It reads clues: the sun's position, landmarks and (probably) Earth's magnetic field. Same sky ideas as your Astro Sketchbook", "icon": ICON_SUN},
    {"text": "It picks the direction home and flies", "icon": ICON_COMPASS},
    {"text": "🔗 Links to Homing Race Graph (page 7): the compass says WHICH WAY, the graph shows HOW FAST", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "A pigeon is released on a cloudy day when the sun is hidden. What other clues could it use?",
    "visualSvg": svg(200, 100,
      "<path d='M40 55 Q40 35 62 35 Q70 20 92 28 Q118 24 122 46 Q140 48 138 62 Q136 72 118 72 L50 72 Q30 72 40 55 Z' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
      + magnet(160, 52),
      "cloud hiding the sun and a magnet"),
    "starters": ["Without the sun, it could use...", "Closer to home it can see..."],
    "keywords": ["magnetic", "landmarks", "sun", "compass"]
  },
  "predict": {
    "question": "A tiny magnet is stuck near a pigeon and may confuse its magnetic sense. On a cloudy day, what could happen?",
    "explanation": "Some experiments suggest magnets can confuse pigeons, especially when the sun is hidden. Scientists are still working out the details, so the safest guess is that it may head the wrong way.",
    "choices": [
      {"text": "It may head in the wrong direction", "correct": True},
      {"text": "It will fly even better", "correct": False},
      {"text": "Nothing can ever change its direction", "correct": False},
    ]
  },
}
build("birds-08-sky-compass", "Pigeon: Sky Compass 🧭", c8)
print("batch 2 done: 4 pages")
