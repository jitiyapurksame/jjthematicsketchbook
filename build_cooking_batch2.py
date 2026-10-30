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
ICON_OIL_DROPS = "<svg viewBox='0 0 40 40'><circle cx='14' cy='14' r='5' fill='#E4C77C'/><circle cx='26' cy='20' r='4' fill='#E4C77C'/><circle cx='18' cy='28' r='5' fill='#E4C77C'/><rect x='2' y='2' width='36' height='36' fill='none' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_WATER_BG = "<svg viewBox='0 0 40 40'><rect x='2' y='2' width='36' height='36' fill='#B9D8EA' opacity='0.5' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_EMULSIFIER = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='6' fill='#C9A24B'/><line x1='20' y1='14' x2='20' y2='4' stroke='#2E6E62' stroke-width='2'/><line x1='20' y1='26' x2='20' y2='36' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_MAYO_JAR = "<svg viewBox='0 0 40 40'><rect x='8' y='6' width='24' height='30' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><ellipse cx='20' cy='20' rx='8' ry='12' fill='#E4C77C' opacity='0.8'/></svg>"
ICON_BAKING_SODA = "<svg viewBox='0 0 40 40'><rect x='10' y='10' width='20' height='20' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_VINEGAR = "<svg viewBox='0 0 40 40'><path d='M14 4 L26 4 L26 12 L32 32 L8 32 L14 12 Z' fill='#D9603B' opacity='0.5' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_BUBBLES = "<svg viewBox='0 0 40 40'><circle cx='14' cy='14' r='4' fill='none' stroke='#2E6E62' stroke-width='2'/><circle cx='24' cy='22' r='5' fill='none' stroke='#2E6E62' stroke-width='2'/><circle cx='16' cy='28' r='3' fill='none' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_PH_SCALE = "<svg viewBox='0 0 40 40'><rect x='4' y='16' width='32' height='8' fill='#D9603B'/><rect x='4' y='16' width='16' height='8' fill='#2E6E62'/></svg>"
ICON_MARINADE_BOWL = "<svg viewBox='0 0 40 40'><ellipse cx='20' cy='26' rx='16' ry='8' fill='#D9603B' opacity='0.4' stroke='#0B2545' stroke-width='2'/><ellipse cx='20' cy='22' rx='10' ry='6' fill='#8B5E3C'/></svg>"
ICON_DIFFUSE_ARROWS = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='6' fill='#D9603B'/><path d='M20 12 L20 4 M20 28 L20 36 M12 20 L4 20 M28 20 L36 20' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_SALT_IN = "<svg viewBox='0 0 40 40'><rect x='16' y='16' width='8' height='8' fill='#F3EEE1' stroke='#0B2545' stroke-width='1.5' transform='rotate(20 20 20)'/></svg>"
ICON_SUGAR_CRYSTAL = "<svg viewBox='0 0 40 40'><path d='M20 4 L28 12 L28 28 L20 36 L12 28 L12 12 Z' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_SLOW_COOL = "<svg viewBox='0 0 40 40'><path d='M20 4 L32 12 L32 28 L20 36 L8 28 L8 12 Z' fill='none' stroke='#2E6E62' stroke-width='2'/><path d='M20 16 L26 20 L26 26 L20 30 L14 26 L14 20 Z' fill='#2E6E62' opacity='0.5'/></svg>"
ICON_FAST_COOL = "<svg viewBox='0 0 40 40'><circle cx='10' cy='10' r='3' fill='#D9603B'/><circle cx='20' cy='8' r='2.5' fill='#D9603B'/><circle cx='30' cy='14' r='3' fill='#D9603B'/><circle cx='14' cy='22' r='2' fill='#D9603B'/><circle cx='26' cy='26' r='2.5' fill='#D9603B'/><circle cx='8' cy='30' r='2' fill='#D9603B'/><circle cx='22' cy='32' r='2.5' fill='#D9603B'/></svg>"
ICON_LINK = "<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/><circle cx='26' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"
ICON_THERMOMETER = "<svg viewBox='0 0 40 40'><rect x='16' y='4' width='8' height='22' rx='4' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='20' cy='30' r='7' fill='#D9603B' stroke='#0B2545' stroke-width='2'/></svg>"

