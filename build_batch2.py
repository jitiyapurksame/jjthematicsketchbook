import json, re

TEMPLATE = open("engine-template-v2.html", encoding="utf-8").read()
DATA_BLOCK_RE = re.compile(r"window\.CONCEPT_DATA = \{.*?\};", re.S)

def build(concept_id, title, data):
    html = TEMPLATE
    html = html.replace('data-concept-id="theme-00-example"', 'data-concept-id="%s"' % concept_id)
    html = html.replace("<title>[CONCEPT TITLE] — Thematic Sketchbook</title>", "<title>%s — Thematic Sketchbook</title>" % title)
    html = html.replace('<h1 id="concept-title">[CONCEPT TITLE]</h1>', '<h1 id="concept-title">%s</h1>' % title)
    json_str = json.dumps(data, ensure_ascii=False)
    html = DATA_BLOCK_RE.sub(lambda m: "window.CONCEPT_DATA = " + json_str + ";", html)
    return html

# ---------------- icons ----------------
ICON_ARROW_SMALL = "<svg viewBox='0 0 80 60'><line x1='10' y1='30' x2='30' y2='30' stroke='#2E6E62' stroke-width='3'/><path d='M24 24 L32 30 L24 36 Z' fill='#2E6E62'/></svg>"
ICON_ARROW_MED = "<svg viewBox='0 0 80 60'><line x1='10' y1='30' x2='50' y2='30' stroke='#C9A24B' stroke-width='3'/><path d='M44 22 L54 30 L44 38 Z' fill='#C9A24B'/></svg>"
ICON_ARROW_BIG = "<svg viewBox='0 0 80 60'><line x1='10' y1='30' x2='68' y2='30' stroke='#D9603B' stroke-width='4'/><path d='M60 18 L74 30 L60 42 Z' fill='#D9603B'/></svg>"
ICON_STEEL = "<svg viewBox='0 0 80 60'><rect x='6' y='10' width='68' height='40' rx='3' fill='#DCD3BC' stroke='#0B2545' stroke-width='2'/><circle cx='16' cy='18' r='2.5' fill='#0B2545'/><circle cx='64' cy='18' r='2.5' fill='#0B2545'/><circle cx='16' cy='42' r='2.5' fill='#0B2545'/><circle cx='64' cy='42' r='2.5' fill='#0B2545'/></svg>"
ICON_ARROW_UP = "<svg viewBox='0 0 40 40'><line x1='20' y1='34' x2='20' y2='8' stroke='#2E6E62' stroke-width='4'/><path d='M10 16 L20 4 L30 16 Z' fill='#2E6E62'/></svg>"
ICON_WAVE = "<svg viewBox='0 0 80 60'><path d='M8 34 Q18 20 28 34 T48 34 T68 34' fill='none' stroke='#2E6E62' stroke-width='3'/><path d='M8 44 Q18 30 28 44 T48 44 T68 44' fill='none' stroke='#2E6E62' stroke-width='2' opacity='0.6'/></svg>"
ICON_HULL_MED = "<svg viewBox='0 0 80 60'><path d='M10 34 L70 34 L60 50 L20 50 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='34' x2='74' y2='34' stroke='#2E6E62' stroke-width='1' stroke-dasharray='4 3'/></svg>"
ICON_DASHLINE = "<svg viewBox='0 0 80 60'><line x1='8' y1='30' x2='72' y2='30' stroke='#2E6E62' stroke-width='2' stroke-dasharray='6 4'/></svg>"
ICON_SHIP_SMALL = "<svg viewBox='0 0 40 40'><path d='M8 24 L32 24 L28 32 L12 32 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><rect x='16' y='10' width='6' height='14' fill='#D9603B'/></svg>"
ICON_WALL = "<svg viewBox='0 0 80 60'><rect x='6' y='8' width='68' height='44' fill='none' stroke='#0B2545' stroke-width='2'/><line x1='30' y1='8' x2='30' y2='52' stroke='#C9A24B' stroke-width='3'/><line x1='52' y1='8' x2='52' y2='52' stroke='#C9A24B' stroke-width='3'/></svg>"
ICON_FLOOD = "<svg viewBox='0 0 80 60'><rect x='10' y='10' width='60' height='40' fill='#B9D8EA' stroke='#2E6E62' stroke-width='2'/><path d='M10 26 Q20 20 30 26 T50 26 T70 26' fill='none' stroke='#0B2545' stroke-width='1.5' opacity='0.5'/></svg>"
ICON_DRY = "<svg viewBox='0 0 80 60'><rect x='10' y='10' width='60' height='40' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_DOOR = "<svg viewBox='0 0 80 60'><rect x='24' y='8' width='32' height='44' rx='3' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='48' cy='30' r='2.5' fill='#C9A24B'/></svg>"
ICON_NARROW_HULL = "<svg viewBox='0 0 80 60'><path d='M30 10 L50 10 L56 50 L24 50 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_WIDE_HULL = "<svg viewBox='0 0 80 60'><path d='M14 16 L66 16 L74 44 L6 44 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_DEEP_HULL = "<svg viewBox='0 0 80 60'><path d='M26 6 L54 6 L58 54 L22 54 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_BALANCE = "<svg viewBox='0 0 40 40'><line x1='20' y1='8' x2='20' y2='30' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='16' x2='34' y2='16' stroke='#0B2545' stroke-width='2'/><circle cx='6' cy='22' r='5' fill='none' stroke='#2E6E62' stroke-width='2'/><circle cx='34' cy='22' r='5' fill='none' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_DOWN_ARROW = "<svg viewBox='0 0 40 40'><line x1='20' y1='6' x2='20' y2='32' stroke='#D9603B' stroke-width='4'/><path d='M10 24 L20 36 L30 24 Z' fill='#D9603B'/></svg>"
ICON_STACKED_WATER = "<svg viewBox='0 0 40 40'><rect x='6' y='6' width='28' height='8' fill='#B9D8EA'/><rect x='6' y='16' width='28' height='8' fill='#8FC0DA'/><rect x='6' y='26' width='28' height='8' fill='#5F9CBF'/></svg>"

