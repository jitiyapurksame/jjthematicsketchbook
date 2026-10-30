"""Pigeons & Doves book, batch 1 (pages 1-4) on the 8-mission engine.

Run from anywhere:  python3 build-tools/build_birds_batch1.py
Reads  engine-template-v2.html from the CURRENT folder if present, otherwise
       build-tools/engine-template-v2-source.html.
Writes birds-0N-*.html into ../deliverables (relative to this script).
Fail-loud: any missing marker or malformed data stops the build.
"""
import json, re, os, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "deliverables"))
if not os.path.isdir(OUT):
    sys.exit("deliverables/ folder not found next to build-tools/: " + OUT)

tpl_path = None
for p in (os.path.join(os.getcwd(), "engine-template-v2.html"),
          os.path.join(HERE, "engine-template-v2-source.html")):
    if os.path.exists(p):
        tpl_path = p
        break
if not tpl_path:
    sys.exit("engine template not found")
TEMPLATE = open(tpl_path, encoding="utf-8").read()
DATA_BLOCK_RE = re.compile(r"window\.CONCEPT_DATA = \{.*?\};", re.S)

REQUIRED = ["observe", "label", "draw", "rotate", "compare", "connect", "explain", "predict"]


def check(cid, data):
    for k in REQUIRED:
        assert k in data, "%s: missing mission %s" % (cid, k)
    for k in ("observe", "compare", "predict"):
        ch = data[k]["choices"]
        assert len(ch) >= 2, "%s.%s needs 2+ choices" % (cid, k)
        assert sum(1 for c in ch if c["correct"]) == 1, "%s.%s needs exactly one correct choice" % (cid, k)
    for c in data["compare"]["choices"]:
        assert c.get("svg") and c.get("label"), "%s compare choice needs svg+label" % cid
    ids = [i["id"] for i in data["label"]["items"]]
    assert len(ids) == len(set(ids)) and len(ids) >= 3, "%s label ids" % cid
    for i in data["label"]["items"]:
        assert i["icon"] and i["fact"] and i["name"], "%s label item incomplete" % cid
    assert re.search(r"<(line|path|circle|ellipse|rect|polygon)", data["draw"]["hintSvg"]), "%s empty draw hint" % cid
    assert data["rotate"]["svg"].strip(), "%s empty rotate svg" % cid
    assert data["connect"]["items"][-1]["text"].startswith("🔗"), "%s connect chain must end with a 🔗 link" % cid
    assert data["explain"]["starters"] and data["explain"]["keywords"], "%s explain chips" % cid


def build(cid, title, data):
    check(cid, data)
    html = TEMPLATE
    for old, new in [
        ('data-concept-id="theme-00-example"', 'data-concept-id="%s"' % cid),
        ("<title>[CONCEPT TITLE] — Thematic Sketchbook</title>", "<title>%s — Thematic Sketchbook</title>" % title),
        ('<h1 id="concept-title">[CONCEPT TITLE]</h1>', '<h1 id="concept-title">%s</h1>' % title),
    ]:
        assert old in html, "template marker missing: " + old
        html = html.replace(old, new)
    assert DATA_BLOCK_RE.search(html), "CONCEPT_DATA block not found"
    json_str = json.dumps(data, ensure_ascii=False)
    html = DATA_BLOCK_RE.sub(lambda m: "window.CONCEPT_DATA = " + json_str + ";", html)
    path = os.path.join(OUT, cid + ".html")
    open(path, "w", encoding="utf-8").write(html)
    print("built", cid + ".html")


# ---------------- palette + tiny SVG helpers ----------------
NAVY = "#0B2545"; ORANGE = "#D9603B"; TEAL = "#2E6E62"; GREEN = "#3F8F5C"
GOLD = "#C9A24B"; SAND = "#DCD3BC"; PG = "#8D9BAF"; PD = "#6F7F95"; NECK = "#5B8F7B"


def arrow(x1, y1, x2, y2, color, w=3, head=9):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx = x2 - head * math.cos(ang); by = y2 - head * math.sin(ang)
    px = -math.sin(ang) * head * 0.6; py = math.cos(ang) * head * 0.6
    return ("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' stroke='%s' stroke-width='%s' stroke-linecap='round'/>"
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>"
            % (x1, y1, bx, by, color, w, x2, y2, bx + px, by + py, bx - px, by - py, color))


