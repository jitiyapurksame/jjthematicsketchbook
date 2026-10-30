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
ICON_ICE = "<svg viewBox='0 0 40 40'><rect x='2' y='24' width='36' height='12' fill='#B9D8EA' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_GRASS = "<svg viewBox='0 0 40 40'><rect x='2' y='24' width='36' height='12' fill='#8FCB9B' stroke='#0B2545' stroke-width='2'/><path d='M6 24 L8 18 M14 24 L16 18 M22 24 L24 18 M30 24 L32 18' stroke='#3F8F5C' stroke-width='2'/></svg>"
ICON_SLIDE_ARROW = "<svg viewBox='0 0 40 40'><line x1='4' y1='20' x2='30' y2='20' stroke='#D9603B' stroke-width='3'/><path d='M22 12 L34 20 L22 28 Z' fill='#D9603B'/></svg>"
ICON_STOP_ARROW = "<svg viewBox='0 0 40 40'><line x1='4' y1='20' x2='14' y2='20' stroke='#2E6E62' stroke-width='3'/><rect x='16' y='12' width='6' height='16' fill='#2E6E62'/></svg>"
ICON_FRICTION_ZIGZAG = "<svg viewBox='0 0 40 40'><path d='M4 20 L10 12 L16 28 L22 12 L28 28 L36 20' fill='none' stroke='#D9603B' stroke-width='2.5'/></svg>"
ICON_ACCEL_STEPS = "<svg viewBox='0 0 40 40'><rect x='4' y='28' width='6' height='8' fill='#2E6E62'/><rect x='14' y='20' width='6' height='16' fill='#2E6E62'/><rect x='24' y='10' width='6' height='26' fill='#2E6E62'/></svg>"
ICON_CONSTANT_STEPS = "<svg viewBox='0 0 40 40'><rect x='4' y='18' width='6' height='18' fill='#0B2545'/><rect x='14' y='18' width='6' height='18' fill='#0B2545'/><rect x='24' y='18' width='6' height='18' fill='#0B2545'/></svg>"
ICON_POTENTIAL = "<svg viewBox='0 0 40 40'><circle cx='20' cy='10' r='8' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><line x1='4' y1='34' x2='36' y2='34' stroke='#0B2545' stroke-width='2'/><line x1='20' y1='18' x2='20' y2='34' stroke='#0B2545' stroke-width='1.5' stroke-dasharray='3 2'/></svg>"
ICON_KINETIC = "<svg viewBox='0 0 40 40'><circle cx='20' cy='28' r='8' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><path d='M8 28 L2 28 M32 28 L38 28' stroke='#2E6E62' stroke-width='2'/></svg>"
ICON_HEIGHT_ARROW = "<svg viewBox='0 0 40 40'><line x1='20' y1='4' x2='20' y2='34' stroke='#C9A24B' stroke-width='3'/><path d='M14 10 L20 2 L26 10' fill='#C9A24B'/></svg>"
ICON_GOOMBA = "<svg viewBox='0 0 40 40'><ellipse cx='20' cy='22' rx='14' ry='10' fill='#8B5E3C' stroke='#0B2545' stroke-width='2'/><rect x='8' y='30' width='8' height='6' fill='#4B3220'/><rect x='24' y='30' width='8' height='6' fill='#4B3220'/></svg>"
ICON_COLLISION_STAR = "<svg viewBox='0 0 40 40'><path d='M20 4 L24 16 L36 16 L26 24 L30 36 L20 28 L10 36 L14 24 L4 16 L16 16 Z' fill='#C9A24B' stroke='#0B2545' stroke-width='1.5'/></svg>"
ICON_MOMENTUM_ARROW = "<svg viewBox='0 0 40 40'><line x1='4' y1='20' x2='30' y2='20' stroke='#0B2545' stroke-width='4'/><path d='M22 10 L34 20 L22 30 Z' fill='#0B2545'/></svg>"
ICON_JUMP_PUSH = "<svg viewBox='0 0 40 40'><circle cx='20' cy='12' r='7' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><line x1='20' y1='19' x2='20' y2='34' stroke='#2E6E62' stroke-width='3'/><path d='M12 26 L20 36 L28 26' fill='none' stroke='#2E6E62' stroke-width='3'/></svg>"
ICON_LINK = "<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/><circle cx='26' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"

