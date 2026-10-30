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
ICON_ICE_CUBE = "<svg viewBox='0 0 40 40'><rect x='8' y='8' width='24' height='24' fill='#B9D8EA' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_WATER_DROP = "<svg viewBox='0 0 40 40'><path d='M20 4 Q28 20 20 30 Q12 20 20 4 Z' fill='#2E6E62' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_STEAM = "<svg viewBox='0 0 40 40'><path d='M14 34 Q10 24 16 18 Q20 12 14 4' fill='none' stroke='#B9D8EA' stroke-width='3'/><path d='M26 34 Q22 24 28 18 Q32 12 26 4' fill='none' stroke='#B9D8EA' stroke-width='3'/></svg>"
ICON_THERMOMETER = "<svg viewBox='0 0 40 40'><rect x='16' y='4' width='8' height='22' rx='4' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='20' cy='30' r='7' fill='#D9603B' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_PAN = "<svg viewBox='0 0 40 40'><ellipse cx='20' cy='24' rx='16' ry='7' fill='#4B5563' stroke='#0B2545' stroke-width='2'/><line x1='34' y1='22' x2='38' y2='18' stroke='#0B2545' stroke-width='3'/></svg>"
ICON_CONDUCTION = "<svg viewBox='0 0 40 40'><rect x='4' y='24' width='32' height='8' fill='#4B5563'/><line x1='10' y1='24' x2='10' y2='10' stroke='#D9603B' stroke-width='2'/><line x1='20' y1='24' x2='20' y2='10' stroke='#D9603B' stroke-width='2'/><line x1='30' y1='24' x2='30' y2='10' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_CONVECTION = "<svg viewBox='0 0 40 40'><path d='M10 34 Q10 24 18 24 Q26 24 26 14 Q26 6 34 6' fill='none' stroke='#D9603B' stroke-width='2.5'/><path d='M28 10 L34 6 L30 14' fill='none' stroke='#D9603B' stroke-width='2'/></svg>"
ICON_BROWN_MEAT = "<svg viewBox='0 0 40 40'><ellipse cx='20' cy='22' rx='16' ry='10' fill='#8B5E3C' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_RAW_MEAT = "<svg viewBox='0 0 40 40'><ellipse cx='20' cy='22' rx='16' ry='10' fill='#E8A9A0' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_FLAVOR_STAR = "<svg viewBox='0 0 40 40'><path d='M20 4 L24 16 L36 16 L26 24 L30 36 L20 28 L10 36 L14 24 L4 16 L16 16 Z' fill='#C9A24B' stroke='#0B2545' stroke-width='1.5'/></svg>"
ICON_OIL_LAYER = "<svg viewBox='0 0 40 40'><rect x='4' y='8' width='32' height='12' fill='#E4C77C' opacity='0.8' stroke='#0B2545' stroke-width='1.5'/><rect x='4' y='20' width='32' height='14' fill='#B9D8EA' opacity='0.6' stroke='#0B2545' stroke-width='1.5'/></svg>"
ICON_DENSITY_SCALE = "<svg viewBox='0 0 40 40'><line x1='20' y1='6' x2='20' y2='28' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='14' x2='34' y2='14' stroke='#0B2545' stroke-width='2'/><circle cx='6' cy='24' r='5' fill='#E4C77C'/><circle cx='34' cy='20' r='5' fill='none' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_LINK = "<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/><circle cx='26' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"

