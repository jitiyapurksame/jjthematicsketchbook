"""Beetles & Buses book, batch 2 (pages 5-8). Run: python3 build-tools/build_cars_batch2.py
Uses shared helpers from cars_common.py (which re-exports birds_common). Writes into ../deliverables."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cars_common import *  # noqa: F401,F403

BG = "#FFFFFF"


# ---------------- extra helpers ----------------
def axes(ox, oy, xend, ytop):
    return ("<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2'/>" % (ox, oy, xend, oy, NAVY)
            + "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2'/>" % (ox, oy, ox, ytop, NAVY)
            + tri_right(xend + 4, oy, NAVY, 5)
            + "<polygon points='%g,%g %g,%g %g,%g' fill='%s'/>" % (ox, ytop - 4, ox - 4, ytop + 5, ox + 4, ytop + 5, NAVY))


def poly(points, color, w=4, dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return "<polyline points='%s' fill='none' stroke='%s' stroke-width='%s' stroke-linecap='round' stroke-linejoin='round'%s/>" % (
        " ".join("%g,%g" % p for p in points), color, w, d)


def hot_waves(xs, y, h=36):
    return "".join("<path d='M%d %d q5 -%d 0 -%d q-5 -%d 0 -%d' fill='none' stroke='%s' stroke-width='2.5' stroke-linecap='round'/>" % (
        x, y, h // 4, h // 2, h // 4, h // 2, ORANGE) for x in xs)


def disc(cx, cy, r, holes=8, marker=False):
    s = "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='3'/>" % (cx, cy, r, PG, NAVY)
    for i in range(holes):
        a = i * 2 * math.pi / holes
        s += "<circle cx='%.1f' cy='%.1f' r='%.1f' fill='%s' stroke='%s' stroke-width='1.5'/>" % (
            cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a), r * 0.1, BG, NAVY)
    s += "<circle cx='%g' cy='%g' r='%.1f' fill='%s' stroke='%s' stroke-width='2'/>" % (cx, cy, r * 0.28, SAND, NAVY)
    if marker:
        s += "<circle cx='%g' cy='%g' r='7' fill='%s' stroke='%s' stroke-width='2'/>" % (cx, cy - r * 0.86, GOLD, NAVY)
    return s


def gear(cx, cy, r, n, phase=0.0, marker=False):
    tw = 2 * math.pi * r / n * 0.45
    s = ""
    for i in range(n):
        a = phase + i * 360.0 / n
        s += "<rect x='%.1f' y='%.1f' width='%.1f' height='9' fill='%s' stroke='%s' stroke-width='1.2' transform='rotate(%.2f %g %g)'/>" % (
            cx - tw / 2, cy - r - 5, tw, PD, NAVY, a, cx, cy)
    s += "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='2'/>" % (cx, cy, r - 4, PD, NAVY)
    s += "<circle cx='%g' cy='%g' r='%.1f' fill='%s' stroke='%s' stroke-width='1.5'/>" % (cx, cy, max(4, r * 0.18), SAND, NAVY)
    if marker:
        s += "<circle cx='%g' cy='%g' r='8' fill='%s' stroke='%s' stroke-width='2'/>" % (cx, cy - r * 0.6, GOLD, NAVY)
    return s


def tilted(pivot_x, ground_y, w, h, fill, theta, kind):
    """Simple vehicle model, body rect right edge 8px past the pivot wheel's contact point. Returns (svg, com_x, com_y)."""
    g = "<g transform='translate(%g,%g) rotate(%g)'>" % (pivot_x, ground_y, theta)
    g += "<rect x='%g' y='%g' width='%g' height='%g' rx='8' fill='%s' stroke='%s' stroke-width='2.5'/>" % (-(w - 8), -h, w, h, fill, NAVY)
    if kind == "bus":
        g += "".join("<rect x='%d' y='%d' width='16' height='18' fill='%s' stroke='%s' stroke-width='1.5'/>" % (x, -h + 10, BLUE, NAVY) for x in (-58, -38, -18))
    else:
        g += "<path d='M-70,-40 Q-50,-62 -26,-40 Z' fill='%s' stroke='%s' stroke-width='2'/>" % (BLUE, NAVY)
    g += "<circle cx='0' cy='-8' r='8' fill='%s'/><circle cx='%g' cy='-8' r='8' fill='%s'/></g>" % (NAVY, -(w - 16), NAVY)
    dx, dy = 8 - w / 2.0, -h / 2.0
    t = math.radians(theta)
    cx = pivot_x + dx * math.cos(t) - dy * math.sin(t)
    cy = ground_y + dx * math.sin(t) + dy * math.cos(t)
    return g, cx, cy