# ================= CONCEPT 5: FRICTION (ICE VS GRASS) =================
c5_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 320 200" role="img" aria-label="Mario sliding a long distance on ice versus stopping quickly on grass">
      <rect x="10" y="60" width="140" height="20" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/>
      <text x="20" y="50" font-size="11" fill="#0B2545">Ice — slides far</text>
      <circle cx="130" cy="50" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="20" y1="70" x2="130" y2="70" stroke="#D9603B" stroke-width="2" stroke-dasharray="4 3"/>
      <rect x="10" y="150" width="140" height="20" fill="#8FCB9B" stroke="#0B2545" stroke-width="2"/>
      <text x="20" y="140" font-size="11" fill="#0B2545">Grass — stops fast</text>
      <circle cx="40" cy="140" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="20" y1="160" x2="40" y2="160" stroke="#D9603B" stroke-width="2" stroke-dasharray="4 3"/>
    </svg>''',
    "question": "Mario slides after jumping onto ice vs. grass. Where does he slide FARTHER before stopping?",
    "explanation": "Ice has very low friction, so it barely slows Mario down — he keeps sliding. Grass has much more friction, so it stops him quickly.",
    "choices": [
      {"text": "Ice — because friction is low there", "correct": True},
      {"text": "Grass — because friction is low there", "correct": False},
      {"text": "Both the same — surface doesn't matter", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"ice_surface","name":"Ice (low friction)","icon":ICON_ICE,"fact":"🧊 Smooth surface, very little friction — Mario slides a long way."},
    {"id":"grass_surface","name":"Grass (high friction)","icon":ICON_GRASS,"fact":"🌱 Rough surface, lots of friction — Mario stops quickly."},
    {"id":"friction_force","name":"Friction force","icon":ICON_FRICTION_ZIGZAG,"fact":"🛑 A force that always opposes motion, converting movement energy into heat."},
  ]},
  "draw": {
    "prompt": "Draw two lanes: ice with a long sliding arrow, grass with a short stopping arrow.",
    "hintSvg": '''<svg viewBox="0 0 320 200" role="img" aria-label="hint">
      <rect x="10" y="60" width="140" height="20" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/>
      <line x1="20" y1="70" x2="130" y2="70" stroke="#D9603B" stroke-width="2" stroke-dasharray="4 3"/>
      <rect x="10" y="150" width="140" height="20" fill="#8FCB9B" stroke="#0B2545" stroke-width="2"/>
      <line x1="20" y1="160" x2="40" y2="160" stroke="#D9603B" stroke-width="2" stroke-dasharray="4 3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the two-lane picture. Does ice still mean 'long slide' no matter which way it's turned?",
    "svg": '''<rect x="10" y="30" width="100" height="15" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/>
      <line x1="20" y1="37" x2="95" y2="37" stroke="#D9603B" stroke-width="2" stroke-dasharray="3 2"/>
      <rect x="10" y="80" width="100" height="15" fill="#8FCB9B" stroke="#0B2545" stroke-width="2"/>
      <line x1="20" y1="87" x2="35" y2="87" stroke="#D9603B" stroke-width="2" stroke-dasharray="3 2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing HIGH friction (short stopping distance).",
    "explanation": "High friction means a strong opposing force, which brings motion to a stop quickly — that's a short arrow, like on grass.",
    "choices": [
      {"label":"A — short stopping arrow (high friction)", "svg": '''<svg viewBox="0 0 200 100"><rect x="20" y="50" width="160" height="20" fill="#8FCB9B" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="60" x2="55" y2="60" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": True},
      {"label":"B — long sliding arrow (low friction)", "svg": '''<svg viewBox="0 0 200 100"><rect x="20" y="50" width="160" height="20" fill="#B9D8EA" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="60" x2="170" y2="60" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario is sliding forward with some velocity", "icon": ICON_SLIDE_ARROW},
    {"text":"Friction pushes back against that motion", "icon": ICON_FRICTION_ZIGZAG},
    {"text":"More friction = velocity drops to zero faster", "icon": ICON_STOP_ARROW},
    {"text":"🔗 Links to Velocity vs Time: friction is exactly what makes that velocity line drop back down", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "If you drew Mario's velocity-vs-time graph while sliding on ice, and another while stopping on grass, how would the two lines look different?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><line x1="20" y1="10" x2="20" y2="90" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="90" x2="180" y2="90" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["On ice, the velocity line would drop...", "On grass, the velocity line would drop..."],
    "keywords": ["friction", "velocity", "slow down", "surface"]
  },
  "predict": {
    "question": "Mario slides at the same speed onto BOTH ice and sandpaper. Which surface has more friction?",
    "explanation": "Sandpaper is rough, creating a much stronger friction force than smooth ice — more friction means Mario stops much sooner on sandpaper.",
    "choices": [
      {"text": "Ice has more friction", "correct": False},
      {"text": "Sandpaper has more friction", "correct": True},
      {"text": "They have exactly equal friction", "correct": False},
    ]
  }
}
open("mario-05-friction.html", "w", encoding="utf-8").write(build("mario-05-friction", "Mario: Friction (Ice vs Grass) 🧊", c5_data))
print("built mario-05-friction.html")

# ================= CONCEPT 6: ACCELERATION =================
c6_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Bar chart of Mario's speed increasing by a bigger amount each second, showing acceleration">
      <line x1="30" y1="170" x2="270" y2="170" stroke="#0B2545" stroke-width="2"/>
      <rect x="50" y="150" width="30" height="20" fill="#2E6E62"/>
      <rect x="110" y="110" width="30" height="60" fill="#2E6E62"/>
      <rect x="170" y="50" width="30" height="120" fill="#2E6E62"/>
      <text x="45" y="185" font-size="10" fill="#0B2545">1s</text>
      <text x="105" y="185" font-size="10" fill="#0B2545">2s</text>
      <text x="165" y="185" font-size="10" fill="#0B2545">3s</text>
    </svg>''',
    "question": "Each second, Mario's speed bar grows by MORE than the second before. What does that pattern show?",
    "explanation": "Speed increasing by a growing amount each second means Mario isn't just moving — he's accelerating, and his acceleration itself is ramping up.",
    "choices": [
      {"text": "Mario is accelerating (speeding up faster and faster)", "correct": True},
      {"text": "Mario is moving at constant speed", "correct": False},
      {"text": "Mario is slowing down", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"accel_bars","name":"Growing bars (accelerating)","icon":ICON_ACCEL_STEPS,"fact":"📈 Each bar taller than the last — speed increasing faster and faster."},
    {"id":"constant_bars","name":"Equal bars (constant speed)","icon":ICON_CONSTANT_STEPS,"fact":"➡️ Same-height bars — speed staying exactly the same, no acceleration."},
    {"id":"push_force","name":"Push force","icon":ICON_JUMP_PUSH,"fact":"👟 The force Mario applies (running harder) that causes acceleration in the first place."},
  ]},
  "draw": {
    "prompt": "Draw a bar chart of Mario's speed at 1, 2, and 3 seconds — make each bar taller than the last to show acceleration.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <line x1="30" y1="170" x2="270" y2="170" stroke="#0B2545" stroke-width="2"/>
      <rect x="50" y="150" width="30" height="20" fill="#2E6E62"/>
      <rect x="110" y="110" width="30" height="60" fill="#2E6E62"/>
      <rect x="170" y="50" width="30" height="120" fill="#2E6E62"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the bar chart sideways. Do the bars still show 'growing bigger' in the same order?",
    "svg": '''<line x1="20" y1="20" x2="20" y2="150" stroke="#0B2545" stroke-width="2"/>
      <rect x="30" y="120" width="20" height="15" fill="#2E6E62"/>
      <rect x="30" y="80" width="60" height="15" fill="#2E6E62"/>
      <rect x="30" y="40" width="110" height="15" fill="#2E6E62"/>'''
  },
  "compare": {
    "question": "Tap the bar chart that shows Mario ACCELERATING (bars growing each second).",
    "explanation": "Bars that grow taller each second show speed increasing over time — that's the visual signature of acceleration.",
    "choices": [
      {"label":"A — growing bars", "svg": '''<svg viewBox="0 0 200 140"><line x1="20" y1="120" x2="180" y2="120" stroke="#0B2545" stroke-width="2"/><rect x="40" y="100" width="20" height="20" fill="#2E6E62"/><rect x="80" y="70" width="20" height="50" fill="#2E6E62"/><rect x="120" y="30" width="20" height="90" fill="#2E6E62"/></svg>''', "correct": True},
      {"label":"B — equal-height bars", "svg": '''<svg viewBox="0 0 200 140"><line x1="20" y1="120" x2="180" y2="120" stroke="#0B2545" stroke-width="2"/><rect x="40" y="70" width="20" height="50" fill="#0B2545"/><rect x="80" y="70" width="20" height="50" fill="#0B2545"/><rect x="120" y="70" width="20" height="50" fill="#0B2545"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario pushes harder off the ground each step", "icon": ICON_JUMP_PUSH},
    {"text":"That extra push force adds extra speed each second", "icon": ICON_ACCEL_STEPS},
    {"text":"Speed growing every second = acceleration", "icon": ICON_SLIDE_ARROW},
    {"text":"🔗 Links to Velocity vs Time: acceleration is just the STEEPNESS of that velocity line", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "How would you tell, just by looking at a velocity-vs-time graph, whether Mario is accelerating or moving at constant speed?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><line x1="20" y1="10" x2="20" y2="90" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="90" x2="180" y2="90" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["If the velocity line is sloped, that means...", "If the velocity line is flat, that means..."],
    "keywords": ["acceleration", "velocity", "slope", "constant"]
  },
  "predict": {
    "question": "Mario runs and his speed grows by exactly the same amount every second (steady growth). What kind of acceleration is that?",
    "explanation": "Equal speed gains every second is the definition of constant (steady) acceleration — not zero acceleration, and not runaway/growing acceleration.",
    "choices": [
      {"text": "Constant acceleration", "correct": True},
      {"text": "Zero acceleration", "correct": False},
      {"text": "Acceleration that keeps increasing", "correct": False},
    ]
  }
}
open("mario-06-acceleration.html", "w", encoding="utf-8").write(build("mario-06-acceleration", "Mario: Acceleration ⏫", c6_data))
print("built mario-06-acceleration.html")

# ================= CONCEPT 7: ENERGY TRANSFORMATION (POTENTIAL <-> KINETIC) =================
c7_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 220" role="img" aria-label="Mario at the top of a pipe with potential energy, then at the bottom moving fast with kinetic energy">
      <rect x="20" y="140" width="30" height="60" fill="#3F8F5C" stroke="#0B2545" stroke-width="2"/>
      <circle cx="35" cy="120" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <text x="8" y="105" font-size="10" fill="#2E6E62">high PE</text>
      <line x1="70" y1="130" x2="230" y2="190" stroke="#0B2545" stroke-width="1.5" stroke-dasharray="4 3"/>
      <circle cx="230" cy="195" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <path d="M245 195 L260 195" stroke="#2E6E62" stroke-width="3"/>
      <path d="M252 188 L262 195 L252 202" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <text x="200" y="215" font-size="10" fill="#2E6E62">high KE</text>
    </svg>''',
    "question": "Mario stands high on a pipe, then slides down. What happens to his potential energy as he goes down?",
    "explanation": "As height decreases, potential energy decreases too — and that lost potential energy doesn't vanish, it converts into kinetic energy (motion), which is why he speeds up.",
    "choices": [
      {"text": "It decreases, converting into kinetic energy", "correct": True},
      {"text": "It increases the whole way down", "correct": False},
      {"text": "It disappears completely with no effect", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"pe","name":"Potential energy","icon":ICON_POTENTIAL,"fact":"⬆️ Stored energy from height — the higher up Mario is, the more he has."},
    {"id":"ke","name":"Kinetic energy","icon":ICON_KINETIC,"fact":"💨 Energy of motion — the faster Mario moves, the more he has."},
    {"id":"height","name":"Height","icon":ICON_HEIGHT_ARROW,"fact":"📏 How far up Mario is — directly controls how much potential energy he's storing."},
  ]},
  "draw": {
    "prompt": "Draw Mario high up on a platform (label potential energy), then at the bottom moving fast (label kinetic energy).",
    "hintSvg": '''<svg viewBox="0 0 300 220" role="img" aria-label="hint">
      <rect x="20" y="140" width="30" height="60" fill="#3F8F5C" stroke="#0B2545" stroke-width="2"/>
      <circle cx="35" cy="120" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="70" y1="130" x2="230" y2="190" stroke="#0B2545" stroke-width="1.5" stroke-dasharray="4 3"/>
      <circle cx="230" cy="195" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the picture. Does 'high up = more potential energy' still make sense, or does rotating break the idea?",
    "svg": '''<rect x="20" y="90" width="25" height="40" fill="#3F8F5C" stroke="#0B2545" stroke-width="2"/>
      <circle cx="32" cy="78" r="8" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="55" y1="85" x2="160" y2="120" stroke="#0B2545" stroke-width="1.5" stroke-dasharray="3 2"/>
      <circle cx="160" cy="122" r="8" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing Mario with HIGH potential energy (high up, not moving yet).",
    "explanation": "Potential energy comes from height, not speed — the picture with Mario perched up high (before sliding) has the most potential energy.",
    "choices": [
      {"label":"A — Mario high up on platform", "svg": '''<svg viewBox="0 0 200 140"><rect x="30" y="80" width="25" height="50" fill="#3F8F5C" stroke="#0B2545" stroke-width="2"/><circle cx="42" cy="65" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": True},
      {"label":"B — Mario at the bottom moving fast", "svg": '''<svg viewBox="0 0 200 140"><circle cx="130" cy="110" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/><path d="M145 110 L165 110" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario climbs up high, storing potential energy", "icon": ICON_POTENTIAL},
    {"text":"He slides down, losing height and losing potential energy", "icon": ICON_HEIGHT_ARROW},
    {"text":"That lost energy shows up as kinetic energy — he moves faster", "icon": ICON_KINETIC},
    {"text":"🔗 Links to Mario's Jump Arc: the SAME energy swap happens going up (KE→PE) and coming back down (PE→KE)", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "At the very peak of Mario's jump, his vertical speed is zero for an instant. What does that tell you about his kinetic and potential energy at that exact moment?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M20 90 Q100 10 180 90" fill="none" stroke="#2E6E62" stroke-width="3"/><circle cx="100" cy="16" r="6" fill="#D9603B"/></svg>''',
    "starters": ["At the peak, kinetic energy from the jump is...", "At the peak, potential energy is..."],
    "keywords": ["potential", "kinetic", "peak", "height"]
  },
  "predict": {
    "question": "Mario climbs to DOUBLE the height before sliding down a frictionless slide. What happens to his speed at the bottom?",
    "explanation": "Double the height means double the starting potential energy, and since energy converts rather than vanishing, that means significantly more kinetic energy — and a noticeably faster speed — at the bottom.",
    "choices": [
      {"text": "He'll be moving faster at the bottom", "correct": True},
      {"text": "His speed at the bottom stays exactly the same", "correct": False},
      {"text": "He'll be moving slower at the bottom", "correct": False},
    ]
  }
}
open("mario-07-energy-transformation.html", "w", encoding="utf-8").write(build("mario-07-energy-transformation", "Mario: Energy Transformation 🔋", c7_data))
print("built mario-07-energy-transformation.html")

# ================= CONCEPT 8: MOMENTUM & COLLISIONS =================
c8_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Mario running fast toward a Goomba, then colliding and stopping the Goomba">
      <circle cx="70" cy="120" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="90" y1="120" x2="140" y2="120" stroke="#2E6E62" stroke-width="3"/>
      <path d="M130 112 L144 120 L130 128" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <ellipse cx="200" cy="130" rx="20" ry="14" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
      <path d="M180 155 L145 175" stroke="#C9A24B" stroke-width="2" stroke-dasharray="3 2"/>
    </svg>''',
    "question": "Mario runs fast and stomps a slow Goomba. What determined how much the Goomba got knocked back?",
    "explanation": "Momentum depends on both mass and velocity. Mario's running speed gives him lots of momentum to transfer, which is what sends the Goomba flying — not just his size.",
    "choices": [
      {"text": "Mario's momentum (mass × velocity)", "correct": True},
      {"text": "Only Mario's mass, speed doesn't matter", "correct": False},
      {"text": "Random chance — physics doesn't decide it", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"momentum","name":"Momentum","icon":ICON_MOMENTUM_ARROW,"fact":"➡️ Mass × velocity — a heavy, fast-moving Mario has a lot of it."},
    {"id":"collision","name":"Collision","icon":ICON_COLLISION_STAR,"fact":"💥 The moment Mario and the Goomba meet — momentum transfers between them."},
    {"id":"goomba","name":"Goomba (target)","icon":ICON_GOOMBA,"fact":"👣 Receives momentum from the collision and gets knocked back or defeated."},
  ]},
  "draw": {
    "prompt": "Draw Mario running toward a Goomba with a speed arrow, then the Goomba flying backward after the hit.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <circle cx="70" cy="120" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="90" y1="120" x2="140" y2="120" stroke="#2E6E62" stroke-width="3"/>
      <ellipse cx="200" cy="130" rx="20" ry="14" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the collision picture. Does 'momentum transfers in the direction Mario was moving' still hold true?",
    "svg": '''<circle cx="60" cy="90" r="12" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="76" y1="90" x2="115" y2="90" stroke="#2E6E62" stroke-width="3"/>
      <ellipse cx="160" cy="95" rx="16" ry="11" fill="#8B5E3C" stroke="#0B2545" stroke-width="2"/>'''
  },
  "compare": {
    "question": "Tap the picture showing Mario with MORE momentum (running fast, not just standing).",
    "explanation": "Momentum needs velocity as well as mass — a fast-moving Mario carries much more momentum than a standing-still Mario of the same size.",
    "choices": [
      {"label":"A — Mario running fast", "svg": '''<svg viewBox="0 0 200 120"><circle cx="60" cy="60" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/><line x1="80" y1="60" x2="140" y2="60" stroke="#2E6E62" stroke-width="4"/></svg>''', "correct": True},
      {"label":"B — Mario standing still", "svg": '''<svg viewBox="0 0 200 120"><circle cx="100" cy="60" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario builds up speed (velocity) while running", "icon": ICON_ACCEL_STEPS},
    {"text":"Mass × velocity gives him momentum", "icon": ICON_MOMENTUM_ARROW},
    {"text":"On collision, that momentum transfers to the Goomba", "icon": ICON_COLLISION_STAR},
    {"text":"🔗 Links to Acceleration: building velocity through acceleration is exactly what loads up Mario's momentum before impact", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Would a slow-moving heavy Mario (like with a shell) or a fast-moving light Mario hit a Goomba harder? Use the idea of momentum to explain.",
    "visualSvg": '''<svg viewBox="0 0 200 100"><circle cx="60" cy="50" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/><line x1="80" y1="50" x2="120" y2="50" stroke="#2E6E62" stroke-width="3"/></svg>''',
    "starters": ["Momentum depends on both mass and velocity, so...", "A heavy but slow Mario would..."],
    "keywords": ["momentum", "mass", "velocity", "collision"]
  },
  "predict": {
    "question": "Mario is running at TOP speed (much faster than usual) when he stomps a Goomba. What happens to the Goomba compared to a normal-speed stomp?",
    "explanation": "More velocity means more momentum for the same mass, so the collision transfers more momentum — the Goomba gets knocked back much harder than in a normal stomp.",
    "choices": [
      {"text": "The Goomba gets knocked back much harder", "correct": True},
      {"text": "Nothing changes — speed doesn't affect the hit", "correct": False},
      {"text": "The Goomba is knocked back less", "correct": False},
    ]
  }
}
open("mario-08-momentum-collisions.html", "w", encoding="utf-8").write(build("mario-08-momentum-collisions", "Mario: Momentum & Collisions 💥", c8_data))
print("built mario-08-momentum-collisions.html")
