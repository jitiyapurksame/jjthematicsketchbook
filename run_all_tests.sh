#!/usr/bin/env bash
# Run from the project root (the folder containing deliverables/ and build-tools/):
#   bash build-tools/run_all_tests.sh
# Requires: python3, node, and `cd build-tools && npm install` once (installs jsdom).
set -u
cd "$(dirname "$0")/.."

fail_total=0

echo "== 1/3  Syntax check (every non-hub page) =="
syn_fail=0
for f in deliverables/*.html; do
  case "$f" in */index.html) continue;; esac
  python3 - "$f" <<'PY'
import re, sys
h = open(sys.argv[1], encoding="utf-8").read()
open("/tmp/_syn.js", "w", encoding="utf-8").write("\n".join(re.findall(r"<script>(.*?)</script>", h, re.S)))
PY
  node --check /tmp/_syn.js >/dev/null 2>&1 || { echo "  FAIL: $f"; syn_fail=$((syn_fail+1)); }
done
echo "  syntax failures: $syn_fail"
fail_total=$((fail_total+syn_fail))

echo "== 2/3  Click-through: 8-mission books (titanic/ocean/mario/cooking/birds/cars) =="
p=0; q=0
for f in deliverables/titanic-*.html deliverables/ocean-*.html deliverables/mario-*.html deliverables/cooking-*.html deliverables/birds-*.html deliverables/cars-*.html; do
  [ -e "$f" ] || continue
  if node build-tools/test_clickthrough.js "$f" >/tmp/_ct.log 2>&1; then p=$((p+1)); else q=$((q+1)); echo "  FAIL: $f"; head -4 /tmp/_ct.log; fi
done
echo "  pass=$p fail=$q"
fail_total=$((fail_total+q))

echo "== 3/3  Click-through: Connections (4-step) + VST (6-step) =="
p=0; q=0
for f in deliverables/connection-*.html; do
  [ -e "$f" ] || continue
  if node build-tools/test_connection_clickthrough.js "$f" >/tmp/_ct.log 2>&1; then p=$((p+1)); else q=$((q+1)); echo "  FAIL: $f"; head -4 /tmp/_ct.log; fi
done
for f in deliverables/vst-*.html; do
  [ -e "$f" ] || continue
  if node build-tools/test_vst_clickthrough.js "$f" >/tmp/_ct.log 2>&1; then p=$((p+1)); else q=$((q+1)); echo "  FAIL: $f"; head -4 /tmp/_ct.log; fi
done
echo "  pass=$p fail=$q"
fail_total=$((fail_total+q))

echo
if [ "$fail_total" -eq 0 ]; then echo "ALL GREEN"; else echo "$fail_total FAILURE(S)"; exit 1; fi
