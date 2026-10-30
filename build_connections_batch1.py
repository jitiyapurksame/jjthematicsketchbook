#!/usr/bin/env python3
"""
Build all 8 Cross-Theme Connection Sketchbook files from connection-template-source.html.
Fail-loud: crashes on missing keys or malformed template markers rather than
silently producing broken output.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT / "connection-template-source.html"
OUT_DIR = ROOT / "deliverables"

# ---------------------------------------------------------------------------
# CONTENT — 8 connection maps. Each node's "why" line is what pops up when the
# kid taps it in the Spot mission. Keep sentences short, punchy, one idea each.
# ---------------------------------------------------------------------------

MAPS = [
    {
        "id": "connection-01-density",
        "title": "Density Connection Map",
        "emoji": "🌊",
        "intro": "One idea. Five costumes. Tap each one in order and watch the SAME rule show up again and again.",
        "chain": [
            ("Titanic", "🚢", "A huge steel ship floats because its shape pushes aside more water than it weighs."),
            ("Iceberg", "🧊", "Ice is less dense than liquid water — that's why 90% of it hides underwater."),
            ("Ocean layers", "🌊", "Cold, salty water is denser, so it sinks below warmer water and makes layers."),
            ("Cooking oil", "🍳", "Oil floats on water in a pan because oil is less dense — same rule, kitchen edition."),
            ("Layered planet", "🌍", "Heavy iron sank to a planet's core while lighter rock floated up — density sorted the whole planet."),
        ],
        "draw_prompt": "Draw your OWN 3-step density chain. Pick any two things you know float or sink, and show why with arrows.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><rect x='20' y='100' width='360' height='80' fill='#BFD9D3' opacity='0.6'/><circle cx='120' cy='65' r='22' fill='#C9A24B'/><text x='120' y='70' font-size='13' text-anchor='middle' fill='#071A33'>floats</text><line x1='120' y1='40' x2='120' y2='12' stroke='#2E6E62' stroke-width='4'/><polygon points='120,6 110,20 130,20' fill='#2E6E62'/><circle cx='280' cy='150' r='18' fill='#D9603B'/><text x='280' y='154' font-size='12' text-anchor='middle' fill='#fff'>sinks</text><line x1='280' y1='170' x2='280' y2='195' stroke='#D9603B' stroke-width='4'/><polygon points='280,199 270,186 290,186' fill='#D9603B'/></svg>",
        "explain_prompt": "In your own words: what does 'density' actually control?",
        "keywords": ["density", "float", "sink", "mass", "volume"],
        "transfer_q": "A bath toy duck floats but a metal spoon sinks in the same water. Why?",
        "transfer_choices": [
            ("The duck is smaller than the spoon", False, "📏"),
            ("The duck is less dense than water, the spoon is denser than water", True, "⚖️"),
            ("The spoon is heavier in total", False, "🏋️"),
        ],
        "transfer_explain": "Size and total weight don't decide float/sink on their own — density (mass packed into that volume) does.",
    },
    {
        "id": "connection-02-energy-transformation",
        "title": "Energy Transformation Map",
        "emoji": "🔥",
        "intro": "Energy never disappears — it just changes costume. Follow the chain and watch one form of energy become another.",
        "chain": [
            ("Stove flame", "🍳", "Chemical energy in gas burns and turns into heat energy in the pan."),
            ("Mario jump", "🍄", "Mario's leg muscles turn stored energy into kinetic (movement) energy mid-jump."),
            ("Ship engine", "🚢", "Burning fuel makes heat, and the engine turns that heat into motion that spins the propeller."),
            ("Sunlight", "☀️", "The Sun turns nuclear energy into light and heat energy that travels through space."),
            ("Toaster", "🔌", "Electrical energy flowing through a wire turns into heat energy that browns your toast."),
        ],
        "draw_prompt": "Pick a machine or process you use every day. Draw the energy chain: what goes in, what comes out?",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><rect x='30' y='70' width='140' height='60' rx='8' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><text x='100' y='105' font-size='15' text-anchor='middle' fill='#071A33'>IN: heat/fuel</text><line x1='180' y1='100' x2='228' y2='100' stroke='#C9A24B' stroke-width='5'/><polygon points='240,100 224,90 224,110' fill='#C9A24B'/><rect x='250' y='70' width='140' height='60' rx='8' fill='#FBEAE3' stroke='#D9603B' stroke-width='2'/><text x='320' y='105' font-size='15' text-anchor='middle' fill='#071A33'>OUT: motion</text></svg>",
        "explain_prompt": "Energy transformation means energy changes FORM but not amount. Explain that idea in your own words.",
        "keywords": ["energy", "transform", "heat", "motion", "chemical"],
        "transfer_q": "A wind-up toy car is wound tight, then let go and zooms across the floor. What transformation happened?",
        "transfer_choices": [
            ("Stored (spring) energy turned into kinetic energy", True, "🌀"),
            ("The toy created brand new energy from nothing", False, "🚫"),
            ("Kinetic energy turned into chemical energy", False, "🔄"),
        ],
        "transfer_explain": "The tightly wound spring stores energy; releasing it converts that stored energy into movement — same pattern as the stove, engine, and Sun.",
    },
    {
        "id": "connection-03-convection",
        "title": "Convection Loops Map",
        "emoji": "🌀",
        "intro": "Hot stuff rises. Cool stuff sinks. That one loop shows up in a soup pot AND in the whole ocean.",
        "chain": [
            ("Simmering pot", "🍲", "Heat at the bottom makes water expand, get less dense, and rise to the top."),
            ("Cooling soup", "🌡️", "At the top, the hot liquid loses heat, gets denser, and sinks back down — a loop!"),
            ("Ocean conveyor", "🌊", "Warm surface water flows toward the poles, cools, sinks, and crawls back along the seafloor."),
            ("Kitchen steam", "💨", "Hot steam rising off a pan is the same 'hot rises' rule you can literally watch."),
        ],
        "draw_prompt": "Draw a convection loop using arrows: where does it heat up, where does it cool down, which way does it circle?",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><rect x='60' y='20' width='280' height='160' rx='12' fill='none' stroke='#0B2545' stroke-width='3'/><line x1='140' y1='160' x2='140' y2='42' stroke='#D9603B' stroke-width='5'/><polygon points='140,32 128,50 152,50' fill='#D9603B'/><text x='140' y='185' font-size='13' text-anchor='middle' fill='#071A33'>hot rises</text><line x1='280' y1='40' x2='280' y2='158' stroke='#2E6E62' stroke-width='5'/><polygon points='280,168 268,150 292,150' fill='#2E6E62'/><text x='280' y='15' font-size='13' text-anchor='middle' fill='#071A33'>cool sinks</text></svg>",
        "explain_prompt": "Why does hot fluid rise and cold fluid sink? Use the word 'density' in your answer.",
        "keywords": ["convection", "rise", "sink", "loop", "density"],
        "transfer_q": "A radiator heater is placed near the FLOOR of a room, not the ceiling. Why does that work well?",
        "transfer_choices": [
            ("Heat only travels sideways, never up", False, "➡️"),
            ("The warmed air near the floor becomes less dense and rises, circulating the whole room", True, "♨️"),
            ("It doesn't matter where the heater is placed", False, "🤷"),
        ],
        "transfer_explain": "Same convection loop as the soup pot and the ocean — warm air rises, cools at the top, sinks, and gets reheated at the bottom.",
    },
    {
        "id": "connection-04-diffusion",
        "title": "Diffusion / Evening Out Map",
        "emoji": "💧",
        "intro": "Particles don't like being crowded. Given time, they always spread out to even things up. Watch it happen three different ways.",
        "chain": [
            ("Marinade", "🍗", "Flavor molecules move from the crowded marinade into the less-crowded meat until it evens out."),
            ("Food coloring in water", "🎨", "Drop dye in water and it spreads on its own — no stirring needed, just diffusion."),
            ("Salt in ocean water", "🌊", "Salt particles spread evenly through seawater over time, moving from high to low concentration."),
            ("Perfume in a room", "🌸", "Scent molecules drift from a crowded spot near the bottle to every corner of the room."),
        ],
        "draw_prompt": "Draw 'before' and 'after' pictures of particles diffusing — crowded on one side, then spread evenly.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><text x='90' y='30' font-size='13' text-anchor='middle' fill='#071A33'>crowded</text><circle cx='70' cy='80' r='6' fill='#D9603B'/><circle cx='85' cy='95' r='6' fill='#D9603B'/><circle cx='60' cy='105' r='6' fill='#D9603B'/><circle cx='90' cy='70' r='6' fill='#D9603B'/><circle cx='75' cy='60' r='6' fill='#D9603B'/><line x1='140' y1='90' x2='258' y2='90' stroke='#C9A24B' stroke-width='5'/><polygon points='270,90 254,80 254,100' fill='#C9A24B'/><text x='330' y='30' font-size='13' text-anchor='middle' fill='#071A33'>spread out</text><circle cx='300' cy='60' r='6' fill='#2E6E62'/><circle cx='340' cy='70' r='6' fill='#2E6E62'/><circle cx='310' cy='110' r='6' fill='#2E6E62'/><circle cx='360' cy='100' r='6' fill='#2E6E62'/><circle cx='330' cy='140' r='6' fill='#2E6E62'/></svg>",
        "explain_prompt": "Diffusion always moves particles from where there are MANY to where there are FEW. Explain why that happens, in your own words.",
        "keywords": ["diffusion", "concentration", "spread", "particles", "even out"],
        "transfer_q": "You open a bag of chips in a quiet room, and soon you can smell it from across the room. What's happening?",
        "transfer_choices": [
            ("The chip smell particles diffuse from high to low concentration through the air", True, "💨"),
            ("The smell teleports instantly to your nose", False, "⚡"),
            ("Only chips do this — it's not a general rule", False, "🚫"),
        ],
        "transfer_explain": "Same rule as the marinade and the dye — smell particles spread from crowded (near the bag) to less crowded (across the room) all on their own.",
    },
    {
        "id": "connection-05-force-balance",
        "title": "Force Balance Map",
        "emoji": "⚖️",
        "intro": "Something staying still or moving at a steady speed means its forces are BALANCED. Two arrows, equal size, opposite ways.",
        "chain": [
            ("Floating ship", "🚢", "Weight pulls down, buoyancy pushes up — when they're equal, the ship floats steady."),
            ("Mario standing still", "🍄", "Gravity pulls Mario down, the ground pushes back up with equal force — he doesn't sink or fly."),
            ("Book on a table", "📚", "The table pushes up on the book exactly as hard as gravity pulls it down."),
            ("Submarine hovering", "🚤", "A submarine adjusts its ballast until upward and downward forces match exactly, so it hangs still in the water."),
        ],
        "draw_prompt": "Draw an object that is balanced. Add two arrows of EQUAL length pointing opposite ways to show the forces.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><rect x='170' y='85' width='60' height='30' fill='#C9A24B'/><line x1='200' y1='80' x2='200' y2='32' stroke='#2E6E62' stroke-width='5'/><polygon points='200,20 188,38 212,38' fill='#2E6E62'/><text x='200' y='15' font-size='12' text-anchor='middle' fill='#071A33'>up force</text><line x1='200' y1='120' x2='200' y2='168' stroke='#D9603B' stroke-width='5'/><polygon points='200,180 188,162 212,162' fill='#D9603B'/><text x='200' y='197' font-size='12' text-anchor='middle' fill='#071A33'>down force (equal!)</text></svg>",
        "explain_prompt": "What does it mean for forces to be 'balanced,' and what happens to an object when they are?",
        "keywords": ["force", "balance", "gravity", "equal", "still"],
        "transfer_q": "A helium balloon floats in place in the middle of a room, not rising or falling. What does that tell you?",
        "transfer_choices": [
            ("There are no forces acting on it at all", False, "🚫"),
            ("The upward buoyant force and downward weight force are balanced", True, "⚖️"),
            ("Helium is immune to gravity", False, "❌"),
        ],
        "transfer_explain": "Same pattern as the floating ship and the standing Mario — two equal, opposite forces cancel out, so nothing moves.",
    },
    {
        "id": "connection-06-pressure",
        "title": "Pressure Connection Map",
        "emoji": "📉",
        "intro": "Pressure is a squeeze — and it changes depending on how deep or how high you go. Follow the squeeze through three worlds.",
        "chain": [
            ("Ocean depth", "🌊", "Every meter you dive, more water sits on top of you, so pressure keeps climbing."),
            ("Titanic's hull", "🚢", "Deep underwater, the crushing water pressure was strong enough to fold steel."),
            ("Mountain air", "⛰️", "Climb a mountain and there's less air above you pressing down, so air pressure drops."),
            ("Airplane cabin", "✈️", "At cruising altitude the air is so thin that cabins must be pressurized so you can breathe normally."),
        ],
        "draw_prompt": "Draw a tall arrow from deep ocean to high mountain. Mark where pressure is highest and where it's lowest.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><text x='200' y='20' font-size='13' text-anchor='middle' fill='#071A33'>less pressure (high up)</text><line x1='200' y1='35' x2='200' y2='175' stroke='#0B2545' stroke-width='3'/><line x1='150' y1='60' x2='250' y2='60' stroke='#2E6E62' stroke-width='3'/><line x1='140' y1='105' x2='260' y2='105' stroke='#C9A24B' stroke-width='5'/><line x1='125' y1='155' x2='275' y2='155' stroke='#D9603B' stroke-width='7'/><text x='200' y='196' font-size='13' text-anchor='middle' fill='#071A33'>more pressure (deep down)</text></svg>",
        "explain_prompt": "Explain why pressure goes UP as you go deeper in water, but goes DOWN as you go higher in the air.",
        "keywords": ["pressure", "depth", "altitude", "squeeze", "atmosphere"],
        "transfer_q": "A sealed bag of chips looks puffed up and tight after a flight, once the plane reaches high altitude. Why?",
        "transfer_choices": [
            ("The chips got warmer and expanded", False, "🌡️"),
            ("Outside air pressure dropped at altitude, so the air trapped inside the bag pushed the bag outward", True, "✈️"),
            ("The bag absorbed extra air from the cabin", False, "🚫"),
        ],
        "transfer_explain": "Same rule as the mountain air — less air pressure outside means the pressure difference pushes the bag to puff out.",
    },
    {
        "id": "connection-07-states-of-matter",
        "title": "States of Matter ↔ Motion Map",
        "emoji": "🌡️",
        "intro": "Solid, liquid, gas — the difference is just how FAST and how FREE the particles are moving. Watch heat flip the switch.",
        "chain": [
            ("Ice cube", "🧊", "In a solid, particles vibrate in place but stay locked in a tight pattern."),
            ("Melting butter", "🧈", "Add heat, particles move faster, break free from the pattern, and start sliding — that's a liquid."),
            ("Boiling water", "💨", "Add even more heat, and particles move so fast they fly apart completely — that's a gas."),
            ("Mario's speed boost", "🍄", "More energy = more motion isn't just for particles — Mario zooms faster with a speed power-up too."),
        ],
        "draw_prompt": "Draw the SAME group of particles three times: packed and still (solid), loose and sliding (liquid), and flying apart (gas).",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><rect x='20' y='40' width='100' height='120' fill='none' stroke='#0B2545' stroke-width='2'/><text x='70' y='30' font-size='12' text-anchor='middle'>solid</text><circle cx='40' cy='60' r='5' fill='#0B2545'/><circle cx='70' cy='60' r='5' fill='#0B2545'/><circle cx='100' cy='60' r='5' fill='#0B2545'/><circle cx='40' cy='90' r='5' fill='#0B2545'/><circle cx='70' cy='90' r='5' fill='#0B2545'/><circle cx='100' cy='90' r='5' fill='#0B2545'/><circle cx='40' cy='120' r='5' fill='#0B2545'/><circle cx='70' cy='120' r='5' fill='#0B2545'/><circle cx='100' cy='120' r='5' fill='#0B2545'/><rect x='150' y='40' width='100' height='120' fill='none' stroke='#0B2545' stroke-width='2'/><text x='200' y='30' font-size='12' text-anchor='middle'>liquid</text><circle cx='170' cy='70' r='5' fill='#2E6E62'/><circle cx='210' cy='80' r='5' fill='#2E6E62'/><circle cx='190' cy='110' r='5' fill='#2E6E62'/><circle cx='230' cy='125' r='5' fill='#2E6E62'/><circle cx='165' cy='135' r='5' fill='#2E6E62'/><rect x='280' y='40' width='100' height='120' fill='none' stroke='#0B2545' stroke-width='2'/><text x='330' y='30' font-size='12' text-anchor='middle'>gas</text><circle cx='300' cy='55' r='5' fill='#D9603B'/><circle cx='360' cy='75' r='5' fill='#D9603B'/><circle cx='310' cy='140' r='5' fill='#D9603B'/><circle cx='355' cy='115' r='5' fill='#D9603B'/></svg>",
        "explain_prompt": "What is heat actually DOING to particles when a solid melts into a liquid?",
        "keywords": ["solid", "liquid", "gas", "particles", "energy"],
        "transfer_q": "A puddle on the sidewalk disappears on a hot sunny day, even without boiling. What's happening to the water particles?",
        "transfer_choices": [
            ("The water particles vanish completely", False, "🚫"),
            ("Sun energy speeds up surface particles enough to escape into the air as gas — evaporation", True, "☀️"),
            ("The puddle sinks into the ground instead", False, "⬇️"),
        ],
        "transfer_explain": "Same particle-speed rule as melting butter and boiling water — enough added energy, and particles break free into a gas, just at a slower pace (evaporation instead of boiling).",
    },
    {
        "id": "connection-08-exception-beats-the-rule",
        "title": "When the Exception Beats the Rule",
        "emoji": "🍯",
        "intro": "Science rules are powerful — but real scientists always check for the ONE thing that breaks the pattern. That's where discoveries hide.",
        "chain": [
            ("Ice floats (weird!)", "🧊", "Almost everything shrinks and gets denser as it freezes. Water does the OPPOSITE — ice is less dense than liquid water, so it floats instead of sinking."),
            ("Oil and vinegar", "🍯", "Density says oil floats on vinegar — true. But shake in an emulsifier (like mustard) and they blend instead, because now tiny forces beat the density rule."),
            ("Mario's mushroom", "🍄", "Normally more mass falls faster... except in Mario's world, a power-up 'exception' rule (game physics) overrides real gravity."),
            ("Submarine ballast", "🚤", "Steel should sink — density says so. But hollow air-filled ballast tanks let a solid steel submarine float anyway, by lowering its AVERAGE density."),
        ],
        "draw_prompt": "Pick one exception from the chain. Draw the 'normal rule' picture next to the 'exception' picture, side by side.",
        "draw_hint_svg": "<svg viewBox='0 0 400 200'><text x='100' y='30' font-size='13' text-anchor='middle'>normal rule</text><circle cx='100' cy='100' r='30' fill='#EAF3F0' stroke='#2E6E62' stroke-width='2'/><line x1='80' y1='80' x2='120' y2='120' stroke='#D9603B' stroke-width='4'/><line x1='120' y1='80' x2='80' y2='120' stroke='#D9603B' stroke-width='4'/><line x1='150' y1='100' x2='248' y2='100' stroke='#C9A24B' stroke-width='5'/><polygon points='260,100 244,90 244,110' fill='#C9A24B'/><text x='320' y='30' font-size='13' text-anchor='middle'>exception!</text><circle cx='320' cy='100' r='30' fill='#FBF3DD' stroke='#C9A24B' stroke-width='3'/><text x='320' y='108' font-size='20' text-anchor='middle'>⭐</text></svg>",
        "explain_prompt": "Why is it useful for a scientist to notice when something breaks the usual rule, instead of ignoring it?",
        "keywords": ["exception", "rule", "density", "anomaly", "override"],
        "transfer_q": "Most metals sink in water. A massive steel cargo ship floats anyway. What's really going on?",
        "transfer_choices": [
            ("Steel secretly isn't a real metal", False, "🚫"),
            ("The ship's hollow shape spreads its mass over a huge volume, making its AVERAGE density less than water", True, "🚢"),
            ("Ships float because of magic buoyancy that ignores density", False, "✨"),
        ],
        "transfer_explain": "This is the submarine trick again — it's not that density stops applying, it's that shape changes the AVERAGE density of the whole object.",
    },
]


def build_concept_data(m):
    return {
        "intro": m["intro"],
        "connect": {
            "items": [
                {"text": name, "icon": icon, "why": why}
                for (name, icon, why) in m["chain"]
            ]
        },
        "draw": {
            "prompt": m["draw_prompt"],
            "hintSvg": m["draw_hint_svg"],
        },
        "explain": {
            "prompt": m["explain_prompt"],
            "visualSvg": "<svg viewBox='0 0 200 140'></svg>",
            "starters": [
                "I think this happens because...",
                "This reminds me of...",
                "The pattern is the same because...",
            ],
            "keywords": m["keywords"],
        },
        "transfer": {
            "question": m["transfer_q"],
            "choices": [
                {"text": text, "correct": correct, "visual": visual}
                for (text, correct, visual) in m["transfer_choices"]
            ],
            "explanation": m["transfer_explain"],
        },
    }


def main():
    if not TEMPLATE_PATH.exists():
        sys.exit(f"FATAL: template not found at {TEMPLATE_PATH}")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if "window.CONCEPT_DATA = {" not in template:
        sys.exit("FATAL: template missing CONCEPT_DATA marker — has the engine changed shape?")
    if "[MAP TITLE]" not in template:
        sys.exit("FATAL: template missing [MAP TITLE] marker")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = []

    data_block_pattern = re.compile(
        r"window\.CONCEPT_DATA = \{.*?\};\n/\* =+ \*/",
        re.DOTALL,
    )

    for m in MAPS:
        concept_data = build_concept_data(m)
        json_str = json.dumps(concept_data, ensure_ascii=False, indent=2)
        new_block = f"window.CONCEPT_DATA = {json_str};\n/* ============================================================================================ */"

        html = data_block_pattern.sub(lambda _match, nb=new_block: nb, template, count=1)
        if "window.CONCEPT_DATA = {" not in html or "[node 1]" in html:
            sys.exit(f"FATAL: CONCEPT_DATA substitution failed for {m['id']}")

        html = html.replace("[MAP TITLE]", f"{m['emoji']} {m['title']}")
        html = html.replace('id="connect-heading">Same idea, different costume<', f'id="connect-heading">{m["emoji"]} Same idea, different costume<')
        html = html.replace('data-concept-id="connection-00-example"', f'data-concept-id="{m["id"]}"')

        out_path = OUT_DIR / f"{m['id']}.html"
        out_path.write_text(html, encoding="utf-8")
        written.append(out_path)
        print(f"  wrote {out_path.name} ({len(html)} bytes)")

    print(f"\nDone — {len(written)} connection map files written to {OUT_DIR}")


if __name__ == "__main__":
    main()
