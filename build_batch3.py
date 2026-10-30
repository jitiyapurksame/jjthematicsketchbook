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
ICON_ENGINE = "<svg viewBox='0 0 80 60'><rect x='16' y='16' width='48' height='30' rx='4' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='30' cy='31' r='6' fill='none' stroke='#C9A24B' stroke-width='2'/><circle cx='50' cy='31' r='6' fill='none' stroke='#C9A24B' stroke-width='2'/></svg>"
ICON_SHAFT = "<svg viewBox='0 0 80 60'><rect x='8' y='26' width='64' height='8' fill='#DCD3BC' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_PROPELLER = "<svg viewBox='0 0 80 60'><circle cx='40' cy='30' r='4' fill='#0B2545'/><path d='M40 30 L20 12 M40 30 L60 12 M40 30 L20 48 M40 30 L60 48' stroke='#0B2545' stroke-width='3'/></svg>"
ICON_WAVE = "<svg viewBox='0 0 80 60'><path d='M8 34 Q18 20 28 34 T48 34 T68 34' fill='none' stroke='#2E6E62' stroke-width='3'/><path d='M8 44 Q18 30 28 44 T48 44 T68 44' fill='none' stroke='#2E6E62' stroke-width='2' opacity='0.6'/></svg>"
ICON_ARROW_FWD = "<svg viewBox='0 0 40 40'><line x1='6' y1='20' x2='30' y2='20' stroke='#D9603B' stroke-width='4'/><path d='M22 10 L34 20 L22 30 Z' fill='#D9603B'/></svg>"
ICON_RULER = "<svg viewBox='0 0 80 60'><rect x='4' y='16' width='72' height='8' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><line x1='14' y1='16' x2='14' y2='24' stroke='#0B2545'/><line x1='24' y1='16' x2='24' y2='24' stroke='#0B2545'/><line x1='34' y1='16' x2='34' y2='24' stroke='#0B2545'/><line x1='44' y1='16' x2='44' y2='24' stroke='#0B2545'/><line x1='54' y1='16' x2='54' y2='24' stroke='#0B2545'/><line x1='64' y1='16' x2='64' y2='24' stroke='#0B2545'/></svg>"
ICON_SHRINK = "<svg viewBox='0 0 80 60'><path d='M12 12 L28 28 M12 12 L12 24 M12 12 L24 12' stroke='#2E6E62' stroke-width='3' fill='none' stroke-linecap='round'/><path d='M68 48 L52 32 M68 48 L68 36 M68 48 L56 48' stroke='#2E6E62' stroke-width='3' fill='none' stroke-linecap='round'/></svg>"
ICON_SHIP_SMALL = "<svg viewBox='0 0 80 60'><path d='M16 40 L64 40 L56 50 L24 50 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><rect x='34' y='20' width='6' height='20' fill='#D9603B'/></svg>"
ICON_SHIP_BIG = "<svg viewBox='0 0 80 60'><path d='M4 34 L76 34 L64 52 L16 52 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><rect x='22' y='10' width='7' height='24' fill='#D9603B'/><rect x='38' y='10' width='7' height='24' fill='#D9603B'/><rect x='54' y='10' width='7' height='24' fill='#D9603B'/></svg>"
ICON_RATIO = "<svg viewBox='0 0 80 60'><text x='40' y='40' text-anchor='middle' font-size='28' font-weight='bold' fill='#0B2545' font-family='Georgia,serif'>1:1000</text></svg>"
ICON_RISING_LINE = "<svg viewBox='0 0 80 60'><polyline points='8,50 40,50 72,10' fill='none' stroke='#2E6E62' stroke-width='3'/></svg>"
ICON_FLAT_LINE = "<svg viewBox='0 0 80 60'><polyline points='8,50 30,20 72,20' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"
ICON_FALLING_LINE = "<svg viewBox='0 0 80 60'><polyline points='8,20 50,20 72,50' fill='none' stroke='#D9603B' stroke-width='3'/></svg>"
ICON_AXES = "<svg viewBox='0 0 80 60'><line x1='12' y1='10' x2='12' y2='50' stroke='#0B2545' stroke-width='2'/><line x1='12' y1='50' x2='72' y2='50' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_WEIGHT = "<svg viewBox='0 0 80 60'><rect x='24' y='16' width='32' height='28' rx='4' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><text x='40' y='36' text-anchor='middle' font-size='16' font-weight='bold' fill='#0B2545'>m</text></svg>"
ICON_CUBE = "<svg viewBox='0 0 80 60'><rect x='20' y='16' width='30' height='30' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><path d='M20 16 L30 8 L60 8 L50 16 Z' fill='#D7E8E3' stroke='#2E6E62' stroke-width='2'/><path d='M50 16 L60 8 L60 38 L50 46 Z' fill='#C4DBD4' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_DENSITY_DOTS = "<svg viewBox='0 0 80 60'><rect x='16' y='10' width='48' height='40' fill='none' stroke='#0B2545' stroke-width='2'/><circle cx='28' cy='22' r='3' fill='#D9603B'/><circle cx='40' cy='22' r='3' fill='#D9603B'/><circle cx='52' cy='22' r='3' fill='#D9603B'/><circle cx='28' cy='34' r='3' fill='#D9603B'/><circle cx='40' cy='34' r='3' fill='#D9603B'/><circle cx='52' cy='34' r='3' fill='#D9603B'/></svg>"
ICON_TRIANGLE = "<svg viewBox='0 0 80 60'><path d='M40 8 L70 50 L10 50 Z' fill='none' stroke='#0B2545' stroke-width='2'/><line x1='10' y1='50' x2='70' y2='50' stroke='#0B2545' stroke-width='2'/><text x='40' y='24' text-anchor='middle' font-size='11' fill='#0B2545'>M</text><text x='24' y='44' text-anchor='middle' font-size='10' fill='#0B2545'>D</text><text x='56' y='44' text-anchor='middle' font-size='10' fill='#0B2545'>V</text></svg>"
ICON_FRACTION = "<svg viewBox='0 0 80 60'><text x='40' y='24' text-anchor='middle' font-size='16' fill='#0B2545'>M</text><line x1='20' y1='32' x2='60' y2='32' stroke='#0B2545' stroke-width='2'/><text x='40' y='50' text-anchor='middle' font-size='16' fill='#0B2545'>V</text></svg>"
ICON_EQUALS = "<svg viewBox='0 0 40 40'><line x1='8' y1='16' x2='32' y2='16' stroke='#0B2545' stroke-width='4'/><line x1='8' y1='26' x2='32' y2='26' stroke='#0B2545' stroke-width='4'/></svg>"

