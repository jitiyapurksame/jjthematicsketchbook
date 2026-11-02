"""Shared helpers for the Beetles & Buses book (beetle(), cyl(), fan(), finned(), car_box(), icons...).
Imported by build_cars_batch2.py. (batch1 still carries its own copy.)

Original batch-1 note: Beetles & Buses, pages 1-4. Run: python3 build-tools/build_cars_batch1.py
Uses shared helpers from birds_common.py (build, check, svg, txt, arrow, colours, icons).
Writes cars-0N-*.html into ../deliverables."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from birds_common import *  # noqa: F401,F403

BLUE = "#CFE3EE"; BODY = "#6BB0C9"

# ---------------- drawing helpers ----------------
def beetle(dot=False, marks=False):
    """VW Beetle facing RIGHT. Occupies x 30..282, y 44..160."""
    s = ("<path d='M36,134 C30,110 50,88 84,70 C112,52 150,44 176,56 C196,64 210,84 232,94 C250,100 270,104 278,118 C282,126 280,134 272,136 L36,134 Z' "
         "fill='%s' stroke='%s' stroke-width='2.5'/>" % (BODY, NAVY)
         + "<path d='M96,86 C110,68 142,58 164,64 C178,72 192,82 200,92 L96,92 Z' fill='%s' stroke='%s' stroke-width='2'/>" % (BLUE, NAVY)
         + "<line x1='150' y1='92' x2='150' y2='126' stroke='%s' stroke-width='1.5'/>" % NAVY
         + "<circle cx='271' cy='116' r='6' fill='%s' stroke='%s' stroke-width='1.5'/>" % (GOLD, NAVY)
         + "<circle cx='88' cy='136' r='22' fill='%s'/><circle cx='88' cy='136' r='9' fill='%s' stroke='%s' stroke-width='1.5'/>" % (NAVY, SAND, NAVY)
         + "<circle cx='224' cy='136' r='22' fill='%s'/><circle cx='224' cy='136' r='9' fill='%s' stroke='%s' stroke-width='1.5'/>" % (NAVY, SAND, NAVY))
    if dot:
        s += "<circle cx='56' cy='112' r='10' fill='%s' stroke='%s' stroke-width='2'/>" % (ORANGE, NAVY)
    if marks:
        s += ("<circle cx='252' cy='86' r='12' fill='#FFFFFF' stroke='%s' stroke-width='2'/>" % NAVY + txt(252, 91, "A", 14, NAVY, "middle", "bold")
              + "<circle cx='52' cy='96' r='12' fill='#FFFFFF' stroke='%s' stroke-width='2'/>" % NAVY + txt(52, 101, "B", 14, NAVY, "middle", "bold"))
    return s


def beetle_at(scale, tx, ty, **kw):
    return "<g transform='translate(%g,%g) scale(%s)'>%s</g>" % (tx, ty, scale, beetle(**kw))


def cyl(x, piston_y, gas, direction=None, spark=False):
    """Small piston-in-cylinder drawing, 50 wide, cylinder top y=30, open bottom y=140."""
    top, bot, w = 30, 140, 50
    cx = x + w / 2
    s = "<rect x='%g' y='%g' width='%g' height='%g' fill='%s'/>" % (x + 2, top + 2, w - 4, piston_y - top - 2, gas)
    s += "<path d='M%g %g V%g H%g V%g' fill='none' stroke='%s' stroke-width='3'/>" % (x, bot, top, x + w, bot, NAVY)
    s += "<rect x='%g' y='%g' width='%g' height='12' fill='%s' stroke='%s' stroke-width='2'/>" % (x + 2, piston_y, w - 4, PG, NAVY)
    s += "<line x1='%g' y1='%g' x2='%g' y2='%g' stroke='%s' stroke-width='3'/>" % (cx, piston_y + 12, cx, bot + 8, NAVY)
    if spark:
        s += "<polygon points='%g,%g %g,%g %g,%g %g,%g %g,%g %g,%g' fill='%s' stroke='%s' stroke-width='1'/>" % (
            cx + 2, top + 4, cx - 6, top + 16, cx - 1, top + 16, cx - 4, top + 26, cx + 6, top + 12, cx + 1, top + 12, GOLD, NAVY)
    if direction == "down":
        s += arrow(cx, piston_y + 20, cx, piston_y + 42, ORANGE, 3, 8)
    elif direction == "up":
        s += arrow(cx, piston_y + 42, cx, piston_y + 20, ORANGE, 3, 8)
    return s


def fan(cx, cy, r, color=TEAL):
    blades = "".join("<ellipse cx='%g' cy='%g' rx='%g' ry='%g' fill='%s' stroke='%s' stroke-width='1.5' transform='rotate(%d %g %g)'/>" % (
        cx, cy - r * 0.55, r * 0.28, r * 0.5, color, NAVY, a, cx, cy) for a in (0, 90, 180, 270))
    return blades + "<circle cx='%g' cy='%g' r='%g' fill='%s' stroke='%s' stroke-width='1.5'/>" % (cx, cy, r * 0.16, GOLD, NAVY)


def finned(x, y, w, h, n, hot="#E39A7F"):
    s = "<rect x='%g' y='%g' width='%g' height='%g' fill='%s' stroke='%s' stroke-width='2'/>" % (x, y, w, h, hot, NAVY)
    step = h / float(n)
    for i in range(n):
        s += "<rect x='%g' y='%g' width='%g' height='%g' fill='%s' stroke='%s' stroke-width='1.5'/>" % (x - 8, y + i * step + step * 0.25, w + 16, step * 0.45, PD, NAVY)
    return s


def car_box(cx, cy, w=50, h=26):
    return ("<rect x='%g' y='%g' width='%g' height='%g' rx='6' fill='%s' stroke='%s' stroke-width='2'/>" % (cx - w / 2, cy - h / 2, w, h, BODY, NAVY)
            + "<circle cx='%g' cy='%g' r='6' fill='%s'/><circle cx='%g' cy='%g' r='6' fill='%s'/>" % (cx - w / 3, cy + h / 2, NAVY, cx + w / 3, cy + h / 2, NAVY))


# ---------------- icons ----------------
ICON_ENGINE = ("<svg viewBox='0 0 40 40'><rect x='6' y='12' width='28' height='20' rx='3' fill='%s' stroke='%s' stroke-width='2'/>"
               "<rect x='12' y='6' width='6' height='8' fill='%s' stroke='%s' stroke-width='1.5'/><rect x='22' y='6' width='6' height='8' fill='%s' stroke='%s' stroke-width='1.5'/></svg>" % (PD, NAVY, PD, NAVY, PD, NAVY))
ICON_TRUNK = ("<svg viewBox='0 0 40 40'><rect x='6' y='14' width='28' height='20' rx='3' fill='%s' stroke='%s' stroke-width='2'/>"
              "<path d='M15 14 V9 H25 V14' fill='none' stroke='%s' stroke-width='2'/></svg>" % (GOLD, NAVY, NAVY))
ICON_ROUND = "<svg viewBox='0 0 40 40'><path d='M6 30 C6 14 18 6 26 8 C34 10 36 24 36 30 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (BODY, NAVY)
ICON_PISTON = ("<svg viewBox='0 0 40 40'><path d='M9 4 V36 M31 4 V36 M9 4 H31' fill='none' stroke='%s' stroke-width='2.5'/>"
               "<rect x='11' y='16' width='18' height='8' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (NAVY, PG, NAVY))
ICON_SPARK = "<svg viewBox='0 0 40 40'><polygon points='22,3 10,22 19,22 15,37 30,16 21,16' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (GOLD, NAVY)
ICON_HOTGAS = ("<svg viewBox='0 0 40 40'><path d='M20 6 Q32 16 28 28 Q24 36 20 34 Q12 36 11 26 Q10 16 20 6 Z' fill='%s' stroke='%s' stroke-width='2'/></svg>" % (ORANGE, NAVY))
ICON_FIN = "<svg viewBox='0 0 40 40'><rect x='14' y='4' width='12' height='32' fill='#E39A7F' stroke='%s' stroke-width='2'/>%s</svg>" % (
    NAVY, "".join("<rect x='6' y='%d' width='28' height='3.5' fill='%s' stroke='%s' stroke-width='1'/>" % (7 + i * 7, PD, NAVY) for i in range(4)))
ICON_FAN = "<svg viewBox='0 0 40 40'>%s</svg>" % fan(20, 20, 17)
ICON_RADIATOR = ("<svg viewBox='0 0 40 40'><rect x='8' y='6' width='24' height='28' fill='#FFFFFF' stroke='%s' stroke-width='2'/>%s</svg>" %
                 (NAVY, "".join("<line x1='11' y1='%d' x2='29' y2='%d' stroke='%s' stroke-width='2'/>" % (11 + i * 5, 11 + i * 5, TEAL) for i in range(5))))
ICON_CAR_DOT = "<svg viewBox='0 0 40 40'><rect x='5' y='13' width='30' height='16' rx='5' fill='%s' stroke='%s' stroke-width='2'/><circle cx='13' cy='30' r='4' fill='%s'/><circle cx='28' cy='30' r='4' fill='%s'/></svg>" % (BODY, NAVY, NAVY, NAVY)
ICON_TYRE = "<svg viewBox='0 0 40 40'><circle cx='20' cy='20' r='15' fill='%s'/><circle cx='20' cy='20' r='6' fill='%s' stroke='%s' stroke-width='1.5'/></svg>" % (NAVY, SAND, NAVY)
ICON_HEATWAVE = ICON_HEAT = ("<svg viewBox='0 0 40 40'><path d='M10 34 q6 -10 0 -20 M20 34 q6 -10 0 -20 M30 34 q6 -10 0 -20' fill='none' stroke='%s' stroke-width='3' stroke-linecap='round'/></svg>" % ORANGE)


def force_arrows(cx, cy, up, down, right, left, labels=True, size=12, w=4):
    """Four arrows leaving (cx, cy). Lengths given per direction."""
    s = (arrow(cx, cy - 12, cx, cy - 12 - up, TEAL, w, 11) + arrow(cx, cy + 12, cx, cy + 12 + down, NAVY, w, 11)
         + arrow(cx + 26, cy, cx + 26 + right, cy, GREEN, w, 11) + arrow(cx - 26, cy, cx - 26 - left, cy, ORANGE, w, 11))
    if labels:
        s += (txt(cx + 8, cy - 12 - up + 10, "Road push", size, TEAL, "start", "bold") + txt(cx + 8, cy + 12 + down, "Weight", size, NAVY, "start", "bold")
              + txt(cx + 26, cy - 8, "Drive", size, GREEN, "start", "bold") + txt(cx - 26 - left, cy - 8, "Drag", size, ORANGE, "start", "bold"))
    return s