# ================= CONCEPT 5: PRESSURE MAP =================
c5_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 240" role="img" aria-label="Pressure diagram showing small arrows near the surface and big arrows near the bottom, pushing on the ship's hull">
      <rect x="60" y="20" width="60" height="200" fill="#B9D8EA" opacity="0.5"/>
      <path d="M90 20 L130 20 L120 220 L100 220 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="60" y1="45" x2="88" y2="45" stroke="#2E6E62" stroke-width="2"/><path d="M82 40 L90 45 L82 50 Z" fill="#2E6E62"/>
      <line x1="60" y1="115" x2="95" y2="115" stroke="#C9A24B" stroke-width="3"/><path d="M87 108 L97 115 L87 122 Z" fill="#C9A24B"/>
      <line x1="60" y1="195" x2="102" y2="195" stroke="#D9603B" stroke-width="4"/><path d="M92 186 L106 195 L92 204 Z" fill="#D9603B"/>
      <text x="150" y="235" text-anchor="middle" font-size="12" fill="#2E6E62">arrows get bigger with depth</text>
    </svg>''',
    "question": "As you go deeper underwater, what happens to the pressure?",
    "explanation": "Pressure comes from the weight of water above pushing down — the deeper you go, the taller (and heavier) that column of water gets.",
    "choices": [
      {"text": "It increases", "correct": True},
      {"text": "It decreases", "correct": False},
      {"text": "It stays exactly the same", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"surface","name":"Near the surface","icon":ICON_ARROW_SMALL,"fact":"Near the surface, there's only a little water above pushing down — so pressure is low."},
    {"id":"middepth","name":"Mid-depth","icon":ICON_ARROW_MED,"fact":"Halfway down, there's more water stacked above — pressure is medium."},
    {"id":"deep","name":"Deep water","icon":ICON_ARROW_BIG,"fact":"Deep down, a huge column of water sits above, pushing hard — pressure is high."},
    {"id":"hull","name":"Hull","icon":ICON_STEEL,"fact":"The hull has to be strongest lower down, where water pressure pushes hardest."},
  ]},
  "draw": {
    "prompt": "Draw the ship's hull underwater. Add arrows pushing on it — small near the top, bigger near the bottom.",
    "hintSvg": '''<svg viewBox="0 0 300 240" role="img" aria-label="hint">
      <path d="M90 20 L130 20 L120 220 L100 220 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="60" y1="45" x2="88" y2="45" stroke="#2E6E62" stroke-width="2"/>
      <line x1="60" y1="115" x2="95" y2="115" stroke="#C9A24B" stroke-width="3"/>
      <line x1="60" y1="195" x2="102" y2="195" stroke="#D9603B" stroke-width="4"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the pressure diagram. Do the arrows still push into the hull from every side?",
    "svg": '''<path d="M90 20 L130 20 L120 220 L100 220 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="60" y1="45" x2="88" y2="45" stroke="#2E6E62" stroke-width="2"/>
      <line x1="60" y1="115" x2="95" y2="115" stroke="#C9A24B" stroke-width="3"/>
      <line x1="60" y1="195" x2="102" y2="195" stroke="#D9603B" stroke-width="4"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows CORRECT pressure (bigger arrows lower down).",
    "explanation": "The correct picture shows arrows growing with depth, matching how water pressure builds up the deeper you go.",
    "choices": [
      {"label":"A — correct", "svg": '''<svg viewBox="0 0 160 160"><rect x="70" y="10" width="20" height="140" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="30" x2="65" y2="30" stroke="#2E6E62" stroke-width="2"/><line x1="20" y1="80" x2="65" y2="80" stroke="#C9A24B" stroke-width="3"/><line x1="20" y1="130" x2="65" y2="130" stroke="#D9603B" stroke-width="4"/></svg>''', "correct": True},
      {"label":"B — equal arrows", "svg": '''<svg viewBox="0 0 160 160"><rect x="70" y="10" width="20" height="140" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="30" x2="65" y2="30" stroke="#D9603B" stroke-width="3"/><line x1="20" y1="80" x2="65" y2="80" stroke="#D9603B" stroke-width="3"/><line x1="20" y1="130" x2="65" y2="130" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Go deeper in the water", "icon": ICON_DOWN_ARROW},
    {"text":"More water stacked above, pushing down", "icon": ICON_STACKED_WATER},
    {"text":"Higher pressure", "icon": ICON_ARROW_BIG},
  ]},
  "explain": {
    "prompt": "Why do you think pressure is bigger deep underwater than near the surface?",
    "visualSvg": '''<svg viewBox="0 0 200 140"><rect x="80" y="10" width="30" height="120" fill="#B9D8EA" opacity="0.6"/><line x1="30" y1="30" x2="75" y2="30" stroke="#2E6E62" stroke-width="2"/><line x1="30" y1="130" x2="75" y2="130" stroke="#D9603B" stroke-width="4"/></svg>''',
    "starters": ["I think deep water has more pressure because...", "The pressure increases because..."],
    "keywords": ["depth", "water", "weight", "push"]
  },
  "predict": {
    "question": "If a diver went twice as deep, what would roughly happen to the pressure on their body?",
    "explanation": "Water pressure increases roughly in direct proportion to depth, so twice the depth means roughly twice the pressure.",
    "choices": [
      {"text": "It would roughly double", "correct": True},
      {"text": "It would stay exactly the same", "correct": False},
      {"text": "It would disappear", "correct": False},
    ]
  }
}
open("titanic-05-pressure-map.html", "w", encoding="utf-8").write(build("titanic-05-pressure-map", "Titanic: Pressure Map", c5_data))
print("built titanic-05-pressure-map.html")

