import json, re

TEMPLATE = open("engine-template-v2.html", encoding="utf-8").read()

DATA_BLOCK_RE = re.compile(
    r"window\.CONCEPT_DATA = \{.*?\};",
    re.S
)

def build(concept_id, title, data):
    html = TEMPLATE
    html = html.replace('data-concept-id="theme-00-example"', 'data-concept-id="%s"' % concept_id)
    html = html.replace("<title>[CONCEPT TITLE] — Thematic Sketchbook</title>", "<title>%s — Thematic Sketchbook</title>" % title)
    html = html.replace('<h1 id="concept-title">[CONCEPT TITLE]</h1>', '<h1 id="concept-title">%s</h1>' % title)
    json_str = json.dumps(data, ensure_ascii=False)
    html = DATA_BLOCK_RE.sub(lambda m: "window.CONCEPT_DATA = " + json_str + ";", html)
    return html

# ---------------- shared small icons ----------------
ICON_ARROW_UP = "<svg viewBox='0 0 40 40'><line x1='20' y1='34' x2='20' y2='8' stroke='#2E6E62' stroke-width='4'/><path d='M10 16 L20 4 L30 16 Z' fill='#2E6E62'/></svg>"
ICON_ARROW_DOWN = "<svg viewBox='0 0 40 40'><line x1='20' y1='6' x2='20' y2='32' stroke='#D9603B' stroke-width='4'/><path d='M10 24 L20 36 L30 24 Z' fill='#D9603B'/></svg>"
ICON_TRIANGLE_BOW = "<svg viewBox='0 0 40 40'><path d='M6 8 L6 32 L34 20 Z' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_WAVE = "<svg viewBox='0 0 40 40'><path d='M4 24 Q10 16 16 24 T28 24 T40 24' fill='none' stroke='#2E6E62' stroke-width='3'/><path d='M4 32 Q10 24 16 32 T28 32 T40 32' fill='none' stroke='#2E6E62' stroke-width='2' opacity='0.6'/></svg>"
ICON_SPEED = "<svg viewBox='0 0 40 40'><line x1='4' y1='14' x2='28' y2='14' stroke='#C9A24B' stroke-width='3'/><line x1='4' y1='22' x2='34' y2='22' stroke='#C9A24B' stroke-width='3'/><line x1='4' y1='30' x2='22' y2='30' stroke='#C9A24B' stroke-width='3'/></svg>"
ICON_RULER = "<svg viewBox='0 0 40 40'><rect x='4' y='16' width='32' height='8' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><line x1='12' y1='16' x2='12' y2='24' stroke='#0B2545'/><line x1='20' y1='16' x2='20' y2='24' stroke='#0B2545'/><line x1='28' y1='16' x2='28' y2='24' stroke='#0B2545'/></svg>"
ICON_SHRINK = "<svg viewBox='0 0 40 40'><path d='M6 6 L16 16 M6 6 L6 14 M6 6 L14 6' stroke='#2E6E62' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M34 34 L24 24 M34 34 L34 26 M34 34 L26 34' stroke='#2E6E62' stroke-width='3' fill='none' stroke-linecap='round'/></svg>"
ICON_SHIP_SMALL = "<svg viewBox='0 0 40 40'><path d='M8 24 L32 24 L28 32 L12 32 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><rect x='16' y='10' width='6' height='14' fill='#D9603B'/></svg>"
ICON_STEEL = "<svg viewBox='0 0 40 40'><rect x='6' y='10' width='28' height='20' rx='2' fill='#DCD3BC' stroke='#0B2545' stroke-width='2'/><circle cx='12' cy='16' r='2' fill='#0B2545'/><circle cx='28' cy='16' r='2' fill='#0B2545'/><circle cx='12' cy='24' r='2' fill='#0B2545'/><circle cx='28' cy='24' r='2' fill='#0B2545'/></svg>"
ICON_CLOUD = "<svg viewBox='0 0 40 40'><ellipse cx='16' cy='22' rx='10' ry='7' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><ellipse cx='26' cy='20' rx='8' ry='6' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_BOX = "<svg viewBox='0 0 40 40'><rect x='8' y='12' width='24' height='20' fill='#F3EEE1' stroke='#C9A24B' stroke-width='2'/><line x1='8' y1='20' x2='32' y2='20' stroke='#C9A24B' stroke-width='2'/></svg>"
ICON_BALANCE = "<svg viewBox='0 0 40 40'><line x1='20' y1='8' x2='20' y2='30' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='16' x2='34' y2='16' stroke='#0B2545' stroke-width='2'/><circle cx='6' cy='22' r='5' fill='none' stroke='#2E6E62' stroke-width='2'/><circle cx='34' cy='22' r='5' fill='none' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_EQUALS = "<svg viewBox='0 0 40 40'><line x1='8' y1='16' x2='32' y2='16' stroke='#0B2545' stroke-width='4'/><line x1='8' y1='26' x2='32' y2='26' stroke='#0B2545' stroke-width='4'/></svg>"
ICON_GRID = "<svg viewBox='0 0 80 60'><rect x='8' y='10' width='64' height='40' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><line x1='30' y1='10' x2='30' y2='50' stroke='#2E6E62'/><line x1='50' y1='10' x2='50' y2='50' stroke='#2E6E62'/></svg>"
ICON_LENGTH_ARROW = "<svg viewBox='0 0 80 60'><line x1='10' y1='30' x2='70' y2='30' stroke='#0B2545' stroke-width='3'/><path d='M10 24 L4 30 L10 36 Z' fill='#0B2545'/><path d='M70 24 L76 30 L70 36 Z' fill='#0B2545'/></svg>"
ICON_WIDTH_ARROW = "<svg viewBox='0 0 80 60'><line x1='40' y1='8' x2='40' y2='52' stroke='#D9603B' stroke-width='3'/><path d='M34 8 L40 2 L46 8 Z' fill='#D9603B'/><path d='M34 52 L40 58 L46 52 Z' fill='#D9603B'/></svg>"
ICON_DASHLINE = "<svg viewBox='0 0 80 60'><line x1='8' y1='30' x2='72' y2='30' stroke='#2E6E62' stroke-width='2' stroke-dasharray='6 4'/></svg>"
ICON_FUNNEL = "<svg viewBox='0 0 80 60'><rect x='34' y='10' width='12' height='30' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><rect x='10' y='40' width='60' height='12' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_HULL = "<svg viewBox='0 0 80 60'><path d='M6 20 L74 20 L64 44 L16 44 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_STERN = "<svg viewBox='0 0 80 60'><path d='M8 10 L8 50 Q60 40 72 30 Q60 20 8 10 Z' fill='#FBEAE3' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_DECKS = "<svg viewBox='0 0 80 60'><rect x='8' y='10' width='64' height='10' fill='#F3EEE1' stroke='#0B2545'/><rect x='8' y='24' width='64' height='10' fill='#F3EEE1' stroke='#0B2545'/><rect x='8' y='38' width='64' height='10' fill='#F3EEE1' stroke='#0B2545'/></svg>"
ICON_PROPELLER = "<svg viewBox='0 0 80 60'><circle cx='40' cy='30' r='4' fill='#0B2545'/><path d='M40 30 L20 12 M40 30 L60 12 M40 30 L20 48 M40 30 L60 48' stroke='#0B2545' stroke-width='3'/></svg>"

