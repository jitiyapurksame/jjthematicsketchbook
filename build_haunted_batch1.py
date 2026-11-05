"""Haunted House book ("Ghost Detective in the Old Arcade"), batch 1 (pages 1-4), 8-mission engine.
Run: python3 build-tools/build_haunted_batch1.py  (then patch_draw_pills.py, then run_all_tests.sh)
Also adds the hub book entry + draw pills (idempotent)."""
import json, os, re
from birds_common import *

BLUE = "#3B82C4"; YEL = "#F4D35E"; GREY = "#CFCFCF"
def R(x, y, w, h, f="#FFFFFF", s=NAVY, sw=2): return "<rect x='%g' y='%g' width='%g' height='%g' fill='%s' stroke='%s' stroke-width='%g'/>" % (x, y, w, h, f, s, sw)
def C(x, y, r, f="#FFFFFF", s=NAVY, sw=2): return "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='%g'/>" % (x, y, r, f, s, sw)
def L(x1, y1, x2, y2, c=NAVY, w=2.5): return "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='%g' stroke-linecap='round'/>" % (x1, y1, x2, y2, c, w)
def ico(inner): return "<svg viewBox='0 0 40 40'>%s</svg>" % inner
def dots(c): return ''.join(C(x, y, 6, NAVY, NAVY, 1) for x, y in c)
def ch(t, ok=False): return {"text": t, "correct": ok}

# ---------- page 1: floor plan ----------
EMPTY = {(0, 1), (0, 4), (1, 0), (1, 2)}
def plan(dy=0, marker=False):
    s = R(25, 70 + dy, 250, 30, "#F4EFD8")
    for row in (0, 1):
        for i in range(5):
            e = (row, i) in EMPTY
            y = (20 if row == 0 else 100) + dy
            s += R(25 + i * 50, y, 50, 50, GREY if e else "#BFE3DA") + (txt(50 + i * 50, y + 29, "empty" if e else "shop", 9, NAVY, "middle") )
    return s + C(25, 85 + dy, 8, GOLD) + (C(25, 85 + dy, 3, NAVY) if marker else "")