# ================= CONCEPT 1: STATES OF MATTER (COOKING) =================
c1_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 320 200" role="img" aria-label="Ice cube melting into water then boiling into steam, showing the three states of matter">
      <rect x="20" y="120" width="60" height="60" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/>
      <text x="20" y="112" font-size="11" fill="#0B2545">Solid (ice)</text>
      <path d="M140 130 Q150 110 160 130 Q170 150 180 130" fill="#2E6E62" stroke="#0B2545" stroke-width="1.5"/>
      <rect x="120" y="130" width="80" height="50" fill="#2E6E62" opacity="0.6" stroke="#0B2545" stroke-width="2"/>
      <text x="120" y="122" font-size="11" fill="#0B2545">Liquid (water)</text>
      <path d="M260 160 Q255 140 262 120 Q268 100 260 80" fill="none" stroke="#B9D8EA" stroke-width="3"/>
      <path d="M280 160 Q275 140 282 120 Q288 100 280 80" fill="none" stroke="#B9D8EA" stroke-width="3"/>
      <text x="245" y="70" font-size="11" fill="#0B2545">Gas (steam)</text>
    </svg>''',
    "question": "Ice, water, and steam are all the SAME substance. What's actually different between them?",
    "explanation": "It's still H₂O the whole time — only how much heat energy is in it, and how tightly the molecules are packed, changes as it goes solid → liquid → gas.",
    "choices": [
      {"text": "How much heat energy the molecules have", "correct": True},
      {"text": "They're totally different chemicals", "correct": False},
      {"text": "Nothing — they're identical in every way", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"solid","name":"Solid (ice)","icon":ICON_ICE_CUBE,"fact":"🧊 Molecules packed tight, barely moving — holds its own shape."},
    {"id":"liquid","name":"Liquid (water)","icon":ICON_WATER_DROP,"fact":"💧 Molecules loose enough to slide past each other — takes the shape of its container."},
    {"id":"gas","name":"Gas (steam)","icon":ICON_STEAM,"fact":"💨 Molecules zooming apart with lots of energy — spreads out to fill any space."},
  ]},
  "draw": {
    "prompt": "Draw all 3 states side by side: an ice cube, a puddle of water, and steam rising. Label each with 'solid,' 'liquid,' or 'gas.'",
    "hintSvg": '''<svg viewBox="0 0 320 200" role="img" aria-label="hint">
      <rect x="20" y="120" width="60" height="60" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/>
      <rect x="120" y="130" width="80" height="50" fill="#2E6E62" opacity="0.6" stroke="#0B2545" stroke-width="2"/>
      <path d="M260 160 Q255 140 262 120 Q268 100 260 80" fill="none" stroke="#B9D8EA" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the ice-water-steam picture. Does 'solid on the left, gas on the right' still make sense in a different orientation?",
    "svg": '''<rect x="10" y="80" width="40" height="40" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/>
      <rect x="70" y="90" width="55" height="30" fill="#2E6E62" opacity="0.6" stroke="#0B2545" stroke-width="2"/>
      <path d="M170 110 Q166 95 172 80" fill="none" stroke="#B9D8EA" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the picture showing molecules PACKED TIGHT (a solid).",
    "explanation": "A solid's molecules barely move and stay locked in place — that's why ice holds a fixed shape while water and steam don't.",
    "choices": [
      {"label":"A — tightly packed dots (solid)", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="30" width="140" height="80" fill="none" stroke="#0B2545" stroke-width="2"/><circle cx="55" cy="50" r="5" fill="#2E6E62"/><circle cx="80" cy="50" r="5" fill="#2E6E62"/><circle cx="105" cy="50" r="5" fill="#2E6E62"/><circle cx="55" cy="75" r="5" fill="#2E6E62"/><circle cx="80" cy="75" r="5" fill="#2E6E62"/><circle cx="105" cy="75" r="5" fill="#2E6E62"/></svg>''', "correct": True},
      {"label":"B — scattered spread-out dots (gas)", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="30" width="140" height="80" fill="none" stroke="#0B2545" stroke-width="2"/><circle cx="45" cy="45" r="5" fill="#2E6E62"/><circle cx="140" cy="95" r="5" fill="#2E6E62"/><circle cx="90" cy="50" r="5" fill="#2E6E62"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"A pot of ice sits on the stove", "icon": ICON_ICE_CUBE},
    {"text":"Heat energy pours in, molecules start moving faster", "icon": ICON_THERMOMETER},
    {"text":"Enough energy melts it to liquid, even more turns it to gas", "icon": ICON_STEAM},
    {"text":"🔗 Links to Mario Energy Transformation: adding heat energy here works just like adding height (potential energy) there — energy in, state changes", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does it take a LOT of heat to turn boiling water into steam, way more than to melt the same amount of ice?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="20" y="60" width="50" height="30" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/><path d="M150 70 Q146 55 152 40" fill="none" stroke="#B9D8EA" stroke-width="3"/></svg>''',
    "starters": ["Turning liquid into gas needs more energy because...", "The molecules in steam are..."],
    "keywords": ["energy", "molecules", "heat", "state"]
  },
  "predict": {
    "question": "You keep adding heat to boiling water, but the temperature stays at 100°C and doesn't rise. Where is all that extra heat energy going?",
    "explanation": "During a change of state, added energy goes into breaking molecules apart (turning liquid into gas) instead of raising temperature — that's why boiling water sits at a steady 100°C while it turns to steam.",
    "choices": [
      {"text": "Into changing the water into steam (changing state)", "correct": True},
      {"text": "The heat just disappears with no effect", "correct": False},
      {"text": "It makes the water colder", "correct": False},
    ]
  }
}
open("cooking-01-states-of-matter.html", "w", encoding="utf-8").write(build("cooking-01-states-of-matter", "Cooking: States of Matter 🧊", c1_data))
print("built cooking-01-states-of-matter.html")

# ================= CONCEPT 2: HEAT TRANSFER (CONDUCTION/CONVECTION) =================
c2_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 320 200" role="img" aria-label="Pan on a stove with heat moving up through the metal by conduction and through the liquid by convection loops">
      <rect x="10" y="150" width="300" height="20" fill="#D9603B"/>
      <ellipse cx="160" cy="130" rx="130" ry="18" fill="#4B5563" stroke="#0B2545" stroke-width="2"/>
      <line x1="60" y1="130" x2="60" y2="90" stroke="#D9603B" stroke-width="2"/>
      <line x1="160" y1="130" x2="160" y2="90" stroke="#D9603B" stroke-width="2"/>
      <line x1="260" y1="130" x2="260" y2="90" stroke="#D9603B" stroke-width="2"/>
      <text x="60" y="80" font-size="10" fill="#D9603B">heat through metal</text>
    </svg>''',
    "question": "Heat moves straight through the solid metal pan. What's that method of heat transfer called?",
    "explanation": "Heat passing directly through a solid material, molecule to molecule, is called conduction — it's why the pan handle eventually gets hot too.",
    "choices": [
      {"text": "Conduction (through the solid metal)", "correct": True},
      {"text": "Convection (through moving liquid/gas)", "correct": False},
      {"text": "Heat doesn't move through solids", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"conduction","name":"Conduction","icon":ICON_CONDUCTION,"fact":"🔥 Heat passing directly through a solid, like the metal of a pan."},
    {"id":"convection","name":"Convection","icon":ICON_CONVECTION,"fact":"🌀 Heat carried by looping, moving liquid or gas — like boiling water circulating."},
    {"id":"pan","name":"Pan (the conductor)","icon":ICON_PAN,"fact":"🍳 Metal is a great conductor — it moves heat from the stove to your food fast."},
  ]},
  "draw": {
    "prompt": "Draw a pan on a stove. Show conduction with straight arrows through the metal, and convection with looping arrows in the liquid.",
    "hintSvg": '''<svg viewBox="0 0 320 200" role="img" aria-label="hint">
      <rect x="10" y="150" width="300" height="20" fill="#D9603B"/>
      <ellipse cx="160" cy="130" rx="130" ry="18" fill="#4B5563" stroke="#0B2545" stroke-width="2"/>
      <line x1="60" y1="130" x2="60" y2="90" stroke="#D9603B" stroke-width="2"/>
      <line x1="160" y1="130" x2="160" y2="90" stroke="#D9603B" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the pan diagram. Does the conduction arrow still mean 'straight through the solid,' no matter the angle?",
    "svg": '''<ellipse cx="100" cy="80" rx="80" ry="12" fill="#4B5563" stroke="#0B2545" stroke-width="2"/>
      <line x1="60" y1="80" x2="60" y2="50" stroke="#D9603B" stroke-width="2"/>
      <line x1="100" y1="80" x2="100" y2="50" stroke="#D9603B" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing CONVECTION (looping arrows in a liquid).",
    "explanation": "Convection is heat carried by moving fluid in loops — rising where it's hot, sinking where it's cooler — unlike conduction's straight-through path.",
    "choices": [
      {"label":"A — looping convection currents", "svg": '''<svg viewBox="0 0 200 140"><rect x="20" y="20" width="160" height="90" fill="#2E6E62" opacity="0.4" stroke="#0B2545" stroke-width="2"/><path d="M50 100 Q50 40 100 40 Q150 40 150 100" fill="none" stroke="#D9603B" stroke-width="2.5"/></svg>''', "correct": True},
      {"label":"B — straight arrows through solid metal", "svg": '''<svg viewBox="0 0 200 140"><rect x="20" y="90" width="160" height="20" fill="#4B5563" stroke="#0B2545" stroke-width="2"/><line x1="60" y1="90" x2="60" y2="50" stroke="#D9603B" stroke-width="2"/><line x1="140" y1="90" x2="140" y2="50" stroke="#D9603B" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"The stove heats the pan's metal directly", "icon": ICON_PAN},
    {"text":"That heat conducts through the solid metal to the food", "icon": ICON_CONDUCTION},
    {"text":"Inside a liquid, heated fluid rises and cooler fluid sinks — a convection loop", "icon": ICON_CONVECTION},
    {"text":"🔗 Links to Ocean Global Conveyor: convection loops in a pot are a tiny version of that same rising-warm/sinking-cool ocean loop", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does stirring a pot of soup help it heat evenly, using what you know about convection?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="20" y="10" width="160" height="80" fill="#2E6E62" opacity="0.4" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["Stirring helps because convection normally...", "Without stirring, the soup would..."],
    "keywords": ["convection", "conduction", "heat", "stirring"]
  },
  "predict": {
    "question": "You heat a metal spoon left resting in a hot pot. A few minutes later, the handle (far from the heat) feels warm too. Why?",
    "explanation": "Heat conducted from the hot end of the spoon all the way through the solid metal to the handle — the exact same molecule-to-molecule conduction that heats a pan.",
    "choices": [
      {"text": "Heat conducted through the solid metal spoon", "correct": True},
      {"text": "The handle heated up on its own, unrelated to the pot", "correct": False},
      {"text": "Metal blocks heat completely", "correct": False},
    ]
  }
}
open("cooking-02-heat-transfer.html", "w", encoding="utf-8").write(build("cooking-02-heat-transfer", "Cooking: Heat Transfer 🔥", c2_data))
print("built cooking-02-heat-transfer.html")

# ================= CONCEPT 3: MAILLARD REACTION (BROWNING) =================
c3_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 320 200" role="img" aria-label="Raw pale meat on the left transforming into browned meat on the right after high heat, with new flavor stars appearing">
      <ellipse cx="80" cy="110" rx="55" ry="35" fill="#E8A9A0" stroke="#0B2545" stroke-width="2"/>
      <text x="40" y="60" font-size="11" fill="#0B2545">Raw (pale)</text>
      <path d="M150 110 L190 110" stroke="#0B2545" stroke-width="2"/>
      <path d="M180 102 L194 110 L180 118" fill="#0B2545"/>
      <ellipse cx="250" cy="110" rx="55" ry="35" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
      <text x="215" y="60" font-size="11" fill="#0B2545">Browned</text>
      <path d="M280 70 L286 82 L298 82 L288 90 L292 102 L280 94 L268 102 L272 90 L262 82 L274 82 Z" fill="#C9A24B"/>
    </svg>''',
    "question": "High heat turns raw pale meat into browned, super-flavorful meat. What causes that new color AND new flavor?",
    "explanation": "That's the Maillard reaction — heat makes proteins and sugars on the surface react and rearrange into hundreds of brand-new flavor and aroma molecules, plus the brown color.",
    "choices": [
      {"text": "A chemical reaction between proteins and sugars (Maillard reaction)", "correct": True},
      {"text": "The meat just loses water and looks darker, nothing chemical", "correct": False},
      {"text": "Browning has no connection to flavor at all", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"raw","name":"Raw / unbrowned","icon":ICON_RAW_MEAT,"fact":"🥩 Proteins and sugars haven't reacted yet — mild flavor, pale color."},
    {"id":"browned","name":"Browned (Maillard)","icon":ICON_BROWN_MEAT,"fact":"🟤 High heat triggered the reaction — deep color, way more flavor."},
    {"id":"flavor","name":"New flavor molecules","icon":ICON_FLAVOR_STAR,"fact":"⭐ Hundreds of new aroma/flavor compounds form — this is why seared food tastes so different from boiled food."},
  ]},
  "draw": {
    "prompt": "Draw raw meat on one side and browned meat on the other, with an arrow labeled 'high heat' between them.",
    "hintSvg": '''<svg viewBox="0 0 320 200" role="img" aria-label="hint">
      <ellipse cx="80" cy="110" rx="55" ry="35" fill="#E8A9A0" stroke="#0B2545" stroke-width="2"/>
      <path d="M150 110 L190 110" stroke="#0B2545" stroke-width="2"/>
      <ellipse cx="250" cy="110" rx="55" ry="35" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the before/after picture. Does 'raw always comes before browned' still hold, or does rotating scramble the order?",
    "svg": '''<ellipse cx="60" cy="80" rx="45" ry="28" fill="#E8A9A0" stroke="#0B2545" stroke-width="2"/>
      <path d="M115 80 L150 80" stroke="#0B2545" stroke-width="2"/>
      <ellipse cx="200" cy="80" rx="45" ry="28" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing a Maillard-BROWNED surface (not just raw).",
    "explanation": "The dark brown color only appears after the Maillard reaction has actually happened — high heat, not just any cooking, is what triggers it.",
    "choices": [
      {"label":"A — dark browned surface", "svg": '''<svg viewBox="0 0 200 140"><ellipse cx="100" cy="70" rx="70" ry="40" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — pale unbrowned surface", "svg": '''<svg viewBox="0 0 200 140"><ellipse cx="100" cy="70" rx="70" ry="40" fill="#E8A9A0" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"A pan gets hot enough (usually above ~140°C)", "icon": ICON_PAN},
    {"text":"Proteins and sugars on the food's surface react together", "icon": ICON_THERMOMETER},
    {"text":"New flavor molecules and brown color form", "icon": ICON_FLAVOR_STAR},
    {"text":"🔗 Links to Cooking Heat Transfer: it's the pan's CONDUCTION delivering exactly the heat needed to trigger this reaction", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does boiling meat in water NOT brown it, even after a long time, while searing it in a hot dry pan browns it fast?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><ellipse cx="100" cy="50" rx="60" ry="30" fill="#E8A9A0" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["Boiling water can't get hotter than 100°C, but a dry pan...", "The Maillard reaction needs..."],
    "keywords": ["heat", "browning", "temperature", "water"]
  },
  "predict": {
    "question": "You want to brown a steak quickly and deeply. Should you cook it in boiling water or a very hot dry pan?",
    "explanation": "Boiling water tops out at 100°C, which isn't hot enough to trigger the Maillard reaction — a dry pan can reach 150°C+ and brown the surface fast.",
    "choices": [
      {"text": "A very hot dry pan", "correct": True},
      {"text": "Boiling water", "correct": False},
      {"text": "Either works equally well for browning", "correct": False},
    ]
  }
}
open("cooking-03-maillard-reaction.html", "w", encoding="utf-8").write(build("cooking-03-maillard-reaction", "Cooking: Maillard Reaction 🟤", c3_data))
print("built cooking-03-maillard-reaction.html")

# ================= CONCEPT 4: DENSITY IN COOKING (OIL FLOATS ON WATER) =================
c4_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="A jar with a layer of oil floating on top of water, showing density difference">
      <rect x="60" y="20" width="180" height="160" fill="none" stroke="#0B2545" stroke-width="2"/>
      <rect x="62" y="30" width="176" height="45" fill="#E4C77C" opacity="0.7"/>
      <rect x="62" y="75" width="176" height="103" fill="#B9D8EA" opacity="0.6"/>
      <text x="70" y="55" font-size="11" fill="#0B2545">Oil (less dense)</text>
      <text x="70" y="130" font-size="11" fill="#0B2545">Water (more dense)</text>
    </svg>''',
    "question": "Oil and water are shaken together, then left alone. Which one ends up on top?",
    "explanation": "Oil is less dense than water, so no matter how hard you shake it, oil always rises back to the top once the mixture settles.",
    "choices": [
      {"text": "Oil (it's less dense)", "correct": True},
      {"text": "Water (it's less dense)", "correct": False},
      {"text": "They stay perfectly mixed forever", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"oil_layer","name":"Oil layer","icon":ICON_OIL_LAYER,"fact":"🟡 Less dense — floats on top of water every time."},
    {"id":"water_layer","name":"Water layer","icon":ICON_WATER_DROP,"fact":"🔵 More dense than oil — settles below it."},
    {"id":"scale","name":"Density comparison","icon":ICON_DENSITY_SCALE,"fact":"⚖️ Same volume of oil weighs less than the same volume of water — that's what 'less dense' means."},
  ]},
  "draw": {
    "prompt": "Draw a jar with two layers: oil on top, water on the bottom. Label which one is denser.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <rect x="60" y="20" width="180" height="160" fill="none" stroke="#0B2545" stroke-width="2"/>
      <rect x="62" y="30" width="176" height="45" fill="#E4C77C" opacity="0.7"/>
      <rect x="62" y="75" width="176" height="103" fill="#B9D8EA" opacity="0.6"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Flip the jar upside down for a second. Does the oil layer try to float back to the top again once it settles?",
    "svg": '''<rect x="40" y="10" width="140" height="120" fill="none" stroke="#0B2545" stroke-width="2"/>
      <rect x="42" y="16" width="136" height="35" fill="#E4C77C" opacity="0.7"/>
      <rect x="42" y="51" width="136" height="75" fill="#B9D8EA" opacity="0.6"/>'''
  },
  "compare": {
    "question": "Tap the picture with the CORRECT layer order (oil on top, water below).",
    "explanation": "Oil's lower density always puts it above water once the mixture settles — the opposite order isn't stable and won't stay that way.",
    "choices": [
      {"label":"A — oil on top, water below", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="10" width="140" height="110" fill="none" stroke="#0B2545" stroke-width="2"/><rect x="32" y="16" width="136" height="40" fill="#E4C77C" opacity="0.7"/><rect x="32" y="56" width="136" height="60" fill="#B9D8EA" opacity="0.6"/></svg>''', "correct": True},
      {"label":"B — water on top, oil below", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="10" width="140" height="110" fill="none" stroke="#0B2545" stroke-width="2"/><rect x="32" y="16" width="136" height="60" fill="#B9D8EA" opacity="0.6"/><rect x="32" y="76" width="136" height="40" fill="#E4C77C" opacity="0.7"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Oil and water get shaken together in a jar", "icon": ICON_OIL_LAYER},
    {"text":"Oil is less dense than water", "icon": ICON_DENSITY_SCALE},
    {"text":"Once settled, oil rises and water sinks below it", "icon": ICON_WATER_DROP},
    {"text":"🔗 Links to Ocean Salinity vs Depth: the EXACT same density rule that stacks ocean layers stacks kitchen liquids too", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "A salad dressing separates into layers after sitting for a while. Using density, explain why shaking it doesn't keep it mixed forever.",
    "visualSvg": '''<svg viewBox="0 0 200 100"><rect x="40" y="10" width="120" height="80" fill="none" stroke="#0B2545" stroke-width="2"/><rect x="42" y="16" width="116" height="30" fill="#E4C77C" opacity="0.7"/><rect x="42" y="46" width="116" height="44" fill="#B9D8EA" opacity="0.6"/></svg>''',
    "starters": ["Shaking mixes them temporarily, but density...", "Over time, the less dense liquid..."],
    "keywords": ["density", "oil", "water", "separate"]
  },
  "predict": {
    "question": "You pour honey (denser than both) into the same oil-and-water jar. Where does the honey end up?",
    "explanation": "The densest liquid always settles at the very bottom — honey being denser than both oil and water means it sinks below everything else.",
    "choices": [
      {"text": "At the very bottom, below the water", "correct": True},
      {"text": "At the very top, above the oil", "correct": False},
      {"text": "It mixes evenly with everything permanently", "correct": False},
    ]
  }
}
open("cooking-04-density-in-cooking.html", "w", encoding="utf-8").write(build("cooking-04-density-in-cooking", "Cooking: Density in Cooking ⚖️", c4_data))
print("built cooking-04-density-in-cooking.html")
