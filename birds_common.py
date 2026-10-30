"""Shared helpers for the Pigeons & Doves book (build(), check(), SVG helpers, icons).
Imported by build_birds_batch2.py. (batch1 still carries its own copy.)

Original batch-1 note: 8-mission engine.

Run from anywhere:  python3 build-tools/build_birds_batch1.py
Reads  engine-template-v2.html from the CURRENT folder if present, otherwise
       build-tools/engine-template-v2-source.html.
Writes birds-0N-*.html into ../deliverables (relative to this script).
Fail-loud: any missing marker or malformed data stops the build.
"""
import json, re, os, sys, math

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "deliverables"))
if not os.path.isdir(OUT):
    sys.exit("deliverables/ folder not found next to build-tools/: " + OUT)

tpl_path = None
for p in (os.path.join(os.getcwd(), "engine-template-v2.html"),
          os.path.join(HERE, "engine-template-v2-source.html")):
    if os.path.exists(p):
        tpl_path = p
        break
if not tpl_path:
    sys.exit("engine template not found")
TEMPLATE = open(tpl_path, encoding="utf-8").read()
DATA_BLOCK_RE = re.compile(r"window\.CONCEPT_DATA = \{.*?\};", re.S)

REQUIRED = ["observe", "label", "draw", "rotate", "compare", "connect", "explain", "predict"]


def check(cid, data):
    for k in REQUIRED:
        assert k in data, "%s: missing mission %s" % (cid, k)
    for k in ("observe", "compare", "predict"):
        ch = data[k]["choices"]
        assert len(ch) >= 2, "%s.%s needs 2+ choices" % (cid, k)
        assert sum(1 for c in ch if c["correct"]) == 1, "%s.%s needs exactly one correct choice" % (cid, k)
    for c in data["compare"]["choices"]:
        assert c.get("svg") and c.get("label"), "%s compare choice needs svg+label" % cid
    ids = [i["id"] for i in data["label"]["items"]]
    assert len(ids) == len(set(ids)) and len(ids) >= 3, "%s label ids" % cid
    for i in data["label"]["items"]:
        assert i["icon"] and i["fact"] and i["name"], "%s label item incomplete" % cid
    assert re.search(r"<(line|path|circle|ellipse|rect|polygon)", data["draw"]["hintSvg"]), "%s empty draw hint" % cid
    assert data["rotate"]["svg"].strip(), "%s empty rotate svg" % cid
    assert data["connect"]["items"][-1]["text"].startswith("🔗"), "%s connect chain must end with a 🔗 link" % cid
    assert data["explain"]["starters"] and data["explain"]["keywords"], "%s explain chips" % cid


def build(cid, title, data):
    check(cid, data)
    html = TEMPLATE
    for old, new in [
        ('data-concept-id="theme-00-example"', 'data-concept-id="%s"' % cid),
        ("<title>[CONCEPT TITLE] — Thematic Sketchbook</title>", "<title>%s — Thematic Sketchbook</title>" % title),
        ('<h1 id="concept-title">[CONCEPT TITLE]</h1>', '<h1 id="concept-title">%s</h1>' % title),
    ]:
        assert old in html, "template marker missing: " + old
        html = html.replace(old, new)
    assert DATA_BLOCK_RE.search(html), "CONCEPT_DATA block not found"
    json_str = json.dumps(data, ensure_ascii=False)
    html = DATA_BLOCK_RE.sub(lambda m: "window.CONCEPT_DATA = " + json_str + ";", html)
    path = os.path.join(OUT, cid + ".html")
    open(path, "w", encoding="utf-8").write(html)
    print("built", cid + ".html")


# ---------------- palette + tiny SVG helpers ----------------
NAVY = "#0B2545"; ORANGE = "#D9603B"; TEAL = "#2E6E62"; GREEN = "#3F8F5C"
GOLD = "#C9A24B"; SAND = "#DCD3BC"; PG = "#8D9BAF"; PD = "#6F7F95"; NECK = "#5B8F7B"


