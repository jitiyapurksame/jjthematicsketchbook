#!/usr/bin/env python3
"""
Build VST Thinking Lab Vol.2 — the 6 remaining skills from vstthinkinglab.txt
(Representation Switching, Explanation, Transfer [advanced], System Thinking,
Research Thinking, Creative Engineering). Same engine as Vol.1
(vst-template-source.html) — no new template needed, these skills fit the
existing 6-step worksheet shape fine.

Fail-loud: crashes on missing keys or malformed template markers.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "vst-template-source.html"
OUT_DIR = ROOT / "deliverables"

LABS = [
    {
        "id": "vst-11-representation-switching",
        "title": "Representation Switching",
        "domain": "🔄 Represent",
        "notice_scenario": "🚢 A ship can be shown 5 different ways: a photo, a labeled diagram, a force-arrow diagram, an equation (F = ma), and a graph. Same ship, 5 costumes.",
        "notice_question": "Why bother switching between so many different ways of showing the SAME thing?",
        "notice_choices": [
            ("Because pictures are prettier than equations", False, "🎨"),
            ("Because each representation reveals something the others hide — a graph shows trends, an equation shows exact math, a diagram shows structure", True, "🔄"),
            ("It's not useful — you should just pick one and stick with it", False, "🚫"),
        ],
        "notice_explain": "Real scientists switch representations on purpose. A graph can't show you the exact formula. An equation can't show you the shape of a trend. Being able to hop between them is a superpower.",
        "practice_mode": "text",
        "practice_instructions": "Take 🧊 'ice floating in water.' Describe it in FOUR different ways: (1) one plain sentence, (2) as a labeled diagram in words, (3) as a simple equation idea, (4) as what a graph of ice-density vs water-density would show.",
        "practice_prompt": "Write all 4 versions, one per line.",
        "practice_starters": ["Plain sentence: ...", "Diagram (in words): ...", "Equation idea: ...", "Graph would show: ..."],
        "practice_keywords": ["density", "diagram", "equation", "graph"],
        "predict_scenario": "🍄 Now do the same 4-way switch for 'Mario jumping higher with a mushroom power-up.'",
        "test_reveal": "A strong answer chain: Sentence → 'power-ups add extra energy.' Diagram → Mario + upward arrow labeled 'boosted force.' Equation idea → more force = more height (like F∝h). Graph → jump height rises sharply right when the power-up is collected.",
        "test_question": "Did you manage all 4 representations, not just 1 or 2?",
        "fix_prompt": "Which representation was hardest for you — sentence, diagram, equation, or graph? Why do you think that one felt tricky?",
    },
    {
        "id": "vst-12-explanation-lab",
        "title": "The Explanation Lab",
        "domain": "🗣️ Explain",
        "notice_scenario": "💬 Level 1 explanation of density: 'Heavy-for-its-size things sink.' Level 4 explanation: 'ρ = m/V, and objects float when their average density is less than the fluid's density.'",
        "notice_question": "Both explanations are TRUE. So why bother learning the harder Level 4 version?",
        "notice_choices": [
            ("Level 4 isn't actually better, just more complicated", False, "🚫"),
            ("Level 4 lets you predict NEW situations with numbers, not just describe ones you've already seen", True, "🔢"),
            ("You should always use Level 4, even for a 5-year-old", False, "👶"),
        ],
        "notice_explain": "Different explanation levels serve different jobs. Level 1 is fast and intuitive. Level 4 lets you calculate exact answers for brand-new numbers you've never seen before.",
        "practice_mode": "text",
        "practice_instructions": "Explain 🌊 buoyancy at THREE levels: Level 1 (one plain sentence), Level 3 (cause → effect chain), Level 5 (as if you're teaching it to a younger kid who's never heard of it).",
        "practice_prompt": "Write your Level 1, Level 3, and Level 5 explanations.",
        "practice_starters": ["Level 1: ...", "Level 3 (cause then effect): ...", "Level 5 (teaching a younger kid): ..."],
        "practice_keywords": ["buoyancy", "cause", "effect", "teach"],
        "predict_scenario": "🍳 Now imagine explaining 'why bread browns when toasted (Maillard reaction)' to a chef who cooks by instinct but has never studied chemistry.",
        "test_reveal": "A Level-5 explanation ditches jargon entirely: 'When you heat sugars and proteins together, they link up into new brown, tasty molecules — that's the crust flavor you're chasing.' No equations, no jargon, just the idea that lands.",
        "test_question": "Did your explanation change its WORDS (not just shorten) depending on who it was for?",
        "fix_prompt": "If your Level 5 explanation still used science jargon, how would you say it in totally everyday words instead?",
    },
    {
        "id": "vst-13-advanced-transfer",
        "title": "Transfer: The Unfamiliar Problem",
        "domain": "🚀 Transfer",
        "notice_scenario": "⭐ Olympiad and NUS High problems almost never look like your textbook examples. They take a familiar rule and hide it inside a brand-new, weird-looking situation.",
        "notice_question": "What's the FIRST move when you see a problem that looks totally unfamiliar?",
        "notice_choices": [
            ("Panic — if it's not familiar, you can't solve it", False, "😱"),
            ("Ask: 'What FAMILIAR rule might be hiding underneath this new costume?'", True, "🔍"),
            ("Guess randomly since there's no way to know", False, "🎲"),
        ],
        "notice_explain": "Unfamiliar-looking problems usually aren't testing new knowledge — they're testing whether you can spot an old rule wearing a new disguise. That's the whole Olympiad game.",
        "practice_mode": "text",
        "practice_instructions": "Here's an unfamiliar-sounding problem: 'A giant space station spins to create artificial gravity for its crew.' What FAMILIAR idea from your sketchbooks might explain how spinning creates a 'gravity' feeling?",
        "practice_prompt": "Name the familiar idea, and explain the connection.",
        "practice_starters": ["This reminds me of...", "The familiar idea hiding here is...", "It connects because..."],
        "practice_keywords": ["force", "spin", "familiar", "hidden"],
        "predict_scenario": "🌡️ Unfamiliar problem: 'A weather balloon shrinks as it rises into thinner air, even though nothing squeezed it.' What familiar idea explains this?",
        "test_reveal": "This is the SAME pressure idea from your Ocean/Titanic sketchbooks, just flipped: less air pressure pushing IN from outside means the balloon's gas pushes it to expand less against resistance — actually it's the opposite, balloons often expand as they rise due to lower outside pressure allowing the gas inside to push outward more. The key transfer skill is recognizing 'pressure difference' as the hidden idea, regardless of which direction it moves.",
        "test_question": "Did you name pressure (or a pressure difference) as the hidden familiar idea?",
        "fix_prompt": "If you got the direction of the effect backwards, what's the corrected version of your explanation?",
    },
    {
        "id": "vst-14-system-thinking",
        "title": "System Thinking Lab",
        "domain": "🧩 Model",
        "notice_scenario": "🚢 A ship engine isn't one lonely thing — burning fuel → spins propeller → pushes ship forward → water resists → more fuel gets burned to keep speed → engine heats up. It's a LOOP of connected parts, a system.",
        "notice_question": "What's different about 'system thinking' compared to just looking at ONE part of something?",
        "notice_choices": [
            ("Nothing — a system is just a bigger single object", False, "🚫"),
            ("A system tracks how changing ONE part ripples through and affects several OTHER connected parts", True, "🔗"),
            ("Systems only apply to machines, never to nature", False, "🌱"),
        ],
        "notice_explain": "Systems thinking means tracing a change through a whole chain of connected parts, not just describing one part in isolation. One change ripples outward.",
        "practice_mode": "text",
        "practice_instructions": "Build a 5-step system chain for 🌍 Earth's climate: Sun → ? → ? → ? → ? (use ideas like atmosphere, ocean, climate, ecosystem).",
        "practice_prompt": "Write your 5-step chain with arrows.",
        "practice_starters": ["Sun affects...", "Which then affects...", "Which then affects..."],
        "practice_keywords": ["sun", "atmosphere", "ocean", "climate", "ecosystem"],
        "predict_scenario": "🍳 Now build a system chain for a stovetop: Flame → ? → ? → ? (think about pan, food, steam, taste).",
        "test_reveal": "One valid chain: Flame → heats pan → heats food's surface → triggers browning/Maillard reaction → changes flavor and releases steam — a small system, but the same 'ripple through connected parts' logic as the whole Earth's climate.",
        "test_question": "Did your chain have at least 4 connected steps, not just 2?",
        "fix_prompt": "If your chain broke off too early, what's the next ripple effect you'd add?",
    },
    {
        "id": "vst-15-research-thinking",
        "title": "Research Thinking Lab",
        "domain": "🔬 Investigate",
        "notice_scenario": "🔬 Most science class questions come from the teacher. Research thinking flips that: YOU notice something curious and ask your OWN question about it.",
        "notice_question": "Which of these is a genuine research question, not just a fact-lookup question?",
        "notice_choices": [
            ("What is the boiling point of water?", False, "📖"),
            ("Does adding salt change how fast water boils, and by how much?", True, "🔬"),
            ("What color is the ocean?", False, "📖"),
        ],
        "notice_explain": "A fact-lookup question already has a known answer somewhere. A research question compares something, tests a relationship, or explores something genuinely uncertain — that's what makes it worth investigating.",
        "practice_mode": "text",
        "practice_instructions": "Pick anything you're curious about from your sketchbooks (density, gravity, heat, pressure — anything). Write your OWN research question — not one I gave you.",
        "practice_prompt": "Write your research question, then note: what evidence would you need to answer it?",
        "practice_starters": ["My research question is...", "To answer it, I'd need to...", "I'm curious about this because..."],
        "practice_keywords": ["question", "evidence", "curious", "uncertain"],
        "predict_scenario": "🧊 Example seed question: 'Does the SHAPE of an ice cube (cube vs. sphere vs. flat disc) change how fast it melts?'",
        "test_reveal": "A real answer needs: a hypothesis (e.g., 'more surface area melts faster'), a fair test (same starting temp/size), data (melt times), and an honest note about limitations (like room temperature not staying perfectly constant).",
        "test_question": "Did your question compare something, or test a relationship — not just ask for a known fact?",
        "fix_prompt": "If your question turned out to be a fact-lookup question, how would you reshape it into a real comparison or test?",
    },
    {
        "id": "vst-16-creative-engineering",
        "title": "Creative Engineering Lab",
        "domain": "🚀 Transfer",
        "notice_scenario": "🚀 The final VST skill isn't just understanding a model or applying it — it's using your model to DESIGN something new that didn't exist before.",
        "notice_question": "What makes a design task different from just answering a question about an existing thing?",
        "notice_choices": [
            ("Nothing, it's basically the same task", False, "🚫"),
            ("A design task means YOU invent the object, using science rules to make sure your invention would actually work", True, "🚀"),
            ("Design tasks don't need any science at all", False, "❌"),
        ],
        "notice_explain": "Creative engineering is 'Understand → Apply → Create.' You're not just describing how something works — you're inventing something new that has to obey the same rules.",
        "practice_mode": "draw",
        "practice_instructions": "Design a SAFER ship using what you know about buoyancy and force balance. Sketch your design and label at least 2 safety features with the science reason they work.",
        "practice_prompt": "",
        "practice_starters": [],
        "practice_keywords": [],
        "draw_prompt": "Sketch your safer-ship design. Add labels for at least 2 features (like a double hull, or extra buoyancy chambers) and note WHY each one helps using ideas like density or force balance.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><path d='M40,120 Q200,180 360,120 L360,150 Q200,190 40,150 Z' fill='#C9A24B' opacity='0.3'/><path d='M40,120 Q200,180 360,120' stroke='#0B2545' stroke-width='4' fill='none'/><path d='M55,115 Q200,165 345,115' stroke='#2E6E62' stroke-width='3' fill='none' stroke-dasharray='4'/><text x='200' y='100' font-size='13' text-anchor='middle' fill='#071A33'>double hull (safety gap)</text><rect x='150' y='122' width='100' height='25' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><text x='200' y='139' font-size='11' text-anchor='middle' fill='#071A33'>extra buoyancy chamber</text></svg>",
        "predict_scenario": "🍄 Now imagine designing a Mario level that uses REAL gravity and force-balance rules, instead of cartoon physics. What would feel different to play?",
        "predict_keywords": ["momentum", "gravity", "real-physics", "jump height"],
        "test_reveal": "A real-physics Mario level would have MUCH lower jumps (since real gravity is stronger relative to a small jump push), slower falls would feel floatier only on smaller worlds (like the Moon), and momentum would carry Mario further before stopping — no instant stop-on-a-dime like cartoon physics allows.",
        "test_question": "Did your idea change something specific (like jump height or momentum), not just say 'it would feel more real'?",
        "fix_prompt": "If your answer was vague, name ONE specific physics rule you'd apply and what exactly would change because of it.",
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

    for i, lab in enumerate(LABS, start=11):
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

    print(f"\nDone — {len(written)} VST Vol.2 lab files written to {OUT_DIR}")


if __name__ == "__main__":
    main()
