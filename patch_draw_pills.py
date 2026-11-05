"""Concept pills for the Draw step.

What it does (idempotent, safe to re-run):
  1. Patches the drawing engine code inside every page that has a draw canvas (and the three template sources) so that:
       - a tray of "idea pills" appears above the canvas (tap a pill, then tap the drawing to stamp it in);
       - "I'm finished drawing" is blocked until every pill is placed AND at least one pen stroke was drawn;
       - Undo now removes exactly one action (the old code removed two) and un-places a pill if its stamp is undone.
  2. Injects the pills for each page from draw_pills.json (key = file name without .html) into CONCEPT_DATA
     (draw.pills for 8-mission + Connection pages, practice.pills for VST draw labs).
Pages whose id has no entry in draw_pills.json keep the old behaviour (no pills, no gate).

Run AFTER any build script (they overwrite pages), together with patch_hub_navigation.py:
    python3 build-tools/patch_draw_pills.py
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
DELIV = os.path.join(ROOT, "deliverables")
PILLS = json.load(open(os.path.join(HERE, "draw_pills.json"), encoding="utf-8"))
MARK = "/*PILLS-V1*/"

PILL_CSS = """
/*PILLS-V1-CSS*/
.pill-tray{ background:#FFFBF0; border:2px dashed #C9A24B; border-radius:10px; padding:10px 12px; margin:10px 0; }
.pill-title{ margin:0 0 4px; font-weight:700; font-size:.95rem; display:flex; justify-content:space-between; gap:8px; }
.pill-help{ margin:0 0 8px; font-size:.92rem; }
.pill-help.warn{ color:#B3401F; font-weight:700; }
.pill-row{ display:flex; flex-wrap:wrap; gap:8px; }
.pill{ border:2px solid #0B2545; background:#FFFFFF; color:#0B2545; border-radius:999px; padding:8px 14px; font-weight:700; font-size:.95rem; min-height:44px; cursor:pointer; }
.pill.armed{ background:#C9A24B; box-shadow:0 0 0 3px rgba(201,162,75,.45); }
.pill.placed{ background:#2E6E62; border-color:#2E6E62; color:#FFFFFF; cursor:default; opacity:1; }
"""

PILL_JS = r"""  /*PILLS-V1*/
  /* ---------- Concept pills: tap an idea, tap the drawing to stamp it in; all must be placed to finish ---------- */
  var PILLS = ((DATA.draw && DATA.draw.pills) || (DATA.practice && DATA.practice.pills) || []).slice();
  var placed = {};
  var armedPill = null;
  var strokeTotal = 0, strokeMarked = false;
  var actionLog = [];
  var pillRow = null, pillCount = null, pillHelp = null;

  function stampPill(text, x, y){
    ctx.save();
    ctx.font = "700 15px system-ui, -apple-system, 'Segoe UI', sans-serif";
    var w = Math.ceil(ctx.measureText(text).width) + 22, h = 30, r = 15;
    var px = Math.min(Math.max(x - w / 2, 4), canvasCSSWidth - w - 4);
    var py = Math.min(Math.max(y - h / 2, 4), canvasCSSHeight - h - 4);
    ctx.beginPath();
    ctx.moveTo(px + r, py);
    ctx.lineTo(px + w - r, py);
    ctx.arc(px + w - r, py + r, r, -Math.PI / 2, Math.PI / 2);
    ctx.lineTo(px + r, py + h);
    ctx.arc(px + r, py + r, r, Math.PI / 2, Math.PI * 1.5);
    ctx.closePath();
    ctx.fillStyle = "#0B2545"; ctx.fill();
    ctx.fillStyle = "#FFFFFF"; ctx.textAlign = "center"; ctx.textBaseline = "middle";
    ctx.fillText(text, px + w / 2, py + h / 2 + 1);
    ctx.restore();
  }
  function pillRefresh(){
    if(!pillRow) return;
    var n = 0;
    Array.prototype.forEach.call(pillRow.children, function(b){
      var t = b.dataset.pill, done = !!placed[t];
      if(done) n++;
      b.classList.toggle("placed", done);
      b.classList.toggle("armed", armedPill === t);
      b.disabled = done;
      b.textContent = (done ? "✓ " : "") + t;
      b.setAttribute("aria-pressed", armedPill === t ? "true" : "false");
    });
    pillCount.textContent = n + " / " + PILLS.length + " placed";
    pillHelp.className = "pill-help";
    pillHelp.textContent = armedPill
      ? ("Now tap your drawing where “" + armedPill + "” belongs.")
      : (n === PILLS.length ? "All ideas placed! Join them with lines and arrows, then press finished."
                            : "Tap an idea, then tap your drawing where it belongs.");
    canvas.style.cursor = armedPill ? "crosshair" : "";
  }
  (function(){
    if(!PILLS.length) return;
    var tray = document.createElement("div");
    tray.className = "pill-tray"; tray.id = "pill-tray";
    tray.innerHTML = '<p class="pill-title"><span>🧩 Put these ideas in your picture</span><span id="pill-count"></span></p><p class="pill-help" id="pill-help"></p><div class="pill-row" id="pill-row"></div>';
    canvas.parentNode.insertBefore(tray, canvas);
    pillRow = tray.querySelector("#pill-row"); pillCount = tray.querySelector("#pill-count"); pillHelp = tray.querySelector("#pill-help");
    PILLS.forEach(function(p){
      var b = document.createElement("button");
      b.type = "button"; b.className = "pill"; b.dataset.pill = p; b.textContent = p;
      b.addEventListener("click", function(){
        if(placed[p]) return;
        armedPill = (armedPill === p) ? null : p;
        pillRefresh();
      });
      pillRow.appendChild(b);
    });
    pillRefresh();
  })();
  function pillPointerDown(e){
    strokeMarked = false;
    if(!armedPill) return false;
    if(!canvasReady) initCanvasIfNeeded();
    var pos = getPos(e);
    var text = armedPill;
    if(ctx){
      pushUndo();
      if(actionLog.length) actionLog[actionLog.length - 1] = { type: "stamp", text: text };
      stampPill(text, pos.x, pos.y);
    }
    placed[text] = true;
    armedPill = null;
    drawing = false;
    pillRefresh();
    return true;
  }
  function pillStrokeSeen(){
    if(strokeMarked) return;
    strokeMarked = true; strokeTotal++;
    if(actionLog.length && actionLog[actionLog.length - 1] === null) actionLog[actionLog.length - 1] = { type: "stroke" };
  }
  function pillUndoRecord(rec){
    if(!rec) return;
    if(rec.type === "stamp"){ placed[rec.text] = false; }
    else if(rec.type === "stroke"){ strokeTotal = Math.max(0, strokeTotal - 1); }
    else if(rec.type === "clear"){ placed = rec.placedBefore; strokeTotal = rec.strokesBefore; }
    pillRefresh();
  }
  function pillGateOk(){
    if(!PILLS.length) return true;
    var missing = PILLS.filter(function(p){ return !placed[p]; });
    if(missing.length){
      pillHelp.textContent = "Almost! Still to place: " + missing.join(", ") + ".";
      pillHelp.className = "pill-help warn";
      return false;
    }
    if(strokeTotal < 1){
      pillHelp.textContent = "Now DRAW something too: join your ideas with lines and arrows.";
      pillHelp.className = "pill-help warn";
      return false;
    }
    return true;
  }

  document.getElementById("undo-btn").addEventListener("click", function(){
    if(!ctx) return;
    if(undoStack.length < 2) return;
    var prev = undoStack.pop();
    var rec = actionLog.pop();
    ctx.putImageData(prev, 0, 0);
    pillUndoRecord(rec);
  });
"""

NEW_CLEAR = """  document.getElementById("clear-btn").addEventListener("click", function(){
    if(!ctx) return;
    pushUndo();
    if(actionLog.length) actionLog[actionLog.length - 1] = { type: "clear", placedBefore: JSON.parse(JSON.stringify(placed)), strokesBefore: strokeTotal };
    ctx.fillStyle = "#F3EEE1";
    ctx.fillRect(0, 0, canvasCSSWidth, canvasCSSHeight);
    placed = {}; strokeTotal = 0; armedPill = null;
    pillRefresh();
  });
"""

NEW_PUSH = """  function pushUndo(){
    if(!ctx) return;
    if(undoStack.length > 19){ undoStack.shift(); actionLog.shift(); }
    undoStack.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
    actionLog.push(null);
  }
"""

RE_PUSH = re.compile(r"  function pushUndo\(\)\{.*?\n  \}\n", re.S)
RE_UNDO = re.compile(r'  document\.getElementById\("undo-btn"\)\.addEventListener\("click", function\(\)\{.*?\n  \}\);\n', re.S)
RE_CLEAR = re.compile(r'  document\.getElementById\("clear-btn"\)\.addEventListener\("click", function\(\)\{.*?\n  \}\);\n', re.S)
RE_FINISH = re.compile(r"saveDrawingToGallery\(\);\n    (drawNext|practiceNext)\.disabled = false;")
DOWN_OLD = 'canvas.addEventListener("pointerdown", function(e){\n'
MOVE_OLD = "if(!drawing || !ctx) return;"
DATA_RE = re.compile(r"window\.CONCEPT_DATA = (\{.*?\});\n", re.S)


def patch_engine(s, name):
    """Return (new_text, status)."""
    if MARK in s:
        return s, "already"
    for label, ok in (("pushUndo", RE_PUSH.search(s)), ("undo", RE_UNDO.search(s)), ("clear", RE_CLEAR.search(s)),
                      ("finish", RE_FINISH.search(s)), ("pointerdown", DOWN_OLD in s), ("pointermove", MOVE_OLD in s),
                      ("style", "</style>" in s)):
        if not ok:
            return s, "MISSING anchor: " + label
    s = RE_PUSH.sub(lambda m: NEW_PUSH, s, count=1)
    s = RE_UNDO.sub(lambda m: PILL_JS, s, count=1)
    s = RE_CLEAR.sub(lambda m: NEW_CLEAR, s, count=1)
    s = RE_FINISH.sub(lambda m: "if(!pillGateOk()) return;\n    saveDrawingToGallery();\n    " + m.group(1) + ".disabled = false;", s, count=1)
    s = s.replace(DOWN_OLD, DOWN_OLD + "    if(pillPointerDown(e)) return;\n", 1)
    s = s.replace(MOVE_OLD, "if(drawing) pillStrokeSeen();\n    " + MOVE_OLD, 1)
    s = s.replace("</style>", PILL_CSS + "</style>", 1)
    return s, "patched"


def inject_data(s, cid):
    pills = PILLS.get(cid)
    m = DATA_RE.search(s)
    if not m:
        return s, "no-data"
    raw = m.group(1)
    try:
        data = json.loads(raw)
    except ValueError:
        return s, "no-data"
    key = "practice" if (data.get("practice", {}).get("mode") == "draw") else "draw"
    if key not in data:
        return s, "no-draw"
    if not pills:
        if "pills" in data[key]:
            del data[key]["pills"]
        else:
            return s, "none-defined"
    else:
        data[key]["pills"] = pills
    pretty = raw.startswith("{\n")
    new = json.dumps(data, ensure_ascii=False, indent=2 if pretty else None)
    return s[:m.start(1)] + new + s[m.end(1):], "data-set" if pills else "data-removed"


def main():
    report = {"patched": 0, "already": 0, "bad": [], "data": 0, "nodata": []}
    # 1) template sources: engine patch only
    for t in ("connection-template-source.html", "vst-template-source.html", os.path.join("build-tools", "engine-template-v2-source.html")):
        p = os.path.join(ROOT, t)
        if not os.path.exists(p):
            continue
        s = open(p, encoding="utf-8").read()
        s2, st = patch_engine(s, t)
        if st.startswith("MISSING"):
            report["bad"].append((t, st))
        elif st == "patched":
            open(p, "w", encoding="utf-8").write(s2)
            print("template patched:", t)
    # 2) built pages
    for f in sorted(os.listdir(DELIV)):
        if not f.endswith(".html") or f == "index.html":
            continue
        p = os.path.join(DELIV, f)
        s = open(p, encoding="utf-8").read()
        if 'id="draw-canvas"' not in s:
            continue
        cid = f[:-5]
        if cid not in PILLS:
            continue  # no drawing step on this page: leave it untouched
        s2, st = patch_engine(s, f)
        if st.startswith("MISSING"):
            report["bad"].append((f, st)); continue
        report["patched" if st == "patched" else "already"] += 1
        s3, dst = inject_data(s2, cid)
        if dst in ("data-set", "data-removed"):
            report["data"] += 1
        elif dst in ("no-data", "no-draw"):
            report["nodata"].append((f, dst))
        if s3 != s:
            open(p, "w", encoding="utf-8").write(s3)
    print("pages engine-patched:", report["patched"], "| already patched:", report["already"], "| pill data written:", report["data"])
    if report["nodata"]:
        print("no draw data found in:", report["nodata"])
    if report["bad"]:
        print("PROBLEMS:", report["bad"]); sys.exit(1)
    missing = [k for k in PILLS if not os.path.exists(os.path.join(DELIV, k + ".html"))]
    if missing:
        print("pills defined for pages that do not exist:", missing); sys.exit(1)


if __name__ == "__main__":
    main()