# icons
ICON_PAD = "<svg viewBox='0 0 40 40'><rect x='12' y='6' width='16' height='28' rx='2' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (NAVY, NAVY)
ICON_DISC = "<svg viewBox='0 0 40 40'>%s</svg>" % disc(20, 20, 16, 6)
ICON_GEAR_S = "<svg viewBox='0 0 40 40'><g transform='translate(20,20) scale(0.45)'>%s</g></svg>" % gear(0, 0, 30, 8)
ICON_GEAR_B = "<svg viewBox='0 0 40 40'><g transform='translate(20,20) scale(0.33)'>%s</g></svg>" % gear(0, 0, 55, 16, 11.25)
ICON_TEETH = "<svg viewBox='0 0 40 40'><g transform='translate(6,20) scale(0.4)'>%s</g><g transform='translate(34,20) scale(0.4)'>%s</g></svg>" % (gear(0, 0, 22, 8), gear(0, 0, 22, 8, 22.5))
ICON_COM = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='9' fill='%s' stroke='%s' stroke-width='2'/>"
            "<path d='M20 4 V36 M4 20 H36' stroke='%s' stroke-width='1.5'/></svg>" % (GOLD, NAVY, NAVY))
ICON_BASE = ("<svg viewBox='0 0 40 40'><circle cx='10' cy='24' r='6' fill='%s'/><circle cx='30' cy='24' r='6' fill='%s'/>"
             "<path d='M10 36 H30 M10 33 V39 M30 33 V39' stroke='%s' stroke-width='2'/></svg>" % (NAVY, NAVY, TEAL))
ICON_PLUMB = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='9' r='5' fill='%s' stroke='%s' stroke-width='1.5'/>"
              "<line x1='20' y1='14' x2='20' y2='34' stroke='%s' stroke-width='2.5' stroke-dasharray='4 3'/><line x1='6' y1='35' x2='34' y2='35' stroke='%s' stroke-width='2'/></svg>" % (GOLD, NAVY, NAVY, NAVY))
ICON_RISE = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='32' x2='28' y2='10' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, GREEN)
ICON_CRUISE = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='12' x2='32' y2='12' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, TEAL)
ICON_ZERO = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='32' x2='32' y2='32' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, ORANGE)
ICON_FALL = "<svg viewBox='0 0 40 40'><path d='M6 6 V34 H34' fill='none' stroke='%s' stroke-width='2'/><line x1='8' y1='10' x2='28' y2='32' stroke='%s' stroke-width='4' stroke-linecap='round'/></svg>" % (NAVY, ORANGE)
ICON_SPEED = ICON_CAR_DOT


