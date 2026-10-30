#!/usr/bin/env python3
"""
Fix-loud patch: every concept/lab/connection page is missing any way back to
the hub (index.html). This adds:
  1. A floating "Hub" button, present on EVERY page (all 3 engines).
  2. For sequential collections (connection-*, vst-*), a "Next ->" link that
     appears once the final step's Complete/badge button is clicked, chaining
     to the next file in that collection (or back to the hub after the last).

Idempotent: safe to re-run, skips files that already have the marker.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DELIV_DIR = ROOT / "deliverables"

MARKER = "<!-- HUB-NAV-PATCH -->"

HOME_BUTTON_HTML = """<!-- HUB-NAV-PATCH -->
<a href="index.html" aria-label="Back to Sketchbook Hub" style="position:fixed;top:12px;right:12px;z-index:9999;width:44px;height:44px;border-radius:50%;background:#C9A24B;color:#071A33;display:flex;align-items:center;justify-content:center;font-size:20px;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,0.35);border:2px solid #E4C77C;">🏠</a>
"""

# ----------------------------------------------------------------------------
# Sequential collections: ordered file lists so we can compute next/prev.
# ----------------------------------------------------------------------------
CONNECTION_ORDER = [
    "connection-01-density.html",
    "connection-02-energy-transformation.html",
    "connection-03-convection.html",
    "connection-04-diffusion.html",
    "connection-05-force-balance.html",
    "connection-06-pressure.html",
    "connection-07-states-of-matter.html",
    "connection-08-exception-beats-the-rule.html",
]

VST_ORDER = [
    "vst-01-see-like-a-scientist.html",
    "vst-02-turn-things-into-pictures.html",
    "vst-03-build-your-first-model.html",
    "vst-04-find-the-hidden-connection.html",
    "vst-05-turn-pictures-into-numbers.html",
    "vst-06-make-data-tell-a-story.html",
    "vst-07-predict-before-you-calculate.html",
    "vst-08-design-the-experiment.html",
    "vst-09-break-and-repair-your-model.html",
    "vst-10-transfer-same-idea-new-world.html",
    "vst-11-representation-switching.html",
    "vst-12-explanation-lab.html",
    "vst-13-advanced-transfer.html",
    "vst-14-system-thinking.html",
    "vst-15-research-thinking.html",
    "vst-16-creative-engineering.html",
]

NEXT_LINK_SCRIPT_TEMPLATE = """
<script>
/* HUB-NAV-PATCH: inject a Next-lab / Next-map link once the final step completes */
(function(){{
  var NEXT_HREF = {next_href!r};
  var NEXT_LABEL = {next_label!r};
  function addNextLink(){{
    if(document.getElementById("hub-nav-next-link")) return;
    var footer = document.querySelector("footer");
    if(!footer) return;
    var a = document.createElement("a");
    a.id = "hub-nav-next-link";
    a.href = NEXT_HREF;
    a.textContent = NEXT_LABEL;
    a.style.cssText = "position:fixed;bottom:64px;right:12px;z-index:9999;background:#C9A24B;color:#071A33;font-weight:700;font-size:13px;padding:10px 16px;border-radius:20px;text-decoration:none;box-shadow:0 2px 8px rgba(0,0,0,0.35);";
    document.body.appendChild(a);
  }}
  var target = document.getElementById("complete-btn");
  if(target){{
    target.addEventListener("click", function(){{ setTimeout(addNextLink, 150); }});
  }}
  var badgeToast = document.getElementById("badge-toast");
  if(badgeToast){{
    var mo = new MutationObserver(function(){{
      if(badgeToast.classList.contains("show")) addNextLink();
    }});
    mo.observe(badgeToast, {{ attributes: true, attributeFilter: ["class"] }});
  }}
}})();
</script>
"""


def patch_home_button(html, path_name):
    if MARKER in html:
        return html, False
    if "<body" not in html:
        sys.exit(f"FATAL: no <body> tag found in {path_name} — cannot patch")
    # insert right after the opening <body ...> tag
    new_html = re.sub(r"(<body[^>]*>)", r"\1\n" + HOME_BUTTON_HTML, html, count=1)
    if new_html == html:
        sys.exit(f"FATAL: body-tag substitution silently failed for {path_name}")
    return new_html, True


def next_target(order_list, filename):
    idx = order_list.index(filename)
    if idx + 1 < len(order_list):
        return order_list[idx + 1], "Next Lab \u2192" if "vst" in filename else "Next Map \u2192"
    return "index.html", "Back to Hub \u2192"


NEXT_LINK_MARKER = "HUB-NAV-PATCH: inject a Next"


def patch_next_link(html, filename, order_list):
    next_href, next_label = next_target(order_list, filename)
    script = NEXT_LINK_SCRIPT_TEMPLATE.format(next_href=next_href, next_label=next_label)

    if NEXT_LINK_MARKER in html:
        # strip the previously-injected script block so we can replace it with
        # a fresh one (handles the case where the sequence order/length changed,
        # e.g. vst-10 used to be "last" and pointed to the hub, but now points
        # to vst-11 since Vol.2 was added).
        pattern = re.compile(
            r"\n<script>\n/\* " + re.escape(NEXT_LINK_MARKER) + r".*?</script>\n",
            re.DOTALL,
        )
        stripped, n = pattern.subn("", html, count=1)
        if n == 0:
            sys.exit(f"FATAL: found next-link marker text but regex failed to strip it in {filename}")
        html = stripped

    if "</body>" not in html:
        sys.exit(f"FATAL: no </body> tag found in {filename} — cannot patch next-link")
    new_html = html.replace("</body>", script + "</body>")
    return new_html, True


def main():
    if not DELIV_DIR.exists():
        sys.exit(f"FATAL: deliverables dir not found at {DELIV_DIR}")

    all_files = sorted(DELIV_DIR.glob("*.html"))
    all_files = [f for f in all_files if f.name != "index.html"]
    if not all_files:
        sys.exit("FATAL: no deliverable HTML files found to patch")

    patched_home = 0
    patched_next = 0
    for f in all_files:
        html = f.read_text(encoding="utf-8")
        html, changed = patch_home_button(html, f.name)
        if changed:
            patched_home += 1

        if f.name in CONNECTION_ORDER:
            html, nchanged = patch_next_link(html, f.name, CONNECTION_ORDER)
            if nchanged:
                patched_next += 1
        elif f.name in VST_ORDER:
            html, nchanged = patch_next_link(html, f.name, VST_ORDER)
            if nchanged:
                patched_next += 1

        f.write_text(html, encoding="utf-8")

    print(f"Home-button patch applied to {patched_home} file(s) (of {len(all_files)} total).")
    print(f"Next-link patch applied to {patched_next} sequential-collection file(s).")


if __name__ == "__main__":
    main()