# ================= CONCEPT 5: EMULSIONS =================
c5_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Mayonnaise jar showing tiny oil droplets evenly suspended throughout water instead of separating into layers">
      <rect x="90" y="20" width="120" height="150" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="120" cy="60" r="8" fill="#E4C77C"/>
      <circle cx="160" cy="80" r="7" fill="#E4C77C"/>
      <circle cx="190" cy="50" r="6" fill="#E4C77C"/>
      <circle cx="130" cy="110" r="7" fill="#E4C77C"/>
      <circle cx="175" cy="130" r="8" fill="#E4C77C"/>
      <circle cx="110" cy="150" r="6" fill="#E4C77C"/>
    </svg>''',
    "question": "In mayonnaise, tiny oil droplets stay spread evenly through the water instead of separating like in an oil-and-water jar. What's holding them apart?",
    "explanation": "An emulsifier (like egg yolk) coats each tiny oil droplet, keeping them from joining back together and rising — that's what makes an emulsion stable instead of separating.",
    "choices": [
      {"text": "An emulsifier coating each droplet", "correct": True},
      {"text": "Nothing — it will separate the same way oil and water do", "correct": False},
      {"text": "The oil turned into water permanently", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"oil_drops","name":"Tiny oil droplets","icon":ICON_OIL_DROPS,"fact":"🟡 Broken into tiny drops instead of one big floating layer."},
    {"id":"emulsifier","name":"Emulsifier","icon":ICON_EMULSIFIER,"fact":"🔗 A molecule with one end that likes oil and one end that likes water — it holds the two together."},
    {"id":"mayo","name":"Stable emulsion","icon":ICON_MAYO_JAR,"fact":"🥚 Mayonnaise: oil droplets trapped in water by egg yolk, staying mixed instead of separating."},
  ]},
  "draw": {
    "prompt": "Draw a jar of mayonnaise: tiny oil circles spread evenly through the water, not stacked in layers.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <rect x="90" y="20" width="120" height="150" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="120" cy="60" r="8" fill="#E4C77C"/>
      <circle cx="160" cy="80" r="7" fill="#E4C77C"/>
      <circle cx="130" cy="110" r="7" fill="#E4C77C"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the jar. Do the oil droplets stay spread evenly, or do emulsions behave like plain oil-and-water when tilted?",
    "svg": '''<rect x="50" y="10" width="100" height="110" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="75" cy="40" r="6" fill="#E4C77C"/>
      <circle cx="105" cy="60" r="5" fill="#E4C77C"/>
      <circle cx="85" cy="90" r="6" fill="#E4C77C"/>'''
  },
  "compare": {
    "question": "Tap the picture showing an EMULSION (tiny droplets spread evenly, not separated into layers).",
    "explanation": "An emulsion keeps droplets tiny and spread throughout, unlike plain oil-and-water which separates into two clean layers.",
    "choices": [
      {"label":"A — tiny droplets spread evenly", "svg": '''<svg viewBox="0 0 200 140"><rect x="40" y="10" width="120" height="110" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><circle cx="70" cy="40" r="7" fill="#E4C77C"/><circle cx="110" cy="55" r="6" fill="#E4C77C"/><circle cx="90" cy="85" r="7" fill="#E4C77C"/><circle cx="130" cy="95" r="6" fill="#E4C77C"/></svg>''', "correct": True},
      {"label":"B — separated into two layers", "svg": '''<svg viewBox="0 0 200 140"><rect x="40" y="10" width="120" height="110" fill="none" stroke="#0B2545" stroke-width="2"/><rect x="42" y="16" width="116" height="40" fill="#E4C77C" opacity="0.7"/><rect x="42" y="56" width="116" height="60" fill="#B9D8EA" opacity="0.6"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Oil and water normally separate by density", "icon": ICON_OIL_DROPS},
    {"text":"An emulsifier grabs onto both oil and water at once", "icon": ICON_EMULSIFIER},
    {"text":"That keeps oil droplets trapped, spread evenly — a stable emulsion", "icon": ICON_MAYO_JAR},
    {"text":"🔗 Links to Density in Cooking: an emulsifier is basically the one trick that BEATS the normal oil-floats-on-water rule", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does mayonnaise stay smooth and mixed for weeks, while a plain oil-and-vinegar dressing separates again within minutes?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="30" y="10" width="140" height="80" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><circle cx="70" cy="40" r="6" fill="#E4C77C"/><circle cx="110" cy="55" r="5" fill="#E4C77C"/></svg>''',
    "starters": ["Mayonnaise has egg yolk, which acts as...", "Oil-and-vinegar dressing separates because it lacks..."],
    "keywords": ["emulsifier", "droplets", "oil", "water"]
  },
  "predict": {
    "question": "You mix oil and vinegar without any emulsifier, shake hard, and let it sit for 10 minutes. What happens?",
    "explanation": "Without an emulsifier holding tiny droplets apart, the oil droplets find each other and merge back into one layer — density wins and it separates again, just like plain oil and water.",
    "choices": [
      {"text": "It separates back into oil and vinegar layers", "correct": True},
      {"text": "It stays permanently mixed like mayonnaise", "correct": False},
      {"text": "The oil turns into vinegar", "correct": False},
    ]
  }
}
open("cooking-05-emulsions.html", "w", encoding="utf-8").write(build("cooking-05-emulsions", "Cooking: Emulsions 🥚", c5_data))
print("built cooking-05-emulsions.html")

# ================= CONCEPT 6: ACIDS & BASES (BAKING SODA + VINEGAR) =================
c6_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Baking soda and vinegar mixing together and producing lots of bubbles">
      <rect x="90" y="60" width="120" height="110" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="120" cy="90" r="6" fill="none" stroke="#2E6E62" stroke-width="2"/>
      <circle cx="150" cy="70" r="8" fill="none" stroke="#2E6E62" stroke-width="2"/>
      <circle cx="180" cy="100" r="7" fill="none" stroke="#2E6E62" stroke-width="2"/>
      <circle cx="135" cy="120" r="5" fill="none" stroke="#2E6E62" stroke-width="2"/>
      <circle cx="165" cy="140" r="6" fill="none" stroke="#2E6E62" stroke-width="2"/>
    </svg>''',
    "question": "Baking soda (a base) meets vinegar (an acid) and it fizzes like crazy. What's making all those bubbles?",
    "explanation": "Acids and bases react together and produce carbon dioxide gas — that gas escaping as bubbles is the fizzing you see.",
    "choices": [
      {"text": "Carbon dioxide gas released by the acid-base reaction", "correct": True},
      {"text": "The mixture is boiling from heat", "correct": False},
      {"text": "Nothing chemical — it's just stirring air in", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"base","name":"Base (baking soda)","icon":ICON_BAKING_SODA,"fact":"⬜ A base — reacts with acids to release gas."},
    {"id":"acid","name":"Acid (vinegar)","icon":ICON_VINEGAR,"fact":"🟠 An acid — reacts with bases like baking soda."},
    {"id":"bubbles","name":"CO₂ bubbles","icon":ICON_BUBBLES,"fact":"🫧 Carbon dioxide gas escaping — the product of the acid-base reaction, and what makes cakes rise!"},
  ]},
  "draw": {
    "prompt": "Draw baking soda and vinegar mixing in a bowl, with lots of bubbles rising up.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <rect x="90" y="60" width="120" height="110" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="120" cy="90" r="6" fill="none" stroke="#2E6E62" stroke-width="2"/>
      <circle cx="150" cy="70" r="8" fill="none" stroke="#2E6E62" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the fizzing bowl picture. Do the bubbles still mean 'gas escaping' no matter which way it's turned?",
    "svg": '''<rect x="40" y="30" width="100" height="90" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="70" cy="55" r="5" fill="none" stroke="#2E6E62" stroke-width="2"/>
      <circle cx="100" cy="45" r="6" fill="none" stroke="#2E6E62" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing an ACID-BASE reaction actually happening (bubbling).",
    "explanation": "Bubbles are the visible sign the reaction is releasing gas — a still, calm liquid means no reaction is currently happening.",
    "choices": [
      {"label":"A — fizzing with bubbles", "svg": '''<svg viewBox="0 0 200 140"><rect x="40" y="20" width="120" height="100" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><circle cx="80" cy="50" r="6" fill="none" stroke="#2E6E62" stroke-width="2"/><circle cx="120" cy="70" r="7" fill="none" stroke="#2E6E62" stroke-width="2"/><circle cx="95" cy="95" r="5" fill="none" stroke="#2E6E62" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — still, calm liquid", "svg": '''<svg viewBox="0 0 200 140"><rect x="40" y="20" width="120" height="100" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Baking soda (base) meets vinegar (acid) in the batter", "icon": ICON_BAKING_SODA},
    {"text":"They react, producing CO₂ gas bubbles", "icon": ICON_BUBBLES},
    {"text":"Those trapped bubbles make cake batter rise and turn fluffy", "icon": ICON_MAYO_JAR},
    {"text":"🔗 Links to Maillard Reaction: both are chemical reactions triggered in the kitchen, just one needs heat and this one just needs mixing", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why do bakers use BOTH an acid and a base in a recipe instead of just one or the other?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="40" y="10" width="120" height="80" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/><circle cx="80" cy="40" r="5" fill="none" stroke="#2E6E62" stroke-width="2"/></svg>''',
    "starters": ["An acid alone can't make gas because...", "You need both because the reaction requires..."],
    "keywords": ["acid", "base", "reaction", "gas"]
  },
  "predict": {
    "question": "You add baking soda to plain water (no acid) and stir. What do you expect to see?",
    "explanation": "Without an acid to react with, baking soda just dissolves quietly — no reaction, no gas, no bubbling, since acid-base reactions need both an acid AND a base present.",
    "choices": [
      {"text": "It just dissolves, with little to no fizzing", "correct": True},
      {"text": "It fizzes exactly like it does with vinegar", "correct": False},
      {"text": "It causes an explosion", "correct": False},
    ]
  }
}
open("cooking-06-acids-and-bases.html", "w", encoding="utf-8").write(build("cooking-06-acids-and-bases", "Cooking: Acids & Bases 🫧", c6_data))
print("built cooking-06-acids-and-bases.html")

# ================= CONCEPT 7: DIFFUSION (MARINADES) =================
c7_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Meat sitting in a marinade with salt and flavor molecules moving from the liquid into the meat">
      <ellipse cx="150" cy="130" rx="90" ry="40" fill="#D9603B" opacity="0.35" stroke="#0B2545" stroke-width="2"/>
      <ellipse cx="150" cy="120" rx="55" ry="25" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
      <path d="M110 130 L130 122" stroke="#C9A24B" stroke-width="1.5"/>
      <path d="M190 130 L170 122" stroke="#C9A24B" stroke-width="1.5"/>
      <path d="M150 155 L150 138" stroke="#C9A24B" stroke-width="1.5"/>
    </svg>''',
    "question": "Meat sits in a salty, flavorful marinade. Which way do the flavor molecules move?",
    "explanation": "Diffusion moves molecules from where they're crowded (the marinade) to where there's less of them (inside the meat) — that's how marinades work their way in over time.",
    "choices": [
      {"text": "From the marinade into the meat", "correct": True},
      {"text": "From the meat out into the marinade", "correct": False},
      {"text": "Nothing moves — marinating is just soaking with no exchange", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"marinade","name":"Marinade","icon":ICON_MARINADE_BOWL,"fact":"🥣 A flavorful, often salty or acidic liquid the food sits in."},
    {"id":"diffusion_arrows","name":"Diffusion","icon":ICON_DIFFUSE_ARROWS,"fact":"↔️ Molecules spreading from a crowded area to a less-crowded one, evening things out over time."},
    {"id":"salt_in","name":"Salt/flavor entering meat","icon":ICON_SALT_IN,"fact":"🧂 Salt and flavor molecules slowly work their way into the meat's fibers."},
  ]},
  "draw": {
    "prompt": "Draw a piece of meat in a bowl of marinade, with arrows showing flavor molecules moving INTO the meat.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <ellipse cx="150" cy="130" rx="90" ry="40" fill="#D9603B" opacity="0.35" stroke="#0B2545" stroke-width="2"/>
      <ellipse cx="150" cy="120" rx="55" ry="25" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
      <path d="M110 130 L130 122" stroke="#C9A24B" stroke-width="1.5"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the marinade bowl. Do the diffusion arrows still point from marinade INTO meat, no matter the angle?",
    "svg": '''<ellipse cx="100" cy="80" rx="60" ry="26" fill="#D9603B" opacity="0.35" stroke="#0B2545" stroke-width="2"/>
      <ellipse cx="100" cy="72" rx="36" ry="16" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
      <path d="M75 78 L88 72" stroke="#C9A24B" stroke-width="1.5"/>'''
  },
  "compare": {
    "question": "Tap the picture showing diffusion arrows pointing the CORRECT direction (marinade → meat).",
    "explanation": "Flavor spreads from where it's concentrated (the marinade) into where it's not yet (the meat) — that's the whole point of diffusion.",
    "choices": [
      {"label":"A — arrows pointing into the meat", "svg": '''<svg viewBox="0 0 200 140"><ellipse cx="100" cy="90" rx="70" ry="30" fill="#D9603B" opacity="0.35" stroke="#0B2545" stroke-width="2"/><ellipse cx="100" cy="80" rx="40" ry="18" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/><path d="M65 90 L82 80" stroke="#C9A24B" stroke-width="2"/><path d="M135 90 L118 80" stroke="#C9A24B" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — arrows pointing out of the meat", "svg": '''<svg viewBox="0 0 200 140"><ellipse cx="100" cy="90" rx="70" ry="30" fill="#D9603B" opacity="0.35" stroke="#0B2545" stroke-width="2"/><ellipse cx="100" cy="80" rx="40" ry="18" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/><path d="M82 80 L65 90" stroke="#C9A24B" stroke-width="2"/><path d="M118 80 L135 90" stroke="#C9A24B" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Marinade has lots of salt and flavor molecules packed in", "icon": ICON_MARINADE_BOWL},
    {"text":"Meat starts with much less of those molecules inside it", "icon": ICON_SALT_IN},
    {"text":"Diffusion slowly evens that difference out, over hours", "icon": ICON_DIFFUSE_ARROWS},
    {"text":"🔗 Links to Ocean Salinity vs Depth: salt spreading through meat is the same 'evening out' idea as salt settling through ocean water", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does marinating meat for 4 hours give WAY more flavor than marinating it for just 2 minutes?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><ellipse cx="100" cy="50" rx="70" ry="30" fill="#D9603B" opacity="0.35" stroke="#0B2545" stroke-width="2"/><ellipse cx="100" cy="45" rx="40" ry="16" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["Diffusion takes time because...", "In just 2 minutes, the molecules have only..."],
    "keywords": ["diffusion", "time", "marinade", "spread"]
  },
  "predict": {
    "question": "You cut meat into thin strips instead of leaving it as one thick chunk before marinating. What happens to flavor absorption?",
    "explanation": "Thin strips have much more surface area exposed to the marinade and a shorter distance for molecules to travel inward, so diffusion happens faster and flavor gets in quicker.",
    "choices": [
      {"text": "Flavor absorbs faster because of more surface area", "correct": True},
      {"text": "Flavor absorbs slower with thin strips", "correct": False},
      {"text": "Thickness makes no difference to diffusion speed", "correct": False},
    ]
  }
}
open("cooking-07-diffusion-marinades.html", "w", encoding="utf-8").write(build("cooking-07-diffusion-marinades", "Cooking: Diffusion & Marinades ↔️", c7_data))
print("built cooking-07-diffusion-marinades.html")

# ================= CONCEPT 8: CRYSTALLIZATION (SUGAR/CHOCOLATE) =================
c8_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 320 200" role="img" aria-label="Slow cooling forming a few large sugar crystals versus fast cooling forming many tiny crystals">
      <path d="M60 60 L100 90 L100 130 L60 160 L20 130 L20 90 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <text x="10" y="45" font-size="11" fill="#0B2545">Slow cool: 1 big crystal</text>
      <circle cx="220" cy="80" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <circle cx="240" cy="95" r="5" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <circle cx="200" cy="110" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <circle cx="260" cy="120" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <circle cx="225" cy="130" r="5" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <text x="185" y="65" font-size="11" fill="#0B2545">Fast cool: many tiny crystals</text>
    </svg>''',
    "question": "Sugar syrup cooled SLOWLY forms one smooth big crystal. Cooled FAST, what do you get instead?",
    "explanation": "Fast cooling doesn't give molecules time to line up into a big orderly structure — instead they lock into place quickly as lots of tiny, gritty crystals.",
    "choices": [
      {"text": "Many tiny crystals (grittier texture)", "correct": True},
      {"text": "One giant crystal, even bigger than slow cooling", "correct": False},
      {"text": "No crystals form at all when cooling fast", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"big_crystal","name":"Slow cooling → big crystal","icon":ICON_SLOW_COOL,"fact":"🐢 Molecules have time to line up neatly into one large, smooth crystal structure."},
    {"id":"tiny_crystals","name":"Fast cooling → tiny crystals","icon":ICON_FAST_COOL,"fact":"⚡ Molecules lock into place quickly and messily — lots of small, gritty crystals instead."},
    {"id":"sugar_molecule","name":"Sugar crystal","icon":ICON_SUGAR_CRYSTAL,"fact":"🍬 A neat, repeating structure sugar molecules form as they solidify."},
  ]},
  "draw": {
    "prompt": "Draw two pans of cooling sugar: one labeled 'slow cool' with one big crystal shape, one labeled 'fast cool' with lots of tiny dots.",
    "hintSvg": '''<svg viewBox="0 0 320 200" role="img" aria-label="hint">
      <path d="M60 60 L100 90 L100 130 L60 160 L20 130 L20 90 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>
      <circle cx="220" cy="80" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <circle cx="240" cy="95" r="5" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
      <circle cx="200" cy="110" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the crystal shape. Does slow cooling's single, neat crystal shape stay recognizable from any angle?",
    "svg": '''<path d="M50 40 L80 60 L80 90 L50 110 L20 90 L20 60 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing FAST cooling (many tiny crystals, not one big one).",
    "explanation": "Speed matters: fast cooling traps molecules before they can organize into one big structure, producing lots of small crystals instead.",
    "choices": [
      {"label":"A — many tiny scattered crystals", "svg": '''<svg viewBox="0 0 200 140"><circle cx="60" cy="50" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/><circle cx="90" cy="70" r="5" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/><circle cx="120" cy="55" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/><circle cx="140" cy="90" r="5" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/><circle cx="70" cy="100" r="4" fill="#F3EEE1" stroke="#0B2545" stroke-width="1"/></svg>''', "correct": True},
      {"label":"B — one large single crystal", "svg": '''<svg viewBox="0 0 200 140"><path d="M100 30 L140 55 L140 95 L100 120 L60 95 L60 55 Z" fill="#F3EEE1" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Hot sugar syrup starts cooling down", "icon": ICON_THERMOMETER},
    {"text":"Cooling speed decides how much TIME molecules get to organize", "icon": ICON_SLOW_COOL},
    {"text":"Slow = one big smooth crystal; fast = many tiny gritty ones", "icon": ICON_FAST_COOL},
    {"text":"🔗 Links to States of Matter: this is the SAME liquid-to-solid change, just with cooling speed controlling how the solid turns out", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Chocolatiers cool melted chocolate very carefully and slowly for a smooth, shiny finish. Why does rushing that step ruin the texture?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M100 15 L130 32 L130 62 L100 79 L70 62 L70 32 Z" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["Rushing the cooling means the crystals don't get time to...", "A smooth chocolate finish needs..."],
    "keywords": ["crystallize", "cooling", "smooth", "gritty"]
  },
  "predict": {
    "question": "You want smooth, creamy fudge instead of gritty, sugary fudge. Should you cool the syrup fast or slow?",
    "explanation": "Slow, controlled cooling lets sugar molecules form fewer, larger, smoother crystals — that's the secret to creamy fudge instead of a gritty, sandy texture.",
    "choices": [
      {"text": "Cool it slowly", "correct": True},
      {"text": "Cool it as fast as possible", "correct": False},
      {"text": "Cooling speed doesn't affect texture", "correct": False},
    ]
  }
}
open("cooking-08-crystallization.html", "w", encoding="utf-8").write(build("cooking-08-crystallization", "Cooking: Crystallization 🍬", c8_data))
print("built cooking-08-crystallization.html")