# ================= CONCEPT 1: SIDE VIEW =================
c1_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 200" role="img" aria-label="Titanic side view with bow, stern, funnels and hull">
      <path d="M20 140 Q10 150 20 160 L370 160 Q390 150 380 130 L360 120 L60 120 Q30 120 20 140 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <rect x="70" y="80" width="220" height="42" fill="#EAF3F0" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="100" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="150" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="200" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="250" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <circle cx="365" cy="150" r="9" fill="none" stroke="#0B2545" stroke-width="1.5"/>
      <text x="200" y="185" text-anchor="middle" font-size="12" fill="#2E6E62">bow (left) → stern (right)</text>
    </svg>''',
    "question": "Which end of the ship is pointed?",
    "explanation": "The bow's pointed shape lets it slice through water with less resistance than a flat front would.",
    "choices": [
      {"text": "The bow (front)", "correct": True},
      {"text": "The stern (back)", "correct": False},
      {"text": "Both ends are the same shape", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"bow","name":"Bow","icon":ICON_TRIANGLE_BOW,"fact":"The bow is the pointed front — it slices through the water."},
    {"id":"stern","name":"Stern","icon":ICON_STERN,"fact":"The stern is the back of the ship — it holds the propellers."},
    {"id":"hull","name":"Hull","icon":ICON_HULL,"fact":"The hull is the ship's outer body — it keeps water out."},
    {"id":"funnels","name":"Funnels","icon":ICON_FUNNEL,"fact":"Funnels let smoke and steam escape from the engines below."},
    {"id":"decks","name":"Decks","icon":ICON_DECKS,"fact":"Decks are the floors, stacked one on top of another."},
    {"id":"propellers","name":"Propellers","icon":ICON_PROPELLER,"fact":"Propellers spin underwater to push the ship forward."},
  ]},
  "draw": {
    "prompt": "Grab your pen. Draw the ship from the side — bow, stern, hull, funnels, and decks. Don't peek at the hint until you've tried!",
    "hintSvg": '''<svg viewBox="0 0 400 200" role="img" aria-label="hint">
      <path d="M20 140 Q10 150 20 160 L370 160 Q390 150 380 130 L360 120 L60 120 Q30 120 20 140 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <rect x="70" y="80" width="220" height="42" fill="#EAF3F0" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="100" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="150" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="200" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="250" y="35" width="16" height="48" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Spin the ship and check: does it still look the same shape upside down?",
    "svg": '''<path d="M40 120 Q30 130 40 140 L260 140 Q275 130 268 115 L250 105 L70 105 Q45 105 40 120 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <rect x="90" y="75" width="16" height="35" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="130" y="75" width="16" height="35" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="170" y="75" width="16" height="35" fill="#D9603B" stroke="#0B2545" stroke-width="1.5"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows the BOW (the pointed front).",
    "explanation": "A pointed shape meets less water resistance than a rounded one — that's why it's at the front.",
    "choices": [
      {"label":"A — pointed", "svg": '''<svg viewBox="0 0 200 160"><path d="M20 140 L20 40 Q100 20 180 80 Q100 100 20 140 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — rounded", "svg": '''<svg viewBox="0 0 200 160"><path d="M20 40 L20 140 Q120 150 180 100 Q140 60 20 40 Z" fill="#FBEAE3" stroke="#D9603B" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Pointed bow", "icon": ICON_TRIANGLE_BOW},
    {"text":"Cuts through water easily", "icon": ICON_WAVE},
    {"text":"Less drag, more speed", "icon": ICON_SPEED},
  ]},
  "explain": {
    "prompt": "Why do you think the front of the ship is pointed instead of flat like the back?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M10 70 L10 30 Q90 15 180 50 Q90 60 10 70 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/></svg>''',
    "starters": ["I think the bow is pointed because...", "This is a bit like..."],
    "keywords": ["water", "drag", "speed", "pointed"]
  },
  "predict": {
    "question": "If a ship had a completely flat, square front instead of a pointed bow, what would happen?",
    "explanation": "More flat surface pushing straight into the water means more drag, so more engine power is needed for the same speed.",
    "choices": [
      {"text": "It would go faster", "correct": False},
      {"text": "It would push more water and go slower", "correct": True},
      {"text": "Nothing would change", "correct": False},
    ]
  }
}