def arrow(x1, y1, x2, y2, color, w=3, head=9):
    ang = math.atan2(y2 - y1, x2 - x1)
    bx = x2 - head * math.cos(ang); by = y2 - head * math.sin(ang)
    px = -math.sin(ang) * head * 0.6; py = math.cos(ang) * head * 0.6
    return ("<line x1='%.1f' y1='%.1f' x2='%.1f' y2='%.1f' stroke='%s' stroke-width='%s' stroke-linecap='round'/>"
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>"
            % (x1, y1, bx, by, color, w, x2, y2, bx + px, by + py, bx - px, by - py, color))


def txt(x, y, s, size=11, color=NAVY, anchor="start", weight="normal"):
    return "<text x='%g' y='%g' font-size='%g' fill='%s' text-anchor='%s' font-weight='%s'>%s</text>" % (
        x, y, size, color, anchor, weight, s)


def svg(w, h, inner, label):
    return "<svg viewBox='0 0 %d %d' role='img' aria-label='%s'>%s</svg>" % (w, h, label.replace("'", "’"), inner)


def tri_right(x, y, color, s=6):
    return "<polygon points='%g,%g %g,%g %g,%g' fill='%s'/>" % (x, y, x - s - 2, y - s + 1, x - s - 2, y + s - 1, color)


def pigeon():
    """Pigeon facing right, drawn inside roughly x 38..254, y 57..168."""
    return (
        "<g>"
        "<polygon points='92,100 40,86 38,116 92,120' fill='%s' stroke='%s' stroke-width='2'/>"
        "<ellipse cx='150' cy='105' rx='66' ry='38' fill='%s' stroke='%s' stroke-width='2'/>"
        "<circle cx='222' cy='76' r='18' fill='%s' stroke='%s' stroke-width='2'/>"
        "<ellipse cx='207' cy='92' rx='20' ry='16' fill='%s'/>"
        "<polygon points='239,74 254,78 239,82' fill='#E8D9B5' stroke='%s' stroke-width='1.5'/>"
        "<circle cx='227' cy='72' r='3' fill='%s'/>"
        "<path d='M118 96 Q152 66 198 98 Q160 128 108 120 Z' fill='%s' stroke='%s' stroke-width='2'/>"
        "<line x1='150' y1='143' x2='150' y2='168' stroke='%s' stroke-width='3'/>"
        "<line x1='170' y1='141' x2='170' y2='168' stroke='%s' stroke-width='3'/>"
        "</g>" % (PD, NAVY, PG, NAVY, PG, NAVY, NECK, NAVY, ORANGE, PD, NAVY, ORANGE, ORANGE))


def pigeon_at(scale, cx, cy):
    # pigeon centre is about (146, 112)
    tx = cx - 146 * scale; ty = cy - 112 * scale
    return "<g transform='translate(%.1f,%.1f) scale(%s)'>%s</g>" % (tx, ty, scale, pigeon())


# icons (40x40)
ICON_WING = "<svg viewBox='0 0 40 40'><path d='M5 29 Q18 3 36 13 Q22 35 5 29 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (PD, NAVY)
ICON_CHEST = ("<svg viewBox='0 0 40 40'><ellipse cx='20' cy='21' rx='14' ry='11' fill='%s' stroke='%s' stroke-width='2'/>"
              "<path d='M10 21 Q20 13 30 21 M11 26 Q20 19 29 26' fill='none' stroke='%s' stroke-width='2'/></svg>" % (ORANGE, NAVY, NAVY))
ICON_TAIL = ("<svg viewBox='0 0 40 40'><polygon points='6,20 34,7 34,33' fill='%s' stroke='%s' stroke-width='2'/>"
             "<line x1='6' y1='20' x2='34' y2='20' stroke='%s' stroke-width='1.5'/></svg>" % (PD, NAVY, NAVY))