def txt(x, y, s, size=11, color=NAVY, anchor="start", weight="normal"):
    return "<text x='%g' y='%g' font-size='%g' fill='%s' text-anchor='%s' font-weight='%s'>%s</text>" % (
        x, y, size, color, anchor, weight, s)


def svg(w, h, inner, label):
    return "<svg viewBox='0 0 %d %d' role='img' aria-label='%s'>%s</svg>" % (w, h, label, inner)


def tri_right(x, y, color, s=6):
    return "<polygon points='%g,%g %g,%g %g,%g' fill='%s'/>" % (x, y, x - s - 2, y - s + 1, x - s - 2, y + s - 1, color)


def pigeon():
    """Pigeon facing right, drawn inside roughly x 38..254, y 57..168."""
    return (
        "<g>"
        "<polygon points='92,100 40,86 38,116 92,120' fill='%s' stroke='%s' stroke-width='2'/>"
        "<ellipse cx='150' cy='105' rx='66' ry='38' fill='%s' stroke='%s' stroke-width='2'/>"
        "<circle cx='222' cy='76' r='18' fill='%s' stroke='%s' stroke-width='2'/>"
        "<ellipse cx='207' cy='92' rx='20' ry='16' fill='%s'/>"
        "<polygon points='239,74 254,78 239,82' fill='#E8D9B5' stroke='%s' stroke-width='1.5'/>"
        "<circle cx='227' cy='72' r='3' fill='%s'/>"
        "<path d='M118 96 Q152 66 198 98 Q160 128 108 120 Z' fill='%s' stroke='%s' stroke-width='2'/>"
        "<line x1='150' y1='143' x2='150' y2='168' stroke='%s' stroke-width='3'/>"
        "<line x1='170' y1='141' x2='170' y2='168' stroke='%s' stroke-width='3'/>"
        "</g>" % (PD, NAVY, PG, NAVY, PG, NAVY, NECK, NAVY, ORANGE, PD, NAVY, ORANGE, ORANGE))


def pigeon_at(scale, cx, cy):
    # pigeon centre is about (146, 112)
    tx = cx - 146 * scale; ty = cy - 112 * scale
    return "<g transform='translate(%.1f,%.1f) scale(%s)'>%s</g>" % (tx, ty, scale, pigeon())


# icons (40x40)
ICON_WING = "<svg viewBox='0 0 40 40'><path d='M5 29 Q18 3 36 13 Q22 35 5 29 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (PD, NAVY)
ICON_CHEST = ("<svg viewBox='0 0 40 40'><ellipse cx='20' cy='21' rx='14' ry='11' fill='%s' stroke='%s' stroke-width='2'/>"
              "<path d='M10 21 Q20 13 30 21 M11 26 Q20 19 29 26' fill='none' stroke='%s' stroke-width='2'/></svg>" % (ORANGE, NAVY, NAVY))
ICON_TAIL = ("<svg viewBox='0 0 40 40'><polygon points='6,20 34,7 34,33' fill='%s' stroke='%s' stroke-width='2'/>"
             "<line x1='6' y1='20' x2='34' y2='20' stroke='%s' stroke-width='1.5'/></svg>" % (PD, NAVY, NAVY))
ICON_UP = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(20, 35, 20, 6, TEAL, 4, 11)
ICON_DOWN = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(20, 5, 20, 35, NAVY, 4, 11)
ICON_RIGHT = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(5, 20, 35, 20, GREEN, 4, 11)
ICON_LEFT = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(35, 20, 5, 20, ORANGE, 4, 11)
ICON_CURVE_TOP = ("<svg viewBox='0 0 40 40'><path d='M4 30 Q20 2 36 30' fill='none' stroke='%s' stroke-width='3'/>"
                  "<line x1='4' y1='30' x2='36' y2='30' stroke='%s' stroke-width='2'/></svg>" % (TEAL, NAVY))
ICON_FLAT_UNDER = ("<svg viewBox='0 0 40 40'><line x1='4' y1='18' x2='36' y2='18' stroke='%s' stroke-width='3'/>%s%s%s</svg>"
                   % (NAVY, arrow(10, 36, 10, 24, ORANGE, 2, 6), arrow(20, 36, 20, 24, ORANGE, 2, 6), arrow(30, 36, 30, 24, ORANGE, 2, 6)))
ICON_FRONT_EDGE = ("<svg viewBox='0 0 40 40'><path d='M34 9 Q8 9 8 20 Q8 31 34 31' fill='none' stroke='%s' stroke-width='3'/>"
                   "<circle cx='8' cy='20' r='3' fill='%s'/></svg>" % (GOLD, ORANGE))