# ================= CONCEPT 9: PROPELLER =================
c9_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 140" role="img" aria-label="Energy flow diagram: engine to shaft to propeller to water">
      <rect x="10" y="40" width="80" height="60" rx="6" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><text x="50" y="75" text-anchor="middle" font-size="12" fill="#0B2545">ENGINE</text>
      <line x1="90" y1="70" x2="150" y2="70" stroke="#0B2545" stroke-width="2"/><path d="M142 63 L152 70 L142 77 Z" fill="#0B2545"/>
      <rect x="155" y="55" width="70" height="30" fill="#DCD3BC" stroke="#0B2545" stroke-width="2"/><text x="190" y="74" text-anchor="middle" font-size="11" fill="#0B2545">SHAFT</text>
      <line x1="225" y1="70" x2="270" y2="70" stroke="#0B2545" stroke-width="2"/><path d="M262 63 L272 70 L262 77 Z" fill="#0B2545"/>
      <circle cx="300" cy="70" r="6" fill="#0B2545"/>
      <path d="M300 70 L280 50 M300 70 L320 50 M300 70 L280 90 M300 70 L320 90" stroke="#0B2545" stroke-width="3"/>
      <text x="300" y="105" text-anchor="middle" font-size="11" fill="#0B2545">PROPELLER</text>
      <line x1="330" y1="70" x2="370" y2="70" stroke="#2E6E62" stroke-width="2"/><path d="M362 63 L372 70 L362 77 Z" fill="#2E6E62"/>
      <text x="380" y="40" text-anchor="middle" font-size="11" fill="#2E6E62">WATER</text>
    </svg>''',
    "question": "In which order does energy flow through the ship's propulsion system?",
    "explanation": "Energy always flows from its source (the engine) through the mechanism (shaft, propeller) and finally into the surroundings (water).",
    "choices": [
      {"text": "Engine → Shaft → Propeller → Water", "correct": True},
      {"text": "Water → Propeller → Shaft → Engine", "correct": False},
      {"text": "Shaft → Engine → Water → Propeller", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"engine","name":"Engine","icon":ICON_ENGINE,"fact":"The engine burns fuel to create turning power."},
    {"id":"shaft","name":"Shaft","icon":ICON_SHAFT,"fact":"The shaft is a long rod that carries the turning power backward."},
    {"id":"propeller","name":"Propeller","icon":ICON_PROPELLER,"fact":"The propeller's spinning blades push water backward."},
    {"id":"water","name":"Water","icon":ICON_WAVE,"fact":"As water gets pushed backward, it pushes the ship forward in return."},
  ]},
  "draw": {
    "prompt": "Draw the energy-flow chain: engine, shaft, propeller, water — connect them with arrows.",
    "hintSvg": '''<svg viewBox="0 0 400 140" role="img" aria-label="hint">
      <rect x="10" y="40" width="80" height="60" rx="6" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <rect x="155" y="55" width="70" height="30" fill="#DCD3BC" stroke="#0B2545" stroke-width="2"/>
      <circle cx="300" cy="70" r="6" fill="#0B2545"/>
      <path d="M300 70 L280 50 M300 70 L320 50 M300 70 L280 90 M300 70 L320 90" stroke="#0B2545" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the propeller. Does it still look like it's ready to spin from this new angle?",
    "svg": '''<circle cx="150" cy="150" r="6" fill="#0B2545"/><path d="M150 150 L110 110 M150 150 L190 110 M150 150 L110 190 M150 150 L190 190" stroke="#0B2545" stroke-width="4"/>'''
  },
  "compare": {
    "question": "Tap the propeller that pushes MORE water with each turn (more blades).",
    "explanation": "More blades means more surface area pushing water backward with each single turn of the propeller.",
    "choices": [
      {"label":"A — 2 blades", "svg": '''<svg viewBox="0 0 160 160"><circle cx="80" cy="80" r="6" fill="#0B2545"/><path d="M80 80 L40 80 M80 80 L120 80" stroke="#0B2545" stroke-width="6"/></svg>''', "correct": False},
      {"label":"B — 4 blades", "svg": '''<svg viewBox="0 0 160 160"><circle cx="80" cy="80" r="6" fill="#0B2545"/><path d="M80 80 L45 45 M80 80 L115 45 M80 80 L45 115 M80 80 L115 115" stroke="#0B2545" stroke-width="6"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Engine burns fuel", "icon": ICON_ENGINE},
    {"text":"Turns the shaft", "icon": ICON_SHAFT},
    {"text":"Spins the propeller", "icon": ICON_PROPELLER},
    {"text":"Pushes water back → ship moves forward", "icon": ICON_WAVE},
  ]},
  "explain": {
    "prompt": "Why does spinning the propeller make the ship move forward instead of just spinning in place?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><circle cx="100" cy="50" r="5" fill="#0B2545"/><path d="M100 50 L75 25 M100 50 L125 25 M100 50 L75 75 M100 50 L125 75" stroke="#0B2545" stroke-width="3"/></svg>''',
    "starters": ["I think the propeller pushes water, and...", "The water pushes back because..."],
    "keywords": ["water", "push", "forward", "spin"]
  },
  "predict": {
    "question": "If the propeller spun faster, what would likely happen to the ship's speed?",
    "explanation": "More spin pushes more water backward each second, so by Newton's third law, more force pushes the ship forward — until drag balances it out.",
    "choices": [
      {"text": "The ship would go faster (up to a point)", "correct": True},
      {"text": "The ship would go slower", "correct": False},
      {"text": "Nothing would change", "correct": False},
    ]
  }
}
open("titanic-09-propeller.html", "w", encoding="utf-8").write(build("titanic-09-propeller", "Titanic: Propeller", c9_data))
print("built titanic-09-propeller.html")

# ================= CONCEPT 10: SCALE DRAWING =================
c10_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 380 180" role="img" aria-label="Real ship compared to a small scale model, with a 1 to 1000 ratio label">
      <path d="M10 40 L280 40 L250 90 L60 90 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="145" y="65" text-anchor="middle" font-size="12" fill="#0B2545">REAL SHIP: 269 m</text>
      <path d="M300 130 L340 130 L336 142 L308 142 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="320" y="160" text-anchor="middle" font-size="10" fill="#0B2545">MODEL: 26.9 cm</text>
      <text x="190" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#C9A24B">scale 1 : 1000</text>
    </svg>''',
    "question": "If the real ship is 269 m long and we use a scale of 1:1000, about how long is the model?",
    "explanation": "Scale 1:1000 means every real-world unit becomes 1/1000th its size: 269 m × (1/1000) = 0.269 m = 26.9 cm.",
    "choices": [
      {"text": "About 26.9 cm", "correct": True},
      {"text": "About 269 cm", "correct": False},
      {"text": "About 2.69 cm", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"real","name":"Real ship","icon":ICON_SHIP_BIG,"fact":"The real ship is the true, full-size object — Titanic was 269 metres long."},
    {"id":"ratio","name":"Scale ratio","icon":ICON_RATIO,"fact":"The scale ratio tells you how many times smaller the model is."},
    {"id":"model","name":"Model","icon":ICON_SHIP_SMALL,"fact":"The model is a smaller copy that keeps the same shape and proportions."},
    {"id":"measure","name":"Measurement", "icon":ICON_RULER,"fact":"You measure both the real object and the model to check the scale is right."},
  ]},
  "draw": {
    "prompt": "Draw a real-size object next to a scaled-down model of it. Label both sizes.",
    "hintSvg": '''<svg viewBox="0 0 380 180" role="img" aria-label="hint">
      <path d="M10 40 L280 40 L250 90 L60 90 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <path d="M300 130 L340 130 L336 142 L308 142 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the scale drawing — does the RATIO between real and model change, even though the picture turns?",
    "svg": '''<path d="M10 40 L200 40 L180 80 L40 80 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <path d="M230 60 L250 60 L248 68 L232 68 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>'''
  },
  "compare": {
    "question": "A 200 m ship is scaled at 1:100. Tap the correctly-sized model.",
    "explanation": "200 m ÷ 100 (the scale) = 2 m — divide the real size by the second number in the ratio to get the model size.",
    "choices": [
      {"label":"A — 2 m model", "svg": '''<svg viewBox="0 0 160 100"><rect x="60" y="40" width="40" height="20" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><text x="80" y="80" text-anchor="middle" font-size="12" fill="#0B2545">2 m</text></svg>''', "correct": True},
      {"label":"B — 20 m model", "svg": '''<svg viewBox="0 0 160 100"><rect x="20" y="25" width="120" height="35" fill="#FBEAE3" stroke="#D9603B" stroke-width="2"/><text x="80" y="80" text-anchor="middle" font-size="12" fill="#D9603B">20 m</text></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Real ship: 269 m", "icon": ICON_RULER},
    {"text":"Divide by scale (1:1000)", "icon": ICON_SHRINK},
    {"text":"Model: 26.9 cm", "icon": ICON_SHIP_SMALL},
  ]},
  "explain": {
    "prompt": "If you doubled the scale ratio (say from 1:1000 to 1:500), what would happen to the size of your model?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M10 40 L120 40 L108 70 L30 70 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><path d="M150 50 L180 50 L177 62 L155 62 Z" fill="#F3EEE1" stroke="#C9A24B" stroke-width="2"/></svg>''',
    "starters": ["I think doubling the ratio would make the model...", "A smaller second number (1:500 vs 1:1000) means..."],
    "keywords": ["scale", "ratio", "bigger", "smaller"]
  },
  "predict": {
    "question": "A model is built at 1:50 scale of a 10 m boat. How long is the model?",
    "explanation": "10 m = 1000 cm. Divide by 50 (the scale): 1000 ÷ 50 = 20 cm.",
    "choices": [
      {"text": "20 cm", "correct": True},
      {"text": "200 cm", "correct": False},
      {"text": "2 cm", "correct": False},
    ]
  }
}
open("titanic-10-scale-drawing.html", "w", encoding="utf-8").write(build("titanic-10-scale-drawing", "Titanic: Scale Drawing", c10_data))
print("built titanic-10-scale-drawing.html")

# ================= CONCEPT 11: SPEED-TIME GRAPH =================
c11_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 320 180" role="img" aria-label="Speed time graph: rising, then flat, then falling">
      <line x1="30" y1="20" x2="30" y2="150" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="150" x2="300" y2="150" stroke="#0B2545" stroke-width="2"/>
      <polyline points="30,150 100,50 200,50 280,140" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <text x="16" y="90" font-size="11" fill="#0B2545" transform="rotate(-90 16 90)">speed</text>
      <text x="160" y="170" text-anchor="middle" font-size="11" fill="#0B2545">time</text>
    </svg>''',
    "question": "Looking at this speed-time graph, during which part is the ship going at a CONSTANT speed?",
    "explanation": "On a speed-time graph, the vertical axis is speed. If the line isn't rising or falling, speed isn't changing — that's constant speed.",
    "choices": [
      {"text": "The flat middle part", "correct": True},
      {"text": "The rising part at the start", "correct": False},
      {"text": "The falling part at the end", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"speedup","name":"Speeding up","icon":ICON_RISING_LINE,"fact":"A line rising means the ship's speed is increasing over time."},
    {"id":"constant","name":"Constant speed","icon":ICON_FLAT_LINE,"fact":"A flat line means the speed isn't changing — it's steady."},
    {"id":"slowdown","name":"Slowing down","icon":ICON_FALLING_LINE,"fact":"A line falling means the ship's speed is decreasing over time."},
    {"id":"axes","name":"Axes","icon":ICON_AXES,"fact":"The up-down axis is speed, the side-to-side axis is time."},
  ]},
  "draw": {
    "prompt": "Draw a speed-time graph for a ship leaving port: speeding up, cruising, then slowing to dock.",
    "hintSvg": '''<svg viewBox="0 0 320 180" role="img" aria-label="hint">
      <line x1="30" y1="20" x2="30" y2="150" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="150" x2="300" y2="150" stroke="#0B2545" stroke-width="2"/>
      <polyline points="30,150 100,50 200,50 280,140" fill="none" stroke="#2E6E62" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the graph. Does a steeper line still mean a faster change in speed, from this angle?",
    "svg": '''<line x1="30" y1="20" x2="30" y2="130" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="130" x2="260" y2="130" stroke="#0B2545" stroke-width="2"/>
      <polyline points="30,130 90,40 180,40 240,120" fill="none" stroke="#2E6E62" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the graph that shows the ship SPEEDING UP the fastest (steepest rising line).",
    "explanation": "A steeper line means speed changes more for the same amount of time — that's a bigger acceleration.",
    "choices": [
      {"label":"A — gentle slope", "svg": '''<svg viewBox="0 0 160 140"><line x1="20" y1="10" x2="20" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="120" x2="140" y2="120" stroke="#0B2545" stroke-width="2"/><polyline points="20,120 140,90" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
      {"label":"B — steep slope", "svg": '''<svg viewBox="0 0 160 140"><line x1="20" y1="10" x2="20" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="120" x2="140" y2="120" stroke="#0B2545" stroke-width="2"/><polyline points="20,120 60,20" fill="none" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Engine pushes harder", "icon": ICON_ENGINE},
    {"text":"Ship accelerates", "icon": ICON_RISING_LINE},
    {"text":"Speed increases over time", "icon": ICON_ARROW_FWD},
  ]},
  "explain": {
    "prompt": "What does a flat (horizontal) line on a speed-time graph tell you about the ship's speed?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><line x1="20" y1="10" x2="20" y2="80" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="80" x2="180" y2="80" stroke="#0B2545" stroke-width="2"/><polyline points="20,80 60,40 160,40" fill="none" stroke="#C9A24B" stroke-width="3"/></svg>''',
    "starters": ["A flat line means the speed is...", "If the line isn't rising or falling, that tells me..."],
    "keywords": ["constant", "speed", "flat", "time"]
  },
  "predict": {
    "question": "If the line on a speed-time graph suddenly drops straight down to zero, what does that mean happened?",
    "explanation": "A near-vertical drop means speed fell to zero in almost no time at all — a sudden stop.",
    "choices": [
      {"text": "The ship stopped very suddenly", "correct": True},
      {"text": "The ship sped up", "correct": False},
      {"text": "The ship turned around", "correct": False},
    ]
  }
}
open("titanic-11-speed-time-graph.html", "w", encoding="utf-8").write(build("titanic-11-speed-time-graph", "Titanic: Speed–Time Graph", c11_data))
print("built titanic-11-speed-time-graph.html")

