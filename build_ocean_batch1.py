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

# ---------------- shared icons (ocean palette) ----------------
ICON_SUN = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='8' fill='#E4C77C' stroke='#C9A24B' stroke-width='2'/><line x1='20' y1='2' x2='20' y2='8' stroke='#C9A24B' stroke-width='3'/><line x1='20' y1='32' x2='20' y2='38' stroke='#C9A24B' stroke-width='3'/><line x1='2' y1='20' x2='8' y2='20' stroke='#C9A24B' stroke-width='3'/><line x1='32' y1='20' x2='38' y2='20' stroke='#C9A24B' stroke-width='3'/></svg>"
ICON_TWILIGHT = "<svg viewBox='0 0 40 40'><rect x='4' y='6' width='32' height='28' fill='#1B3A5C' stroke='#0B2545' stroke-width='2'/><circle cx='14' cy='16' r='2' fill='#EAF3F0'/><circle cx='26' cy='22' r='2' fill='#EAF3F0'/></svg>"
ICON_MIDNIGHT = "<svg viewBox='0 0 40 40'><rect x='4' y='6' width='32' height='28' fill='#071A33' stroke='#000' stroke-width='2'/><circle cx='20' cy='20' r='3' fill='#C9A24B'/></svg>"
ICON_TRENCH = "<svg viewBox='0 0 40 40'><path d='M2 10 L14 10 L20 28 L26 10 L38 10 L38 34 L2 34 Z' fill='#DCD3BC' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_THERMOMETER_HOT = "<svg viewBox='0 0 40 40'><rect x='16' y='4' width='8' height='22' rx='4' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='20' cy='30' r='7' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><rect x='18' y='10' width='4' height='16' fill='#D9603B'/></svg>"
ICON_THERMOMETER_COLD = "<svg viewBox='0 0 40 40'><rect x='16' y='4' width='8' height='22' rx='4' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='20' cy='30' r='7' fill='#2E6E62' stroke='#0B2545' stroke-width='2'/><rect x='18' y='18' width='4' height='8' fill='#2E6E62'/></svg>"
ICON_LAYER_SPLIT = "<svg viewBox='0 0 40 40'><rect x='4' y='6' width='32' height='12' fill='#D9603B' opacity='0.8'/><rect x='4' y='18' width='32' height='4' fill='#0B2545'/><rect x='4' y='22' width='32' height='12' fill='#2E6E62' opacity='0.8'/></svg>"
ICON_SALT_GRAIN = "<svg viewBox='0 0 40 40'><rect x='16' y='16' width='8' height='8' fill='#F3EEE1' stroke='#0B2545' stroke-width='1.5' transform='rotate(20 20 20)'/><rect x='6' y='24' width='6' height='6' fill='#F3EEE1' stroke='#0B2545' stroke-width='1.5'/><rect x='26' y='8' width='6' height='6' fill='#F3EEE1' stroke='#0B2545' stroke-width='1.5'/></svg>"
ICON_DOWN_ARROW_HEAVY = "<svg viewBox='0 0 40 40'><line x1='20' y1='4' x2='20' y2='28' stroke='#0B2545' stroke-width='5'/><path d='M8 20 L20 34 L32 20 Z' fill='#0B2545'/></svg>"
ICON_SCALE_SALT = "<svg viewBox='0 0 40 40'><line x1='20' y1='6' x2='20' y2='28' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='14' x2='34' y2='14' stroke='#0B2545' stroke-width='2'/><circle cx='6' cy='20' r='5' fill='none' stroke='#2E6E62' stroke-width='2'/><circle cx='34' cy='20' r='5' fill='#D9603B'/></svg>"
ICON_CREST = "<svg viewBox='0 0 40 40'><path d='M4 26 Q12 10 20 26 T36 26' fill='none' stroke='#2E6E62' stroke-width='3'/><circle cx='12' cy='14' r='2.5' fill='#D9603B'/></svg>"
ICON_TROUGH = "<svg viewBox='0 0 40 40'><path d='M4 14 Q12 30 20 14 T36 14' fill='none' stroke='#2E6E62' stroke-width='3'/><circle cx='12' cy='26' r='2.5' fill='#D9603B'/></svg>"
ICON_WAVELENGTH = "<svg viewBox='0 0 40 40'><path d='M2 20 Q10 6 18 20 T34 20' fill='none' stroke='#2E6E62' stroke-width='2.5'/><line x1='2' y1='34' x2='2' y2='30' stroke='#0B2545'/><line x1='34' y1='34' x2='34' y2='30' stroke='#0B2545'/><line x1='2' y1='32' x2='34' y2='32' stroke='#0B2545' stroke-width='1.5'/></svg>"
ICON_AMPLITUDE = "<svg viewBox='0 0 40 40'><path d='M2 20 Q10 6 18 20' fill='none' stroke='#2E6E62' stroke-width='2.5'/><line x1='10' y1='20' x2='10' y2='6' stroke='#D9603B' stroke-width='2' stroke-dasharray='3 2'/></svg>"
ICON_SHIP_BOB = "<svg viewBox='0 0 40 40'><path d='M6 24 L34 24 L30 32 L10 32 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><rect x='16' y='12' width='6' height='12' fill='#D9603B'/><path d='M2 24 Q10 18 20 24 T38 24' fill='none' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_LINK = "<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/><circle cx='26' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"

