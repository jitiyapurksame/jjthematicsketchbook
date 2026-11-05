// Real-canvas test for the concept-pill drawing step (needs the `canvas` npm package; skipped if it is missing).
// Checks: stamping paints pixels, the gate blocks finishing, Undo removes ONE action (stroke first, then the stamp),
// Clear un-places everything and Undo restores it.
const fs = require("fs");
const path = require("path");
let JSDOM;
try { ({ JSDOM } = require("jsdom")); require("canvas"); } catch (e) { console.log("SKIP real-canvas pill test (install `canvas` with: npm install canvas --no-save)"); process.exit(0); }

const file = path.join(__dirname, "..", "deliverables", "birds-03-forces-in-flight.html");
const dom = new JSDOM(fs.readFileSync(file, "utf-8"), { runScripts: "dangerously", resources: "usable", pretendToBeVisual: true });
const { window } = dom; const doc = window.document;
const errors = [];
window.onerror = (m) => errors.push("window.onerror: " + m);
const click = (el) => el.dispatchEvent(new window.MouseEvent("click", { bubbles: true }));
const canvasEl = doc.getElementById("draw-canvas");
const fire = (type, x, y) => canvasEl.dispatchEvent(new window.MouseEvent(type, { bubbles: true, clientX: x, clientY: y }));
const px = (x, y) => Array.from(canvasEl.getContext("2d").getImageData(x, y, 1, 1).data).slice(0, 3);
const isNavy = (c) => Math.abs(c[0] - 11) < 12 && Math.abs(c[1] - 37) < 12 && Math.abs(c[2] - 69) < 12;
const isBg = (c) => Math.abs(c[0] - 243) < 6 && Math.abs(c[1] - 238) < 6 && Math.abs(c[2] - 225) < 6;
const pill = (t) => Array.from(doc.querySelectorAll("#pill-row .pill")).find((b) => b.dataset.pill === t);
const placed = (t) => pill(t).classList.contains("placed");
const next = doc.getElementById("draw-next");
const finish = doc.getElementById("draw-finished-btn");
const undo = doc.getElementById("undo-btn"), clear = doc.getElementById("clear-btn");
const check = (ok, msg) => { if (!ok) errors.push(msg); };

const names = ["Lift", "Weight", "Thrust", "Drag"];
check(doc.querySelectorAll("#pill-row .pill").length === 4, "expected 4 pills");

// 1. stamp "Lift"
click(pill("Lift")); check(pill("Lift").classList.contains("armed"), "pill should be armed after click");
fire("pointerdown", 100, 60);
check(placed("Lift"), "Lift should be placed");
check(isNavy(px(100, 48)), "stamp should paint navy pixels (got " + px(100, 48) + ")");

// 2. a stroke, then try to finish with pills missing
fire("pointerdown", 200, 150); fire("pointermove", 260, 150); fire("pointermove", 300, 150); fire("pointerup", 300, 150);
check(!isBg(px(260, 150)), "stroke should paint pixels");
click(finish);
check(next.disabled, "must stay locked with pills missing");
check(/Weight, Thrust, Drag/.test(doc.getElementById("pill-help").textContent), "help text should list missing pills, got: " + doc.getElementById("pill-help").textContent);

// 3. Undo once = only the stroke goes
click(undo);
check(isBg(px(260, 150)), "undo #1 should remove the stroke");
check(placed("Lift") && isNavy(px(100, 48)), "undo #1 must keep the Lift stamp");
// 4. Undo again = the stamp goes, pill is free again
click(undo);
check(!placed("Lift") && isBg(px(100, 48)), "undo #2 should remove the stamp and un-place Lift");
click(undo); // nothing left, must not throw

// 5. place all, stroke, finish
names.forEach((n, i) => { click(pill(n)); fire("pointerdown", 80 + i * 110, 40 + (i % 2) * 90); });
check(names.every(placed), "all four should be placed");
click(finish); check(next.disabled, "locked until a stroke is drawn");
check(/DRAW something/.test(doc.getElementById("pill-help").textContent), "help should ask for a stroke");
fire("pointerdown", 20, 200); fire("pointermove", 80, 210); fire("pointerup", 80, 210);
click(finish); check(!next.disabled, "draw-next should unlock once everything is done");

// 6. Clear + Undo (use a fresh page state: undo restores the placed pills)
click(clear); check(names.every((n) => !placed(n)), "clear should un-place every pill");
click(undo); check(names.every(placed), "undo after clear should restore the placed pills");

console.log(errors.length ? "FAIL\n  " + errors.join("\n  ") : "PASS real-canvas pill test (stamp, gate, 1-step undo, clear/undo)");
process.exit(errors.length ? 1 : 0);
