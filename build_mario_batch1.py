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

# ---------------- shared icons (Mario palette, reuse ocean/titanic hues) ----------------
ICON_MARIO_DOT = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='10' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><rect x='14' y='14' width='12' height='5' fill='#0B2545'/></svg>"
ICON_FLAG = "<svg viewBox='0 0 40 40'><line x1='10' y1='4' x2='10' y2='36' stroke='#0B2545' stroke-width='3'/><path d='M10 6 L32 12 L10 18 Z' fill='#3F8F5C'/></svg>"
ICON_CLOCK_GRAPH = "<svg viewBox='0 0 40 40'><line x1='6' y1='34' x2='6' y2='6' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='34' x2='34' y2='34' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='30' x2='30' y2='10' stroke='#2E6E62' stroke-width='3'/></svg>"
ICON_FLAT_LINE = "<svg viewBox='0 0 40 40'><line x1='6' y1='34' x2='6' y2='6' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='34' x2='34' y2='34' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='20' x2='34' y2='20' stroke='#D9603B' stroke-width='3'/></svg>"
ICON_STEEP_LINE = "<svg viewBox='0 0 40 40'><line x1='6' y1='34' x2='6' y2='6' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='34' x2='34' y2='34' stroke='#0B2545' stroke-width='2'/><line x1='6' y1='32' x2='26' y2='8' stroke='#2E6E62' stroke-width='3'/></svg>"
ICON_SPEED_UP = "<svg viewBox='0 0 40 40'><path d='M4 30 Q18 30 36 6' fill='none' stroke='#D9603B' stroke-width='3'/></svg>"
ICON_GRAVITY = "<svg viewBox='0 0 40 40'><line x1='20' y1='6' x2='20' y2='30' stroke='#0B2545' stroke-width='3'/><path d='M12 22 L20 34 L28 22 Z' fill='#0B2545'/></svg>"
ICON_NORMAL_FORCE = "<svg viewBox='0 0 40 40'><line x1='20' y1='34' x2='20' y2='10' stroke='#2E6E62' stroke-width='3'/><path d='M12 20 L20 8 L28 20 Z' fill='#2E6E62'/></svg>"
ICON_JUMP_PUSH = "<svg viewBox='0 0 40 40'><circle cx='20' cy='12' r='7' fill='#D9603B' stroke='#0B2545' stroke-width='2'/><line x1='20' y1='19' x2='20' y2='34' stroke='#2E6E62' stroke-width='3'/><path d='M12 26 L20 36 L28 26' fill='none' stroke='#2E6E62' stroke-width='3'/></svg>"
ICON_GROUND = "<svg viewBox='0 0 40 40'><rect x='2' y='24' width='36' height='12' fill='#DCD3BC' stroke='#0B2545' stroke-width='2'/></svg>"
ICON_ARC = "<svg viewBox='0 0 40 40'><path d='M4 32 Q20 4 36 32' fill='none' stroke='#2E6E62' stroke-width='3'/><circle cx='20' cy='11' r='3' fill='#D9603B'/></svg>"
ICON_ARC_HALF_UP = "<svg viewBox='0 0 40 40'><path d='M4 32 Q20 4 20 4' fill='none' stroke='#2E6E62' stroke-width='3'/></svg>"
ICON_ARC_HALF_DOWN = "<svg viewBox='0 0 40 40'><path d='M20 4 Q20 4 36 32' fill='none' stroke='#D9603B' stroke-width='3'/></svg>"
ICON_LINK = "<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/><circle cx='26' cy='20' r='8' fill='none' stroke='#C9A24B' stroke-width='3'/></svg>"