# ================= CONCEPT 1: OCEAN CROSS SECTION =================
c1_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 240" role="img" aria-label="Ocean cross section from surface to seafloor, four colored layers">
      <rect x="10" y="20" width="380" height="45" fill="#8FCB9B"/>
      <rect x="10" y="65" width="380" height="45" fill="#3F8F5C" opacity="0.8"/>
      <rect x="10" y="110" width="380" height="55" fill="#1B3A5C"/>
      <rect x="10" y="165" width="380" height="50" fill="#071A33"/>
      <rect x="10" y="215" width="380" height="15" fill="#DCD3BC"/>
      <text x="20" y="46" font-size="12" fill="#0B2545">☀️ Sunlight Zone</text>
      <text x="20" y="91" font-size="12" fill="#F3EEE1">🌫️ Twilight Zone</text>
      <text x="20" y="141" font-size="12" fill="#F3EEE1">🌑 Midnight Zone</text>
      <text x="20" y="194" font-size="12" fill="#F3EEE1">⚫ The Deep Dark</text>
    </svg>''',
    "question": "Quick! Which zone gets ALL the sunlight?",
    "explanation": "Sunlight only punches through the top ~200m. Below that, it's twilight, then total darkness — no light = no plants growing down there.",
    "choices": [
      {"text": "The Sunlight Zone (top)", "correct": True},
      {"text": "The Midnight Zone (deep)", "correct": False},
      {"text": "All zones get equal light", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"sunlight","name":"Sunlight Zone","icon":ICON_SUN,"fact":"🔆 Top layer. Bright, warm, full of fish and plants."},
    {"id":"twilight","name":"Twilight Zone","icon":ICON_TWILIGHT,"fact":"🌫️ Dim blue light only. Getting cold fast."},
    {"id":"midnight","name":"Midnight Zone","icon":ICON_MIDNIGHT,"fact":"🌑 Pitch black. No sunlight ever reaches here."},
    {"id":"trench","name":"Seafloor / Trench","icon":ICON_TRENCH,"fact":"⛰️ The bottom. Freezing, crushing pressure, weird creatures."},
  ]},
  "draw": {
    "prompt": "Draw the 4 stacked layers top to bottom. Label each one. Bonus: color the top layer bright and the bottom layer almost black — that's the light disappearing!",
    "hintSvg": '''<svg viewBox="0 0 400 240" role="img" aria-label="hint">
      <rect x="10" y="20" width="380" height="45" fill="#8FCB9B"/>
      <rect x="10" y="65" width="380" height="45" fill="#3F8F5C" opacity="0.8"/>
      <rect x="10" y="110" width="380" height="55" fill="#1B3A5C"/>
      <rect x="10" y="165" width="380" height="50" fill="#071A33"/>
      <rect x="10" y="215" width="380" height="15" fill="#DCD3BC"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Flip the layer stack. Does the ORDER of light → dark stay the same, or does it scramble?",
    "svg": '''<rect x="30" y="15" width="260" height="30" fill="#8FCB9B"/>
      <rect x="30" y="45" width="260" height="30" fill="#3F8F5C" opacity="0.8"/>
      <rect x="30" y="75" width="260" height="35" fill="#1B3A5C"/>
      <rect x="30" y="110" width="260" height="35" fill="#071A33"/>'''
  },
  "compare": {
    "question": "Tap the picture that shows the SUNLIGHT ZONE (bright top layer).",
    "explanation": "Bright green-blue = sunlight reaching in. The dark navy block is way deeper, where light can't go.",
    "choices": [
      {"label":"A — bright top layer", "svg": '''<svg viewBox="0 0 200 140"><rect x="20" y="20" width="160" height="100" fill="#8FCB9B" stroke="#2E6E62" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — dark bottom layer", "svg": '''<svg viewBox="0 0 200 140"><rect x="20" y="20" width="160" height="100" fill="#071A33" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Sunlight hits the surface", "icon": ICON_SUN},
    {"text":"Light fades with every meter down", "icon": ICON_TWILIGHT},
    {"text":"No light + freezing cold = Midnight Zone", "icon": ICON_MIDNIGHT},
    {"text":"🔗 Links to Titanic Cross Section: layers stack the same way a ship's decks do", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why do you think NOTHING can grow (like plants) below the Sunlight Zone?",
    "visualSvg": '''<svg viewBox="0 0 200 120"><rect x="20" y="10" width="160" height="30" fill="#8FCB9B"/><rect x="20" y="40" width="160" height="70" fill="#071A33"/></svg>''',
    "starters": ["Plants need sunlight, so...", "Below the Sunlight Zone..."],
    "keywords": ["sunlight", "plants", "energy", "dark"]
  },
  "predict": {
    "question": "If a submarine dives from the Sunlight Zone straight to the Midnight Zone, what changes?",
    "explanation": "Going down = losing light AND losing heat at the same time. Both drop together the deeper you go — that's the big pattern of the whole ocean.",
    "choices": [
      {"text": "Nothing — the ocean is the same everywhere", "correct": False},
      {"text": "It gets darker AND colder the deeper it goes", "correct": True},
      {"text": "It gets brighter but colder", "correct": False},
    ]
  }
}
open("ocean-01-cross-section.html", "w", encoding="utf-8").write(build("ocean-01-cross-section", "Ocean: Cross Section 🌊", c1_data))
print("built ocean-01-cross-section.html")

# ================= CONCEPT 2: TEMPERATURE VS DEPTH =================
c2_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 220" role="img" aria-label="Line graph of temperature dropping fast as depth increases, showing the thermocline">
      <line x1="50" y1="20" x2="50" y2="190" stroke="#0B2545" stroke-width="2"/>
      <line x1="50" y1="190" x2="280" y2="190" stroke="#0B2545" stroke-width="2"/>
      <text x="10" y="20" font-size="11" fill="#0B2545">Depth</text>
      <text x="250" y="210" font-size="11" fill="#0B2545">Temp →</text>
      <path d="M240 30 Q230 90 100 140 T60 180" fill="none" stroke="#D9603B" stroke-width="3"/>
      <text x="150" y="105" font-size="11" fill="#2E6E62">← thermocline (steep drop)</text>
    </svg>''',
    "question": "Look at the graph. Where does temperature drop the FASTEST?",
    "explanation": "That steep middle section is the thermocline — a narrow band where warm surface water meets cold deep water and temperature nose-dives.",
    "choices": [
      {"text": "The steep middle section (thermocline)", "correct": True},
      {"text": "It drops evenly the whole way down", "correct": False},
      {"text": "Right at the very bottom", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"warm_surface","name":"Warm surface water","icon":ICON_THERMOMETER_HOT,"fact":"🔥 Sun heats the top layer directly — it's the warmest water in the ocean."},
    {"id":"thermocline","name":"Thermocline","icon":ICON_LAYER_SPLIT,"fact":"⚡ The fast-change zone — temperature drops hard here, like a cliff-edge on the graph."},
    {"id":"cold_deep","name":"Cold deep water","icon":ICON_THERMOMETER_COLD,"fact":"🧊 Barely above freezing. Sunlight never warms it."},
  ]},
  "draw": {
    "prompt": "Draw the temperature graph: start warm (top), then a STEEP drop in the middle, then flat and cold at the bottom.",
    "hintSvg": '''<svg viewBox="0 0 300 220" role="img" aria-label="hint">
      <line x1="50" y1="20" x2="50" y2="190" stroke="#0B2545" stroke-width="2"/>
      <line x1="50" y1="190" x2="280" y2="190" stroke="#0B2545" stroke-width="2"/>
      <path d="M240 30 Q230 90 100 140 T60 180" fill="none" stroke="#D9603B" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the graph. Does the STEEP part stay in the same relative spot, or move?",
    "svg": '''<line x1="40" y1="15" x2="40" y2="150" stroke="#0B2545" stroke-width="2"/>
      <line x1="40" y1="150" x2="220" y2="150" stroke="#0B2545" stroke-width="2"/>
      <path d="M190 25 Q180 70 90 110 T50 140" fill="none" stroke="#D9603B" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the graph that shows a THERMOCLINE (a fast, steep temperature drop).",
    "explanation": "A real thermocline is a sharp bend, not a smooth line — that steep bend is the fast-change zone.",
    "choices": [
      {"label":"A — steep sudden drop", "svg": '''<svg viewBox="0 0 200 140"><line x1="30" y1="10" x2="30" y2="120" stroke="#0B2545" stroke-width="2"/><path d="M170 20 Q160 60 60 90 T40 115" fill="none" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": True},
      {"label":"B — smooth straight line", "svg": '''<svg viewBox="0 0 200 140"><line x1="30" y1="10" x2="30" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="170" y1="20" x2="40" y2="115" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Sun warms the surface", "icon": ICON_THERMOMETER_HOT},
    {"text":"Warm water is less dense, so it floats on top", "icon": ICON_LAYER_SPLIT},
    {"text":"Cold, dense water sinks and stays deep", "icon": ICON_THERMOMETER_COLD},
    {"text":"🔗 Links to Titanic Density Triangle: same rule — less dense stuff floats above denser stuff", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does warm water float ABOVE cold water instead of the two mixing evenly?",
    "visualSvg": '''<svg viewBox="0 0 200 120"><rect x="20" y="10" width="160" height="45" fill="#D9603B" opacity="0.6"/><rect x="20" y="55" width="160" height="55" fill="#2E6E62" opacity="0.6"/></svg>''',
    "starters": ["Warm water floats because...", "Density decides..."],
    "keywords": ["density", "warm", "cold", "float"]
  },
  "predict": {
    "question": "A submarine drops a temperature sensor straight down. What pattern will it record?",
    "explanation": "Warm near the top, a steep thermocline drop in the middle, then flat and freezing near the bottom — that's the classic pattern almost everywhere in the open ocean.",
    "choices": [
      {"text": "Warm the whole way down", "correct": False},
      {"text": "Warm → steep drop → cold and flat", "correct": True},
      {"text": "Random ups and downs with no pattern", "correct": False},
    ]
  }
}
open("ocean-02-temperature-vs-depth.html", "w", encoding="utf-8").write(build("ocean-02-temperature-vs-depth", "Ocean: Temperature vs Depth 🌡️", c2_data))
print("built ocean-02-temperature-vs-depth.html")

# ================= CONCEPT 3: SALINITY VS DEPTH =================
c3_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 220" role="img" aria-label="Diagram showing salt grains sinking through water to settle in denser layers below">
      <rect x="30" y="20" width="240" height="170" fill="#B9D8EA" opacity="0.4" stroke="#0B2545" stroke-width="2"/>
      <circle cx="80" cy="50" r="4" fill="#F3EEE1" stroke="#0B2545"/>
      <circle cx="150" cy="60" r="4" fill="#F3EEE1" stroke="#0B2545"/>
      <circle cx="200" cy="45" r="4" fill="#F3EEE1" stroke="#0B2545"/>
      <path d="M80 54 L85 150" stroke="#0B2545" stroke-width="1" stroke-dasharray="2 3"/>
      <path d="M150 64 L145 155" stroke="#0B2545" stroke-width="1" stroke-dasharray="2 3"/>
      <rect x="30" y="150" width="240" height="40" fill="#1B3A5C" opacity="0.7"/>
      <text x="40" y="175" font-size="11" fill="#F3EEE1">salty, dense water</text>
    </svg>''',
    "question": "Salty water is denser than fresh water. Where does the saltiest water end up?",
    "explanation": "Denser fluids sink below less-dense ones — that's why the saltiest, heaviest water pools down deep, not at the surface.",
    "choices": [
      {"text": "Near the bottom (denser water sinks)", "correct": True},
      {"text": "At the very top (denser water floats)", "correct": False},
      {"text": "Salt has no effect on where water sits", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"salt","name":"Salt (dissolved)","icon":ICON_SALT_GRAIN,"fact":"🧂 Salt dissolved in water adds mass without adding much extra volume — that makes the water denser."},
    {"id":"halocline","name":"Halocline","icon":ICON_LAYER_SPLIT,"fact":"⚡ The zone where saltiness jumps quickly with depth — salinity's version of the thermocline."},
    {"id":"dense_layer","name":"Dense salty layer","icon":ICON_DOWN_ARROW_HEAVY,"fact":"⬇️ The heaviest, saltiest water settles at the bottom of the layer stack."},
  ]},
  "draw": {
    "prompt": "Draw salt grains dissolving near the surface, then sinking down into a denser layer below. Use arrows to show the sinking!",
    "hintSvg": '''<svg viewBox="0 0 300 220" role="img" aria-label="hint">
      <rect x="30" y="20" width="240" height="170" fill="#B9D8EA" opacity="0.4" stroke="#0B2545" stroke-width="2"/>
      <circle cx="80" cy="50" r="4" fill="#F3EEE1" stroke="#0B2545"/>
      <circle cx="150" cy="60" r="4" fill="#F3EEE1" stroke="#0B2545"/>
      <rect x="30" y="150" width="240" height="40" fill="#1B3A5C" opacity="0.7"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Flip the tank upside down. Does the salty layer float to the new 'top', or does it fight to sink again?",
    "svg": '''<rect x="20" y="15" width="200" height="140" fill="#B9D8EA" opacity="0.4" stroke="#0B2545" stroke-width="2"/>
      <rect x="20" y="115" width="200" height="40" fill="#1B3A5C" opacity="0.7"/>'''
  },
  "compare": {
    "question": "Tap the tank that shows salty water sitting BELOW fresh water (correct density stacking).",
    "explanation": "Denser salty water always settles underneath — if you shook it up, it would separate back into this same order.",
    "choices": [
      {"label":"A — salty layer on the bottom", "svg": '''<svg viewBox="0 0 200 140"><rect x="20" y="10" width="160" height="60" fill="#B9D8EA" opacity="0.5" stroke="#0B2545" stroke-width="2"/><rect x="20" y="70" width="160" height="55" fill="#1B3A5C" opacity="0.8" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — salty layer on the top", "svg": '''<svg viewBox="0 0 200 140"><rect x="20" y="10" width="160" height="55" fill="#1B3A5C" opacity="0.8" stroke="#0B2545" stroke-width="2"/><rect x="20" y="65" width="160" height="60" fill="#B9D8EA" opacity="0.5" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Salt dissolves into the water", "icon": ICON_SALT_GRAIN},
    {"text":"Saltier water = denser water", "icon": ICON_SCALE_SALT},
    {"text":"Denser water sinks below lighter water", "icon": ICON_DOWN_ARROW_HEAVY},
    {"text":"🔗 Links to Ocean Temperature vs Depth: temperature AND salinity both control density together", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Both temperature and salt change water's density. Which one do you think matters more near icebergs, and why?",
    "visualSvg": '''<svg viewBox="0 0 200 120"><rect x="20" y="10" width="160" height="45" fill="#B9D8EA" opacity="0.5"/><rect x="20" y="55" width="160" height="55" fill="#1B3A5C" opacity="0.8"/></svg>''',
    "starters": ["I think temperature/salt matters more because...", "Near icebergs, the water is..."],
    "keywords": ["density", "salt", "temperature", "sink"]
  },
  "predict": {
    "question": "You pour a cup of super-salty water gently into a tank of plain fresh water. What happens?",
    "explanation": "Being denser, the salty water sinks straight to the bottom instead of mixing evenly — you'd actually see it sink as a visible blob before it gradually diffuses.",
    "choices": [
      {"text": "It instantly mixes evenly", "correct": False},
      {"text": "It sinks to the bottom because it's denser", "correct": True},
      {"text": "It floats on top because it's denser", "correct": False},
    ]
  }
}
open("ocean-03-salinity-vs-depth.html", "w", encoding="utf-8").write(build("ocean-03-salinity-vs-depth", "Ocean: Salinity vs Depth 🧂", c3_data))
print("built ocean-03-salinity-vs-depth.html")

# ================= CONCEPT 4: WAVE ANATOMY =================
c4_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 180" role="img" aria-label="Ocean wave diagram showing crest, trough, wavelength and amplitude">
      <path d="M10 100 Q50 40 90 100 T170 100 T250 100 T330 100 T400 100" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <line x1="200" y1="100" x2="200" y2="150" stroke="#0B2545" stroke-width="1" stroke-dasharray="3 3"/>
      <text x="45" y="35" font-size="11" fill="#D9603B">crest</text>
      <text x="120" y="150" font-size="11" fill="#D9603B">trough</text>
      <line x1="50" y1="160" x2="130" y2="160" stroke="#0B2545"/>
      <text x="55" y="172" font-size="10" fill="#0B2545">wavelength</text>
    </svg>''',
    "question": "The crest is the TOP of the wave. What's the very BOTTOM point called?",
    "explanation": "Crest = the peak (highest point). Trough = the valley (lowest point). They alternate all along the wave.",
    "choices": [
      {"text": "The trough", "correct": True},
      {"text": "The crest", "correct": False},
      {"text": "The wavelength", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"crest","name":"Crest","icon":ICON_CREST,"fact":"⛰️ The highest point of the wave."},
    {"id":"trough","name":"Trough","icon":ICON_TROUGH,"fact":"🕳️ The lowest point of the wave."},
    {"id":"wavelength","name":"Wavelength","icon":ICON_WAVELENGTH,"fact":"📏 The distance from one crest to the next crest."},
    {"id":"amplitude","name":"Amplitude","icon":ICON_AMPLITUDE,"fact":"📈 How TALL the wave is — measured from the middle to the crest."},
  ]},
  "draw": {
    "prompt": "Draw one full wave. Label the crest, trough, wavelength, and amplitude. Bigger amplitude = a scarier wave!",
    "hintSvg": '''<svg viewBox="0 0 400 180" role="img" aria-label="hint">
      <path d="M10 100 Q50 40 90 100 T170 100 T250 100 T330 100 T400 100" fill="none" stroke="#2E6E62" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Flip the wave upside down. Do the crests and troughs SWAP places?",
    "svg": '''<path d="M10 90 Q50 30 90 90 T170 90 T250 90 T330 90" fill="none" stroke="#2E6E62" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the wave with the BIGGER amplitude (taller wave, same wavelength).",
    "explanation": "Amplitude measures height — a bigger amplitude means a taller, more powerful wave, even if the wavelength (spacing) is the same.",
    "choices": [
      {"label":"A — tall wave", "svg": '''<svg viewBox="0 0 200 140"><path d="M10 70 Q40 10 70 70 T130 70 T190 70" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": True},
      {"label":"B — flat wave", "svg": '''<svg viewBox="0 0 200 140"><path d="M10 70 Q40 55 70 70 T130 70 T190 70" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Wind blows across the ocean surface", "icon": ICON_WAVELENGTH},
    {"text":"Energy transfers into the water, making it rise and fall", "icon": ICON_CREST},
    {"text":"Bigger wind energy = bigger amplitude = bigger waves", "icon": ICON_AMPLITUDE},
    {"text":"🔗 Links to Titanic Speed-Time Graph: both are graphs showing a pattern changing over distance/time", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "A storm makes wind much stronger. What happens to the wave's amplitude, and why does that matter for a ship like the Titanic?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M10 55 Q40 10 70 55 T130 55 T190 55" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''',
    "starters": ["Stronger wind means...", "For a ship, bigger waves would..."],
    "keywords": ["amplitude", "energy", "wind", "ship"]
  },
  "predict": {
    "question": "Wind speed doubles during a storm. What most likely happens to the waves?",
    "explanation": "More wind energy pumps into the water, so amplitude (wave height) increases — that's exactly why storms create dangerously tall waves for ships.",
    "choices": [
      {"text": "Waves get taller (bigger amplitude)", "correct": True},
      {"text": "Waves disappear completely", "correct": False},
      {"text": "Waves stay exactly the same size", "correct": False},
    ]
  }
}
open("ocean-04-wave-anatomy.html", "w", encoding="utf-8").write(build("ocean-04-wave-anatomy", "Ocean: Wave Anatomy 🌊", c4_data))
print("built ocean-04-wave-anatomy.html")