open("titanic-01-side-view.html", "w", encoding="utf-8").write(build("titanic-01-side-view", "Titanic: Side View", c1_data))
print("built titanic-01-side-view.html")

# ================= CONCEPT 2: TOP VIEW =================
c2_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 180" role="img" aria-label="Titanic top view, long and narrow, with a centerline">
      <path d="M20 90 Q40 60 120 60 L320 60 Q380 70 380 90 Q380 110 320 120 L120 120 Q40 120 20 90 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/>
      <line x1="20" y1="90" x2="380" y2="90" stroke="#0B2545" stroke-width="1" stroke-dasharray="4 4"/>
      <line x1="150" y1="60" x2="150" y2="120" stroke="#D9603B" stroke-width="1.5"/>
      <line x1="250" y1="60" x2="250" y2="120" stroke="#D9603B" stroke-width="1.5"/>
      <text x="200" y="145" text-anchor="middle" font-size="12" fill="#2E6E62">length: long | width: narrow</text>
    </svg>''',
    "question": "Looking from above, which is bigger on this ship?",
    "explanation": "Ships are built long and narrow because that shape moves through water more efficiently than a short, wide one.",
    "choices": [
      {"text": "The length (front to back)", "correct": True},
      {"text": "The width (side to side)", "correct": False},
      {"text": "They are exactly equal", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"length","name":"Length","icon":ICON_LENGTH_ARROW,"fact":"Length is the distance from bow to stern — Titanic was about 269 metres long!"},
    {"id":"width","name":"Width","icon":ICON_WIDTH_ARROW,"fact":"Width (or beam) is the distance across the ship, side to side."},
    {"id":"centerline","name":"Centerline","icon":ICON_DASHLINE,"fact":"The centerline splits the ship into two matching halves — that's symmetry."},
    {"id":"compartments","name":"Compartments","icon":ICON_GRID,"fact":"Compartments are sections dividing the inside of the ship, like rooms in a house."},
  ]},
  "draw": {
    "prompt": "Draw the ship from directly above. Mark the length, the width, and a dashed centerline down the middle.",
    "hintSvg": '''<svg viewBox="0 0 400 180" role="img" aria-label="hint">
      <path d="M20 90 Q40 60 120 60 L320 60 Q380 70 380 90 Q380 110 320 120 L120 120 Q40 120 20 90 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/>
      <line x1="20" y1="90" x2="380" y2="90" stroke="#0B2545" stroke-width="1" stroke-dasharray="4 4"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the top view 90°. Does it still look symmetric — same on both halves?",
    "svg": '''<path d="M20 90 Q35 65 100 65 L240 65 Q285 75 285 90 Q285 105 240 115 L100 115 Q35 115 20 90 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/>
      <line x1="20" y1="90" x2="285" y2="90" stroke="#0B2545" stroke-width="1" stroke-dasharray="4 4"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows the LEFT half of the ship.",
    "explanation": "The centerline splits the ship exactly in half — left and right are mirror images of each other.",
    "choices": [
      {"label":"A — left half", "svg": '''<svg viewBox="0 0 200 160"><path d="M20 80 Q30 55 90 55 L180 55 L180 105 L90 105 Q30 105 20 80 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — right half", "svg": '''<svg viewBox="0 0 200 160"><path d="M180 80 Q170 55 110 55 L20 55 L20 105 L110 105 Q170 105 180 80 Z" fill="#FBEAE3" stroke="#D9603B" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Real ship: 269 m long", "icon": ICON_RULER},
    {"text":"Scale it down 1:1000", "icon": ICON_SHRINK},
    {"text":"Model: 26.9 cm long", "icon": ICON_SHIP_SMALL},
  ]},
  "explain": {
    "prompt": "Why do you think ship builders make both sides of a ship match exactly (symmetric)?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M10 50 Q20 30 60 30 L160 30 Q190 38 190 50 Q190 62 160 70 L60 70 Q20 70 10 50 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/><line x1="10" y1="50" x2="190" y2="50" stroke="#0B2545" stroke-dasharray="4 4"/></svg>''',
    "starters": ["I think the ship is symmetric because...", "If it wasn't symmetric..."],
    "keywords": ["symmetry", "balance", "steer", "lean"]
  },
  "predict": {
    "question": "If a ship was built lopsided (uneven on both sides), what would likely happen?",
    "explanation": "If one side is heavier or shaped differently, buoyancy and weight aren't balanced left-to-right, so the ship leans toward the heavier side.",
    "choices": [
      {"text": "It would float and steer just fine", "correct": False},
      {"text": "It would tend to lean or turn to one side", "correct": True},
      {"text": "Symmetry only affects how it looks", "correct": False},
    ]
  }
}
open("titanic-02-top-view.html", "w", encoding="utf-8").write(build("titanic-02-top-view", "Titanic: Top View", c2_data))
print("built titanic-02-top-view.html")