ICON_UP = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(20, 35, 20, 6, TEAL, 4, 11)
ICON_DOWN = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(20, 5, 20, 35, NAVY, 4, 11)
ICON_RIGHT = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(5, 20, 35, 20, GREEN, 4, 11)
ICON_LEFT = "<svg viewBox='0 0 40 40'>%s</svg>" % arrow(35, 20, 5, 20, ORANGE, 4, 11)
ICON_CURVE_TOP = ("<svg viewBox='0 0 40 40'><path d='M4 30 Q20 2 36 30' fill='none' stroke='%s' stroke-width='3'/>"
                  "<line x1='4' y1='30' x2='36' y2='30' stroke='%s' stroke-width='2'/></svg>" % (TEAL, NAVY))
ICON_FLAT_UNDER = ("<svg viewBox='0 0 40 40'><line x1='4' y1='18' x2='36' y2='18' stroke='%s' stroke-width='3'/>%s%s%s</svg>"
                   % (NAVY, arrow(10, 36, 10, 24, ORANGE, 2, 6), arrow(20, 36, 20, 24, ORANGE, 2, 6), arrow(30, 36, 30, 24, ORANGE, 2, 6)))
ICON_FRONT_EDGE = ("<svg viewBox='0 0 40 40'><path d='M34 9 Q8 9 8 20 Q8 31 34 31' fill='none' stroke='%s' stroke-width='3'/>"
                   "<circle cx='8' cy='20' r='3' fill='%s'/></svg>" % (GOLD, ORANGE))
ICON_AIR_CORE = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='13' fill='#FFFFFF' stroke='%s' stroke-width='3'/>"
                 "<path d='M12 18 q4 -4 8 0 t8 0 M12 24 q4 -4 8 0 t8 0' fill='none' stroke='%s' stroke-width='1.5'/></svg>" % (NAVY, TEAL))
ICON_STRUT = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='14' fill='#FFFFFF' stroke='%s' stroke-width='3'/>"
              "<line x1='6' y1='20' x2='34' y2='20' stroke='%s' stroke-width='2'/><line x1='20' y1='6' x2='20' y2='34' stroke='%s' stroke-width='2'/>"
              "<line x1='10' y1='10' x2='30' y2='30' stroke='%s' stroke-width='2'/><line x1='30' y1='10' x2='10' y2='30' stroke='%s' stroke-width='2'/></svg>"
              % (NAVY, NAVY, NAVY, NAVY, NAVY))
ICON_WALL = ("<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='12' fill='none' stroke='%s' stroke-width='7'/>"
             "<circle cx='20' cy='20' r='15.5' fill='none' stroke='%s' stroke-width='1.5'/><circle cx='20' cy='20' r='8.5' fill='none' stroke='%s' stroke-width='1.5'/></svg>" % (SAND, NAVY, NAVY))
ICON_LINK = ("<svg viewBox='0 0 40 40'><circle cx='14' cy='20' r='8' fill='none' stroke='%s' stroke-width='3'/>"
             "<circle cx='26' cy='20' r='8' fill='none' stroke='%s' stroke-width='3'/></svg>" % (GOLD, GOLD))
ICON_AIR_PUSH = ("<svg viewBox='0 0 40 40'><path d='M4 14 Q20 6 36 14' fill='none' stroke='%s' stroke-width='3'/>%s</svg>" % (TEAL, arrow(20, 18, 20, 36, GOLD, 3, 8)))
ICON_DROP = "<svg viewBox='0 0 40 40'><path d='M20 5 Q34 24 20 35 Q6 24 20 5 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (TEAL, NAVY)
ICON_BIRD_DOT = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='9' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (PG, NAVY)
ICON_FEATHER = "<svg viewBox='0 0 40 40'><path d='M8 34 Q10 10 34 6 Q30 28 8 34 Z' fill='%s' stroke='%s' stroke-width='2'/><line x1='8' y1='34' x2='28' y2='12' stroke='%s' stroke-width='1.5'/></svg>" % (PG, NAVY, NAVY)

# shared shapes
TEARDROP = "M30 70 C30 30 90 25 120 40 C150 52 175 65 185 70 C175 75 150 88 120 100 C90 115 30 110 30 70 Z"
AIRFOIL = "M40,108 C45,84 90,66 150,68 C205,70 245,92 272,108 C200,112 100,114 40,108 Z"
GRID = ("<line x1='6' y1='6' x2='6' y2='6' stroke='none'/>")