def grid10(n):
    return "".join(R(30 + (i % 5) * 28, 30 + (i // 5) * 40, 24, 32, "#BFE3DA" if i < n else GREY, NAVY, 1.5) for i in range(10))
d1 = {
 "observe": {"svg": svg(300, 170, plan() + txt(150, 165, "Old Arcade, seen from ABOVE", 11, NAVY, "middle"), "Top view of an arcade with 10 shop units, 4 of them empty"),
   "question": "From above you can count the boxes. 10 shop units, 4 are empty. What fraction is rented?",
   "explanation": "10 units minus 4 empty = 6 rented. 6 out of 10 is 6/10, which is 60%. A top view lets you count at a glance.",
   "choices": [ch("6/10 = 60%", True), ch("4/10 = 40%"), ch("10/4")]},
 "label": {"items": [
   {"id": "walk", "name": "Walkway", "icon": ico(R(4, 14, 32, 12, "#F4EFD8")), "fact": "🚶 The path between the shops. In a top view it is a long strip."},
   {"id": "unit", "name": "Shop unit", "icon": ico(R(8, 8, 24, 24, "#BFE3DA")), "fact": "🏪 One rentable box. Same shape, same size: easy to count and measure."},
   {"id": "door", "name": "Entrance", "icon": ico(C(20, 20, 10, GOLD)), "fact": "🚪 Where people come in. Always mark it so the plan makes sense."}]},
 "draw": {"prompt": "Draw the arcade from above: one long walkway with a row of shop boxes on each side, and the entrance.",
   "hintSvg": svg(300, 200, R(30, 50, 240, 40) + R(30, 90, 240, 24, "#F4EFD8") + R(30, 114, 240, 40) + C(30, 102, 7, GOLD) + txt(150, 185, "boxes + walkway + entrance", 11, NAVY, "middle"), "hint: walkway with shop boxes on both sides")},
 "rotate": {"prompt": "Rotate the plan. The gold dot (entrance) turns too. The arcade is the SAME, only your view changed. Can you still find the entrance?", "svg": plan(75, True)},
 "compare": {"question": "Two arcades, 10 shops each. Tap the one with the LOWER percent rented.",
   "explanation": "A has 7 shops rented (70%). B has only 4 rented (40%). B has the lower percent, so it looks more deserted.",
   "choices": [{"label": "A: 7 rented", "svg": svg(200, 100, grid10(7), "7 of 10 rented"), "correct": False},
               {"label": "B: 4 rented", "svg": svg(200, 100, grid10(4), "4 of 10 rented"), "correct": True}]},
 "connect": {"items": [
   {"text": "A top view shows every shop as a box", "icon": ICON_RIGHT},
   {"text": "Count the boxes: 10 units, 4 empty", "icon": ICON_RIGHT},
   {"text": "6 rented out of 10 = 6/10 = 60%", "icon": ICON_DROP},
   {"text": "🔗 Links to Titanic Scale Drawing: a plan shrinks a real place by the same scale, like a ship plan. Ghost Detective rule: measure before you panic", "icon": ICON_LINK}]},
 "explain": {"prompt": "Why is a top view handy for finding which shops are empty? Use a fraction or percent in your answer.",
   "visualSvg": svg(200, 100, R(20, 20, 40, 30, GREY) + R(60, 20, 40, 30, "#BFE3DA") + R(100, 20, 40, 30, "#BFE3DA") + txt(20, 80, "6/10 = 60% rented", 12, TEAL, "start", "bold"), "boxes with 6 of 10 rented"),
   "starters": ["From above I can count...", "6 out of 10 means..."], "keywords": ["top view", "boxes", "fraction", "percent"]},
 "predict": {"question": "2 more shops rent a unit. Now 8 of 10 are rented. What percent is that?",
   "explanation": "8 out of 10 = 8/10 = 80%. Each shop is worth 10%.",
   "choices": [ch("80%", True), ch("20%"), ch("8%")]}}

# ---------- page 2: echo ----------
def scene(ox, hard):
    s = C(ox + 22, 50, 8, SAND) + L(ox + 22, 58, ox + 22, 90) + R(ox + 118, 25, 12, 90, "#8D9BAF" if hard else GOLD)
    s += arrow(ox + 36, 65, ox + 116, 65, BLUE, 3)
    return s + (arrow(ox + 116, 85, ox + 36, 85, ORANGE, 3) if hard else txt(ox + 100, 88, "…silence", 10, NAVY, "end"))
d2 = {
 "observe": {"svg": svg(300, 150, scene(0, True) + scene(150, False) + txt(75, 140, "hard bare wall", 11, NAVY, "middle") + txt(225, 140, "soft curtain wall", 11, NAVY, "middle"), "A shout bounces back from a hard wall but fades at a soft wall"),
   "question": "Why do you hear an echo in an empty hall but not in a room full of curtains and sofas?",
   "explanation": "Hard, flat surfaces bounce sound waves back to you. Soft things soak up the sound, so it never comes back. Empty hall = echo = a spooky 'whisper'.",
   "choices": [ch("Hard flat walls bounce the sound back", True), ch("Soft things make sound louder"), ch("Sound cannot travel in a full room")]},
 "label": {"items": [
   {"id": "shout", "name": "Shout (source)", "icon": ico(C(10, 20, 5, SAND) + "<path d='M18 12 Q26 20 18 28 M24 8 Q35 20 24 32' fill='none' stroke='%s' stroke-width='2.5'/>" % BLUE), "fact": "📣 Your shout makes the air shake. Those shakes are sound waves."},
   {"id": "wall", "name": "Hard wall", "icon": ico(R(14, 5, 12, 30, "#8D9BAF")), "fact": "🧱 A smooth hard wall bounces sound, like a ball off a wall."},
   {"id": "echo", "name": "Echo", "icon": ICON_LEFT, "fact": "🔁 The bounced sound comes back a moment later. That delay is the echo."}]},
 "draw": {"prompt": "Draw a person, a wall, and sound arrows: one going to the wall and one coming back.",
   "hintSvg": svg(300, 200, scene(70, True) + txt(150, 185, "person + wall + echo back", 11, NAVY, "middle"), "hint: person, wall, arrow out and back")},
 "rotate": {"prompt": "Rotate the picture. The sound still goes out and bounces straight back. Change the view and the path stays the same!", "svg": "<g transform='translate(25,75) scale(1.6)'>" + scene(0, True) + "</g>"},
 "compare": {"question": "Two halls. Tap the hall with the LOUDER echo.",
   "explanation": "The bare hall (A) has hard walls that bounce sound. The hall with curtains and sofas (B) soaks it up.",
   "choices": [{"label": "A: empty hall, bare walls", "svg": svg(200, 120, scene(40, True).replace("translate", "t"), "empty hall with echo"), "correct": True},
               {"label": "B: curtains and sofas", "svg": svg(200, 120, scene(40, False), "soft hall with no echo"), "correct": False}]},
 "connect": {"items": [
   {"text": "A shout makes sound waves", "icon": ICON_RIGHT},
   {"text": "The waves hit a hard wall and bounce back", "icon": ICON_LEFT},
   {"text": "The echo arrives late: distance = speed × time (sound is about 340 m/s)", "icon": ICON_DROP},
   {"text": "🔗 Links to Ocean & Earth: ships time echoes from the sea floor (sonar). Same idea, but sound goes faster in water", "icon": ICON_LINK}]},
 "explain": {"prompt": "An echo comes back after 0.2 seconds. Sound travels 340 m/s. Explain why the wall is NOT 68 m away, and say how far it is.",
   "visualSvg": svg(200, 100, scene(0, True).replace("ox", "") if False else R(20, 30, 10, 40, "#8D9BAF") + arrow(160, 40, 34, 40, BLUE, 3) + arrow(34, 60, 160, 60, ORANGE, 3) + txt(100, 90, "out + back = 2 trips", 11, TEAL, "middle", "bold"), "sound goes there and back"),
   "starters": ["The sound travels 68 m, but it goes...", "The wall is half because..."], "keywords": ["there and back", "half", "speed", "time"]},
 "predict": {"question": "Echo returns after 0.2 s. Sound goes 340 m/s, so it travels 68 m in total. How far away is the wall?",
   "explanation": "68 m is the whole trip: there AND back. The wall is half of that: 34 m.",
   "choices": [ch("34 m", True), ch("68 m"), ch("17 m")]}}

# ---------- page 3: cold spot ----------
def room(arrows=True):
    s = R(30, 20, 240, 140, "#FFFFFF") + R(125, 20, 50, 12, "#8D9BAF") + txt(150, 14, "air-con vent", 10, NAVY, "middle")
    if arrows:
        s += arrow(150, 36, 150, 120, BLUE, 3) + arrow(150, 145, 50, 145, BLUE, 3) + arrow(150, 145, 250, 145, BLUE, 3)
        s += arrow(45, 120, 45, 45, ORANGE, 3) + arrow(255, 120, 255, 45, ORANGE, 3)
    return s
def dbox(coords): return R(40, 25, 120, 90) + dots(coords)
d3 = {
 "observe": {"svg": svg(300, 180, room() + txt(150, 175, "cold air sinks along the floor 🥶", 11, BLUE, "middle", "bold"), "Cold air from a vent sinks and spreads along the floor while warm air rises at the sides"),
   "question": "Cold air from the air-con vent flows down to your ankles. Why does cold air sink?",
   "explanation": "Cold air is denser: the same space holds more air particles. Denser air sinks. Warm air is less dense and rises. The 'ghost breath' is just a cold air stream.",
   "choices": [ch("Cold air is denser than warm air", True), ch("Cold air is lighter than warm air"), ch("Ghosts pull it down")]},
 "label": {"items": [
   {"id": "vent", "name": "Air-con vent", "icon": ico(R(6, 10, 28, 10, "#8D9BAF") + L(12, 24, 12, 34, BLUE) + L(20, 24, 20, 34, BLUE) + L(28, 24, 28, 34, BLUE)), "fact": "❄️ Blows out air that was cooled down."},
   {"id": "sink", "name": "Cold air sinks", "icon": ICON_DOWN, "fact": "⬇️ Cold = denser = heavier per space. It slides down and along the floor."},
   {"id": "rise", "name": "Warm air rises", "icon": ICON_UP, "fact": "⬆️ Warm = less dense. It floats up and takes the cold air's place later. A loop!"}]},
 "draw": {"prompt": "Draw the air loop: cold air sinking from the vent, sliding along the floor, and warm air rising back up.",
   "hintSvg": svg(300, 200, room() + txt(150, 190, "down, along, up", 11, NAVY, "middle"), "hint: loop of blue arrows down and orange arrows up")},
 "rotate": {"prompt": "Rotate the loop. The arrows turn, but the rule stays: cold goes DOWN, warm goes UP. Gravity decides, not the picture!", "svg": "<g transform='translate(0,20) scale(1)'>" + room() + "</g>"},
 "compare": {"question": "Both boxes are the same size. Tap the air that is DENSER and will sink.",
   "explanation": "More dots in the same box = more particles = denser. Cold air is packed closer, so box A sinks.",
   "choices": [{"label": "A: cold air (packed)", "svg": svg(200, 140, dbox([(65, 50), (100, 50), (135, 50), (65, 72), (100, 72), (135, 72), (65, 95), (100, 95), (135, 95)]), "packed dots"), "correct": True},
               {"label": "B: warm air (few dots)", "svg": svg(200, 140, dbox([(70, 70), (130, 70)]), "few dots"), "correct": False}]},
 "connect": {"items": [
   {"text": "The air-con cools the air", "icon": ICON_RIGHT},
   {"text": "Cold air is denser, so it sinks", "icon": ICON_DOWN},
   {"text": "It slides across the floor: a cold spot on your ankles = 'ghost breath'", "icon": ICON_DROP},
   {"text": "🔗 Links to Connections: Convection. Warm up, cold down: same loop as soup in a pot and the ocean conveyor", "icon": ICON_LINK}]},
 "explain": {"prompt": "A cold spot is felt near the floor but not near the ceiling. Explain why, using the word density.",
   "visualSvg": svg(200, 100, arrow(40, 15, 40, 85, BLUE, 3) + txt(60, 35, "cold: dense, sinks", 12, BLUE, "start", "bold") + txt(60, 70, "warm: rises", 12, ORANGE, "start", "bold"), "cold goes down warm goes up"),
   "starters": ["Cold air is denser, so...", "Warm air rises, so near the ceiling..."], "keywords": ["cold", "dense", "sink", "warm", "rise"]},
 "predict": {"question": "You stand on a chair, 1 metre higher. Where is the air warmer?",
   "explanation": "Cold air sank to the floor and warm air rose. Higher up it is warmer, so the ghost is just air layers.",
   "choices": [ch("Warmer up on the chair", True), ch("Colder up on the chair"), ch("The same everywhere")]}}

# ---------- page 4: flickering light ----------
def circ(closed=True, ty=0):
    s = "<g transform='translate(0,%d)'>" % ty + L(60, 50, 135, 50) + C(150, 50, 16, YEL if closed else "#FFFFFF") + L(166, 50, 240, 50)
    s += L(60, 50, 60, 80) + L(48, 80, 72, 80, NAVY, 4) + L(54, 92, 66, 92, NAVY, 3) + L(60, 92, 60, 130) + L(60, 130, 240, 130)
    s += L(240, 50, 240, 130) if closed else L(240, 50, 240, 82) + L(240, 100, 240, 130) + C(240, 91, 4, ORANGE)
    return s + txt(150, 100, "loop OK" if closed else "GAP!", 12, TEAL if closed else ORANGE, "middle", "bold") + "</g>"
d4 = {
 "observe": {"svg": svg(300, 160, circ(False), "A battery and bulb circuit with a gap in the wire on the right"),
   "question": "The bulb flickers whenever a loose wire touches and un-touches the gap. What does the bulb need to stay on?",
   "explanation": "Charge only flows round a complete loop. A gap stops the flow and the bulb goes dark. A loose wire joins and breaks the loop again and again: flicker.",
   "choices": [ch("A complete loop with no gaps", True), ch("A ghost nearby"), ch("A longer wire")]},
 "label": {"items": [
   {"id": "bat", "name": "Battery", "icon": ico(L(8, 12, 8, 28, NAVY, 4) + L(16, 15, 16, 25, NAVY, 3) + L(8, 20, 2, 20) + L(16, 20, 38, 20)), "fact": "🔋 The pusher. It pushes charge round the loop."},
   {"id": "bulb", "name": "Bulb", "icon": ico(C(20, 20, 11, YEL)), "fact": "💡 Changes electrical energy into light (and a little heat)."},
   {"id": "gap", "name": "Loose wire gap", "icon": ico(L(4, 20, 14, 20) + L(26, 20, 36, 20) + C(20, 20, 4, ORANGE)), "fact": "⚠️ A gap breaks the loop. Touching again = flicker."}]},
 "draw": {"prompt": "Draw a full circuit: a battery and a bulb joined by wires in a complete loop.",
   "hintSvg": svg(300, 200, circ(True, 10) + txt(150, 190, "battery + bulb + closed loop", 11, NAVY, "middle"), "hint: closed circuit")},
 "rotate": {"prompt": "Rotate the circuit. It still has a gap, so the bulb is still dark. A loop is a loop from any side.", "svg": circ(False, 70)},
 "compare": {"question": "Tap the circuit where the bulb WILL light.",
   "explanation": "A is a closed loop, so the bulb lights. B has a gap, so the charge stops.",
   "choices": [{"label": "A: closed loop", "svg": svg(300, 160, circ(True), "closed circuit"), "correct": True},
               {"label": "B: gap in the wire", "svg": svg(300, 160, circ(False), "open circuit"), "correct": False}]},
 "connect": {"items": [
   {"text": "The battery pushes charge round a loop", "icon": ICON_RIGHT},
   {"text": "A gap breaks the loop, so the charge stops", "icon": ICON_RIGHT},
   {"text": "A loose wire joins and breaks it over and over = flicker, not a ghost", "icon": ICON_DROP},
   {"text": "🔗 Links to Mario Energy Transformation: the bulb turns electrical energy into light and heat, like energy changing form", "icon": ICON_LINK}]},
 "explain": {"prompt": "Why does a loose wire make the light flicker? Use the words loop and gap.",
   "visualSvg": svg(200, 100, C(60, 50, 16, YEL) + txt(90, 45, "loop closed = ON", 12, TEAL, "start", "bold") + txt(90, 68, "gap = OFF", 12, ORANGE, "start", "bold"), "bulb on when loop closed"),
   "starters": ["The loose wire joins the loop and then...", "When there is a gap, the charge..."], "keywords": ["loop", "gap", "battery", "charge"]},
 "predict": {"question": "Three bulbs share ONE wire loop, one after another (a series circuit). One bulb burns out. What happens to the other two?",
   "explanation": "Burning out makes a gap in the only loop, so all three go dark. (In a parallel circuit each bulb has its own loop, so the others stay on.)",
   "choices": [ch("All go dark: the loop is broken", True), ch("The other two get brighter"), ch("Nothing changes")]}}

PAGES = [("haunted-01-floor-plan", "Old Arcade: Floor Plan 🗺️", d1), ("haunted-02-echo-hall", "Old Arcade: Echo in the Empty Hall 🔊", d2),
         ("haunted-03-cold-spot", "Old Arcade: Cold Spot ❄️", d3), ("haunted-04-flickering-light", "Old Arcade: Flickering Light 💡", d4)]
for cid, t, d in PAGES: build(cid, t, d)

# ---- pills ----
pp = os.path.join(HERE, "draw_pills.json"); P = json.load(open(pp, encoding="utf-8"))
P.update({"haunted-01-floor-plan": ["Walkway", "Shop boxes", "Entrance"], "haunted-02-echo-hall": ["Person", "Wall", "Echo back"],
          "haunted-03-cold-spot": ["Vent", "Cold air sinks", "Warm air rises"], "haunted-04-flickering-light": ["Battery", "Bulb", "Closed loop"]})
json.dump(P, open(pp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- hub entry (idempotent) ----
ip = os.path.join(OUT, "index.html"); h = open(ip, encoding="utf-8").read()
if 'id: "haunted"' not in h:
    names = ["Floor Plan", "Echo in the Empty Hall", "Cold Spot ⭐", "Flickering Light ⭐", "Rust & Dust", "Giant Shadow", "Who Lives Here?", "Drip, Drip"]
    files = {1: "haunted-01-floor-plan", 2: "haunted-02-echo-hall", 3: "haunted-03-cold-spot", 4: "haunted-04-flickering-light"}
    cs = ",\n".join('      { id: "%s", label: "%d. %s"%s }' % (files.get(i + 1, "haunted-0%d-planned" % (i + 1)), i + 1, n,
                    (', file: "%s.html"' % files[i + 1]) if (i + 1) in files else "") for i, n in enumerate(names))
    book = '  {\n    id: "haunted",\n    icon: "🏚️",\n    title: "Haunted House: Ghost Detective",\n    subtitle: "Every spooky thing has a science cause",\n    locked: false,\n    concepts: [\n%s\n    ]\n  },\n' % cs
    k = h.index('id: "connections"'); st = h.rfind("  {\n", 0, k)
    h = h[:st] + book + h[st:]; open(ip, "w", encoding="utf-8").write(h)
print("haunted batch 1 done")