# ================= CONCEPT 1: POSITION VS TIME =================
c1_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Position vs time graph showing Mario's distance from start increasing over time">
      <line x1="40" y1="20" x2="40" y2="170" stroke="#0B2545" stroke-width="2"/>
      <line x1="40" y1="170" x2="270" y2="170" stroke="#0B2545" stroke-width="2"/>
      <text x="6" y="20" font-size="11" fill="#0B2545">Position</text>
      <text x="230" y="190" font-size="11" fill="#0B2545">Time →</text>
      <line x1="40" y1="150" x2="230" y2="40" stroke="#D9603B" stroke-width="3"/>
    </svg>''',
    "question": "The line goes UP and to the right the whole time. What does that mean Mario is doing?",
    "explanation": "A rising position-vs-time line means position keeps increasing — Mario is moving forward the whole time, never stopping or going back.",
    "choices": [
      {"text": "Moving forward the whole time", "correct": True},
      {"text": "Standing completely still", "correct": False},
      {"text": "Running backward", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"steep","name":"Steep line","icon":ICON_STEEP_LINE,"fact":"⚡ A steep line means Mario covers LOTS of distance in a short time — he's moving fast."},
    {"id":"flat","name":"Flat line","icon":ICON_FLAT_LINE,"fact":"⏸️ A flat line means position isn't changing at all — Mario is standing still."},
    {"id":"rising","name":"Rising line","icon":ICON_CLOCK_GRAPH,"fact":"📈 Any upward slope means Mario is moving forward — the steeper it is, the faster he's going."},
  ]},
  "draw": {
    "prompt": "Draw a position-vs-time graph for Mario: flat while he's standing still, then rising while he runs.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <line x1="40" y1="20" x2="40" y2="170" stroke="#0B2545" stroke-width="2"/>
      <line x1="40" y1="170" x2="270" y2="170" stroke="#0B2545" stroke-width="2"/>
      <line x1="40" y1="150" x2="120" y2="150" stroke="#D9603B" stroke-width="3"/>
      <line x1="120" y1="150" x2="230" y2="40" stroke="#D9603B" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the graph. Does a flat section still mean 'standing still' no matter how you turn it?",
    "svg": '''<line x1="30" y1="15" x2="30" y2="130" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="130" x2="200" y2="130" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="110" x2="170" y2="30" stroke="#D9603B" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the graph showing Mario moving FASTER (steeper line).",
    "explanation": "A steeper slope on a position-vs-time graph always means faster movement — more distance covered per second.",
    "choices": [
      {"label":"A — steep line", "svg": '''<svg viewBox="0 0 200 140"><line x1="30" y1="10" x2="30" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="120" x2="180" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="110" x2="150" y2="20" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": True},
      {"label":"B — gentle line", "svg": '''<svg viewBox="0 0 200 140"><line x1="30" y1="10" x2="30" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="120" x2="180" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="115" x2="150" y2="95" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario starts at position 0", "icon": ICON_MARIO_DOT},
    {"text":"Each second, his position number grows", "icon": ICON_CLOCK_GRAPH},
    {"text":"Plotting position over time draws a rising line", "icon": ICON_STEEP_LINE},
    {"text":"🔗 Links to Titanic Speed-Time Graph: same graph skill, just tracking a different kind of mover", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "If Mario runs, then stops to think, then runs again, what would the shape of his position-vs-time graph look like?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><line x1="20" y1="10" x2="20" y2="90" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="90" x2="180" y2="90" stroke="#0B2545" stroke-width="2"/></svg>''',
    "starters": ["While Mario runs, the line...", "While Mario is stopped, the line..."],
    "keywords": ["rising", "flat", "position", "time"]
  },
  "predict": {
    "question": "Mario's position-vs-time graph suddenly goes flat for 3 seconds. What is he doing?",
    "explanation": "A flat line means position isn't changing at all — no matter how much time passes, Mario stays in the same spot, so he must be standing still.",
    "choices": [
      {"text": "Running at top speed", "correct": False},
      {"text": "Standing completely still", "correct": True},
      {"text": "Running backward fast", "correct": False},
    ]
  }
}
open("mario-01-position-vs-time.html", "w", encoding="utf-8").write(build("mario-01-position-vs-time", "Mario: Position vs Time 🏃", c1_data))
print("built mario-01-position-vs-time.html")

# ================= CONCEPT 2: VELOCITY VS TIME =================
c2_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Velocity vs time graph showing Mario speeding up then holding steady speed">
      <line x1="40" y1="20" x2="40" y2="170" stroke="#0B2545" stroke-width="2"/>
      <line x1="40" y1="170" x2="270" y2="170" stroke="#0B2545" stroke-width="2"/>
      <path d="M40 160 Q100 60 150 60 L250 60" fill="none" stroke="#D9603B" stroke-width="3"/>
      <text x="150" y="45" font-size="11" fill="#2E6E62">steady top speed</text>
    </svg>''',
    "question": "The line rises, then goes FLAT while staying up high. What's happening in that flat part?",
    "explanation": "A flat velocity line (that isn't at zero) means speed has stopped changing — Mario has reached his top speed and is now cruising at a constant velocity.",
    "choices": [
      {"text": "Mario is cruising at a constant top speed", "correct": True},
      {"text": "Mario has stopped moving completely", "correct": False},
      {"text": "Mario is still speeding up", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"speeding_up","name":"Speeding up","icon":ICON_SPEED_UP,"fact":"⏫ Velocity line rising = Mario is accelerating, getting faster each second."},
    {"id":"constant_v","name":"Constant velocity","icon":ICON_FLAT_LINE,"fact":"➡️ A flat (non-zero) velocity line = same speed every second, no speeding up or slowing down."},
    {"id":"zero_v","name":"Zero velocity","icon":ICON_GROUND,"fact":"🛑 Velocity line sitting right on the zero axis = Mario isn't moving at all."},
  ]},
  "draw": {
    "prompt": "Draw a velocity-vs-time graph: rising while Mario speeds up, then flat while he holds top speed.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <line x1="40" y1="20" x2="40" y2="170" stroke="#0B2545" stroke-width="2"/>
      <line x1="40" y1="170" x2="270" y2="170" stroke="#0B2545" stroke-width="2"/>
      <path d="M40 160 Q100 60 150 60 L250 60" fill="none" stroke="#D9603B" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Rotate the graph. Does a flat section at the top still mean 'constant speed,' or does rotating scramble the meaning?",
    "svg": '''<line x1="30" y1="15" x2="30" y2="130" stroke="#0B2545" stroke-width="2"/>
      <line x1="30" y1="130" x2="200" y2="130" stroke="#0B2545" stroke-width="2"/>
      <path d="M30 120 Q80 50 120 50 L180 50" fill="none" stroke="#D9603B" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the graph showing Mario at CONSTANT velocity (flat, non-zero line).",
    "explanation": "A flat line above zero means the speed itself isn't changing — that's the definition of constant velocity.",
    "choices": [
      {"label":"A — flat line above zero", "svg": '''<svg viewBox="0 0 200 140"><line x1="30" y1="10" x2="30" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="120" x2="180" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="60" x2="170" y2="60" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": True},
      {"label":"B — rising line", "svg": '''<svg viewBox="0 0 200 140"><line x1="30" y1="10" x2="30" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="120" x2="180" y2="120" stroke="#0B2545" stroke-width="2"/><line x1="30" y1="110" x2="170" y2="20" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario pushes off and speeds up (velocity line rises)", "icon": ICON_SPEED_UP},
    {"text":"He reaches his top running speed", "icon": ICON_CLOCK_GRAPH},
    {"text":"The velocity line goes flat — constant speed now", "icon": ICON_FLAT_LINE},
    {"text":"🔗 Links to Position vs Time: this velocity graph is showing the SLOPE of that position graph", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "How is a velocity-vs-time graph different from a position-vs-time graph, even though they're both about the same run?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><line x1="20" y1="10" x2="20" y2="90" stroke="#0B2545" stroke-width="2"/><line x1="20" y1="90" x2="180" y2="90" stroke="#0B2545" stroke-width="2"/><path d="M20 80 Q60 30 100 30 L160 30" fill="none" stroke="#D9603B" stroke-width="3"/></svg>''',
    "starters": ["Position tells you where he is, but velocity tells you...", "A flat line means something different on each graph because..."],
    "keywords": ["velocity", "position", "constant", "speed"]
  },
  "predict": {
    "question": "Mario's velocity graph rises, flattens, then suddenly drops straight to zero. What just happened?",
    "explanation": "Dropping straight to zero means his speed instantly became nothing — he stopped moving, probably by hitting a wall or a Goomba.",
    "choices": [
      {"text": "He sped up even more", "correct": False},
      {"text": "He stopped suddenly (hit something)", "correct": True},
      {"text": "He kept the same constant speed", "correct": False},
    ]
  }
}
open("mario-02-velocity-vs-time.html", "w", encoding="utf-8").write(build("mario-02-velocity-vs-time", "Mario: Velocity vs Time 💨", c2_data))
print("built mario-02-velocity-vs-time.html")

# ================= CONCEPT 3: FORCES ON MARIO (FREE BODY DIAGRAM) =================
c3_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 220" role="img" aria-label="Free body diagram of Mario standing on the ground showing gravity down and normal force up">
      <rect x="2" y="150" width="296" height="20" fill="#DCD3BC" stroke="#0B2545" stroke-width="2"/>
      <circle cx="150" cy="110" r="18" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="150" y1="110" x2="150" y2="60" stroke="#2E6E62" stroke-width="3"/>
      <path d="M142 70 L150 56 L158 70 Z" fill="#2E6E62"/>
      <text x="150" y="46" text-anchor="middle" font-size="12" fill="#2E6E62">Normal force ↑</text>
      <line x1="150" y1="128" x2="150" y2="185" stroke="#D9603B" stroke-width="3"/>
      <path d="M142 175 L150 189 L158 175 Z" fill="#D9603B"/>
      <text x="150" y="205" text-anchor="middle" font-size="12" fill="#D9603B">Weight ↓</text>
    </svg>''',
    "question": "Mario stands still on flat ground. What happens when weight (down) exactly equals normal force (up)?",
    "explanation": "When the two forces are equal, they cancel out to a net force of zero — that's why Mario just stands there instead of sinking into the ground or floating up.",
    "choices": [
      {"text": "Mario stays still — the forces are balanced", "correct": True},
      {"text": "Mario shoots up into the air", "correct": False},
      {"text": "Mario sinks through the floor", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"gravity","name":"Weight (gravity)","icon":ICON_GRAVITY,"fact":"⬇️ Gravity pulls Mario straight down toward the ground, always."},
    {"id":"normal","name":"Normal force","icon":ICON_NORMAL_FORCE,"fact":"⬆️ The ground pushes back up on Mario, exactly opposing gravity when he's standing still."},
    {"id":"ground","name":"Ground / floor","icon":ICON_GROUND,"fact":"🧱 The surface providing the normal force — no floor, no push back."},
  ]},
  "draw": {
    "prompt": "Draw Mario standing on the ground with two arrows: one down for weight, one up for normal force.",
    "hintSvg": '''<svg viewBox="0 0 300 220" role="img" aria-label="hint">
      <rect x="2" y="150" width="296" height="20" fill="#DCD3BC" stroke="#0B2545" stroke-width="2"/>
      <circle cx="150" cy="110" r="18" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="150" y1="110" x2="150" y2="60" stroke="#2E6E62" stroke-width="3"/>
      <line x1="150" y1="128" x2="150" y2="185" stroke="#D9603B" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Tilt the whole picture sideways. Do the force arrows tilt with Mario, or do they still point straight up/down?",
    "svg": '''<circle cx="110" cy="90" r="16" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <line x1="110" y1="90" x2="110" y2="45" stroke="#2E6E62" stroke-width="3"/>
      <line x1="110" y1="106" x2="110" y2="150" stroke="#D9603B" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the diagram showing Mario about to be LAUNCHED upward (unbalanced forces).",
    "explanation": "When the up-arrow (like a jump force) is bigger than weight, the net force points up — that's what launches Mario off the ground.",
    "choices": [
      {"label":"A — balanced (standing)", "svg": '''<svg viewBox="0 0 200 140"><circle cx="100" cy="70" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/><line x1="100" y1="70" x2="100" y2="35" stroke="#2E6E62" stroke-width="2"/><line x1="100" y1="84" x2="100" y2="120" stroke="#2E6E62" stroke-width="2"/></svg>''', "correct": False},
      {"label":"B — unbalanced (jumping)", "svg": '''<svg viewBox="0 0 200 140"><circle cx="100" cy="70" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/><line x1="100" y1="70" x2="100" y2="15" stroke="#D9603B" stroke-width="4"/><line x1="100" y1="84" x2="100" y2="105" stroke="#D9603B" stroke-width="2"/></svg>''', "correct": True},
    ]
  },
  "connect": {"items": [
    {"text":"Gravity pulls Mario down every moment", "icon": ICON_GRAVITY},
    {"text":"The ground pushes back up with normal force", "icon": ICON_NORMAL_FORCE},
    {"text":"When they're equal, Mario stands still — unequal, he moves", "icon": ICON_JUMP_PUSH},
    {"text":"🔗 Links to Titanic Free Body Diagram: same two-arrow balance trick, just gravity+ground instead of gravity+buoyancy", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "The Titanic floats because buoyant force balances weight. Mario stands because normal force balances weight. What's the same about these two ideas, and what's different?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><circle cx="100" cy="50" r="14" fill="#D9603B" stroke="#0B2545" stroke-width="2"/><line x1="100" y1="50" x2="100" y2="15" stroke="#2E6E62" stroke-width="3"/><line x1="100" y1="64" x2="100" y2="90" stroke="#D9603B" stroke-width="3"/></svg>''',
    "starters": ["Both ideas are the same because...", "The difference is..."],
    "keywords": ["balanced", "gravity", "normal force", "buoyant force"]
  },
  "predict": {
    "question": "Mario jumps by pushing off the ground with a force bigger than his weight. What happens the instant he pushes off?",
    "explanation": "An upward force bigger than weight creates a net upward force, launching Mario off the ground — same unbalanced-force logic as any launch or takeoff.",
    "choices": [
      {"text": "He launches upward off the ground", "correct": True},
      {"text": "He stays perfectly still", "correct": False},
      {"text": "He sinks further into the ground", "correct": False},
    ]
  }
}
open("mario-03-forces-on-mario.html", "w", encoding="utf-8").write(build("mario-03-forces-on-mario", "Mario: Forces on Mario ⚖️", c3_data))
print("built mario-03-forces-on-mario.html")