# ====================== PAGE 5: BRAKES ======================
c5 = {
  "observe": {
    "svg": svg(300, 190,
      disc(110, 105, 55, 8)
      + arrow(88, 38, 132, 38, TEAL, 3, 9) + txt(110, 26, "spinning", 10, TEAL, "middle")
      + "<rect x='166' y='78' width='20' height='54' rx='3' fill='%s' stroke='%s' stroke-width='2'/>" % (NAVY, NAVY)
      + hot_waves((205, 219, 233), 100) + txt(219, 54, "heat", 11, ORANGE, "middle", "bold")
      + txt(110, 180, "brake disc", 11, NAVY, "middle", "bold") + txt(176, 148, "pad", 11, NAVY, "middle", "bold"),
      "A spinning brake disc with a brake pad pressing on it and heat rising"),
    "question": "When you press the brake pedal, where does the car's motion energy go?",
    "explanation": "The pads rub against the spinning disc. Rubbing is friction, and friction turns motion energy into heat. That is why brakes get hot. The energy is not lost, it changes form.",
    "choices": [
      {"text": "Into heat in the brakes 🔥", "correct": True},
      {"text": "It just disappears", "correct": False},
      {"text": "Back into the fuel tank", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "pad", "name": "Brake pad", "icon": ICON_PAD, "fact": "🧱 The pad squeezes and rubs against the spinning disc. Rubbing = friction."},
    {"id": "disc", "name": "Brake disc", "icon": ICON_DISC, "fact": "💿 The disc spins with the wheel. When the pad grips it, the wheel slows down."},
    {"id": "heat", "name": "Heat", "icon": ICON_HEAT, "fact": "🔥 Motion energy turns into heat. Hard braking can make brakes glow hot!"},
  ]},
  "draw": {
    "prompt": "Draw a brake disc with a pad pressing on its edge. Add wavy heat lines above the pad.",
    "hintSvg": svg(300, 200,
      "<circle cx='130' cy='105' r='55' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='7 5'/>" % NAVY
      + "<circle cx='130' cy='105' r='15' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='5 4'/>" % NAVY
      + "<rect x='187' y='80' width='18' height='50' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % ORANGE
      + hot_waves((225, 239, 253), 105) + txt(239, 58, "heat", 11, ORANGE, "middle", "bold"),
      "hint: dotted disc with a pad and heat lines"),
  },
  "rotate": {
    "prompt": "Rotate the brake disc. The gold dot turns with the wheel. When the pads grip the disc, the spin slows down, and so does the car.",
    "svg": disc(150, 150, 100, 8, marker=True)
  },
  "compare": {
    "question": "A car goes 30 km/h. Another goes TWICE as fast, 60 km/h. Both brake the same way. Tap the bar showing the faster car's braking distance.",
    "explanation": "Motion energy grows with speed squared. Twice the speed means 4 times the energy to get rid of, so about 4 times the braking distance. Speed matters a LOT!",
    "choices": [
      {"label": "A — 2 times as long", "svg": svg(200, 140,
          "<rect x='20' y='25' width='30' height='16' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY) + txt(58, 38, "30 km/h", 10, NAVY)
          + "<rect x='20' y='80' width='60' height='16' fill='%s' stroke='%s' stroke-width='2'/>" % (ORANGE, NAVY) + txt(88, 93, "60 km/h", 10, NAVY), "bar twice as long"), "correct": False},
      {"label": "B — 4 times as long", "svg": svg(200, 140,
          "<rect x='20' y='25' width='30' height='16' fill='%s' stroke='%s' stroke-width='2'/>" % (GOLD, NAVY) + txt(58, 38, "30 km/h", 10, NAVY)
          + "<rect x='20' y='80' width='120' height='16' fill='%s' stroke='%s' stroke-width='2'/>" % (ORANGE, NAVY) + txt(146, 93, "60 km/h", 10, NAVY), "bar four times as long"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "The moving car has motion energy", "icon": ICON_CAR_DOT},
    {"text": "Brake pads rub the spinning disc: friction", "icon": ICON_PAD},
    {"text": "Friction changes motion energy into heat", "icon": ICON_HEAT},
    {"text": "🔗 Links to Mario Energy and Momentum: energy changes form but never vanishes, and fast heavy things take longer to stop. Same 'heat has to go somewhere' idea as the air-cooled engine", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why do a car's brakes get very hot after a long drive downhill?",
    "visualSvg": svg(200, 100, disc(60, 50, 36, 6) + hot_waves((125, 140, 155), 62), "disc with heat"),
    "starters": ["Friction changes motion energy into...", "Going downhill, the car keeps..."],
    "keywords": ["friction", "heat", "energy", "brakes"]
  },
  "predict": {
    "question": "A car drives twice as fast as before and brakes just as hard. How does its braking distance change?",
    "explanation": "Twice the speed means 4 times the motion energy, so the brakes need about 4 times the distance to turn it all into heat.",
    "choices": [
      {"text": "About 4 times longer", "correct": True},
      {"text": "About 2 times longer", "correct": False},
      {"text": "The same distance", "correct": False},
    ]
  },
}
build("cars-05-brakes", "Car: Brakes Turn Motion into Heat 🛑", c5)

# ====================== PAGE 6: GEARS & TORQUE ======================
c6 = {
  "observe": {
    "svg": svg(300, 180,
      gear(75, 85, 30, 8) + gear(160, 85, 55, 16, 11.25)
      + arrow(58, 38, 92, 38, ORANGE, 3, 9) + arrow(190, 14, 130, 14, ORANGE, 3, 9)
      + txt(75, 160, "small gear", 11, NAVY, "middle", "bold") + txt(75, 174, "spins FAST", 10, TEAL, "middle")
      + txt(205, 160, "big gear", 11, NAVY, "middle", "bold") + txt(205, 174, "slower, stronger twist", 10, TEAL, "middle"),
      "A small gear turning a big gear, with arrows showing opposite spin directions"),
    "question": "A small gear drives a big gear. Which one spins slower but twists harder?",
    "explanation": "The big gear turns slower, but it twists with MORE force. That twisting force is called torque. Gears trade speed for strength, like a lever does.",
    "choices": [
      {"text": "The big gear ⚙️", "correct": True},
      {"text": "The small gear", "correct": False},
      {"text": "They are exactly the same", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "small", "name": "Small gear", "icon": ICON_GEAR_S, "fact": "⚙️ Fewer teeth. It spins fast, but with less twisting force."},
    {"id": "big", "name": "Big gear", "icon": ICON_GEAR_B, "fact": "⚙️ More teeth. It turns slower, but with MORE twisting force (torque)."},
    {"id": "teeth", "name": "Teeth", "icon": ICON_TEETH, "fact": "🦷 The teeth lock together, so one gear drives the next one without slipping."},
  ]},
  "draw": {
    "prompt": "Draw two gears touching: a small one and a big one. Add an arrow on each to show which way it turns.",
    "hintSvg": svg(300, 200,
      "<circle cx='95' cy='110' r='30' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % ORANGE
      + "<circle cx='180' cy='110' r='55' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='6 4'/>" % ORANGE
      + arrow(78, 62, 112, 62, NAVY, 3, 9) + arrow(210, 40, 150, 40, NAVY, 3, 9),
      "hint: two dotted circles touching, a small and a big one"),
  },
  "rotate": {
    "prompt": "Rotate the gear. Its teeth repeat all the way round, so a gear can keep turning forever and keep driving the next gear.",
    "svg": gear(150, 150, 85, 20, marker=True)
  },
  "compare": {
    "question": "A bus must climb a steep hill. Tap the gear pair that gives the biggest twisting push at the wheels.",
    "explanation": "A small gear driving a big gear gives slower speed but MORE twist. That is low gear, perfect for hills. The other pair is more like top gear: fast, but weaker.",
    "choices": [
      {"label": "A — small drives big", "svg": svg(200, 140,
          gear(48, 70, 20, 8) + gear(108, 70, 40, 16, 11.25)
          + txt(48, 112, "engine", 10, NAVY, "middle") + txt(130, 130, "wheels", 10, NAVY, "middle"), "small gear driving a big gear"), "correct": True},
      {"label": "B — big drives small", "svg": svg(200, 140,
          gear(60, 70, 40, 16) + gear(120, 70, 20, 8, 22.5)
          + txt(60, 128, "engine", 10, NAVY, "middle") + txt(120, 112, "wheels", 10, NAVY, "middle"), "big gear driving a small gear"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "The engine spins a small gear fast", "icon": ICON_GEAR_S},
    {"text": "It turns a bigger gear", "icon": ICON_GEAR_B},
    {"text": "The bigger gear turns slower but twists harder (more torque)", "icon": ICON_RISE},
    {"text": "🔗 Links to Titanic Propeller and Mario Acceleration: a spinning shaft turns engine power into push, and low gear gives a strong push for a quick getaway", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does a bus use a low gear to climb a steep hill?",
    "visualSvg": svg(200, 100, "<g transform='translate(0,-10)'>" + gear(60, 65, 22, 8) + gear(113, 65, 33, 12, 15) + "</g>", "two gears"),
    "starters": ["Low gear gives...", "The trade-off is..."],
    "keywords": ["torque", "speed", "push", "hill"]
  },
  "predict": {
    "question": "A Beetle shifts into a HIGHER gear on a flat road. What happens?",
    "explanation": "A higher gear trades twisting push for speed. The car can go faster for the same engine speed, but it has less push for climbing or quick getaways.",
    "choices": [
      {"text": "Faster, but with less push", "correct": True},
      {"text": "Slower, but with more push", "correct": False},
      {"text": "Nothing changes", "correct": False},
    ]
  },
}
build("cars-06-gears-torque", "Car: Gears & Torque ⚙️", c6)

# ====================== PAGE 7: CENTRE OF MASS ======================
THETA = 50
b_svg, b_cx, b_cy = tilted(85, 150, 100, 40, BODY, THETA, "beetle")
u_svg, u_cx, u_cy = tilted(215, 150, 70, 90, "#E9A66B", THETA, "bus")


def com_dot(x, y, ground_y):
    return ("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%g' stroke='%s' stroke-width='2' stroke-dasharray='5 4'/>" % (x, y, x, ground_y, NAVY)
            + "<circle cx='%.1f' cy='%.1f' r='6' fill='%s' stroke='%s' stroke-width='2'/>" % (x, y, GOLD, NAVY))


c7 = {
  "observe": {
    "svg": svg(300, 200,
      "<line x1='5' y1='150' x2='295' y2='150' stroke='%s' stroke-width='3'/>" % SAND
      + b_svg + u_svg + com_dot(b_cx, b_cy, 150) + com_dot(u_cx, u_cy, 150)
      + txt(75, 172, "low Beetle", 11, NAVY, "middle", "bold") + txt(232, 172, "tall bus", 11, NAVY, "middle", "bold")
      + txt(75, 188, "falls back down", 10, TEAL, "middle") + txt(232, 188, "tips over!", 10, ORANGE, "middle", "bold"),
      "A low Beetle and a tall bus tilted the same amount; the bus's balance point falls past its wheel"),
    "question": "Both vehicles are tilted the same amount. The gold dot is each one's balance point. Which vehicle is about to tip over?",
    "explanation": "A vehicle tips when the dashed line from its balance point lands past its tilted wheel. The tall bus has a HIGH balance point, so it tips after only a small tilt. The low Beetle can tilt much further. (This is a simple model.)",
    "choices": [
      {"text": "The tall bus 🚌", "correct": True},
      {"text": "The low Beetle 🚗", "correct": False},
      {"text": "Neither can ever tip", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "com", "name": "Centre of mass", "icon": ICON_COM, "fact": "⚖️ The balance point of the whole vehicle. Pretend all its weight pulls down from this one spot."},
    {"id": "base", "name": "Wheel base", "icon": ICON_BASE, "fact": "🛞 The wheels set the width of the base. The vehicle stays steady while its balance point is over this base."},
    {"id": "plumb", "name": "Dashed drop line", "icon": ICON_PLUMB, "fact": "📏 Drop a line straight down from the balance point. If it lands outside the wheels, the vehicle tips."},
  ]},
  "draw": {
    "prompt": "Draw a tall bus and a low Beetle. Mark each balance point with a dot and drop a dashed line down to the ground.",
    "hintSvg": svg(300, 200,
      "<line x1='5' y1='160' x2='295' y2='160' stroke='%s' stroke-width='3'/>" % SAND
      + "<rect x='40' y='40' width='70' height='120' rx='8' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='7 5'/>" % ORANGE
      + "<rect x='160' y='112' width='110' height='48' rx='8' fill='none' stroke='%s' stroke-width='3' stroke-dasharray='7 5'/>" % ORANGE
      + com_dot(75, 100, 160) + com_dot(215, 136, 160),
      "hint: tall dotted box and low wide dotted box with balance points"),
  },
  "rotate": {
    "prompt": "Rotate the bus model. Tilt it in your mind past the point where the dashed line leaves the wheels, and it would fall over.",
    "svg": "<line x1='40' y1='222' x2='260' y2='222' stroke='%s' stroke-width='3'/>" % SAND
           + "<rect x='105' y='82' width='90' height='140' rx='10' fill='#E9A66B' stroke='%s' stroke-width='3'/>" % NAVY
           + "".join("<rect x='%d' y='96' width='20' height='22' fill='%s' stroke='%s' stroke-width='1.5'/>" % (x, BLUE, NAVY) for x in (115, 140, 165))
           + "<circle cx='125' cy='222' r='10' fill='%s'/><circle cx='175' cy='222' r='10' fill='%s'/>" % (NAVY, NAVY)
           + com_dot(150, 152, 222)
           + "<path d='M108 238 H192 M108 233 V243 M192 233 V243' stroke='%s' stroke-width='2.5' fill='none'/>" % TEAL
           + txt(150, 258, "wheel base", 11, TEAL, "middle", "bold")
  },
  "compare": {
    "question": "Tap the vehicle that is MORE stable (harder to tip over).",
    "explanation": "Low and wide is the stable recipe. A low balance point and a wide base mean you have to tilt it a LOT before the dashed line leaves the wheels.",
    "choices": [
      {"label": "A — tall and narrow", "svg": svg(200, 140,
          "<line x1='5' y1='120' x2='195' y2='120' stroke='%s' stroke-width='3'/>" % SAND
          + "<rect x='80' y='30' width='40' height='90' rx='6' fill='#E9A66B' stroke='%s' stroke-width='2'/>" % NAVY + com_dot(100, 75, 120), "tall narrow vehicle"), "correct": False},
      {"label": "B — low and wide", "svg": svg(200, 140,
          "<line x1='5' y1='120' x2='195' y2='120' stroke='%s' stroke-width='3'/>" % SAND
          + "<rect x='45' y='75' width='110' height='45' rx='8' fill='%s' stroke='%s' stroke-width='2'/>" % (BODY, NAVY) + com_dot(100, 97, 120), "low wide vehicle"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "A Beetle is low and wide: a LOW balance point", "icon": ICON_ROUND},
    {"text": "A tall bus has a HIGHER balance point", "icon": ICON_COM},
    {"text": "The bus's dashed line leaves its wheels after a smaller tilt, so it tips sooner", "icon": ICON_PLUMB},
    {"text": "🔗 Links to Titanic Buoyancy Model and Watertight Compartments: ships stay upright the same way. A low balance point and a wide base keep them steady", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "A Beetle's heavy engine is at the back, over the driving wheels. Why does that help it grip on a slippery hill? What is the downside?",
    "visualSvg": svg(200, 120, beetle_at(0.5, 22, 8, dot=True) + arrow(50, 66, 50, 100, NAVY, 3, 8) + txt(100, 114, "weight over back wheels", 9, NAVY, "middle"), "Beetle with its engine weight over the back wheels"),
    "starters": ["Weight over the back wheels means...", "The downside is the heavy tail can..."],
    "keywords": ["weight", "grip", "wheels", "tail"]
  },
  "predict": {
    "question": "Heavy luggage is piled on a bus's roof. What happens to the bus's balance point?",
    "explanation": "Heavy things up high pull the balance point UP. A higher balance point means a smaller tilt is enough to tip the bus, so roof luggage makes it less stable.",
    "choices": [
      {"text": "It moves UP, so the bus tips more easily", "correct": True},
      {"text": "It moves DOWN, so the bus is steadier", "correct": False},
      {"text": "It does not change at all", "correct": False},
    ]
  },
}
build("cars-07-centre-of-mass", "Beetle vs Bus: Centre of Mass ⚖️", c7)

# ====================== PAGE 8: BUS STOP-AND-GO GRAPHS ======================
BUS_PTS = [(40, 160), (80, 60), (140, 60), (170, 160), (210, 160), (250, 70)]
c8 = {
  "observe": {
    "svg": svg(300, 200,
      axes(40, 160, 285, 20) + poly(BUS_PTS, TEAL, 4)
      + txt(46, 16, "speed", 11, NAVY) + txt(288, 178, "time", 11, NAVY, "end")
      + txt(64, 124, "go", 10, GREEN, "start", "bold") + txt(110, 50, "cruise", 10, TEAL, "middle", "bold")
      + txt(178, 108, "brake", 10, ORANGE, "start", "bold") + txt(190, 148, "stop", 10, ORANGE, "middle", "bold") + txt(236, 118, "go", 10, GREEN, "start", "bold"),
      "Speed-time graph of a bus: speeds up, cruises, brakes, stops, then goes again"),
    "question": "This is a SPEED–time graph of a bus. Where is the bus standing still at a bus stop?",
    "explanation": "On a speed–time graph, standing still means speed is zero, so the line sits on the bottom. (Careful: on a distance–time graph, still means a flat line. Different graph, different clue!)",
    "choices": [
      {"text": "Where the line sits on zero", "correct": True},
      {"text": "Where the line goes up", "correct": False},
      {"text": "Where the line is flat high up", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "rise", "name": "Rising line", "icon": ICON_RISE, "fact": "📈 Speeding up (acceleration). The drive force is bigger than the drag."},
    {"id": "flat", "name": "Flat high line", "icon": ICON_CRUISE, "fact": "➡️ Cruising at a steady speed. The forces are balanced."},
    {"id": "zero", "name": "Line on zero", "icon": ICON_ZERO, "fact": "🛑 Speed is zero. The bus is stopped at the bus stop."},
  ]},
  "draw": {
    "prompt": "Draw a speed–time graph for a bus: speed up, cruise, brake, stop at a bus stop, then go again.",
    "hintSvg": svg(300, 200,
      axes(40, 160, 285, 20) + poly(BUS_PTS, ORANGE, 3, "6 5")
      + txt(46, 16, "speed", 11, NAVY) + txt(288, 178, "time", 11, NAVY, "end"),
      "hint: axes with a dotted go, cruise, brake, stop, go line"),
  },
  "rotate": {
    "prompt": "Rotate the graph. It looks different, but the meaning is the same. Rising means speeding up, flat at the top means cruising, falling means braking.",
    "svg": axes(50, 250, 275, 40) + poly([(50, 250), (100, 120), (170, 120), (205, 250), (235, 250), (270, 150)], TEAL, 5)
           + txt(84, 204, "go", 12, GREEN, "start", "bold") + txt(135, 108, "cruise", 12, TEAL, "middle", "bold")
           + txt(190, 185, "brake", 12, ORANGE, "start", "bold") + txt(220, 240, "stop", 12, ORANGE, "middle", "bold")
  },
  "compare": {
    "question": "Tap the graph of the bus that is braking HARD.",
    "explanation": "A steeper fall means the speed drops faster, so the brakes are working harder. The gentler fall is a bus slowing down gradually.",
    "choices": [
      {"label": "A — gentle fall", "svg": svg(200, 140,
          axes(30, 115, 185, 15) + poly([(30, 35), (170, 108)], ORANGE, 4), "gently falling line"), "correct": False},
      {"label": "B — steep fall", "svg": svg(200, 140,
          axes(30, 115, 185, 15) + poly([(30, 35), (80, 115), (170, 115)], ORANGE, 4), "steeply falling line"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "The bus pulls away from the stop: the line rises", "icon": ICON_RISE},
    {"text": "It cruises at a steady speed: the line is flat", "icon": ICON_CRUISE},
    {"text": "It brakes: speed falls (the brakes turn motion into heat, page 5)", "icon": ICON_FALL},
    {"text": "🔗 Links back to Forces on the Road (page 4), plus Mario graphs: rising = drive bigger than drag, flat = forces balanced, falling = braking wins", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "A bus is cruising at a steady speed. What does that look like on the speed–time graph, and what do the forces look like?",
    "visualSvg": svg(200, 100, axes(25, 85, 185, 10) + poly([(25, 85), (60, 35), (170, 35)], TEAL, 3) + txt(110, 28, "cruise", 10, TEAL, "middle", "bold"), "speed graph rising then flat"),
    "starters": ["A flat line means the speed is...", "So the forces are..."],
    "keywords": ["flat", "speed", "balanced", "drive"]
  },
  "predict": {
    "question": "The driver brakes GENTLY instead of hard. How does the falling part of the graph change?",
    "explanation": "Gentle braking slows the bus gradually, so the speed line falls more slowly. That makes the falling part of the graph less steep.",
    "choices": [
      {"text": "It gets gentler (less steep)", "correct": True},
      {"text": "It gets steeper", "correct": False},
      {"text": "It goes upward", "correct": False},
    ]
  },
}
build("cars-08-bus-graphs", "Bus: Stop-and-Go Graphs 🚌", c8)
print("cars batch 2 done: 4 pages")