# ================= CONCEPT 6: BUOYANCY MODEL =================
c6_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 220" role="img" aria-label="Ship floating in water with the displaced water shown to the side and an upward arrow showing buoyant force">
      <rect x="20" y="120" width="260" height="80" fill="#B9D8EA" opacity="0.5"/>
      <path d="M100 100 L200 100 L190 140 L110 140 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <path d="M110 140 Q150 155 190 140 L190 150 Q150 165 110 150 Z" fill="#2E6E62" opacity="0.6"/>
      <text x="150" y="175" text-anchor="middle" font-size="11" fill="#0B2545">displaced water</text>
      <line x1="150" y1="100" x2="150" y2="60" stroke="#2E6E62" stroke-width="3"/><path d="M142 70 L150 56 L158 70 Z" fill="#2E6E62"/>
      <text x="150" y="48" text-anchor="middle" font-size="12" fill="#2E6E62">buoyant force ↑</text>
    </svg>''',
    "question": "When the ship pushes water out of the way, what pushes back?",
    "explanation": "This is Archimedes' Principle: an object pushes fluid out of the way, and that fluid pushes back with an equal upward force.",
    "choices": [
      {"text": "The displaced water pushes up on the ship", "correct": True},
      {"text": "Nothing pushes back", "correct": False},
      {"text": "The water pushes the ship sideways", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"displaced","name":"Displaced water","icon":ICON_WAVE,"fact":"Displaced water is the water the ship's hull pushes out of the way."},
    {"id":"buoyant","name":"Buoyant force","icon":ICON_ARROW_UP,"fact":"Buoyant force is the upward push the displaced water gives back to the ship."},
    {"id":"ship","name":"Ship","icon":ICON_HULL_MED,"fact":"The ship floats where these forces balance out."},
    {"id":"waterline","name":"Waterline","icon":ICON_DASHLINE,"fact":"The waterline shows exactly how deep the ship sits in the water."},
  ]},
  "draw": {
    "prompt": "Draw the ship floating, then draw the water it pushes out of the way, and an arrow showing the force pushing back up.",
    "hintSvg": '''<svg viewBox="0 0 300 220" role="img" aria-label="hint">
      <path d="M100 100 L200 100 L190 140 L110 140 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="150" y1="100" x2="150" y2="60" stroke="#2E6E62" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the buoyancy diagram — does the upward force change direction with the ship, or stay pointing up?",
    "svg": '''<path d="M100 100 L200 100 L190 140 L110 140 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <line x1="150" y1="100" x2="150" y2="60" stroke="#2E6E62" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows MORE water being displaced (a heavier ship).",
    "explanation": "A heavier ship sinks deeper, displacing more water, until the extra buoyant force balances its extra weight.",
    "choices": [
      {"label":"A — small displacement", "svg": '''<svg viewBox="0 0 160 160"><rect x="30" y="20" width="100" height="140" fill="#F3EEE1" stroke="#0B2545" stroke-width="0" opacity="0"/><path d="M40 90 L120 90 L115 105 L45 105 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><rect x="20" y="105" width="120" height="35" fill="#B9D8EA"/></svg>''', "correct": False},
      {"label":"B — large displacement", "svg": '''<svg viewBox="0 0 160 160"><path d="M30 70 L130 70 L120 105 L40 105 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><rect x="20" y="105" width="120" height="45" fill="#B9D8EA"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Ship enters the water", "icon": ICON_SHIP_SMALL},
    {"text":"Pushes water out of the way (displaces it)", "icon": ICON_WAVE},
    {"text":"Displaced water pushes back up", "icon": ICON_ARROW_UP},
  ]},
  "explain": {
    "prompt": "Why does a heavier ship need to displace more water to float?",
    "visualSvg": '''<svg viewBox="0 0 200 120"><path d="M40 50 L160 50 L150 85 L50 85 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><rect x="30" y="85" width="140" height="25" fill="#B9D8EA"/></svg>''',
    "starters": ["A heavier ship needs to displace more water because...", "To balance the extra weight, ..."],
    "keywords": ["displace", "weight", "buoyant", "balance"]
  },
  "predict": {
    "question": "If you replaced the ship with a much heavier version of the same shape, what happens to how much water it displaces?",
    "explanation": "Buoyant force must equal weight for a ship to float, so more weight means more water must be displaced to generate that extra upward force.",
    "choices": [
      {"text": "It displaces more water and sits lower", "correct": True},
      {"text": "It displaces less water", "correct": False},
      {"text": "Nothing changes", "correct": False},
    ]
  }
}
open("titanic-06-buoyancy-model.html", "w", encoding="utf-8").write(build("titanic-06-buoyancy-model", "Titanic: Buoyancy Model", c6_data))
print("built titanic-06-buoyancy-model.html")

