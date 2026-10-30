#!/usr/bin/env python3
"""
Build all 10 VST Thinking Lab (Vol.1) files from vst-template-source.html.
Fail-loud: crashes on missing keys or malformed template markers rather than
silently producing broken output.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "vst-template-source.html"
OUT_DIR = ROOT / "deliverables"

# ---------------------------------------------------------------------------
# CONTENT — 10 labs, Vol.1. Each lab drills ONE thinking skill using a fresh
# example pulled from an existing theme (no new science content, just reps).
# ---------------------------------------------------------------------------

LABS = [
    {
        "id": "vst-01-see-like-a-scientist",
        "title": "See Like a Scientist",
        "domain": "👀 See",
        "notice_scenario": "🚢 Cargo is slowly being loaded onto the Titanic. Crate after crate goes into the hold.",
        "notice_question": "What changes as more cargo goes in — and what changes does that CAUSE?",
        "notice_choices": [
            ("The ship gets heavier, and it sits lower in the water", True, "⚖️"),
            ("Nothing changes until the ship is 100% full", False, "🚫"),
            ("The ship gets lighter as it fills up", False, "❌"),
        ],
        "notice_explain": "A real scientist doesn't just say 'it changed' — they say WHAT changed and WHAT ELSE changed because of it. Weight up → sits lower. That's a chain.",
        "practice_mode": "text",
        "practice_instructions": "Pick ONE of these and list at least 3 things that change as it happens: 🌙 the Moon over a month, 🍳 a pancake as it cooks, 🍄 Mario as gravity gets weaker.",
        "practice_prompt": "What did you pick? List everything you notice changing, one at a time.",
        "practice_starters": ["I noticed the shape changes...", "I noticed the size changes...", "I noticed the position changes..."],
        "practice_keywords": ["shape", "size", "position", "color", "speed", "pattern"],
        "predict_scenario": "🍄 Now imagine gravity on Mario's world gets EVEN weaker, little by little, over several jumps.",
        "test_reveal": "Real scientists call this 'systematic observation' — checking the SAME thing changes in a predictable direction, step by step, instead of jumping to conclusions after one look.",
        "test_question": "Did your prediction describe a clear, step-by-step change?",
        "fix_prompt": "If you only wrote 'it got different,' what could you add to make your observation sharper?",
    },
    {
        "id": "vst-02-turn-things-into-pictures",
        "title": "Turn Things into Pictures",
        "domain": "✏️ Represent",
        "notice_scenario": "🚢 A ship isn't just a photo. Scientists draw it as a CROSS-SECTION with force arrows, not a pretty picture.",
        "notice_question": "Which picture below counts as a real scientific diagram, not just art?",
        "notice_choices": [
            ("A detailed painting of the ship's colors and flags", False, "🎨"),
            ("A simple ship shape with an up arrow and a down arrow labeled", True, "📐"),
            ("A photo-realistic sketch with shading and shadows", False, "🖼️"),
        ],
        "notice_explain": "Scientific diagrams strip away decoration and keep only what matters: shapes, arrows, and labels that show forces or parts.",
        "practice_mode": "draw",
        "practice_instructions": "Draw 🍞 a slice of bread as a MOLECULAR model — not what it looks like, but tiny circles/dots showing how its particles are packed.",
        "practice_prompt": "",
        "practice_starters": [],
        "practice_keywords": [],
        "draw_prompt": "Draw particles (dots or circles) packed together to represent bread's structure. Don't draw a realistic bread photo — draw the PATTERN of particles instead.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><rect x='60' y='30' width='280' height='140' rx='8' fill='#F3EEE1' stroke='#0B2545' stroke-width='2'/><circle cx='100' cy='60' r='7' fill='#C9A24B'/><circle cx='140' cy='60' r='7' fill='#C9A24B'/><circle cx='180' cy='60' r='7' fill='#C9A24B'/><circle cx='220' cy='60' r='7' fill='#C9A24B'/><circle cx='260' cy='60' r='7' fill='#C9A24B'/><circle cx='300' cy='60' r='7' fill='#C9A24B'/><circle cx='100' cy='95' r='7' fill='#C9A24B'/><circle cx='140' cy='95' r='7' fill='#C9A24B'/><circle cx='180' cy='95' r='7' fill='#C9A24B'/><circle cx='220' cy='95' r='7' fill='#C9A24B'/><circle cx='260' cy='95' r='7' fill='#C9A24B'/><circle cx='300' cy='95' r='7' fill='#C9A24B'/><circle cx='100' cy='130' r='7' fill='#C9A24B'/><circle cx='140' cy='130' r='7' fill='#C9A24B'/><circle cx='180' cy='130' r='7' fill='#C9A24B'/><circle cx='220' cy='130' r='7' fill='#C9A24B'/><circle cx='260' cy='130' r='7' fill='#C9A24B'/><circle cx='300' cy='130' r='7' fill='#C9A24B'/><text x='200' y='20' font-size='13' text-anchor='middle' fill='#071A33'>packed particles, not a bread photo</text></svg>",
        "predict_scenario": "🚢 If you turned the Titanic sideways and sliced it in half, what shapes would you expect to see inside?",
        "predict_keywords": ["deck", "layer", "hull", "section", "engine room"],
        "test_reveal": "A real cross-section shows deck layers stacked like a cake, with the engine room low and heavy (for balance) and passenger decks higher up.",
        "test_question": "Did your prediction include more than one layer or section?",
        "fix_prompt": "If your drawing was too realistic instead of diagram-style, what would you simplify?",
    },
    {
        "id": "vst-03-build-your-first-model",
        "title": "Build Your First Model",
        "domain": "🧩 Model",
        "notice_scenario": "🚢 A photo of the Titanic floating is NOT a model. A model shows the forces that make it float.",
        "notice_question": "Which one is actually a MODEL of floating, not just a picture?",
        "notice_choices": [
            ("A photo of the ship on calm water", False, "📷"),
            ("Water ↑ Buoyant Force, Ship, ↓ Weight — with two labeled arrows", True, "📐"),
            ("A drawing of passengers waving from the deck", False, "🖼️"),
        ],
        "notice_explain": "Model ≠ Picture. A model shows the invisible things — forces, variables, relationships — using arrows and labels, not just what a camera would see.",
        "practice_mode": "draw",
        "practice_instructions": "Build a model of 🍄 Mario standing still on the ground. Use arrows for the invisible forces acting on him, not just a picture of Mario.",
        "practice_prompt": "",
        "practice_starters": [],
        "practice_keywords": [],
        "draw_prompt": "Draw Mario as a simple shape. Add an arrow pointing DOWN labeled 'weight' and an arrow pointing UP labeled 'normal force' — same two-arrow trick as the ship.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><circle cx='200' cy='90' r='16' fill='#C9A24B'/><line x1='200' y1='106' x2='200' y2='150' stroke='#0B2545' stroke-width='5'/><line x1='200' y1='150' x2='180' y2='180' stroke='#0B2545' stroke-width='4'/><line x1='200' y1='150' x2='220' y2='180' stroke='#0B2545' stroke-width='4'/><line x1='200' y1='74' x2='200' y2='30' stroke='#2E6E62' stroke-width='5'/><polygon points='200,20 188,38 212,38' fill='#2E6E62'/><text x='200' y='15' font-size='12' text-anchor='middle' fill='#071A33'>normal force (up)</text><text x='200' y='198' font-size='12' text-anchor='middle' fill='#071A33'>weight (down, equal!)</text></svg>",
        "predict_scenario": "🌊 Now think about an iceberg floating in the ocean instead of a ship.",
        "predict_keywords": ["buoyancy", "weight", "density", "arrow", "balance"],
        "test_reveal": "An iceberg's model looks identical to the ship's: buoyant force pushing up, weight pulling down — just a different object. Same invisible rule, new example.",
        "test_question": "Did your model use the same two-arrow idea as the ship?",
        "fix_prompt": "If you only drew the object without any arrows, what invisible force would you add now?",
    },
    {
        "id": "vst-04-find-the-hidden-connection",
        "title": "Find the Hidden Connection",
        "domain": "🧩 Model",
        "notice_scenario": "🌊 Ocean temperature drops → water gets denser → it sinks → that sinking creates a current.",
        "notice_question": "What kind of chain is this — just 'A and B,' or something else?",
        "notice_choices": [
            ("Just two facts sitting next to each other, unrelated", False, "🔀"),
            ("A causal chain — each step CAUSES the next one", True, "🔗"),
            ("A random coincidence with no pattern", False, "🎲"),
        ],
        "notice_explain": "This is causal thinking: not 'A + B' but 'A affects B, which affects C.' Spotting the arrows between ideas is a superpower.",
        "practice_mode": "text",
        "practice_instructions": "Build your own 3-step causal chain using 🍳 Cooking: Temperature → ? → ?. What does temperature change, and what does THAT change?",
        "practice_prompt": "Write your chain using arrows, like: Temperature ↓ [next thing] ↓ [next thing].",
        "practice_starters": ["Temperature affects...", "Which then affects...", "Which finally causes..."],
        "practice_keywords": ["temperature", "protein", "texture", "causes", "leads to"],
        "predict_scenario": "🌌 Now try Astronomy: Distance from a star → ? → ?",
        "test_reveal": "One real chain: Distance ↓ Gravitational force ↓ Orbital speed — farther away means weaker pull, which means a slower, wider orbit.",
        "test_question": "Did your chain have at least 2 arrows (3 steps)?",
        "fix_prompt": "If your chain only had 2 steps with no clear 'causes,' what missing link would you add?",
    },
    {
        "id": "vst-05-turn-pictures-into-numbers",
        "title": "Turn Pictures into Numbers",
        "domain": "🔢 Reason",
        "notice_scenario": "🚢 You're looking at the Titanic in a diagram. A scientist doesn't just see a ship — they see NUMBERS waiting to be measured.",
        "notice_question": "Which of these could you actually measure about the ship, with a real unit?",
        "notice_choices": [
            ("How 'majestic' it looks", False, "💭"),
            ("Its mass in kilograms, or its speed in knots", True, "📏"),
            ("How much passengers enjoyed the trip", False, "💭"),
        ],
        "notice_explain": "Quantification means picking things with real units — mass, distance, time, temperature — not opinions or feelings.",
        "practice_mode": "text",
        "practice_instructions": "Look at 🍳 a pancake cooking. List at least 4 things about it you could measure with a number and a unit.",
        "practice_prompt": "List your 4+ measurable things (e.g., 'temperature in °C').",
        "practice_starters": ["I could measure...", "The unit for that would be..."],
        "practice_keywords": ["mass", "temperature", "time", "distance", "angle", "speed", "unit"],
        "predict_scenario": "🍄 Now think of Mario mid-jump.",
        "test_reveal": "Measurable things about Mario's jump: height reached (m), time in the air (s), horizontal speed (m/s), angle of the jump (degrees).",
        "test_question": "Did you list a NUMBER + UNIT for each thing, not just a word?",
        "fix_prompt": "If you listed something without a unit (like just 'heat'), what unit would fix it (like '°C')?",
    },
    {
        "id": "vst-06-make-data-tell-a-story",
        "title": "Make Data Tell a Story",
        "domain": "🔢 Reason",
        "notice_scenario": "📊 A line graph of pancake height vs. cooking temperature slopes steadily upward, then flattens out near the top.",
        "notice_question": "What does the FLAT part of the graph tell you, that the numbers alone might hide?",
        "notice_choices": [
            ("Nothing — flat parts don't mean anything", False, "🚫"),
            ("The pancake stopped rising even though temperature kept going up — a limit was reached", True, "📈"),
            ("The data must be wrong if it flattens", False, "❌"),
        ],
        "notice_explain": "A graph is also a model — its SHAPE tells a story: rising, flattening, dropping. Reading the shape is as important as reading the numbers.",
        "practice_mode": "text",
        "practice_instructions": "Imagine a graph of 🌙 Moon phase (0=new moon, 1=full moon) vs. days since new moon. Describe the SHAPE you'd expect — rising, falling, repeating?",
        "practice_prompt": "Describe the shape of your graph in words.",
        "practice_starters": ["The graph would go up when...", "The graph would go down when...", "The pattern repeats because..."],
        "practice_keywords": ["rises", "falls", "repeats", "cycle", "peak", "trend"],
        "predict_scenario": "🚢 Now picture a graph of ship mass vs. how deep it sits in the water (displacement).",
        "test_reveal": "That graph is a straight line going up — more mass always means sitting deeper, in a steady, predictable way (unlike the Moon's repeating cycle).",
        "test_question": "Did your description mention whether the shape was a straight line, a curve, or a repeating cycle?",
        "fix_prompt": "If you only said 'it changes' without describing the SHAPE, how would you describe the shape now?",
    },
    {
        "id": "vst-07-predict-before-you-calculate",
        "title": "Predict Before You Calculate",
        "domain": "🧪 Investigate",
        "notice_scenario": "🧊 An ice cube is dropped into a full glass of water. Before doing any math, a scientist guesses what happens first.",
        "notice_question": "What's the POINT of guessing before calculating, if you're going to calculate anyway?",
        "notice_choices": [
            ("There's no point — just calculate", False, "🚫"),
            ("It trains your instinct, so if your calculation disagrees wildly with your guess, you know to double-check", True, "🔮"),
            ("Guessing is more accurate than math", False, "❌"),
        ],
        "notice_explain": "Predicting first builds your science instinct — and gives you a sanity check. If your calculation says something totally different from your guess, that's a clue to look closer.",
        "practice_mode": "text",
        "practice_instructions": "Before checking anything: if the SALT level in ocean water increases, what do you predict happens to how easily things float?",
        "practice_prompt": "Write: I predict ___ because ___.",
        "practice_starters": ["I predict things float more because...", "I predict things float less because...", "I predict nothing changes because..."],
        "practice_keywords": ["density", "salt", "float", "buoyancy"],
        "predict_scenario": "🍄 If Mario's world gravity DECREASES, what do you predict happens to his jump height?",
        "test_reveal": "Saltier water is denser, so things float MORE easily (this is why the Dead Sea makes people float so well). Lower gravity means Mario jumps HIGHER for the same push.",
        "test_question": "Did your prediction include a reason, not just a guess?",
        "fix_prompt": "If you predicted without a 'because,' what reason would you add now?",
    },
    {
        "id": "vst-08-design-the-experiment",
        "title": "Design the Experiment",
        "domain": "🧪 Investigate",
        "notice_scenario": "🍬 Question: Does temperature affect how fast sugar dissolves in water? A real experiment needs more than just 'try it once.'",
        "notice_question": "What's missing if you only test ONE cup of hot water with sugar in it, once?",
        "notice_choices": [
            ("Nothing is missing, one test is enough", False, "🚫"),
            ("A comparison — you need a COLD water cup too, to know if temperature actually made the difference", True, "🧪"),
            ("You need a bigger spoon", False, "🥄"),
        ],
        "notice_explain": "An experiment needs a variable you change (temperature) and something to compare against (a control) — otherwise you can't tell what actually caused the result.",
        "practice_mode": "text",
        "practice_instructions": "Design a simple experiment: Does hull width affect ship stability? List what you'd CHANGE, what you'd KEEP THE SAME (control), and what you'd MEASURE.",
        "practice_prompt": "Fill in: Change = ___, Keep the same = ___, Measure = ___.",
        "practice_starters": ["I would change...", "I would keep the same...", "I would measure..."],
        "practice_keywords": ["variable", "control", "measure", "compare"],
        "predict_scenario": "🍳 Now sketch the same 3-part plan for: does higher heat make pancakes brown faster?",
        "test_reveal": "A solid version: Change = stove temperature; Keep the same = pancake batter amount, pan, cook time checks; Measure = color/darkness at fixed time intervals.",
        "test_question": "Did your plan have all 3 parts — change, control, and measurement?",
        "fix_prompt": "If you forgot the 'keep the same' part, what would you control now?",
    },
    {
        "id": "vst-09-break-and-repair-your-model",
        "title": "Break & Repair Your Model",
        "domain": "🧪 Investigate",
        "notice_scenario": "🧊 Someone predicts: 'All ice sinks in water, because most solids are denser than their liquid.' Then they see an ice cube floating.",
        "notice_question": "What TYPE of thinking mistake is this — the model itself, or just a one-time error?",
        "notice_choices": [
            ("Calculation error — they just did the math wrong", False, "🔢"),
            ("Model error — the rule 'solids always sink' doesn't apply to water, which is a special exception", True, "🧩"),
            ("There's no mistake, ice really does sink", False, "🚫"),
        ],
        "notice_explain": "Real scientists sort out WHERE thinking broke: was it a bad model, a missed variable, wrong math, or a bad prediction? Naming the type of mistake helps you fix it faster.",
        "practice_mode": "text",
        "practice_instructions": "Someone says: 'Mario always jumps the same height no matter what.' Find the flaw in this model — what variable did they forget?",
        "practice_prompt": "What's wrong with the model, and what variable is missing?",
        "practice_starters": ["The flaw is...", "They forgot that...", "A better model would include..."],
        "practice_keywords": ["gravity", "power-up", "variable", "forgot"],
        "predict_scenario": "🌊 Now break this one: 'Ocean water is the same temperature everywhere, from top to bottom.'",
        "test_reveal": "Real oceans have a thermocline — a layer where temperature drops fast with depth. Surface water is warmed by the sun; deep water stays cold, so 'same everywhere' is a model error.",
        "test_question": "Did you name what specific variable (like depth) the broken model ignored?",
        "fix_prompt": "Write your REPAIRED version of the model in one sentence.",
    },
    {
        "id": "vst-10-transfer-same-idea-new-world",
        "title": "Transfer: Same Idea, New World",
        "domain": "🚀 Transfer",
        "notice_scenario": "🌊 Density explains why ships float. The SAME idea explains why a planet's core is iron and its outside is lighter rock.",
        "notice_question": "What skill are you using when you notice the SAME rule works for a ship and for a whole planet?",
        "notice_choices": [
            ("Memorizing more facts about ships", False, "📚"),
            ("Transfer — applying one concept to a completely new, unfamiliar situation", True, "🔗"),
            ("Guessing randomly until something matches", False, "🎲"),
        ],
        "notice_explain": "Transfer is the skill Olympiad and NUS High problems test most: can you use an idea you already know somewhere you've NEVER seen it applied before?",
        "practice_mode": "text",
        "practice_instructions": "Take the idea of FORCE BALANCE (two equal, opposite arrows = staying still). Apply it to something NOT in the sketchbooks yet — like a kite hanging in steady wind, or a person hanging from monkey bars.",
        "practice_prompt": "Describe your new example and the two balanced forces in it.",
        "practice_starters": ["My new example is...", "The two forces are...", "They balance because..."],
        "practice_keywords": ["force", "balance", "equal", "opposite"],
        "predict_scenario": "🔗 If you could apply DIFFUSION (particles spreading from crowded to spread-out) to something totally outside science — like information, traffic, or even a rumor — what would that look like?",
        "test_reveal": "Many students say 'a rumor spreading through a school' — starts crowded (a few people know), spreads out (more people know) until it evens out (everyone's heard it). Same shape, totally different subject!",
        "test_question": "Did you pick something genuinely NEW, not just another science example?",
        "fix_prompt": "If your example was still 'science-flavored,' what everyday, non-science example could you swap in?",
    },
]


PREDICT_STARTERS = [
    "I predict...",
    "...will increase because...",
    "...will decrease because...",
    "...will stay the same because...",
]


def build_concept_data(lab):
    practice = {
        "mode": lab["practice_mode"],
        "heading": "🎯 " + lab["title"].split(":")[0],
        "instructions": lab["practice_instructions"],
        "prompt": lab.get("practice_prompt", ""),
        "starters": lab.get("practice_starters", []),
        "keywords": lab.get("practice_keywords", []),
        "drawPrompt": lab.get("draw_prompt", ""),
        "hintSvg": lab.get("draw_hint_svg", "<svg viewBox='0 0 400 200'></svg>"),
    }
    return {
        "domain": lab["domain"],
        "notice": {
            "scenario": lab["notice_scenario"],
            "question": lab["notice_question"],
            "choices": [{"text": t, "correct": c, "visual": v} for (t, c, v) in lab["notice_choices"]],
            "explanation": lab["notice_explain"],
        },
        "practice": practice,
        "predict": {
            "scenario": lab["predict_scenario"],
            "starters": PREDICT_STARTERS,
            "keywords": lab.get("predict_keywords", lab.get("practice_keywords", [])),
        },
        "test": {
            "reveal": lab["test_reveal"],
            "question": lab["test_question"],
            "choices": [{"text": "Yes, close enough!"}, {"text": "Not quite — I learned something new"}],
        },
        "fix": {
            "errorOptions": [
                "I mixed up two ideas",
                "I forgot a variable",
                "My model was too simple",
                "I read the pattern backwards",
                "I'm not sure yet — and that's okay",
            ],
            "prompt": lab["fix_prompt"],
        },
    }


def main():
    if not TEMPLATE_PATH.exists():
        sys.exit(f"FATAL: template not found at {TEMPLATE_PATH}")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if "window.CONCEPT_DATA = {" not in template:
        sys.exit("FATAL: template missing CONCEPT_DATA marker — has the engine changed shape?")
    if "[LAB TITLE]" not in template:
        sys.exit("FATAL: template missing [LAB TITLE] marker")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = []

    data_block_pattern = re.compile(
        r"window\.CONCEPT_DATA = \{.*?\};\n/\* =+ \*/",
        re.DOTALL,
    )

    for i, lab in enumerate(LABS, start=1):
        concept_data = build_concept_data(lab)
        json_str = json.dumps(concept_data, ensure_ascii=False, indent=2)
        new_block = f"window.CONCEPT_DATA = {json_str};\n/* ===================================================================================== */"

        html = data_block_pattern.sub(lambda _match, nb=new_block: nb, template, count=1)
        if "window.CONCEPT_DATA = {" not in html or '"[DOMAIN]"' in html:
            sys.exit(f"FATAL: CONCEPT_DATA substitution failed for {lab['id']}")

        html = html.replace("[LAB TITLE]", f"{i}. {lab['title']}")
        html = html.replace(">[DOMAIN]<", f">{lab['domain']}<")
        html = html.replace('data-concept-id="vst-00-example"', f'data-concept-id="{lab["id"]}"')

        out_path = OUT_DIR / f"{lab['id']}.html"
        out_path.write_text(html, encoding="utf-8")
        written.append(out_path)
        print(f"  wrote {out_path.name} ({len(html)} bytes)")

    print(f"\nDone — {len(written)} VST lab files written to {OUT_DIR}")


if __name__ == "__main__":
    main()