# ================= CONCEPT 4: PROJECTILE MOTION (JUMP ARC) =================
c4_data = {
  "observe": {
    "svg": '''<svg viewBox="0 0 300 200" role="img" aria-label="Parabolic arc showing Mario's jump trajectory, rising then falling symmetrically">
      <rect x="0" y="180" width="300" height="12" fill="#DCD3BC"/>
      <path d="M30 175 Q150 20 270 175" fill="none" stroke="#2E6E62" stroke-width="3"/>
      <circle cx="150" cy="45" r="10" fill="#D9603B" stroke="#0B2545" stroke-width="2"/>
      <text x="150" y="30" text-anchor="middle" font-size="11" fill="#2E6E62">peak</text>
    </svg>''',
    "question": "Look at the jump arc shape. Is the rising half a MIRROR of the falling half?",
    "explanation": "A projectile's path (with no other forces like wind) is symmetric — the way up mirrors the way down exactly, just reversed in time.",
    "choices": [
      {"text": "Yes — it's a symmetric mirror shape", "correct": True},
      {"text": "No — the falling half is much steeper", "correct": False},
      {"text": "No — Mario falls straight down after the peak", "correct": False},
    ]
  },
  "label": {"items": [
    {"id":"peak","name":"Peak of jump","icon":ICON_MARIO_DOT,"fact":"⛰️ The highest point — for just an instant, Mario's vertical velocity is zero."},
    {"id":"rising_half","name":"Rising half","icon":ICON_ARC_HALF_UP,"fact":"⬆️ Mario moves up and forward, slowing down vertically as gravity fights him."},
    {"id":"falling_half","name":"Falling half","icon":ICON_ARC_HALF_DOWN,"fact":"⬇️ Mario moves down and forward, speeding up vertically as gravity wins."},
  ]},
  "draw": {
    "prompt": "Draw Mario's jump arc — a smooth symmetric curve, up then down, like a rainbow.",
    "hintSvg": '''<svg viewBox="0 0 300 200" role="img" aria-label="hint">
      <rect x="0" y="180" width="300" height="12" fill="#DCD3BC"/>
      <path d="M30 175 Q150 20 270 175" fill="none" stroke="#2E6E62" stroke-width="3"/>
    </svg>'''
  },
  "rotate": {
    "prompt": "Flip the arc upside down. Does it still look like a valid jump shape, or does gravity's direction stop making sense?",
    "svg": '''<path d="M30 40 Q150 190 270 40" fill="none" stroke="#2E6E62" stroke-width="3"/>'''
  },
  "compare": {
    "question": "Tap the picture showing the CORRECT jump arc shape (smooth curve, symmetric).",
    "explanation": "A real jump arc is a smooth, symmetric curve — a sharp V-shape would mean Mario instantly changed direction, which isn't how gravity works.",
    "choices": [
      {"label":"A — smooth curved arc", "svg": '''<svg viewBox="0 0 200 140"><path d="M20 120 Q100 20 180 120" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''', "correct": True},
      {"label":"B — sharp V shape", "svg": '''<svg viewBox="0 0 200 140"><path d="M20 120 L100 20 L180 120" fill="none" stroke="#D9603B" stroke-width="3"/></svg>''', "correct": False},
    ]
  },
  "connect": {"items": [
    {"text":"Mario pushes off, launching up and forward at once", "icon": ICON_JUMP_PUSH},
    {"text":"Gravity constantly pulls him down while he moves forward", "icon": ICON_GRAVITY},
    {"text":"Those two motions combine into one smooth curved arc", "icon": ICON_ARC},
    {"text":"🔗 Links to Forces on Mario: gravity is the exact same downward force that shapes this whole curve", "icon": ICON_LINK},
  ]},
  "explain": {
    "prompt": "Why does Mario's jump arc curve instead of forming a straight diagonal line?",
    "visualSvg": '''<svg viewBox="0 0 200 100"><path d="M20 80 Q100 10 180 80" fill="none" stroke="#2E6E62" stroke-width="3"/></svg>''',
    "starters": ["The arc curves because gravity...", "If there were no gravity, the path would..."],
    "keywords": ["gravity", "arc", "curve", "forward"]
  },
  "predict": {
    "question": "Mario jumps with MORE forward speed but the SAME jump force. How does the arc change?",
    "explanation": "More forward speed stretches the same up-and-down arc shape out wider — same height, but Mario covers more ground before landing.",
    "choices": [
      {"text": "The arc gets wider (covers more distance) but stays the same height", "correct": True},
      {"text": "The arc gets much taller", "correct": False},
      {"text": "The arc disappears completely", "correct": False},
    ]
  }
}
open("mario-04-projectile-motion.html", "w", encoding="utf-8").write(build("mario-04-projectile-motion", "Mario: Jump Arc 🌈", c4_data))
print("built mario-04-projectile-motion.html")