# ================= CONCEPT 7: WATERTIGHT COMPARTMENTS =================
c7_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 340 200" role="img" aria-label="Ship divided into compartments by walls, with one compartment flooded blue">
      <rect x="20" y="30" width="300" height="140" fill="none" stroke="#0B2545" stroke-width="2"/>
      <line x1="80" y1="30" x2="80" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <line x1="140" y1="30" x2="140" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <line x1="200" y1="30" x2="200" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <line x1="260" y1="30" x2="260" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <rect x="140" y="30" width="60" height="140" fill="#B9D8EA"/>
      <text x="170" y="105" text-anchor="middle" font-size="11" fill="#0B2545">flooded</text>
    </svg>''',
    "question": "If one compartment fills with water, what happens to the rest of the ship?",
    "explanation": "Bulkheads (walls) seal off flooding to just one section, so the rest of the ship keeps its air and stays buoyant enough to float.",
    "choices": [
      {"text": "The other compartments can stay dry and keep the ship afloat", "correct": True},
      {"text": "The whole ship instantly sinks", "correct": False},
      {"text": "Nothing happens at all", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"bulkhead","name":"Bulkhead (wall)","icon":ICON_WALL,"fact":"A bulkhead is a strong wall that divides the ship into separate sections."},
    {"id":"flooded","name":"Flooded compartment","icon":ICON_FLOOD,"fact":"A flooded compartment has filled with water — but it can be sealed off."},
    {"id":"dry","name":"Dry compartment","icon":ICON_DRY,"fact":"A dry compartment stays full of air, keeping that part of the ship light."},
    {"id":"door","name":"Watertight door","icon":ICON_DOOR,"fact":"A watertight door can seal shut to stop water spreading between compartments."},
  ]},
  "draw": {
    "prompt": "Draw the ship divided into sections by walls (bulkheads). Shade in one compartment as flooded.",
    "hintSvg": '''<svg viewBox="0 0 340 200" role="img" aria-label="hint">
      <rect x="20" y="30" width="300" height="140" fill="none" stroke="#0B2545" stroke-width="2"/>
      <line x1="80" y1="30" x2="80" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <line x1="140" y1="30" x2="140" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <line x1="200" y1="30" x2="200" y2="170" stroke="#C9A24B" stroke-width="3"/>
      <rect x="140" y="30" width="60" height="140" fill="#B9D8EA"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the compartment diagram — do the walls still separate the sections the same way?",
    "svg": '''<rect x="20" y="30" width="260" height="120" fill="none" stroke="#0B2545" stroke-width="2"/>
      <line x1="90" y1="30" x2="90" y2="150" stroke="#C9A24B" stroke-width="3"/>
      <line x1="160" y1="30" x2="160" y2="150" stroke="#C9A24B" stroke-width="3"/>
      <line x1="220" y1="30" x2="220" y2="150" stroke="#C9A24B" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the SAFER design — more compartments means flooding stays contained.",
    "explanation": "More, smaller compartments mean a single flood affects a smaller fraction of the ship's total buoyancy.",
    "choices": [
      {"label":"A — 2 big compartments", "svg": '''<svg viewBox="0 0 160 100"><rect x="10" y="20" width="140" height="60" fill="none" stroke="#0B2545" stroke-width="2"/><line x1="80" y1="20" x2="80" y2="80" stroke="#C9A24B" stroke-width="3"/></svg>''', "correct": False},
      {"label":"B — 5 small compartments", "svg": '''<svg viewBox="0 0 160 100"><rect x="10" y="20" width="140" height="60" fill="none" stroke="#0B2545" stroke-width="2"/><line x1="38" y1="20" x2="38" y2="80" stroke="#C9A24B" stroke-width="2"/><line x1="66" y1="20" x2="66" y2="80" stroke="#C9A24B" stroke-width="2"/><line x1="94" y1="20" x2="94" y2="80" stroke="#C9A24B" stroke-width="2"/><line x1="122" y1="20" x2="122" y2="80" stroke="#C9A24B" stroke-width="2"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Wall (bulkhead) divides the ship", "icon": ICON_WALL},
    {"text":"One compartment floods", "icon": ICON_FLOOD},
    {"text":"Other compartments stay dry → ship still floats", "icon": ICON_SHIP_SMALL},
  ]},
  "explain": {
    "prompt": "Why do you think engineers divide a ship into separate watertight sections instead of leaving it as one big open space?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="10" y="15" width="180" height="70" fill="none" stroke="#0B2545" stroke-width="2"/><line x1="70" y1="15" x2="70" y2="85" stroke="#C9A24B" stroke-width="2"/><line x1="130" y1="15" x2="130" y2="85" stroke="#C9A24B" stroke-width="2"/><rect x="70" y="15" width="60" height="70" fill="#B9D8EA"/></svg>''',
    "starters": ["I think dividing the ship helps because...", "If it was all one open space..."],
    "keywords": ["flood", "contain", "safety", "compartment"]
  },
  "predict": {
    "question": "If TOO MANY compartments flood at once, what would likely happen?",
    "explanation": "Every design has a limit — Titanic could survive a few flooded compartments, but too many overwhelmed its remaining buoyancy.",
    "choices": [
      {"text": "The ship could still sink, even with compartments", "correct": True},
      {"text": "The ship is always 100% safe no matter what", "correct": False},
      {"text": "The ship would float higher", "correct": False},
    ]
  }
}
open("titanic-07-watertight-compartments.html", "w", encoding="utf-8").write(build("titanic-07-watertight-compartments", "Titanic: Watertight Compartments", c7_data))
print("built titanic-07-watertight-compartments.html")

