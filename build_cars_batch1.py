"""Beetles & Buses book, batch 1 (pages 1-4). Run: python3 build-tools/build_cars_batch1.py
Uses shared helpers from birds_common.py (build, check, svg, txt, arrow, colours, icons).
Writes cars-0N-*.html into ../deliverables."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from birds_common import *  # noqa: F401,F403

BLUE = "#CFE3EE"; BODY = "#6BB0C9"

# ---------------- drawing helpers ----------------
def beetle(dot=False, marks=False):
    """VW Beetle facing RIGHT. Occupies x 30..282, y 44..160."""
    s = ("<path d='M36,134 C30,110 50,88 84,70 C112,52 150,44 176,56 C196,64 210,84 232,94 C250,100 270,104 278,118 C282,126 280,134 272,136 L36,134 Z' "
         "fill='%s' stroke='%s' stroke-width='2.5'/>" % (BODY, NAVY)
         + "<path d='M96,86 C110,68 142,58 164,64 C178,72 192,82 200,92 L96,92 Z' fill='%s' stroke='%s' stroke-width='2'/>" % (BLUE, NAVY)
         + "<line x1='150' y1='92' x2='150' y2='126' stroke='%s' stroke-width='1.5'/>" % NAVY
         + "<circle cx='271' cy='116' r='6' fill='%s' stroke='%s' stroke-width='1.5'/>" % (GOLD, NAVY)
         + "<circle cx='88' cy='136' r='22' fill='%s'/><circle cx='88' cy='136' r='9' fill='%s' stroke='%s' stroke-width='1.5'/>" % (NAVY, SAND, NAVY)
         + "<circle cx='224' cy='136' r='22' fill='%s'/><circle cx='224' cy='136' r='9' fill='%s' stroke='%s' stroke-width='1.5'/>" % (NAVY, SAND, NAVY))
    if dot:
        s += "<circle cx='56' cy='112' r='10' fill='%s' stroke='%s' stroke-width='2'/>" % (ORANGE, NAVY)
    if marks:
        s += ("<circle cx='252' cy='86' r='12' fill='#FFFFFF' stroke='%s' stroke-width='2'/>" % NAVY + txt(252, 91, "A", 14, NAVY, "middle", "bold")
              + "<circle cx='52' cy='96' r='12' fill='#FFFFFF' stroke='%s' stroke-width='2'/>" % NAVY + txt(52, 101, "B", 14, NAVY, "middle", "bold"))
    return s


def beetle_at(scale, tx, ty, **kw):
    return "<g transform='translate(%g,%g) scale(%s)'>%s</g>" % (tx, ty, scale, beetle(**kw))


def cyl(x, piston_y, gas, direction=None, spark=False):
    """Small piston-in-cylinder drawing, 50 wide, cylinder top y=30, open bottom y=140."""
    top, bot, w = 30, 140, 50
    cx = x + w / 2
    s = "<rect x='%g' y='%g' width='%g' height='%g' fill='%s'/>" % (x + 2, top + 2, w - 4, piston_y - top - 2, gas)
    s += "<path d='M%g %g V%g H%g V%g' fill='none' stroke='%s' stroke-width='3'/>" % (x, bot, top, x + w, bot, NAVY)
    s += "<rect x='%g' y='%g' width='%g' height='12' fill='%s' stroke='%s' stroke-width='2'/>" % (x + 2, piston_y, w - 4, PG, NAVY)
    s += "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='3'/>" % (cx, piston_y + 12, cx, bot + 8, NAVY)
    if spark:
        s += "<polygon points='%g,%g %g,%g %g,%g %g,%g %g,%g %g,%g' fill='%s' stroke='%s' stroke-width='1'/>" % (
            cx + 2, top + 4, cx - 6, top + 16, cx - 1, top + 16, cx - 4, top + 26, cx + 6, top + 12, cx + 1, top + 12, GOLD, NAVY)
    if direction == "down":
        s += arrow(cx, piston_y + 20, cx, piston_y + 42, ORANGE, 3, 8)
    elif direction == "up":
        s += arrow(cx, piston_y + 42, cx, piston_y + 20, ORANGE, 3, 8)
    return s


def fan(cx, cy, r, color=TEAL):
    blades = "".join("<ellipse cx='%g' cy='%g' rx='%g' ry='%g' fill='%s' stroke='%s' stroke-width='1.5' transform='rotate(%d %g %g)'/>" % (
        cx, cy - r * 0.55, r * 0.28, r * 0.5, color, NAVY, a, cx, cy) for a in (0, 90, 180, 270))
    return blades + "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='1.5'/>" % (cx, cy, r * 0.16, GOLD, NAVY)


def finned(x, y, w, h, n, hot="#E39A7F"):
    s = "<rect x='%g' y='%g' width='%g' height='%g' fill='%s' stroke='%s' stroke-width='2'/>" % (x, y, w, h, hot, NAVY)
    step = h / float(n)
    for i in range(n):
        s += "<rect x='%g' y='%g' width='%g' height='%g' fill='%s' stroke='%s' stroke-width='1.5'/>" % (x - 8, y + i * step + step * 0.25, w + 16, step * 0.45, PD, NAVY)
    return s


def car_box(cx, cy, w=50, h=26):
    return ("<rect x='%g' y='%g' width='%g' height='%g' rx='6' fill='%s' stroke='%s' stroke-width='2'/>" % (cx - w / 2, cy - h / 2, w, h, BODY, NAVY)
            + "<circle cx='%g' cy='%g' r='6' fill='%s'/><circle cx='%g' cy='%g' r='6' fill='%s'/>" % (cx - w / 3, cy + h / 2, NAVY, cx + w / 3, cy + h / 2, NAVY))


# ---------------- icons ----------------
ICON_ENGINE = ("<svg viewBox='0 0 40 40'><rect x='6' y='12' width='28' height='20' rx='3' fill='%s' stroke='%s' stroke-width='2'/>"
               "<rect x='12' y='6' width='6' height='8' fill='%s' stroke='%s' stroke-width='1.5'/><rect x='22' y='6' width='6' height='8' fill='%s' stroke='%s' stroke-width='1.5'/></svg>" % (PD, NAVY, PD, NAVY, PD, NAVY))
ICON_TRUNK = ("<svg viewBox='0 0 40 40'><rect x='6' y='14' width='28' height='20' rx='3' fill='%s' stroke='%s' stroke-width='2'/>"
              "<path d='M15 14 V9 H25 V14' fill='none' stroke='%s' stroke-width='2'/></svg>" % (GOLD, NAVY, NAVY))
ICON_ROUND = "<svg viewBox='0 0 40 40'><path d='M6 30 C6 14 18 6 26 8 C34 10 36 24 36 30 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (BODY, NAVY)
ICON_PISTON = ("<svg viewBox='0 0 40 40'><path d='M9 4 V36 M31 4 V36 M9 4 H31' fill='none' stroke='%s' stroke-width='2.5'/>"
               "<rect x='11' y='16' width='18' height='8' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (NAVY, PG, NAVY))
ICON_SPARK = "<svg viewBox='0 0 40 40'><polygon points='22,3 10,22 19,22 15,37 30,16 21,16' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (GOLD, NAVY)
ICON_HOTGAS = ("<svg viewBox='0 0 40 40'><path d='M20 6 Q32 16 28 28 Q24 36 20 34 Q12 36 11 26 Q10 16 20 6 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (ORANGE, NAVY))
ICON_FIN = "<svg viewBox='0 0 40 40'><rect x='14' y='4' width='12' height='32' fill='#E39A7F' stroke='%s' stroke-width='2'/>%s</svg>" % (
    NAVY, "".join("<rect x='6' y='%d' width='28' height='3.5' fill='%s' stroke='%s' stroke-width='1'/>" % (7 + i * 7, PD, NAVY) for i in range(4)))
ICON_FAN = "<svg viewBox='0 0 40 40'>%s</svg>" % fan(20, 20, 17)
ICON_RADIATOR = ("<svg viewBox='0 0 40 40'><rect x='8' y='6' width='24' height='28' fill='#FFFFFF' stroke='%s' stroke-width='2'/>%s</svg>" %
                 (NAVY, "".join("<line x1='11' y1='%d' x2='29' y2='%d' stroke='%s' stroke-width='2'/>" % (11 + i * 5, 11 + i * 5, TEAL) for i in range(5))))
ICON_CAR_DOT = "<svg viewBox='0 0 40 40'><rect x='5' y='13' width='30' height='16' rx='5' fill='%s' stroke='%s' stroke-width='2'/><circle cx='13' cy='30' r='4' fill='%s'/><circle cx='28' cy='30' r='4' fill='%s'/></svg>" % (BODY, NAVY, NAVY, NAVY)
ICON_TYRE = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='15' fill='%s'/><circle cx='20' cy='20' r='6' fill='%s' stroke='%s' stroke-width='1.5'/></svg>" % (NAVY, SAND, NAVY)
ICON_HEATWAVE = ICON_HEAT = ("<svg viewBox='0 0 40 40'><path d='M10 34 q6 -10 0 -20 M20 34 q6 -10 0 -20 M30 34 q6 -10 0 -20' fill='none' stroke='%s' stroke-width='3' stroke-linecap='round'/></svg>" % ORANGE)


def force_arrows(cx, cy, up, down, right, left, labels=True, size=12, w=4):
    """Four arrows leaving (cx, cy). Lengths given per direction."""
    s = (arrow(cx, cy - 12, cx, cy - 12 - up, TEAL, w, 11) + arrow(cx, cy + 12, cx, cy + 12 + down, NAVY, w, 11)
         + arrow(cx + 26, cy, cx + 26 + right, cy, GREEN, w, 11) + arrow(cx - 26, cy, cx - 26 - left, cy, ORANGE, w, 11))
    if labels:
        s += (txt(cx + 8, cy - 12 - up + 10, "Road push", size, TEAL, "start", "bold") + txt(cx + 8, cy + 12 + down, "Weight", size, NAVY, "start", "bold")
              + txt(cx + 26, cy - 8, "Drive", size, GREEN, "start", "bold") + txt(cx - 26 - left, cy - 8, "Drag", size, ORANGE, "start", "bold"))
    return s


# ====================== PAGE 1: BEETLE SIDE VIEW ======================
c1 = {
  "observe": {
    "svg": svg(300, 170, beetle(marks=True), "A VW Beetle seen from the side with two spots marked A at the front and B at the back"),
    "question": "Most cars keep their engine at the FRONT. Where does a VW Beetle keep its engine?",
    "explanation": "The Beetle is a rear-engine car. Its engine sits at the BACK, over the back wheels, and the trunk is at the front. The VW Bus uses the same back-engine idea.",
    "choices": [
      {"text": "At the back (B) 🔙", "correct": True},
      {"text": "At the front (A)", "correct": False},
      {"text": "On the roof", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "engine", "name": "Engine (at the back)", "icon": ICON_ENGINE, "fact": "🔧 The Beetle's engine sits at the BACK, over the back wheels. It is cooled by air."},
    {"id": "trunk", "name": "Trunk (at the front)", "icon": ICON_TRUNK, "fact": "🧳 Luggage goes in the FRONT. A back engine leaves free space up there!"},
    {"id": "body", "name": "Rounded body", "icon": ICON_ROUND, "fact": "🥚 The curvy shape lets air flow around it, a bit like a pigeon's teardrop."},
  ]},
  "draw": {
    "prompt": "Draw a Beetle from the side: a round roof, two wheels, the engine at the back and the trunk at the front.",
    "hintSvg": svg(300, 190,
      "<path d='M36,134 C30,110 50,88 84,70 C112,52 150,44 176,56 C196,64 210,84 232,94 C250,100 270,104 278,118 C282,126 280,134 272,136 L36,134 Z' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='7 5'/>" % ORANGE
      + "<circle cx='88' cy='136' r='22' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/><circle cx='224' cy='136' r='22' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % (NAVY, NAVY)
      + txt(52, 172, "engine", 11, NAVY, "middle", "bold") + txt(250, 172, "trunk", 11, NAVY, "middle", "bold"),
      "hint: dotted Beetle outline with two wheels"),
  },
  "rotate": {
    "prompt": "Rotate the Beetle. Turn it upside down. The shape stays the same. Can you still tell which end has the engine? Look for the orange dot!",
    "svg": "<g transform='translate(0,72)'>" + beetle(dot=True) + "</g>"
  },
  "compare": {
    "question": "Wind blows from the left. Tap the vehicle shape that lets air slide past more easily.",
    "explanation": "A rounded shape lets air flow around it. A boxy front hits the air like a wall, and the air swirls behind it. That swirl is drag.",
    "choices": [
      {"label": "A — round Beetle", "svg": svg(200, 140, beetle_at(0.66, 10, 22) + arrow(4, 18, 36, 18, TEAL, 3, 8), "round Beetle shape"), "correct": True},
      {"label": "B — boxy bus", "svg": svg(200, 140,
          "<rect x='25' y='28' width='165' height='72' rx='8' fill='#E9A66B' stroke='%s' stroke-width='2'/>" % NAVY
          + "".join("<rect x='%d' y='40' width='28' height='22' fill='%s' stroke='%s' stroke-width='1.5'/>" % (x, BLUE, NAVY) for x in (36, 72, 108, 144))
          + "<circle cx='62' cy='104' r='14' fill='%s'/><circle cx='153' cy='104' r='14' fill='%s'/>" % (NAVY, NAVY)
          + arrow(4, 18, 36, 18, TEAL, 3, 8), "boxy bus shape"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "The Beetle's engine sits at the BACK", "icon": ICON_ENGINE},
    {"text": "That leaves the front free for a trunk", "icon": ICON_TRUNK},
    {"text": "The rounded body lets air flow around it smoothly", "icon": ICON_ROUND},
    {"text": "🔗 Links to Pigeon Side View and Titanic Hull Shape: a pigeon, a ship and a Beetle all use smooth, rounded shapes to slide through air or water", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why might a car designer put the engine at the back instead of the front?",
    "visualSvg": svg(200, 112, beetle_at(0.5, 22, 8, dot=True) + txt(50, 106, "engine", 10, NAVY, "middle", "bold"), "small Beetle with its engine marked at the back"),
    "starters": ["With the engine at the back, the front can...", "The engine's weight sits over..."],
    "keywords": ["engine", "weight", "trunk", "wheels"]
  },
  "predict": {
    "question": "A Beetle's engine is at the back. Which end of the car is probably heavier?",
    "explanation": "The engine is one of the heaviest parts of a car. With it at the back, more weight sits over the back wheels. (Page 7 shows how this helps grip and why it can make the tail swing.)",
    "choices": [
      {"text": "The back", "correct": True},
      {"text": "The front", "correct": False},
      {"text": "Both ends exactly the same", "correct": False},
    ]
  },
}
build("cars-01-beetle-side-view", "Beetle: Side View 🚗", c1)

# ====================== PAGE 2: FOUR-STROKE ENGINE ======================
GAS_IN = BLUE; GAS_SQ = "#8FB8D0"; GAS_BANG = "#F2B36B"; GAS_OUT = "#C9C9C9"
stages = [(15, 90, GAS_IN, "down", False, "1 suck"), (88, 48, GAS_SQ, "up", False, "2 squeeze"),
          (161, 62, GAS_BANG, "down", True, "3 bang"), (234, 80, GAS_OUT, "up", False, "4 blow")]
c2 = {
  "observe": {
    "svg": svg(300, 180,
      "".join(cyl(x, py, g, d, sp) + txt(x + 25, 168, lab, 11, NAVY, "middle", "bold") for x, py, g, d, sp, lab in stages),
      "Four steps of an engine: suck, squeeze, bang, blow, shown as pistons in cylinders"),
    "question": "An engine repeats four steps. Which step gives the engine its push?",
    "explanation": "In the BANG step a spark lights the squeezed fuel-and-air mix. It burns, gets very hot, and the hot gas expands and shoves the piston down. That push is what turns the wheels.",
    "choices": [
      {"text": "Bang: burning gas expands and pushes the piston 💥", "correct": True},
      {"text": "Suck: fresh air and fuel come in", "correct": False},
      {"text": "Squeeze: the piston crushes the mix", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "piston", "name": "Piston", "icon": ICON_PISTON, "fact": "🔩 The piston slides up and down inside the cylinder. The hot gas pushes it."},
    {"id": "spark", "name": "Spark", "icon": ICON_SPARK, "fact": "⚡ A spark lights the squeezed fuel-and-air mix. It burns fast and gets very hot."},
    {"id": "gas", "name": "Hot expanding gas", "icon": ICON_HOTGAS, "fact": "🔥 Hot gas takes up MORE space. It pushes the piston down hard."},
  ]},
  "draw": {
    "prompt": "Draw one cylinder with a piston inside. Add arrows: DOWN for suck, UP for squeeze, DOWN for bang, UP for blow.",
    "hintSvg": svg(300, 200,
      "<path d='M110 170 V30 H190 V170' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='7 5'/>" % ORANGE
      + "<rect x='112' y='95' width='76' height='14' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % NAVY
      + arrow(215, 75, 215, 135, ORANGE, 3, 9) + arrow(85, 135, 85, 75, ORANGE, 3, 9)
      + txt(222, 108, "down", 11, NAVY) + txt(78, 108, "up", 11, NAVY, "end"),
      "hint: dotted cylinder with a piston and up and down arrows"),
  },
  "rotate": {
    "prompt": "Rotate the picture. The Beetle's engine is a FLAT engine: its cylinders lie on their sides and face each other, pushing in and out like boxers punching 🥊.",
    "svg": "<rect x='36' y='128' width='92' height='44' fill='none' stroke='%s' stroke-width='4'/>" % NAVY
           + "<rect x='172' y='128' width='92' height='44' fill='none' stroke='%s' stroke-width='4'/>" % NAVY
           + "<rect x='96' y='132' width='12' height='36' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
           + "<rect x='192' y='132' width='12' height='36' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
           + "<line x1='108' y1='150' x2='150' y2='150' stroke='%s' stroke-width='4'/><line x1='192' y1='150' x2='150' y2='150' stroke='%s' stroke-width='4'/>" % (NAVY, NAVY)
           + "<circle cx='150' cy='150' r='12' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY)
           + arrow(70, 100, 100, 100, ORANGE, 3, 9) + arrow(230, 100, 200, 100, ORANGE, 3, 9)
           + txt(150, 205, "flat engine: pistons face each other", 11, NAVY, "middle", "bold")
  },
  "compare": {
    "question": "Tap the step where the gas is squeezed into the SMALLEST space.",
    "explanation": "In the squeeze step the piston is high, so the same gas is packed into a tiny space. Same gas, less room means it is packed tighter (higher density and pressure).",
    "choices": [
      {"label": "A — suck", "svg": svg(200, 170, cyl(75, 90, GAS_IN, "down") , "piston low, lots of room for gas"), "correct": False},
      {"label": "B — squeeze", "svg": svg(200, 170, cyl(75, 48, GAS_SQ, "up"), "piston high, gas squeezed small"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "A spark lights the squeezed fuel-and-air mix", "icon": ICON_SPARK},
    {"text": "Burning makes the gas VERY hot", "icon": ICON_HEAT},
    {"text": "Hot gas expands and pushes the piston down", "icon": ICON_HOTGAS},
    {"text": "🔗 Links to Cooking States of Matter and Mario Energy: heat makes gas spread out (like steam lifting a pot lid), and fuel's chemical energy becomes motion energy", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does hot gas push the piston down in the bang step?",
    "visualSvg": svg(200, 100, "<g transform='translate(70,-15) scale(0.8)'>" + cyl(15, 62, GAS_BANG, "down", True) + "</g>", "cylinder with hot gas pushing the piston down"),
    "starters": ["Hot gas takes up...", "That pushes the piston..."],
    "keywords": ["gas", "heat", "expand", "piston"]
  },
  "predict": {
    "question": "The spark stops working for one round. What happens in the bang step?",
    "explanation": "No spark means no burning, so the gas does not get hot and expand. There is no push for that round. The engine needs the spark every time to keep going.",
    "choices": [
      {"text": "No bang, so no push that round", "correct": True},
      {"text": "An extra big bang", "correct": False},
      {"text": "The piston flies out of the engine", "correct": False},
    ]
  },
}
build("cars-02-four-stroke-engine", "Beetle: Four-Stroke Engine ⚙️", c2)

# ====================== PAGE 3: AIR COOLING ======================
def hot_waves(x, y):
    return "".join("<path d='M%d %d q5 -9 0 -18 q-5 -9 0 -18' fill='none' stroke='%s' stroke-width='2.5' stroke-linecap='round'/>" % (x + dx, y, ORANGE) for dx in (0, 14, 28))


c3 = {
  "observe": {
    "svg": svg(300, 190,
      finned(75, 55, 36, 80, 6) + fan(28, 95, 18) + arrow(52, 80, 70, 80, TEAL, 2.5, 7) + arrow(52, 105, 70, 105, TEAL, 2.5, 7)
      + hot_waves(78, 48)
      + "<line x1='150' y1='20' x2='150' y2='150' stroke='%s' stroke-width='1.5' stroke-dasharray='4 4'/>" % SAND
      + "<rect x='180' y='75' width='38' height='50' fill='#E39A7F' stroke='%s' stroke-width='2'/>" % NAVY
      + "<rect x='255' y='55' width='30' height='90' fill='#FFFFFF' stroke='%s' stroke-width='2'/>" % NAVY
      + "".join("<line x1='258' y1='%d' x2='282' y2='%d' stroke='%s' stroke-width='2'/>" % (64 + i * 10, 64 + i * 10, TEAL) for i in range(8))
      + "<line x1='218' y1='88' x2='255' y2='88' stroke='%s' stroke-width='5'/><line x1='218' y1='112' x2='255' y2='112' stroke='%s' stroke-width='5'/>" % (TEAL, TEAL)
      + txt(237, 80, "water", 9, TEAL, "middle") + txt(70, 170, "air-cooled", 11, NAVY, "middle", "bold") + txt(232, 170, "water-cooled", 11, NAVY, "middle", "bold"),
      "Left: a finned engine cylinder cooled by a fan. Right: an engine cooled by water pipes and a radiator"),
    "question": "An engine makes a lot of heat. How does the Beetle's engine get rid of it?",
    "explanation": "The Beetle is air-cooled. A fan blows air over metal fins on the hot cylinders and carries the heat away. Most other cars use water and a radiator instead.",
    "choices": [
      {"text": "A fan blows air over metal fins 🌀", "correct": True},
      {"text": "A big water radiator 💧", "correct": False},
      {"text": "It never gets hot", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "fins", "name": "Cooling fins", "icon": ICON_FIN, "fact": "🧱 Fins give the hot metal MORE surface for air to touch. More surface means faster cooling."},
    {"id": "fan", "name": "Cooling fan", "icon": ICON_FAN, "fact": "🌀 The fan blows cool air across the fins and pushes the hot air away."},
    {"id": "radiator", "name": "Radiator", "icon": ICON_RADIATOR, "fact": "🌡️ Most cars use water instead. Water carries heat to the radiator, and air carries it away."},
  ]},
  "draw": {
    "prompt": "Draw a hot cylinder with fins. Add blue arrows for cool air coming in and red arrows for hot air going away.",
    "hintSvg": svg(300, 200,
      "<rect x='125' y='50' width='50' height='100' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='7 5'/>" % ORANGE
      + "".join("<line x1='112' y1='%d' x2='188' y2='%d' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % (62 + i * 18, 62 + i * 18, NAVY) for i in range(5))
      + arrow(40, 85, 105, 85, TEAL, 3, 9) + arrow(40, 125, 105, 125, TEAL, 3, 9)
      + arrow(195, 85, 260, 85, ORANGE, 3, 9) + arrow(195, 125, 260, 125, ORANGE, 3, 9),
      "hint: dotted finned cylinder with cool air in and hot air out"),
  },
  "rotate": {
    "prompt": "Rotate the fin picture. Fins stick out in every direction around the hot cylinder, so heat can escape from all sides. The gold dot shows the turn.",
    "svg": "".join("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' stroke='%s' stroke-width='9' stroke-linecap='round'/>" % (
              150 + 42 * math.cos(a), 150 + 42 * math.sin(a), 150 + 95 * math.cos(a), 150 + 95 * math.sin(a), PD)
              for a in [i * math.pi / 8 for i in range(16)])
           + "<circle cx='150' cy='150' r='46' fill='#E39A7F' stroke='%s' stroke-width='3'/>" % NAVY
           + "<circle cx='150' cy='46' r='8' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY)
  },
  "compare": {
    "question": "Both hot cylinders sit in the same breeze. Tap the one that cools faster.",
    "explanation": "The finned cylinder has far more surface touching the moving air, so it hands over heat faster. More surface area means faster cooling.",
    "choices": [
      {"label": "A — smooth cylinder", "svg": svg(200, 140,
          "<rect x='85' y='25' width='40' height='90' fill='#E39A7F' stroke='%s' stroke-width='2'/>" % NAVY + arrow(10, 55, 70, 55, TEAL, 3, 8) + arrow(10, 90, 70, 90, TEAL, 3, 8), "smooth cylinder"), "correct": False},
      {"label": "B — finned cylinder", "svg": svg(200, 140,
          finned(85, 25, 40, 90, 6) + arrow(10, 55, 62, 55, TEAL, 3, 8) + arrow(10, 90, 62, 90, TEAL, 3, 8), "finned cylinder"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "Burning fuel makes the engine hot", "icon": ICON_HOTGAS},
    {"text": "Heat moves from the hot metal into the fins (conduction)", "icon": ICON_FIN},
    {"text": "The fan blows air past the fins and carries the heat away (convection)", "icon": ICON_FAN},
    {"text": "🔗 Links to Cooking Heat Transfer and Connection: Convection: same team as a hot pan and a breeze. Heat travels through metal, then moving air carries it off. Heat always has to go somewhere", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why do the Beetle's cylinders have fins instead of being smooth?",
    "visualSvg": svg(200, 100, "<g transform='translate(70,5) scale(0.55)'>" + finned(15, 15, 40, 90, 6) + "</g>" + arrow(10, 40, 62, 40, TEAL, 3, 8) + arrow(10, 62, 62, 62, TEAL, 3, 8), "finned cylinder in a breeze"),
    "starters": ["Fins give the metal more...", "More surface touching air means..."],
    "keywords": ["fins", "surface", "air", "heat"]
  },
  "predict": {
    "question": "The belt that spins the cooling fan snaps. What happens to the engine's temperature?",
    "explanation": "Without the fan, much less air flows over the fins, so heat is not carried away fast enough. The engine temperature rises, and an overheated engine can be badly damaged.",
    "choices": [
      {"text": "It rises", "correct": True},
      {"text": "It falls", "correct": False},
      {"text": "It stays exactly the same", "correct": False},
    ]
  },
}
build("cars-03-air-cooling", "Beetle: Air Cooling 🌀", c3)

# ====================== PAGE 4: FORCES ON THE ROAD ======================
c4 = {
  "observe": {
    "svg": svg(300, 220,
      "<line x1='10' y1='161' x2='290' y2='161' stroke='%s' stroke-width='3'/>" % SAND
      + beetle_at(0.65, 60, 60)
      + arrow(160, 112, 160, 52, TEAL, 4, 11) + txt(168, 62, "Road push", 12, TEAL, "start", "bold")
      + arrow(160, 140, 160, 200, NAVY, 4, 11) + txt(168, 208, "Weight", 12, NAVY, "start", "bold")
      + arrow(250, 126, 292, 126, GREEN, 4, 11) + txt(252, 118, "Drive", 12, GREEN, "start", "bold")
      + arrow(70, 126, 28, 126, ORANGE, 4, 11) + txt(16, 118, "Drag", 12, ORANGE, "start", "bold"),
      "A Beetle with four force arrows: road push up, weight down, drive forward and drag back, all balanced"),
    "question": "The Beetle drives at a steady speed on a flat road. What do the equal arrows tell you?",
    "explanation": "Equal arrows in opposite directions cancel out. The road push balances the weight, and the drive force balances the drag. Balanced forces mean steady speed, with no speeding up or slowing down.",
    "choices": [
      {"text": "The forces are balanced, so it keeps a steady speed", "correct": True},
      {"text": "Drive is bigger, so it is speeding up", "correct": False},
      {"text": "No forces act on it", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "drive", "name": "Drive force", "icon": ICON_RIGHT, "fact": "🛞 Friction between the tyres and the road pushes the car FORWARD. No grip, no go!"},
    {"id": "drag", "name": "Drag", "icon": ICON_LEFT, "fact": "💨 Drag is air pushing BACK against the car. Go faster and it grows a lot."},
    {"id": "weight", "name": "Weight", "icon": ICON_DOWN, "fact": "⬇️ Weight is gravity pulling the car DOWN."},
    {"id": "road", "name": "Road push", "icon": ICON_UP, "fact": "⬆️ The road pushes UP on the tyres. It balances the weight so the car doesn't sink."},
  ]},
  "draw": {
    "prompt": "Draw the car as a simple box. Add 4 arrows: drive forward, drag back, weight down, road push up.",
    "hintSvg": svg(300, 200,
      car_box(150, 97, 70, 34)
      + arrow(150, 76, 150, 22, TEAL, 3, 10) + txt(158, 32, "road push", 11, TEAL)
      + arrow(150, 125, 150, 180, NAVY, 3, 10) + txt(158, 178, "weight", 11, NAVY)
      + arrow(190, 97, 258, 97, GREEN, 3, 10) + txt(205, 87, "drive", 11, GREEN)
      + arrow(110, 97, 42, 97, ORANGE, 3, 10) + txt(44, 87, "drag", 11, ORANGE),
      "hint: a box car with four arrows"),
  },
  "rotate": {
    "prompt": "Rotate the force picture. The arrows turn, but the balance stays the same. Equal arrows pointing opposite ways still cancel out.",
    "svg": car_box(150, 150, 50, 28)
           + arrow(150, 132, 150, 62, TEAL, 4, 11) + txt(158, 76, "road push", 12, TEAL, "start", "bold")
           + arrow(150, 172, 150, 238, NAVY, 4, 11) + txt(158, 236, "weight", 12, NAVY, "start", "bold")
           + arrow(178, 150, 246, 150, GREEN, 4, 11) + txt(196, 140, "drive", 12, GREEN, "start", "bold")
           + arrow(122, 150, 54, 150, ORANGE, 4, 11) + txt(56, 140, "drag", 12, ORANGE, "start", "bold")
  },
  "compare": {
    "question": "Tap the picture where the car is slowing down.",
    "explanation": "When drag is bigger than the drive force, the forces are unbalanced. A leftover push points backwards, so the car slows down. Equal arrows mean steady speed.",
    "choices": [
      {"label": "A — drag is bigger", "svg": svg(200, 140,
          car_box(100, 75, 40, 22) + arrow(124, 75, 150, 75, GREEN, 4, 10) + arrow(76, 75, 12, 75, ORANGE, 4, 10)
          + txt(128, 62, "drive", 10, GREEN) + txt(12, 62, "drag", 10, ORANGE), "long drag arrow, short drive arrow"), "correct": True},
      {"label": "B — drive = drag", "svg": svg(200, 140,
          car_box(100, 75, 40, 22) + arrow(124, 75, 172, 75, GREEN, 4, 10) + arrow(76, 75, 28, 75, ORANGE, 4, 10)
          + txt(130, 62, "drive", 10, GREEN) + txt(28, 62, "drag", 10, ORANGE), "equal drive and drag arrows"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "The engine turns the wheels", "icon": ICON_ENGINE},
    {"text": "The tyres grip the road: friction", "icon": ICON_TYRE},
    {"text": "Friction pushes the car forward: the drive force", "icon": ICON_RIGHT},
    {"text": "🔗 Links to Mario Friction and Pigeon Forces in Flight: tyre grip is the car's thrust, and air drag pushes back on cars and pigeons alike. A wet road is like Mario on ice!", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why is it harder to stop or turn on a wet road?",
    "visualSvg": svg(200, 100, "<line x1='10' y1='70' x2='190' y2='70' stroke='%s' stroke-width='3'/>" % SAND
      + "<path d='M20 76 q8 6 16 0 t16 0 t16 0 t16 0 t16 0 t16 0 t16 0' fill='none' stroke='%s' stroke-width='2'/>" % TEAL
      + "<circle cx='100' cy='54' r='14' fill='%s'/><circle cx='100' cy='54' r='5' fill='%s'/>" % (NAVY, SAND), "tyre on a wet road"),
    "starters": ["Water on the road makes friction...", "Less grip means the tyres..."],
    "keywords": ["friction", "grip", "tyres", "slide"]
  },
  "predict": {
    "question": "The Beetle drives onto ice, where there is almost no friction. What happens to its drive force?",
    "explanation": "The drive force comes from tyre grip on the road. With almost no grip, the force almost disappears, so the wheels just spin and the car barely speeds up.",
    "choices": [
      {"text": "It almost disappears, so the wheels spin", "correct": True},
      {"text": "It gets bigger", "correct": False},
      {"text": "It stays exactly the same", "correct": False},
    ]
  },
}
build("cars-04-forces-on-the-road", "Car: Forces on the Road 🛞", c4)
print("cars batch 1 done: 4 pages")