# ================= CONCEPT 3: CROSS SECTION =================
c3_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 360 260" role="img" aria-label="Titanic cross section showing decks, cabins, engine room, and water below the waterline">
      <rect x="40" y="20" width="280" height="220" rx="8" fill="none" stroke="#0B2545" stroke-width="2"/>
      <rect x="40" y="20" width="280" height="70" fill="#EAF3F0" stroke="#2E6E62" stroke-width="1"/>
      <text x="180" y="60" text-anchor="middle" font-size="13" fill="#2E6E62">CABINS (air)</text>
      <rect x="40" y="90" width="280" height="70" fill="#F3EEE1" stroke="#C9A24B" stroke-width="1"/>
      <text x="180" y="130" text-anchor="middle" font-size="13" fill="#8A6C24">ENGINE ROOM</text>
      <rect x="40" y="160" width="280" height="80" fill="#B9D8EA" stroke="#2E6E62" stroke-width="1"/>
      <text x="180" y="205" text-anchor="middle" font-size="13" fill="#0B2545">WATER</text>
    </svg>''',
    "question": "This is the ship sliced in half. Which layer is full of air?",
    "explanation": "Air weighs far less than water for the same amount of space, so air-filled compartments keep the ship's overall density low enough to float.",
    "choices": [
      {"text": "The top layer (cabins)", "correct": True},
      {"text": "The bottom layer (water)", "correct": False},
      {"text": "The middle layer (engine room)", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"air","name":"Air","icon":ICON_CLOUD,"fact":"Air fills the cabins and empty spaces — it's much lighter than water, which helps the ship float."},
    {"id":"steel","name":"Steel","icon":ICON_STEEL,"fact":"Steel is the strong metal skin of the hull that keeps water out."},
    {"id":"water","name":"Water","icon":ICON_WAVE,"fact":"Water surrounds the hull below the waterline and pushes up on the ship."},
    {"id":"cargo","name":"Cargo","icon":ICON_BOX,"fact":"Cargo is the stuff being carried — it adds weight to the ship."},
  ]},
  "draw": {
    "prompt": "Draw the ship sliced in half, like a layer cake. Show cabins, engine room, and water — then label air, steel, and water.",
    "hintSvg": '''<svg viewBox="0 0 360 260" role="img" aria-label="hint">
      <rect x="40" y="20" width="280" height="220" rx="8" fill="none" stroke="#0B2545" stroke-width="2"/>
      <rect x="40" y="20" width="280" height="70" fill="#EAF3F0" stroke="#2E6E62" stroke-width="1"/>
      <rect x="40" y="90" width="280" height="70" fill="#F3EEE1" stroke="#C9A24B" stroke-width="1"/>
      <rect x="40" y="160" width="280" height="80" fill="#B9D8EA" stroke="#2E6E62" stroke-width="1"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Flip the cross section upside down. Does the water end up on top? Why not?",
    "svg": '''<rect x="40" y="20" width="220" height="180" rx="8" fill="none" stroke="#0B2545" stroke-width="2"/>
      <rect x="40" y="20" width="220" height="60" fill="#EAF3F0" stroke="#2E6E62" stroke-width="1"/>
      <rect x="40" y="80" width="220" height="60" fill="#F3EEE1" stroke="#C9A24B" stroke-width="1"/>
      <rect x="40" y="140" width="220" height="60" fill="#B9D8EA" stroke="#2E6E62" stroke-width="1"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows the ship riding LOWER in the water (a heavier load).",
    "explanation": "More cargo means more weight, which means more buoyant force is needed to balance it — so the ship sinks deeper until it does.",
    "choices": [
      {"label":"A — normal load", "svg": '''<svg viewBox="0 0 200 160"><rect x="20" y="20" width="160" height="120" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><rect x="20" y="90" width="160" height="50" fill="#B9D8EA" stroke="#2E6E62" stroke-width="1"/></svg>''', "correct": False},
      {"label":"B — heavy load", "svg": '''<svg viewBox="0 0 200 160"><rect x="20" y="20" width="160" height="120" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><rect x="20" y="60" width="160" height="80" fill="#B9D8EA" stroke="#D9603B" stroke-width="1"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Steel hull", "icon": ICON_STEEL},
    {"text":"Keeps water out of compartments", "icon": ICON_HULL},
    {"text":"Air-filled space stays light → ship floats", "icon": ICON_CLOUD},
  ]},
  "explain": {
    "prompt": "Why does it matter that the cabins are full of air and not water?",
    "visualSvg": '''<svg viewBox="0 0 200 120"><rect x="20" y="10" width="160" height="100" rx="6" fill="none" stroke="#0B2545" stroke-width="2"/><rect x="20" y="10" width="160" height="35" fill="#EAF3F0"/><rect x="20" y="75" width="160" height="35" fill="#B9D8EA"/></svg>''',
    "starters": ["I think air matters because...", "If water got inside, ..."],
    "keywords": ["air", "weight", "float", "water"]
  },
  "predict": {
    "question": "If water floods one compartment, what happens to the ship?",
    "explanation": "Water flooding in replaces air with something much heavier, adding weight without adding buoyancy — so that part pulls the ship down.",
    "choices": [
      {"text": "Nothing changes", "correct": False},
      {"text": "That part gets heavier and the ship sits lower", "correct": True},
      {"text": "The ship floats higher", "correct": False},
    ]
  }
}
open("titanic-03-cross-section.html", "w", encoding="utf-8").write(build("titanic-03-cross-section", "Titanic: Cross Section ⭐", c3_data))
print("built titanic-03-cross-section.html")