ICON_AIR_CORE = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='13' fill='#FFFFFF' stroke='%s' stroke-width='3'/>"
                 "<path d='M12 18 q4 -4 8 0 t8 0 M12 24 q4 -4 8 0 t8 0' fill='none' stroke='%s' stroke-width='1.5'/></svg>" % (NAVY, TEAL))
ICON_STRUT = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='14' fill='#FFFFFF' stroke='%s' stroke-width='3'/>"
              "<line x1='6' y1='20' x2='34' y2='20' stroke='%s' stroke-width='2'/><line x1='20' y1='6' x2='20' y2='34' stroke='%s' stroke-width='2'/>"
              "<line x1='10' y1='10' x2='30' y2='30' stroke='%s' stroke-width='2'/><line x1='30' y1='10' x2='10' y2='30' stroke='%s' stroke-width='2'/></svg>"
              % (NAVY, NAVY, NAVY, NAVY, NAVY))
ICON_WALL = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='12' fill='none' stroke='%s' stroke-width='7'/>"
             "<circle cx='20' cy='20' r='15.5' fill='none' stroke='%s' stroke-width='1.5'/><circle cx='20' cy='20' r='8.5' fill='none' stroke='%s' stroke-width='1.5'/></svg>" % (SAND, NAVY, NAVY))
ICON_LINK = ("<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='%s' stroke-width='3'/>"
             "<circle cx='26' cy='20' r='8' fill='none' stroke='%s' stroke-width='3'/></svg>" % (GOLD, GOLD))
ICON_AIR_PUSH = ("<svg viewBox='0 0 40 40'><path d='M4 14 Q20 6 36 14' fill='none' stroke='%s' stroke-width='3'/>%s</svg>" % (TEAL, arrow(20, 18, 20, 36, GOLD, 3, 8)))
ICON_DROP = "<svg viewBox='0 0 40 40'><path d='M20 5 Q34 24 20 35 Q6 24 20 5 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (TEAL, NAVY)
ICON_BIRD_DOT = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='9' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (PG, NAVY)
ICON_FEATHER = "<svg viewBox='0 0 40 40'><path d='M8 34 Q10 10 34 6 Q30 28 8 34 Z' fill='%s' stroke='%s' stroke-width='2'/><line x1='8' y1='34' x2='28' y2='12' stroke='%s' stroke-width='1.5'/></svg>" % (PG, NAVY, NAVY)

# shared shapes
TEARDROP = "M30 70 C30 30 90 25 120 40 C150 52 175 65 185 70 C175 75 150 88 120 100 C90 115 30 110 30 70 Z"
AIRFOIL = "M40,108 C45,84 90,66 150,68 C205,70 245,92 272,108 C200,112 100,114 40,108 Z"
GRID = ("<line x1='6' y1='6' x2='6' y2='6' stroke='none'/>")

