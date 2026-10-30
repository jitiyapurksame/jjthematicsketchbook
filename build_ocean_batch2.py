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

# ---------------- shared icons ----------------
ICON_SHIP_PITCH = "<svg viewBox='0 0 40 40'><path d='M6 22 L34 22 L30 30 L10 30 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2' transform='rotate(-8 20 26)'/><rect x='16' y='10' width='6' height='12' fill='#D9603B' transform='rotate(-8 20 26)'/></svg>"
ICON_WAVE_BIG = "<svg viewBox='0 0 40 40'><path d='M2 26 Q10 6 18 26 T34 26' fill='none' stroke='#2E6E62' stroke-width='4'/></svg>"
ICON_ROLL = "<svg viewBox='0 0 40 40'><ellipse cx='20' cy='24' rx='16' ry='8' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><path d='M8 24 Q20 12 32 24' fill='none' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_SWAMP = "<svg viewBox='0 0 40 40'><path d='M4 20 L36 20 L30 30 L10 30 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><path d='M2 14 Q10 4 18 14 T34 14' fill='#2E6E62' opacity='0.7'/></svg>"
ICON_CONVEYOR_ARROW = "<svg viewBox='0 0 40 40'><path d='M4 30 Q20 4 36 30' fill='none' stroke='#0B2545' stroke-width='3'/><path d='M28 24 L36 30 L30 36' fill='none' stroke='#0B2545' stroke-width='3'/></svg>"
ICON_POLAR_SINK = "<svg viewBox='0 0 40 40'><rect x='4' y='4' width='32' height='12' fill='#B9D8EA' stroke='#0B2545' stroke-width='2'/><path d='M20 16 L20 34' stroke='#0B2545' stroke-width='3'/><path d='M14 28 L20 36 L26 28' fill='#0B2545'/></svg>"
ICON_TROPIC_RISE = "<svg viewBox='0 0 40 40'><rect x='4' y='24' width='32' height='12' fill='#D9603B' opacity='0.6' stroke='#0B2545' stroke-width='2'/><path d='M20 24 L20 6' stroke='#0B2545' stroke-width='3'/><path d='M14 12 L20 4 L26 12' fill='#0B2545'/></svg>"
ICON_GLOBE_LOOP = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='16' fill='none' stroke='#0B2545' stroke-width='2'/><path d='M6 14 Q20 4 34 14 Q20 24 6 14' fill='none' stroke='#2E6E62' stroke-width='2'/><path d='M6 26 Q20 36 34 26' fill='none' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_DENSE_DROP = "<svg viewBox='0 0 40 40'><path d='M20 4 Q28 20 20 30 Q12 20 20 4 Z' fill='#1B3A5C' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_LIGHT_DROP = "<svg viewBox='0 0 40 40'><path d='M20 4 Q28 20 20 30 Q12 20 20 4 Z' fill='#B9D8EA' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_CURRENT_FLOW = "<svg viewBox='0 0 40 40'><path d='M4 12 Q20 2 36 12' fill='none' stroke='#2E6E62' stroke-width='3'/><path d='M4 20 Q20 10 36 20' fill='none' stroke='#2E6E62' stroke-width='2' opacity='0.6'/><path d='M28 6 L36 12 L28 18' fill='none' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_ICE_FRESH = "<svg viewBox='0 0 40 40'><path d='M20 4 L24 14 L34 14 L26 20 L29 30 L20 24 L11 30 L14 20 L6 14 L16 14 Z' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_ICE_FLOAT = "<svg viewBox='0 0 40 40'><rect x='4' y='20' width='32' height='14' fill='#B9D8EA' opacity='0.5'/><path d='M12 22 L16 10 L24 10 L28 22 Z' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_ICEBERG_TIP = "<svg viewBox='0 0 40 40'><path d='M10 22 L20 6 L30 22 Z' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><path d='M6 22 L34 22 L28 36 L12 36 Z' fill='#B9D8EA' opacity='0.6' stroke='#2E6E62' stroke-width='1.5' stroke-dasharray='3 2'/></svg>"
ICON_LINK = "<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/><circle cx='26' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"