# ================= CONCEPT 4: FREE BODY DIAGRAM =================
c4_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 220" role="img" aria-label="Free body diagram of the ship showing buoyant force pushing up and weight pulling down">
      <rect x="60" y="90" width="180" height="50" rx="8" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="150" y="118" text-anchor="middle" font-size="13" fill="#0B2545">SHIP</text>
      <line x1="150" y1="90" x2="150" y2="30" stroke="#2E6E62" stroke-width="3"/>
      <path d="M142 40 L150 26 L158 40 Z" fill="#2E6E62"/>
      <text x="150" y="20" text-anchor="middle" font-size="12" fill="#2E6E62">Buoyant force ↑</text>
      <line x1="150" y1="140" x2="150" y2="195" stroke="#D9603B" stroke-width="3"/>
      <path d="M142 185 L150 199 L158 185 Z" fill="#D9603B"/>
      <text x="150" y="215" text-anchor="middle" font-size="12" fill="#D9603B">Weight ↓</text>
    </svg>''',
    "question": "Two forces pull on the ship in opposite directions. What happens when they're perfectly equal?",
    "explanation": "When buoyant force (up) exactly equals weight (down), the net force is zero — so the ship neither sinks nor rises.",
    "choices": [
      {"text": "The ship floats steadily", "correct": True},
      {"text": "The ship flies upward", "correct": False},
      {"text": "The ship spins in circles", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"buoyant","name":"Buoyant force","icon":ICON_ARROW_UP,"fact":"Buoyant force is water pushing up on the ship, from underneath."},
    {"id":"weight","name":"Weight","icon":ICON_ARROW_DOWN,"fact":"Weight is gravity pulling the ship (and everything on it) straight down."},
  ]},
  "draw": {
    "prompt": "Draw a box for the ship with two arrows: one pointing up labeled buoyant force, one pointing down labeled weight.",
    "hintSvg": '''<svg viewBox="0 0 300 220" role="img" aria-label="hint">
      <rect x="60" y="90" width="180" height="50" rx="8" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="150" y1="90" x2="150" y2="30" stroke="#2E6E62" stroke-width="3"/>
      <line x1="150" y1="140" x2="150" y2="195" stroke="#D9603B" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Tilt the ship sideways. Do the force arrows tilt with it, or do they still point straight up/down?",
    "svg": '''<rect x="50" y="80" width="160" height="45" rx="8" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="130" y1="80" x2="130" y2="30" stroke="#2E6E62" stroke-width="3"/>
      <line x1="130" y1="125" x2="130" y2="175" stroke="#D9603B" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows a SINKING ship (unbalanced forces).",
    "explanation": "In the sinking picture the arrows are unequal — weight is bigger than buoyant force, creating a net downward force.",
    "choices": [
      {"label":"A — balanced", "svg": '''<svg viewBox="0 0 200 160"><rect x="40" y="60" width="120" height="35" rx="6" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/><line x1="100" y1="60" x2="100" y2="25" stroke="#2E6E62" stroke-width="2"/><line x1="100" y1="95" x2="100" y2="130" stroke="#2E6E62" stroke-width="2"/></svg>''', "correct": False},
      {"label":"B — unbalanced", "svg": '''<svg viewBox="0 0 200 160"><rect x="40" y="70" width="120" height="35" rx="6" fill="#FBEAE3" stroke="#D9603B" stroke-width="2"/><line x1="100" y1="70" x2="100" y2="45" stroke="#D9603B" stroke-width="2"/><line x1="100" y1="105" x2="100" y2="150" stroke="#D9603B" stroke-width="4"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Weight = buoyant force", "icon": ICON_BALANCE},
    {"text":"Forces balance", "icon": ICON_EQUALS},
    {"text":"Ship floats steadily", "icon": ICON_SHIP_SMALL},
  ]},
  "explain": {
    "prompt": "If you loaded the ship with a lot of extra cargo, what would happen to the weight arrow — and what would the ship need to do to stay balanced?",
    "visualSvg": '''<svg viewBox="0 0 200 140"><rect x="60" y="60" width="80" height="35" rx="6" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><line x1="100" y1="60" x2="100" y2="20" stroke="#2E6E62" stroke-width="3"/><line x1="100" y1="95" x2="100" y2="130" stroke="#D9603B" stroke-width="3"/></svg>''',
    "starters": ["If we added more cargo...", "The weight arrow would..."],
    "keywords": ["weight", "buoyant", "balance", "cargo"]
  },
  "predict": {
    "question": "If you loaded the ship with a lot of extra cargo, what would happen?",
    "explanation": "Adding cargo increases weight. To rebalance, the ship displaces more water and sinks lower until buoyant force grows to match the new weight.",
    "choices": [
      {"text": "Nothing changes", "correct": False},
      {"text": "Weight increases, so the ship sinks lower until forces balance again", "correct": True},
      {"text": "The ship floats higher", "correct": False},
    ]
  }
}
open("titanic-04-free-body-diagram.html", "w", encoding="utf-8").write(build("titanic-04-free-body-diagram", "Titanic: Free Body Diagram", c4_data))
print("built titanic-04-free-body-diagram.html")