# ================= CONCEPT 8: HULL SHAPE =================
c8_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 360 160" role="img" aria-label="Three hull cross-sections side by side: narrow, wide, and deep">
      <path d="M60 20 L80 20 L86 110 L54 110 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="70" y="130" text-anchor="middle" font-size="11" fill="#2E6E62">A: narrow</text>
      <path d="M150 40 L230 40 L245 100 L135 100 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="190" y="120" text-anchor="middle" font-size="11" fill="#2E6E62">B: wide</text>
      <path d="M290 10 L330 10 L336 130 L284 130 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="310" y="145" text-anchor="middle" font-size="11" fill="#2E6E62">C: deep</text>
    </svg>''',
    "question": "Looking at these three hull shapes, which do you think tips over most easily?",
    "explanation": "A narrow hull has a small base, so it doesn't take much tilt before it becomes easier to tip over.",
    "choices": [
      {"text": "The narrow one (A)", "correct": True},
      {"text": "The wide one (B)", "correct": False},
      {"text": "The deep one (C)", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"narrow","name":"Narrow hull","icon":ICON_NARROW_HULL,"fact":"A narrow hull has less base to resist tipping — it's less stable."},
    {"id":"wide","name":"Wide hull","icon":ICON_WIDE_HULL,"fact":"A wide hull has a bigger base, which resists tipping — more stable."},
    {"id":"deep","name":"Deep hull","icon":ICON_DEEP_HULL,"fact":"A deep hull sits lower in the water, which can also add stability."},
    {"id":"stability","name":"Stability","icon":ICON_BALANCE,"fact":"Stability is how well a ship resists tipping over."},
  ]},
  "draw": {
    "prompt": "Draw three hull cross-sections side by side: one narrow, one wide, one deep.",
    "hintSvg": '''<svg viewBox="0 0 360 160" role="img" aria-label="hint">
      <path d="M60 20 L80 20 L86 110 L54 110 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <path d="M150 40 L230 40 L245 100 L135 100 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <path d="M290 10 L330 10 L336 130 L284 130 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the wide hull. Does it still look wide and stable from this new angle?",
    "svg": '''<path d="M60 60 L200 60 L215 130 L45 130 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows the MORE STABLE hull (wide base).",
    "explanation": "A wider hull spreads its support over a bigger base, resisting tipping much like a wide-based table is harder to knock over.",
    "choices": [
      {"label":"A — narrow", "svg": '''<svg viewBox="0 0 160 140"><path d="M65 20 L95 20 L100 120 L60 120 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
      {"label":"B — wide", "svg": '''<svg viewBox="0 0 160 140"><path d="M20 40 L140 40 L150 110 L10 110 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Wide hull", "icon": ICON_WIDE_HULL},
    {"text":"Bigger base resists tipping", "icon": ICON_BALANCE},
    {"text":"More stable ship", "icon": ICON_SHIP_SMALL},
  ]},
  "explain": {
    "prompt": "Why do you think a wider hull tends to be more stable than a narrow one?",
    "visualSvg": '''<svg viewBox="0 0 200 120"><path d="M20 40 L180 40 L190 100 L10 100 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["I think a wide hull is more stable because...", "It's a bit like..."],
    "keywords": ["wide", "base", "stable", "tip"]
  },
  "predict": {
    "question": "If a ship's hull was made narrower to go faster, what trade-off might happen?",
    "explanation": "Narrower hulls often reduce drag (helping speed) but also reduce the stable base — a classic engineering trade-off.",
    "choices": [
      {"text": "It might become easier to tip over", "correct": True},
      {"text": "It would become perfectly stable", "correct": False},
      {"text": "Speed and stability are completely unrelated", "correct": False},
    ]
  }
}
open("titanic-08-hull-shape.html", "w", encoding="utf-8").write(build("titanic-08-hull-shape", "Titanic: Hull Shape", c8_data))
print("built titanic-08-hull-shape.html")