# ================= CONCEPT 12: MASS-VOLUME-DENSITY TRIANGLE =================
c12_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 240 180" role="img" aria-label="Mass Volume Density triangle: Mass on top, Density and Volume on the bottom">
      <path d="M120 20 L210 150 L30 150 Z" fill="none" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="150" x2="210" y2="150" stroke="#0B2545" stroke-width="2"/>
      <line x1="120" y1="20" x2="120" y2="150" stroke="#0B2545" stroke-width="1" stroke-dasharray="4 3"/>
      <text x="120" y="60" text-anchor="middle" font-size="18" font-weight="bold" fill="#0B2545">MASS</text>
      <text x="72" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="#0B2545">DENSITY</text>
      <text x="168" y="130" text-anchor="middle" font-size="16" font-weight="bold" fill="#0B2545">VOLUME</text>
    </svg>''',
    "question": "Using the triangle, how do you calculate density?",
    "explanation": "Cover the letter you want to find. Density and Volume sit side by side on the bottom, Mass sits on top — so Density = Mass ÷ Volume.",
    "choices": [
      {"text": "Density = Mass ÷ Volume", "correct": True},
      {"text": "Density = Mass × Volume", "correct": False},
      {"text": "Density = Volume ÷ Mass", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"mass","name":"Mass","icon":ICON_WEIGHT,"fact":"Mass is how much matter (stuff) is in an object, measured in kilograms."},
    {"id":"volume","name":"Volume","icon":ICON_CUBE,"fact":"Volume is how much space an object takes up."},
    {"id":"density","name":"Density","icon":ICON_DENSITY_DOTS,"fact":"Density is how tightly packed the mass is inside that volume."},
    {"id":"triangle","name":"The triangle", "icon":ICON_TRIANGLE,"fact":"Cover the letter you want to find — the triangle shows you the formula for the other two."},
  ]},
  "draw": {
    "prompt": "Draw your own Mass–Volume–Density triangle. Put Mass on top, Density and Volume on the bottom.",
    "hintSvg": '''<svg viewBox="0 0 240 180" role="img" aria-label="hint">
      <path d="M120 20 L210 150 L30 150 Z" fill="none" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="150" x2="210" y2="150" stroke="#0B2545" stroke-width="2"/>
      <line x1="120" y1="20" x2="120" y2="150" stroke="#0B2545" stroke-width="1" stroke-dasharray="4 3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the triangle. Can you still cover up 'Density' and see Mass over Volume?",
    "svg": '''<path d="M100 20 L170 130 L30 130 Z" fill="none" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="130" x2="170" y2="130" stroke="#0B2545" stroke-width="2"/>
      <line x1="100" y1="20" x2="100" y2="130" stroke="#0B2545" stroke-width="1" stroke-dasharray="4 3"/>'''
  },
  "compare": {
    "question": "Tap the object that is MORE dense (same size, more mass packed inside).",
    "explanation": "Same size (same volume) but more mass squeezed inside means higher density, since density = mass ÷ volume.",
    "choices": [
      {"label":"A — sparse", "svg": '''<svg viewBox="0 0 160 140"><rect x="30" y="20" width="100" height="100" fill="none" stroke="#0B2545" stroke-width="2"/><circle cx="55" cy="45" r="4" fill="#D9603B"/><circle cx="105" cy="45" r="4" fill="#D9603B"/><circle cx="80" cy="95" r="4" fill="#D9603B"/></svg>''', "correct": False},
      {"label":"B — packed", "svg": '''<svg viewBox="0 0 160 140"><rect x="30" y="20" width="100" height="100" fill="none" stroke="#0B2545" stroke-width="2"/><circle cx="48" cy="40" r="4" fill="#D9603B"/><circle cx="70" cy="40" r="4" fill="#D9603B"/><circle cx="92" cy="40" r="4" fill="#D9603B"/><circle cx="114" cy="40" r="4" fill="#D9603B"/><circle cx="48" cy="65" r="4" fill="#D9603B"/><circle cx="70" cy="65" r="4" fill="#D9603B"/><circle cx="92" cy="65" r="4" fill="#D9603B"/><circle cx="114" cy="65" r="4" fill="#D9603B"/><circle cx="48" cy="90" r="4" fill="#D9603B"/><circle cx="70" cy="90" r="4" fill="#D9603B"/><circle cx="92" cy="90" r="4" fill="#D9603B"/><circle cx="114" cy="90" r="4" fill="#D9603B"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Cover up Density", "icon": ICON_TRIANGLE},
    {"text":"Left with Mass over Volume", "icon": ICON_FRACTION},
    {"text":"Density = Mass ÷ Volume", "icon": ICON_EQUALS},
  ]},
  "explain": {
    "prompt": "If two objects are the same size (same volume) but one is heavier, which one is more dense? Why?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="20" y="20" width="60" height="60" fill="none" stroke="#0B2545" stroke-width="2"/><circle cx="40" cy="40" r="3" fill="#D9603B"/><circle cx="60" cy="60" r="3" fill="#D9603B"/><rect x="120" y="20" width="60" height="60" fill="none" stroke="#0B2545" stroke-width="2"/><circle cx="135" cy="35" r="3" fill="#D9603B"/><circle cx="150" cy="35" r="3" fill="#D9603B"/><circle cx="165" cy="35" r="3" fill="#D9603B"/><circle cx="135" cy="55" r="3" fill="#D9603B"/><circle cx="150" cy="55" r="3" fill="#D9603B"/><circle cx="165" cy="55" r="3" fill="#D9603B"/></svg>''',
    "starters": ["The heavier one is more dense because...", "Density depends on how much mass is..."],
    "keywords": ["mass", "volume", "density", "packed"]
  },
  "predict": {
    "question": "If you keep the mass the same but increase the volume, what happens to density?",
    "explanation": "Density = mass ÷ volume. If mass stays the same but volume grows, you're dividing by a bigger number, so density gets smaller.",
    "choices": [
      {"text": "Density decreases", "correct": True},
      {"text": "Density increases", "correct": False},
      {"text": "Density stays exactly the same", "correct": False},
    ]
  }
}
open("titanic-12-density-triangle.html", "w", encoding="utf-8").write(build("titanic-12-density-triangle", "Titanic: Mass–Volume–Density Triangle", c12_data))
print("built titanic-12-density-triangle.html")