# ================= CONCEPT 5: TITANIC + WAVES =================
c5_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 200" role="img" aria-label="Ship tilting up and down as it crosses wave crests and troughs">
      <path d="M0 130 Q40 100 80 130 T160 130 T240 130 T320 130 T400 130" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <g transform="translate(150,90) rotate(-10)">
        <path d="M-40 20 L40 20 L30 35 L-30 35 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
        <rect x="-8" y="-2" width="6" height="22" fill="#D9603B"/>
      </g>
      <text x="200" y="180" text-anchor="middle" font-size="12" fill="#2E6E62">ship tilts to match the wave shape</text>
    </svg>''',
    "question": "As the ship crosses a wave, what happens to it?",
    "explanation": "The ship's front and back rise and fall to match the crest and trough underneath it — it literally follows the wave's shape (this up-down tilt is called pitching).",
    "choices": [
      {"text": "It tilts up and down, matching the wave", "correct": True},
      {"text": "It stays perfectly flat no matter what", "correct": False},
      {"text": "It sinks every time a wave passes", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"pitch","name":"Pitching","icon":ICON_SHIP_PITCH,"fact":"⬆️⬇️ Bow and stern rocking up and down as waves pass under the ship."},
    {"id":"roll","name":"Rolling","icon":ICON_ROLL,"fact":"↔️ Side-to-side tilting, caused by waves hitting the ship's side."},
    {"id":"swamp","name":"Swamping","icon":ICON_SWAMP,"fact":"🌊💥 A wave taller than the deck crashes straight over the top."},
    {"id":"amplitude_link","name":"Big amplitude waves","icon":ICON_WAVE_BIG,"fact":"📈 Taller waves (bigger amplitude) mean rougher pitching and rolling."},
  ]},
  "draw": {
    "prompt": "Draw a wave under a ship. Tilt the ship's bow up on the crest and down in the trough — show the pitch!",
    "hintSvg": '''<svg viewBox="0 0 400 200" role="img" aria-label="hint">
      <path d="M0 130 Q40 100 80 130 T160 130 T240 130 T320 130 T400 130" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <g transform="translate(150,90) rotate(-10)"><path d="M-40 20 L40 20 L30 35 L-30 35 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></g>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the ship+wave picture. Does the tilt direction of the ship stay linked to the wave, or does it stay fixed?",
    "svg": '''<path d="M20 110 Q50 90 80 110 T140 110 T200 110" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <g transform="translate(110,80) rotate(-8)"><path d="M-30 15 L30 15 L22 26 L-22 26 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></g>'''
  },
  "compare": {
    "question": "Tap the picture showing a wave BIG enough to swamp (wash over) the deck.",
    "explanation": "When wave height goes above the deck line, water pours straight over the top — that's swamping, and it's exactly the danger bigger amplitude waves create.",
    "choices": [
      {"label":"A — wave stays below deck", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="70" width="140" height="30" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><path d="M20 100 Q60 90 100 100 T180 100" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
      {"label":"B — wave crashes over deck", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="70" width="140" height="30" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><path d="M20 40 Q60 10 100 40 T180 40" fill="none" stroke="#2E6E62" stroke-width="4"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Storm winds pump energy into the water", "icon": ICON_WAVE_BIG},
    {"text":"Amplitude (wave height) grows", "icon": ICON_SHIP_PITCH},
    {"text":"Bigger waves rock, roll, and can swamp the ship", "icon": ICON_SWAMP},
    {"text":"🔗 Links to Ocean Wave Anatomy: amplitude is the exact number that decides how rough this gets", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why do you think a ship built LOW and WIDE (like a cargo barge) handles rough waves differently than one built TALL and NARROW?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M10 60 Q40 30 70 60 T130 60 T190 60" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''',
    "starters": ["A low, wide ship would...", "A tall, narrow ship would..."],
    "keywords": ["amplitude", "pitch", "roll", "stability"]
  },
  "predict": {
    "question": "A ship sails from calm water into a storm where wave amplitude triples. What should the crew expect?",
    "explanation": "Tripling amplitude means much rougher pitching and rolling, and a real risk of waves reaching high enough to swamp the deck — bigger amplitude always means a rougher, more dangerous ride.",
    "choices": [
      {"text": "Smoother sailing than before", "correct": False},
      {"text": "Much rougher pitching/rolling and a swamping risk", "correct": True},
      {"text": "No noticeable difference", "correct": False},
    ]
  }
}
open("ocean-05-titanic-and-waves.html", "w", encoding="utf-8").write(build("ocean-05-titanic-and-waves", "Ocean: Titanic + Waves 🚢🌊", c5_data))
print("built ocean-05-titanic-and-waves.html")

# ================= CONCEPT 6: GLOBAL OCEAN CONVEYOR =================
c6_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 400 220" role="img" aria-label="Global map style loop showing cold dense water sinking at poles and warm water rising near the equator, connected by a giant loop">
      <ellipse cx="200" cy="110" rx="170" ry="80" fill="none" stroke="#0B2545" stroke-width="2" stroke-dasharray="6 4"/>
      <rect x="20" y="20" width="60" height="20" fill="#B9D8EA" stroke="#0B2545" stroke-width="1.5"/>
      <text x="24" y="15" font-size="11" fill="#0B2545">Polar (cold, salty)</text>
      <path d="M50 40 L50 100" stroke="#0B2545" stroke-width="3"/>
      <path d="M42 90 L50 104 L58 90" fill="#0B2545"/>
      <rect x="320" y="180" width="60" height="20" fill="#D9603B" opacity="0.6" stroke="#0B2545" stroke-width="1.5"/>
      <text x="300" y="215" font-size="11" fill="#0B2545">Tropics (warm)</text>
      <path d="M350 178 L350 120" stroke="#0B2545" stroke-width="3"/>
      <path d="M342 130 L350 116 L358 130" fill="#0B2545"/>
    </svg>''',
    "question": "This giant loop is powered by density differences. Where does water SINK to start the loop?",
    "explanation": "Near the poles, water is cold AND extra salty (because sea ice forms and leaves the salt behind) — that makes it very dense, so it sinks and starts the whole global conveyor moving.",
    "choices": [
      {"text": "At the poles (cold + salty = dense)", "correct": True},
      {"text": "At the equator (warm = dense)", "correct": False},
      {"text": "Density has nothing to do with it", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"polar_sink","name":"Polar sinking","icon":ICON_POLAR_SINK,"fact":"⬇️ Cold, salty, dense water sinks near the poles — this is the engine that starts everything."},
    {"id":"tropic_rise","name":"Tropical rising","icon":ICON_TROPIC_RISE,"fact":"⬆️ Warm water near the equator is less dense and rises to replace sinking water elsewhere."},
    {"id":"conveyor","name":"The conveyor loop","icon":ICON_GLOBE_LOOP,"fact":"🔄 One giant loop connecting every ocean — it takes roughly 1,000 years to go all the way around."},
    {"id":"conveyor_arrow","name":"Deep current flow","icon":ICON_CONVEYOR_ARROW,"fact":"➡️ Deep, cold, dense water flows along the ocean floor toward the tropics."},
  ]},
  "draw": {
    "prompt": "Draw the loop: cold dense water sinking at one end, warm water rising at the other, connected by arrows going both ways.",
    "hintSvg": '''<svg viewBox="0 0 400 220" role="img" aria-label="hint">
      <ellipse cx="200" cy="110" rx="170" ry="80" fill="none" stroke="#0B2545" stroke-width="2" stroke-dasharray="6 4"/>
      <rect x="20" y="20" width="60" height="20" fill="#B9D8EA" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="320" y="180" width="60" height="20" fill="#D9603B" opacity="0.6" stroke="#0B2545" stroke-width="1.5"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the loop diagram. Does 'sinking = cold/dense' and 'rising = warm/light' stay true no matter how you turn it?",
    "svg": '''<ellipse cx="140" cy="90" rx="110" ry="60" fill="none" stroke="#0B2545" stroke-width="2" stroke-dasharray="6 4"/>
      <rect x="20" y="20" width="40" height="16" fill="#B9D8EA" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="220" y="130" width="40" height="16" fill="#D9603B" opacity="0.6" stroke="#0B2545" stroke-width="1.5"/>'''
  },
  "compare": {
    "question": "Tap the picture showing the CORRECT sinking spot for the conveyor (cold + salty).",
    "explanation": "Only cold + salty water is dense enough to sink and drive the conveyor — warm water always rises instead.",
    "choices": [
      {"label":"A — cold polar water sinking", "svg": '''<svg viewBox="0 0 200 140"><rect x="60" y="10" width="80" height="20" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/><path d="M100 30 L100 110" stroke="#0B2545" stroke-width="3"/><path d="M92 98 L100 112 L108 98" fill="#0B2545"/></svg>''', "correct": True},
      {"label":"B — warm tropical water sinking", "svg": '''<svg viewBox="0 0 200 140"><rect x="60" y="10" width="80" height="20" fill="#D9603B" opacity="0.6" stroke="#0B2545" stroke-width="2"/><path d="M100 30 L100 110" stroke="#0B2545" stroke-width="3"/><path d="M92 98 L100 112 L108 98" fill="#0B2545"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Cold + salty water becomes extra dense at the poles", "icon": ICON_POLAR_SINK},
    {"text":"Dense water sinks and creeps along the ocean floor", "icon": ICON_CONVEYOR_ARROW},
    {"text":"Warm water rises near the tropics to take its place", "icon": ICON_TROPIC_RISE},
    {"text":"🔗 Links to Salinity vs Depth: it's the SAME density rule, just powering a whole planet-sized loop", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "If the poles suddenly got warmer and less salty (melting ice adds fresh water), what might happen to the conveyor?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><ellipse cx="100" cy="50" rx="80" ry="35" fill="none" stroke="#0B2545" stroke-width="2" stroke-dasharray="5 3"/></svg>''',
    "starters": ["If polar water got warmer and less salty...", "The conveyor might..."],
    "keywords": ["density", "sink", "melt", "conveyor"]
  },
  "predict": {
    "question": "Melting polar ice adds a lot of fresh water to the poles. What's the most likely effect on the conveyor?",
    "explanation": "Fresh water is less dense than salty water, so adding lots of it makes polar water less able to sink — that can slow down or even weaken the entire global conveyor.",
    "choices": [
      {"text": "The conveyor speeds up a lot", "correct": False},
      {"text": "The conveyor could slow down, since polar water sinks less easily", "correct": True},
      {"text": "Nothing changes — melting ice has no effect", "correct": False},
    ]
  }
}
open("ocean-06-global-conveyor.html", "w", encoding="utf-8").write(build("ocean-06-global-conveyor", "Ocean: Global Conveyor 🔄", c6_data))
print("built ocean-06-global-conveyor.html")

# ================= CONCEPT 7: DENSITY → CURRENT =================
c7_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Two water masses of different density with an arrow showing current flowing from dense to less dense region">
      <rect x="20" y="30" width="110" height="140" fill="#1B3A5C" opacity="0.75" stroke="#0B2545" stroke-width="2"/>
      <rect x="170" y="30" width="110" height="140" fill="#B9D8EA" opacity="0.5" stroke="#0B2545" stroke-width="2"/>
      <text x="30" y="20" font-size="11" fill="#0B2545">dense (cold/salty)</text>
      <text x="180" y="20" font-size="11" fill="#0B2545">less dense (warm/fresh)</text>
      <path d="M135 100 L165 100" stroke="#D9603B" stroke-width="4"/>
      <path d="M155 92 L168 100 L155 108" fill="#D9603B"/>
    </svg>''',
    "question": "Two water masses of different density sit next to each other. Which way does the current flow?",
    "explanation": "Density differences create pressure differences — water moves from the denser (heavier, lower) side, pushing underneath and sliding toward the less dense side. That flow of water IS a current.",
    "choices": [
      {"text": "From the denser water toward the less dense water", "correct": True},
      {"text": "From the less dense water toward the denser water", "correct": False},
      {"text": "Density doesn't affect current direction", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"dense_mass","name":"Dense water mass","icon":ICON_DENSE_DROP,"fact":"⬛ Cold and/or salty — heavier, sits lower, pushes outward underneath."},
    {"id":"light_mass","name":"Less dense water mass","icon":ICON_LIGHT_DROP,"fact":"🟦 Warm and/or fresh — lighter, floats higher, gets pushed aside."},
    {"id":"current_flow","name":"Current","icon":ICON_CURRENT_FLOW,"fact":"➡️ Moving water, driven by the density difference trying to even itself out."},
  ]},
  "draw": {
    "prompt": "Draw two side-by-side blocks of water (one dense, one light) with an arrow showing which way the current flows between them.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <rect x="20" y="30" width="110" height="140" fill="#1B3A5C" opacity="0.75" stroke="#0B2545" stroke-width="2"/>
      <rect x="170" y="30" width="110" height="140" fill="#B9D8EA" opacity="0.5" stroke="#0B2545" stroke-width="2"/>
      <path d="M135 100 L165 100" stroke="#D9603B" stroke-width="4"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the two blocks. Does the current still flow FROM dense TOWARD less-dense, or does the rule flip?",
    "svg": '''<rect x="20" y="30" width="90" height="110" fill="#1B3A5C" opacity="0.75" stroke="#0B2545" stroke-width="2"/>
      <rect x="130" y="30" width="90" height="110" fill="#B9D8EA" opacity="0.5" stroke="#0B2545" stroke-width="2"/>
      <path d="M112 85 L128 85" stroke="#D9603B" stroke-width="4"/>'''
  },
  "compare": {
    "question": "Tap the picture with the current arrow pointing the CORRECT direction (dense → less dense).",
    "explanation": "Current always flows away from the denser mass, not toward it — the denser water is doing the pushing.",
    "choices": [
      {"label":"A — arrow from dense to light", "svg": '''<svg viewBox="0 0 200 140"><rect x="10" y="20" width="80" height="100" fill="#1B3A5C" opacity="0.75"/><rect x="110" y="20" width="80" height="100" fill="#B9D8EA" opacity="0.5"/><path d="M92 70 L108 70" stroke="#D9603B" stroke-width="4"/><path d="M100 62 L110 70 L100 78" fill="#D9603B"/></svg>''', "correct": True},
      {"label":"B — arrow from light to dense", "svg": '''<svg viewBox="0 0 200 140"><rect x="10" y="20" width="80" height="100" fill="#1B3A5C" opacity="0.75"/><rect x="110" y="20" width="80" height="100" fill="#B9D8EA" opacity="0.5"/><path d="M108 70 L92 70" stroke="#D9603B" stroke-width="4"/><path d="M100 62 L90 70 L100 78" fill="#D9603B"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Temperature and salt both change density", "icon": ICON_DENSE_DROP},
    {"text":"Two water masses next to each other end up different densities", "icon": ICON_LIGHT_DROP},
    {"text":"Water flows from dense to less-dense, creating a current", "icon": ICON_CURRENT_FLOW},
    {"text":"🔗 Links to Global Conveyor: this small dense→light flow is the exact same rule driving the WHOLE planet's current system", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Ocean Temperature vs Depth and Salinity vs Depth both change density. Explain in your own words how those two ideas combine to CREATE a current.",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="10" y="10" width="80" height="80" fill="#1B3A5C" opacity="0.75"/><rect x="110" y="10" width="80" height="80" fill="#B9D8EA" opacity="0.5"/></svg>''',
    "starters": ["Temperature and salinity both...", "When two water masses have different density..."],
    "keywords": ["density", "temperature", "salinity", "current"]
  },
  "predict": {
    "question": "A river dumps a huge amount of warm fresh water into a patch of cold salty ocean. What current pattern forms?",
    "explanation": "The river water is much less dense (warm + fresh), so it stays near the surface and spreads outward, while the colder saltier ocean water pushes in and sinks beneath it — a small current forms right at that boundary.",
    "choices": [
      {"text": "The river water sinks and the ocean water floats", "correct": False},
      {"text": "The river water spreads out on top; denser ocean water pushes in underneath", "correct": True},
      {"text": "Nothing happens — they instantly mix perfectly evenly", "correct": False},
    ]
  }
}
open("ocean-07-density-to-current.html", "w", encoding="utf-8").write(build("ocean-07-density-to-current", "Ocean: Density → Current ⚡", c7_data))
print("built ocean-07-density-to-current.html")

# ================= CONCEPT 8: ICEBERG FORMATION (FRESH VS SALT ICE) =================
c8_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Iceberg floating in ocean water, showing most of its mass hidden below the surface">
      <rect x="10" y="110" width="280" height="70" fill="#1B3A5C" opacity="0.6"/>
      <path d="M100 60 L140 15 L180 60 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/>
      <path d="M80 110 L100 60 L180 60 L200 110 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="1.5"/>
      <path d="M80 110 L60 175 L220 175 L200 110 Z" fill="#B9D8EA" opacity="0.7" stroke="#2E6E62" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="10" y1="110" x2="290" y2="110" stroke="#0B2545" stroke-width="1.5" stroke-dasharray="5 3"/>
      <text x="240" y="105" font-size="11" fill="#0B2545">waterline</text>
    </svg>''',
    "question": "About how much of an iceberg is hidden UNDERWATER?",
    "explanation": "Ice is only slightly less dense than seawater, so only a small fraction pokes above the surface — roughly 90% of an iceberg's bulk is hidden below the waterline.",
    "choices": [
      {"text": "About 90% — most of it is hidden", "correct": True},
      {"text": "About 50% — half and half", "correct": False},
      {"text": "About 10% — most of it sticks up", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"tip","name":"Visible tip","icon":ICON_ICEBERG_TIP,"fact":"👁️ The small part above water — what lookouts on a ship can actually see."},
    {"id":"hidden_mass","name":"Hidden underwater mass","icon":ICON_ICE_FLOAT,"fact":"🙈 The huge chunk below the waterline — invisible from a ship's deck at night."},
    {"id":"fresh_ice","name":"Freshwater ice","icon":ICON_ICE_FRESH,"fact":"❄️ Icebergs form from glaciers/snow — almost pure freshwater, even though they float in salty ocean."},
  ]},
  "draw": {
    "prompt": "Draw an iceberg with a dashed waterline. Make the underwater part MUCH bigger than the tip above water.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <rect x="10" y="110" width="280" height="70" fill="#1B3A5C" opacity="0.6"/>
      <path d="M100 60 L140 15 L180 60 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/>
      <path d="M80 110 L60 175 L220 175 L200 110 Z" fill="#B9D8EA" opacity="0.7" stroke="#2E6E62" stroke-width="1.5" stroke-dasharray="4 3"/>
      <line x1="10" y1="110" x2="290" y2="110" stroke="#0B2545" stroke-width="1.5" stroke-dasharray="5 3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the iceberg. Does the underwater part stay the BIGGER chunk, or does rotating change the proportion?",
    "svg": '''<rect x="20" y="90" width="220" height="55" fill="#1B3A5C" opacity="0.6"/>
      <path d="M90 90 L120 50 L150 90 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/>
      <path d="M70 90 L55 140 L180 140 L165 90 Z" fill="#B9D8EA" opacity="0.7" stroke="#2E6E62" stroke-width="1.5" stroke-dasharray="4 3"/>'''
  },
  "compare": {
    "question": "Tap the picture that correctly shows iceberg proportions (mostly hidden underwater).",
    "explanation": "Real icebergs are almost entirely underwater — a picture where most of the ice sticks up above the surface has the proportions backwards.",
    "choices": [
      {"label":"A — small tip, huge underwater mass", "svg": '''<svg viewBox="0 0 200 140"><rect x="10" y="60" width="180" height="60" fill="#1B3A5C" opacity="0.6"/><path d="M80 60 L100 30 L120 60 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/><path d="M60 60 L45 120 L155 120 L140 60 Z" fill="#B9D8EA" opacity="0.7" stroke="#2E6E62" stroke-width="1.5" stroke-dasharray="3 2"/></svg>''', "correct": True},
      {"label":"B — huge tip, small underwater mass", "svg": '''<svg viewBox="0 0 200 140"><rect x="10" y="95" width="180" height="25" fill="#1B3A5C" opacity="0.6"/><path d="M60 95 L100 15 L140 95 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/><path d="M75 95 L70 115 L130 115 L125 95 Z" fill="#B9D8EA" opacity="0.7" stroke="#2E6E62" stroke-width="1.5" stroke-dasharray="3 2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Freshwater ice is slightly less dense than seawater", "icon": ICON_ICE_FRESH},
    {"text":"Being less dense means it floats — but just barely", "icon": ICON_ICE_FLOAT},
    {"text":"Only a small tip pokes above the waterline", "icon": ICON_ICEBERG_TIP},
    {"text":"🔗 Links to Titanic Density Triangle: same mass/volume/density rule that decides how the whole ship floats", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Lookouts on the Titanic could only see the tip of an iceberg. Why is that so dangerous, using what you know about density?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="10" y="55" width="180" height="35" fill="#1B3A5C" opacity="0.6"/><path d="M80 55 L100 25 L120 55 Z" fill="#EAF3F0" stroke="#2E6E62" stroke-width="2"/></svg>''',
    "starters": ["Because most of the iceberg is hidden...", "The visible tip can trick you because..."],
    "keywords": ["density", "hidden", "tip", "danger"]
  },
  "predict": {
    "question": "A lookout spots an iceberg tip that looks small and far away. What should they actually assume about the danger?",
    "explanation": "Since roughly 90% of the iceberg is hidden underwater and often spreads wider than the tip, a 'small' visible tip can still mean a massive, ship-wrecking mass just beneath the surface — never judge an iceberg by its tip alone.",
    "choices": [
      {"text": "It's probably small and not very dangerous", "correct": False},
      {"text": "It could be hiding a huge mass underwater — treat it as a serious hazard", "correct": True},
      {"text": "Icebergs are always exactly the size they appear", "correct": False},
    ]
  }
}
open("ocean-08-iceberg-formation.html", "w", encoding="utf-8").write(build("ocean-08-iceberg-formation", "Ocean: Iceberg Formation 🧊", c8_data))
print("built ocean-08-iceberg-formation.html")
