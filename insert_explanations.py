import re

EXPLANATIONS = {
  "build_batch1_v2.py": [
    ("Which end of the ship is pointed?",
     "The bow's pointed shape lets it slice through water with less resistance than a flat front would."),
    ("Tap the picture that shows the BOW (the pointed front).",
     "A pointed shape meets less water resistance than a rounded one — that's why it's at the front."),
    ("If a ship had a completely flat, square front instead of a pointed bow, what would happen?",
     "More flat surface pushing straight into the water means more drag, so more engine power is needed for the same speed."),
    ("Looking from above, which is bigger on this ship?",
     "Ships are built long and narrow because that shape moves through water more efficiently than a short, wide one."),
    ("Tap the picture that shows the LEFT half of the ship.",
     "The centerline splits the ship exactly in half — left and right are mirror images of each other."),
    ("If a ship was built lopsided (uneven on both sides), what would likely happen?",
     "If one side is heavier or shaped differently, buoyancy and weight aren't balanced left-to-right, so the ship leans toward the heavier side."),
    ("This is the ship sliced in half. Which layer is full of air?",
     "Air weighs far less than water for the same amount of space, so air-filled compartments keep the ship's overall density low enough to float."),
    ("Tap the picture that shows the ship riding LOWER in the water (a heavier load).",
     "More cargo means more weight, which means more buoyant force is needed to balance it — so the ship sinks deeper until it does."),
    ("If water floods one compartment, what happens to the ship?",
     "Water flooding in replaces air with something much heavier, adding weight without adding buoyancy — so that part pulls the ship down."),
    ("Two forces pull on the ship in opposite directions. What happens when they're perfectly equal?",
     "When buoyant force (up) exactly equals weight (down), the net force is zero — so the ship neither sinks nor rises."),
    ("Tap the picture that shows a SINKING ship (unbalanced forces).",
     "In the sinking picture the arrows are unequal — weight is bigger than buoyant force, creating a net downward force."),
    ("If you loaded the ship with a lot of extra cargo, what would happen?",
     "Adding cargo increases weight. To rebalance, the ship displaces more water and sinks lower until buoyant force grows to match the new weight."),
  ],
  "build_batch2.py": [
    ("As you go deeper underwater, what happens to the pressure?",
     "Pressure comes from the weight of water above pushing down — the deeper you go, the taller (and heavier) that column of water gets."),
    ("Tap the picture that shows CORRECT pressure (bigger arrows lower down).",
     "The correct picture shows arrows growing with depth, matching how water pressure builds up the deeper you go."),
    ("If a diver went twice as deep, what would roughly happen to the pressure on their body?",
     "Water pressure increases roughly in direct proportion to depth, so twice the depth means roughly twice the pressure."),
    ("When the ship pushes water out of the way, what pushes back?",
     "This is Archimedes' Principle: an object pushes fluid out of the way, and that fluid pushes back with an equal upward force."),
    ("Tap the picture that shows MORE water being displaced (a heavier ship).",
     "A heavier ship sinks deeper, displacing more water, until the extra buoyant force balances its extra weight."),
    ("If you replaced the ship with a much heavier version of the same shape, what happens to how much water it displaces?",
     "Buoyant force must equal weight for a ship to float, so more weight means more water must be displaced to generate that extra upward force."),
    ("If one compartment fills with water, what happens to the rest of the ship?",
     "Bulkheads (walls) seal off flooding to just one section, so the rest of the ship keeps its air and stays buoyant enough to float."),
    ("Tap the SAFER design — more compartments means flooding stays contained.",
     "More, smaller compartments mean a single flood affects a smaller fraction of the ship's total buoyancy."),
    ("If TOO MANY compartments flood at once, what would likely happen?",
     "Every design has a limit — Titanic could survive a few flooded compartments, but too many overwhelmed its remaining buoyancy."),
    ("Looking at these three hull shapes, which do you think tips over most easily?",
     "A narrow hull has a small base, so it doesn't take much tilt before it becomes easier to tip over."),
    ("Tap the picture that shows the MORE STABLE hull (wide base).",
     "A wider hull spreads its support over a bigger base, resisting tipping much like a wide-based table is harder to knock over."),
    ("If a ship's hull was made narrower to go faster, what trade-off might happen?",
     "Narrower hulls often reduce drag (helping speed) but also reduce the stable base — a classic engineering trade-off."),
  ],
  "build_batch3.py": [
    ("In which order does energy flow through the ship's propulsion system?",
     "Energy always flows from its source (the engine) through the mechanism (shaft, propeller) and finally into the surroundings (water)."),
    ("Tap the propeller that pushes MORE water with each turn (more blades).",
     "More blades means more surface area pushing water backward with each single turn of the propeller."),
    ("If the propeller spun faster, what would likely happen to the ship's speed?",
     "More spin pushes more water backward each second, so by Newton's third law, more force pushes the ship forward — until drag balances it out."),
    ("If the real ship is 269 m long and we use a scale of 1:1000, about how long is the model?",
     "Scale 1:1000 means every real-world unit becomes 1/1000th its size: 269 m × (1/1000) = 0.269 m = 26.9 cm."),
    ("A 200 m ship is scaled at 1:100. Tap the correctly-sized model.",
     "200 m ÷ 100 (the scale) = 2 m — divide the real size by the second number in the ratio to get the model size."),
    ("A model is built at 1:50 scale of a 10 m boat. How long is the model?",
     "10 m = 1000 cm. Divide by 50 (the scale): 1000 ÷ 50 = 20 cm."),
    ("Looking at this speed-time graph, during which part is the ship going at a CONSTANT speed?",
     "On a speed-time graph, the vertical axis is speed. If the line isn't rising or falling, speed isn't changing — that's constant speed."),
    ("Tap the graph that shows the ship SPEEDING UP the fastest (steepest rising line).",
     "A steeper line means speed changes more for the same amount of time — that's a bigger acceleration."),
    ("If the line on a speed-time graph suddenly drops straight down to zero, what does that mean happened?",
     "A near-vertical drop means speed fell to zero in almost no time at all — a sudden stop."),
    ("Using the triangle, how do you calculate density?",
     "Cover the letter you want to find. Density and Volume sit side by side on the bottom, Mass sits on top — so Density = Mass ÷ Volume."),
    ("Tap the object that is MORE dense (same size, more mass packed inside).",
     "Same size (same volume) but more mass squeezed inside means higher density, since density = mass ÷ volume."),
    ("If you keep the mass the same but increase the volume, what happens to density?",
     "Density = mass ÷ volume. If mass stays the same but volume grows, you're dividing by a bigger number, so density gets smaller."),
  ],
}

for filename, pairs in EXPLANATIONS.items():
    text = open(filename, encoding="utf-8").read()
    for question, explanation in pairs:
        old = '"question": "%s",' % question
        assert old in text, "MISSING ANCHOR in %s: %r" % (filename, question)
        new = '"question": "%s",\n    "explanation": "%s",' % (question, explanation)
        assert text.count(old) == 1, "NOT UNIQUE in %s: %r (found %d times)" % (filename, question, text.count(old))
        text = text.replace(old, new)
    open(filename, "w", encoding="utf-8").write(text)
    print("updated", filename, "with", len(pairs), "explanations")