# ====================== PAGE 1: SIDE VIEW ======================
c1 = {
  "observe": {
    "svg": svg(300, 200,
      pigeon()
      + "<path d='M5 60 Q150 15 295 60' fill='none' stroke='%s' stroke-width='2'/>" % TEAL
      + "<path d='M5 160 Q150 205 295 160' fill='none' stroke='%s' stroke-width='2'/>" % TEAL
      + tri_right(295, 60, TEAL) + tri_right(295, 160, TEAL)
      + txt(8, 22, "air flows past the pigeon", 11, TEAL),
      "A pigeon seen from the side with air flowing smoothly around its body"),
    "question": "Look at the pigeon's body from the side. Which smooth shape does it look most like?",
    "explanation": "A pigeon's body is a smooth teardrop: round at the front, tapered at the back. Air can slide around the round front and close up neatly behind. Scientists call this shape streamlined.",
    "choices": [
      {"text": "A teardrop 💧: round front, tapered back", "correct": True},
      {"text": "A flat board 🟫", "correct": False},
      {"text": "A spiky star ⭐", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "chest", "name": "Chest muscle", "icon": ICON_CHEST, "fact": "💪 The big chest muscle is the flapping engine. It is a BIG slice of the pigeon's weight."},
    {"id": "wing", "name": "Wing", "icon": ICON_WING, "fact": "🪶 Wings push air down and back when they flap. That gives the pigeon lift and thrust."},
    {"id": "tail", "name": "Tail", "icon": ICON_TAIL, "fact": "🎛️ The tail fans out to steer, and spreads wide like a brake when landing."},
  ]},
  "draw": {
    "prompt": "Draw a pigeon from the side. Start with a teardrop body, then add a small head, a tail and a wing.",
    "hintSvg": svg(300, 200,
      "<path d='M50,100 C90,62 170,54 214,88 C206,132 110,146 50,112 Z' fill='none' stroke='%s' stroke-width='3'/>" % ORANGE
      + "<circle cx='226' cy='76' r='16' fill='none' stroke='%s' stroke-width='3'/>" % ORANGE
      + "<path d='M110 100 Q150 72 195 100' fill='none' stroke='%s' stroke-width='3'/>" % TEAL
      + "<polygon points='54,100 26,88 26,114 54,111' fill='none' stroke='%s' stroke-width='3'/>" % NAVY
      + txt(70, 175, "teardrop body + head + wing + tail", 11, NAVY),
      "hint: teardrop body with head, wing and tail"),
  },
  "rotate": {
    "prompt": "Rotate the pigeon. Turn it up, down, even upside down. Is the teardrop still a teardrop? Same shape, new direction.",
    "svg": "<g transform='translate(8,70) scale(0.95)'>" + pigeon() + "</g>"
           + arrow(70, 270, 250, 270, GOLD, 4, 10) + txt(150, 290, "flying direction", 11, NAVY, "middle")
  },
  "compare": {
    "question": "Wind blows from the left. Tap the shape that lets air slide past most easily.",
    "explanation": "The teardrop is smooth, so air flows around it and closes up behind. The flat board makes the air crash and swirl. Swirls mean more drag, which is a push backwards.",
    "choices": [
      {"label": "A — teardrop", "svg": svg(200, 140,
          "<path d='%s' fill='%s' stroke='%s' stroke-width='2'/>" % (TEARDROP, PG, NAVY) + arrow(2, 70, 26, 70, TEAL, 3, 8),
          "teardrop shape"), "correct": True},
      {"label": "B — flat board", "svg": svg(200, 140,
          "<rect x='100' y='25' width='14' height='90' fill='%s' stroke='%s' stroke-width='2'/>" % (SAND, NAVY) + arrow(40, 70, 96, 70, TEAL, 3, 8)
          + "<path d='M122 45 q14 -10 8 2 q-8 10 8 16 q14 6 4 18 q-8 8 6 14' fill='none' stroke='%s' stroke-width='2'/>" % ORANGE,
          "flat board with swirling air behind it"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "A pigeon pushes through the air as it flies", "icon": ICON_BIRD_DOT},
    {"text": "The air has to flow around its body", "icon": ICON_AIR_PUSH},
    {"text": "A smooth teardrop lets air slide past: less drag", "icon": ICON_DROP},
    {"text": "🔗 Links to Titanic Hull Shape: ships are streamlined too. Water slides around a hull the way air slides around a pigeon", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why is a smooth, tapered body good for a bird that flies fast?",
    "visualSvg": svg(200, 100,
      "<g transform='translate(35,15) scale(0.7)'><path d='%s' fill='%s' stroke='%s' stroke-width='2'/></g>" % (TEARDROP, PG, NAVY)
      + arrow(4, 50, 30, 50, TEAL, 3, 8),
      "teardrop with air arrow"),
    "starters": ["A teardrop body lets the air...", "Less drag means..."],
    "keywords": ["air", "drag", "smooth", "teardrop"]
  },
  "predict": {
    "question": "A pigeon fluffs its feathers into a big, rough ball while flying. What happens?",
    "explanation": "A rough, puffed-up shape makes the air tumble and swirl instead of sliding past. That is more drag, so the pigeon has to work harder to keep its speed.",
    "choices": [
      {"text": "More drag: the air can't slide past easily", "correct": True},
      {"text": "Less drag: it slips through the air faster", "correct": False},
      {"text": "Nothing changes at all", "correct": False},
    ]
  },
}
build("birds-01-side-view", "Pigeon: Side View 🕊️", c1)

# ====================== PAGE 2: WING CROSS SECTION ======================
FLOW_TOP = "M5 80 C60 60 110 40 150 42 C200 44 250 70 295 80"
FLOW_BOT = "M5 130 C100 140 200 140 295 130"
c2 = {
  "observe": {
    "svg": svg(300, 200,
      "<path d='%s' fill='%s' stroke='%s' stroke-width='2'/>" % (AIRFOIL, PG, NAVY)
      + "<path d='%s' fill='none' stroke='%s' stroke-width='2'/>" % (FLOW_TOP, TEAL)
      + "<path d='%s' fill='none' stroke='%s' stroke-width='2'/>" % (FLOW_BOT, TEAL)
      + tri_right(295, 80, TEAL) + tri_right(295, 130, TEAL)
      + txt(8, 22, "faster air = lower pressure", 10, TEAL)
      + txt(8, 172, "slower air = higher pressure", 10, TEAL),
      "A slice through a wing with air flowing over the curved top and under the flatter bottom"),
    "question": "Air flows left to right past this wing slice. Which way does the wing get pushed?",
    "explanation": "The curved top speeds the air up, so pressure above the wing drops. The wing also pushes air DOWN, and the air pushes back UP. Lower pressure on top plus higher pressure below gives a push up. That push is called lift.",
    "choices": [
      {"text": "UP ⬆️", "correct": True},
      {"text": "DOWN ⬇️", "correct": False},
      {"text": "Backward ⬅️", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "top", "name": "Curved top", "icon": ICON_CURVE_TOP, "fact": "🌊 Air speeds up as it flows over the curve. Fast air means lower pressure up here."},
    {"id": "under", "name": "Flatter underside", "icon": ICON_FLAT_UNDER, "fact": "⬆️ Air under the wing is slower, so its pressure stays higher. It pushes the wing up."},
    {"id": "front", "name": "Rounded front edge", "icon": ICON_FRONT_EDGE, "fact": "👃 The round front splits the air: some goes over the top, some goes underneath."},
  ]},
  "draw": {
    "prompt": "Draw a wing slice: curved on top, flatter underneath. Add air arrows going over the top and under the bottom.",
    "hintSvg": svg(300, 200,
      "<path d='%s' fill='none' stroke='%s' stroke-width='3'/>" % (AIRFOIL, ORANGE)
      + "<path d='%s' fill='none' stroke='%s' stroke-width='2'/>" % (FLOW_TOP, TEAL)
      + "<path d='%s' fill='none' stroke='%s' stroke-width='2'/>" % (FLOW_BOT, TEAL)
      + tri_right(295, 80, TEAL) + tri_right(295, 130, TEAL),
      "hint: wing slice with air arrows over and under"),
  },
  "rotate": {
    "prompt": "Rotate the wing a half turn, 180°. Watch the lift arrow. It now points DOWN! A race car's wing works this way: it presses the car onto the road.",
    "svg": "<g transform='translate(0,90)'><path d='%s' fill='%s' stroke='%s' stroke-width='2'/></g>" % (AIRFOIL, PG, NAVY)
           + arrow(156, 152, 156, 98, ORANGE, 4, 11) + txt(166, 112, "lift", 12, ORANGE, "start", "bold")
  },
  "compare": {
    "question": "Tap the wing slice that is shaped like a pigeon's wing.",
    "explanation": "A pigeon's wing is curved on top and flatter underneath. That curve is what speeds up the air over the top and helps the wing push air downward.",
    "choices": [
      {"label": "A — curved top", "svg": svg(200, 140,
          "<g transform='translate(5,25) scale(0.7)'><path d='%s' fill='%s' stroke='%s' stroke-width='2.5'/></g>" % (AIRFOIL, PG, NAVY)
          + arrow(2, 30, 26, 30, TEAL, 3, 8), "curved top wing slice"), "correct": True},
      {"label": "B — flat plank", "svg": svg(200, 140,
          "<rect x='30' y='62' width='150' height='12' fill='%s' stroke='%s' stroke-width='2'/>" % (SAND, NAVY)
          + arrow(2, 30, 26, 30, TEAL, 3, 8), "flat plank"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "The wing is curved on top and flatter below", "icon": ICON_CURVE_TOP},
    {"text": "Air speeds up as it flows over the curve", "icon": ICON_AIR_PUSH},
    {"text": "Faster air means LOWER pressure above the wing", "icon": ICON_DROP},
    {"text": "Lower pressure above + higher pressure below = a push UP (lift)", "icon": ICON_UP},
    {"text": "🔗 Links to Titanic Pressure Map: a pressure difference always makes a push. Water pushes a hull the same way air pushes a wing", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does a pigeon spread its wings wide just before landing?",
    "visualSvg": svg(200, 100,
      "<g transform='translate(45,5) scale(0.5)'><path d='%s' fill='%s' stroke='%s' stroke-width='3'/></g>" % (AIRFOIL, PG, NAVY)
      + arrow(80, 50, 80, 90, GOLD, 3, 8) + arrow(110, 50, 110, 90, GOLD, 3, 8) + arrow(140, 50, 140, 90, GOLD, 3, 8),
      "wing pushing air downward"),
    "starters": ["Wide wings catch more air, so...", "Tilting the wings makes..."],
    "keywords": ["air", "slow", "drag", "lift"]
  },
  "predict": {
    "question": "A pigeon flaps its wing so lots of air is pushed DOWN. What happens to the pigeon?",
    "explanation": "When the wing pushes air down, the air pushes back on the wing, up. Push down on the air, get pushed up. It is the same idea as pushing off a wall to roll backwards.",
    "choices": [
      {"text": "It gets pushed UP", "correct": True},
      {"text": "It gets pushed DOWN", "correct": False},
      {"text": "Nothing happens to it", "correct": False},
    ]
  },
}
build("birds-02-wing-cross-section", "Pigeon: Wing Cross Section 🌬️", c2)

# ====================== PAGE 3: FORCES IN FLIGHT ======================
c3 = {
  "observe": {
    "svg": svg(300, 220,
      pigeon_at(0.45, 150, 110)
      + arrow(150, 80, 150, 24, TEAL, 4, 11) + txt(158, 34, "Lift", 12, TEAL, "start", "bold")
      + arrow(150, 140, 150, 196, NAVY, 4, 11) + txt(158, 196, "Weight", 12, NAVY, "start", "bold")
      + arrow(205, 110, 275, 110, GREEN, 4, 11) + txt(222, 100, "Thrust", 12, GREEN, "start", "bold")
      + arrow(97, 110, 27, 110, ORANGE, 4, 11) + txt(30, 100, "Drag", 12, ORANGE, "start", "bold"),
      "A pigeon with four force arrows: lift up, weight down, thrust forward, drag back, all balanced"),
    "question": "The pigeon is flying straight and level at a steady speed. What do the equal arrows tell you?",
    "explanation": "Equal arrows in opposite directions cancel out. Lift balances weight, and thrust balances drag. Balanced forces mean the pigeon keeps cruising smoothly, with no change in speed or height.",
    "choices": [
      {"text": "The forces are balanced, so it cruises steadily", "correct": True},
      {"text": "Lift is bigger, so it is climbing fast", "correct": False},
      {"text": "There are no forces on it", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "lift", "name": "Lift", "icon": ICON_UP, "fact": "⬆️ Lift pushes the pigeon UP. It comes from air flowing over the wings."},
    {"id": "weight", "name": "Weight", "icon": ICON_DOWN, "fact": "⬇️ Weight is gravity pulling the pigeon DOWN toward the ground."},
    {"id": "thrust", "name": "Thrust", "icon": ICON_RIGHT, "fact": "➡️ Thrust pushes the pigeon FORWARD. Flapping makes it."},
    {"id": "drag", "name": "Drag", "icon": ICON_LEFT, "fact": "⬅️ Drag is air pushing BACK against the pigeon. A teardrop body keeps it small."},
  ]},
  "draw": {
    "prompt": "Draw the pigeon as a simple dot. Add 4 arrows: lift up, weight down, thrust forward, drag back.",
    "hintSvg": svg(300, 200,
      "<circle cx='150' cy='100' r='14' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
      + arrow(150, 80, 150, 24, TEAL, 3, 10) + txt(158, 34, "lift", 11, TEAL)
      + arrow(150, 120, 150, 176, NAVY, 3, 10) + txt(158, 176, "weight", 11, NAVY)
      + arrow(170, 100, 250, 100, GREEN, 3, 10) + txt(205, 90, "thrust", 11, GREEN)
      + arrow(130, 100, 50, 100, ORANGE, 3, 10) + txt(52, 90, "drag", 11, ORANGE),
      "hint: dot with four arrows"),
  },
  "rotate": {
    "prompt": "Rotate the force picture. The arrows turn, but the balance stays the same. Equal arrows pointing opposite ways still cancel out.",
    "svg": "<circle cx='150' cy='150' r='14' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
           + arrow(150, 130, 150, 62, TEAL, 4, 11) + txt(158, 76, "lift", 12, TEAL, "start", "bold")
           + arrow(150, 170, 150, 238, NAVY, 4, 11) + txt(158, 236, "weight", 12, NAVY, "start", "bold")
           + arrow(172, 150, 240, 150, GREEN, 4, 11) + txt(196, 140, "thrust", 12, GREEN, "start", "bold")
           + arrow(128, 150, 60, 150, ORANGE, 4, 11) + txt(62, 140, "drag", 12, ORANGE, "start", "bold")
  },
  "compare": {
    "question": "Tap the picture where the pigeon is speeding up.",
    "explanation": "When thrust is bigger than drag, the forces are not balanced. A leftover push goes forward, so the pigeon speeds up. Equal arrows mean steady speed.",
    "choices": [
      {"label": "A — thrust is bigger", "svg": svg(200, 140,
          "<circle cx='100' cy='75' r='10' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
          + arrow(112, 75, 192, 75, GREEN, 4, 10) + arrow(88, 75, 60, 75, ORANGE, 4, 10)
          + txt(130, 62, "thrust", 10, GREEN) + txt(40, 62, "drag", 10, ORANGE),
          "long thrust arrow, short drag arrow"), "correct": True},
      {"label": "B — thrust = drag", "svg": svg(200, 140,
          "<circle cx='100' cy='75' r='10' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
          + arrow(112, 75, 160, 75, GREEN, 4, 10) + arrow(88, 75, 40, 75, ORANGE, 4, 10)
          + txt(120, 62, "thrust", 10, GREEN) + txt(40, 62, "drag", 10, ORANGE),
          "equal thrust and drag arrows"), "correct": False},
    ]
  },
  "connect": {"items": [
    {"text": "The pigeon flaps its wings", "icon": ICON_WING},
    {"text": "The wings push air down and back", "icon": ICON_AIR_PUSH},
    {"text": "The air pushes the pigeon up and forward: lift + thrust", "icon": ICON_UP},
    {"text": "🔗 Links to Titanic Free Body Diagram: the ship's buoyancy arrow balances its weight, just like lift balances weight for the pigeon", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "If a pigeon stops flapping, which force disappears? What happens next?",
    "visualSvg": svg(200, 100,
      "<circle cx='100' cy='50' r='10' fill='%s' stroke='%s' stroke-width='2'/>" % (PG, NAVY)
      + arrow(88, 50, 40, 50, ORANGE, 4, 10) + txt(30, 38, "drag", 11, ORANGE)
      + txt(112, 38, "thrust?", 11, GREEN),
      "bird with only a drag arrow"),
    "starters": ["Without flapping, thrust is...", "Then drag will..."],
    "keywords": ["thrust", "drag", "slow", "sink"]
  },
  "predict": {
    "question": "Thrust becomes bigger than drag. What happens to the pigeon's speed?",
    "explanation": "Unbalanced forces change motion. Extra push forward means the pigeon speeds up, until drag grows and balances the thrust again.",
    "choices": [
      {"text": "It speeds up", "correct": True},
      {"text": "It slows down", "correct": False},
      {"text": "It stays exactly the same", "correct": False},
    ]
  },
}
build("birds-03-forces-in-flight", "Pigeon: Forces in Flight ⚖️", c3)

# ====================== PAGE 4: HOLLOW BONES ======================
def bone_slice(cx, cy, r_out, r_in, hollow=True, marker=False):
    s = "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='2.5'/>" % (cx, cy, r_out, SAND, NAVY)
    if hollow:
        s += "<circle cx='%g' cy='%g' r='%g' fill='#FFFFFF' stroke='%s' stroke-width='2'/>" % (cx, cy, r_in, NAVY)
        k = r_in * 0.707
        s += ("<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2.5'/>" % (cx - r_in, cy, cx + r_in, cy, NAVY)
              + "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2.5'/>" % (cx, cy - r_in, cx, cy + r_in, NAVY)
              + "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2'/>" % (cx - k, cy - k, cx + k, cy + k, NAVY)
              + "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='2'/>" % (cx + k, cy - k, cx - k, cy + k, NAVY))
    if marker:
        s += "<circle cx='%g' cy='%g' r='7' fill='%s' stroke='%s' stroke-width='2'/>" % (cx, cy - (r_out + r_in) / 2, GOLD, NAVY)
    return s


def dots(coords):
    return "".join("<circle cx='%g' cy='%g' r='6' fill='%s'/>" % (x, y, NAVY) for x, y in coords)


BOX = "<rect x='40' y='25' width='120' height='90' fill='#FFFFFF' stroke='%s' stroke-width='2.5'/>" % NAVY
c4 = {
  "observe": {
    "svg": svg(300, 180,
      bone_slice(80, 85, 45, 0, hollow=False)
      + bone_slice(220, 85, 45, 33, hollow=True)
      + txt(80, 155, "solid bone", 11, NAVY, "middle")
      + txt(220, 155, "hollow bone + struts", 11, NAVY, "middle"),
      "End view of a solid bone next to a hollow bone with tiny struts inside"),
    "question": "Both bone slices are the same width. Which bone is lighter?",
    "explanation": "The hollow bone has air where the solid bone has material. Less material in the same space means less mass, so the hollow bone is lighter. The tiny struts keep it strong.",
    "choices": [
      {"text": "The hollow bone with struts", "correct": True},
      {"text": "The solid bone", "correct": False},
      {"text": "They weigh the same", "correct": False},
    ]
  },
  "label": {"items": [
    {"id": "air", "name": "Air space", "icon": ICON_AIR_CORE, "fact": "💨 Air inside means less mass in the same space. That is a LOWER density. (Many bird bones are hollow like this.)"},
    {"id": "struts", "name": "Tiny struts", "icon": ICON_STRUT, "fact": "🏗️ Tiny cross-braces stop the tube from snapping. Light but strong!"},
    {"id": "wall", "name": "Thin bone wall", "icon": ICON_WALL, "fact": "🦴 The thin hard wall takes the pushing and pulling when the wing flaps."},
  ]},
  "draw": {
    "prompt": "Draw the end of a hollow bone: a thick ring with 3 or 4 tiny struts across the middle.",
    "hintSvg": svg(300, 200, bone_slice(150, 100, 62, 46, hollow=True) + txt(150, 190, "ring + struts", 11, NAVY, "middle"),
      "hint: ring with struts"),
  },
  "rotate": {
    "prompt": "Rotate the bone slice. The gold dot turns, but the ring with its struts looks almost the same from every side. It is strong in all directions!",
    "svg": bone_slice(150, 150, 95, 72, hollow=True, marker=True)
  },
  "compare": {
    "question": "Both boxes are the same size. Each dot is a bit of material. Tap the box with the LOWER density.",
    "explanation": "Density = mass ÷ volume. Same size box means same volume. Fewer dots means less mass, so the density is lower.",
    "choices": [
      {"label": "A — packed with dots", "svg": svg(200, 140,
          BOX + dots([(65, 50), (100, 50), (135, 50), (65, 70), (100, 70), (135, 70), (65, 92), (100, 92), (135, 92)]),
          "box packed with nine dots"), "correct": False},
      {"label": "B — only a few dots", "svg": svg(200, 140,
          BOX + dots([(70, 70), (130, 70)]), "box with two dots"), "correct": True},
    ]
  },
  "connect": {"items": [
    {"text": "A hollow bone has an air core", "icon": ICON_AIR_CORE},
    {"text": "Less material fills the same space", "icon": ICON_WALL},
    {"text": "Less mass for the same volume = lower density", "icon": ICON_DROP},
    {"text": "🔗 Links to Titanic Mass–Volume–Density: a ship's hull is mostly air too. Same density idea. The ship floats, the pigeon flies", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why is a bird with hollow bones easier to lift into the air than a bird with solid bones of the same size?",
    "visualSvg": svg(200, 100,
      bone_slice(60, 50, 32, 24, hollow=True) + txt(115, 45, "light", 12, TEAL, "start", "bold") + txt(115, 63, "+ strong", 12, TEAL, "start", "bold"),
      "hollow bone with the words light and strong"),
    "starters": ["Hollow bones have less mass, so...", "Lower density means..."],
    "keywords": ["mass", "density", "light", "strong"]
  },
  "predict": {
    "question": "A pigeon's bone is filled in until it is solid, but it stays the same size. What happens to its density?",
    "explanation": "Same size means same volume, but now there is more material inside, so more mass. More mass in the same volume means higher density.",
    "choices": [
      {"text": "Density goes UP", "correct": True},
      {"text": "Density goes DOWN", "correct": False},
      {"text": "Density stays the same", "correct": False},
    ]
  },
}
build("birds-04-hollow-bones", "Pigeon: Hollow Bones 🦴", c4)
print("batch 1 done: 4 pages")
