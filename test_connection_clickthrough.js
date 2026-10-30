const fs = require("fs");
const path = require("path");
const { JSDOM } = require("jsdom");

function runTest(htmlPath, label){
  const html = fs.readFileSync(htmlPath, "utf-8");
  const errors = [];
  const dom = new JSDOM(html, {
    runScripts: "dangerously",
    resources: "usable",
    pretendToBeVisual: true,
    virtualConsole: (() => {
      const { VirtualConsole } = require("jsdom");
      const vc = new VirtualConsole();
      vc.on("jsdomError", (e) => {
        const msg = e.message || "";
        const isKnownEnvGap = msg.includes("scrollTo") || msg.includes("getContext");
        if(!isKnownEnvGap) errors.push(msg);
      });
      vc.on("error", (e) => errors.push(String(e)));
      return vc;
    })()
  });
  const { window } = dom;
  window.onerror = function(msg){ errors.push("window.onerror: " + msg); };

  const doc = window.document;
  function click(el){
    if(!el){ errors.push("tried to click a null element"); return; }
    el.dispatchEvent(new window.MouseEvent("click", { bubbles: true }));
  }

  const data = window.CONCEPT_DATA;
  if(!data) errors.push("window.CONCEPT_DATA missing");

  // Step 1: Spot the Pattern — tap chain items in order
  const connectButtons = doc.querySelectorAll("#connect-chain .choice");
  if(connectButtons.length !== data.connect.items.length){
    errors.push("connect-chain button count (" + connectButtons.length + ") != items (" + data.connect.items.length + ")");
  }
  connectButtons.forEach(b => click(b));
  const connectFeedback = doc.getElementById("connect-feedback");
  if(!connectFeedback.textContent.includes("whole pattern")) errors.push("connect chain did not complete correctly");
  const connectNext = doc.getElementById("connect-next");
  if(connectNext.disabled) errors.push("connect-next still disabled after full chain tapped");
  click(connectNext);

  // Step 2: Draw — click finished, then Next
  click(doc.getElementById("draw-finished-btn"));
  const drawNext = doc.getElementById("draw-next");
  if(drawNext.disabled) errors.push("draw-next still disabled after marking finished");
  click(drawNext);

  // Step 3: Explain — click a starter chip and a keyword chip, check textarea updates
  const starterChip = doc.querySelector("#explain-starters .chip");
  const keywordChip = doc.querySelector("#explain-keywords .chip");
  click(starterChip);
  click(keywordChip);
  const explainTextEl = doc.getElementById("explain-text");
  if(!explainTextEl.value || explainTextEl.value.length < 3) errors.push("explain textarea not populated by chips");
  click(doc.getElementById("explain-next"));

  // Step 4: Transfer — click correct choice, then complete
  const transferCorrectIndex = data.transfer.choices.findIndex(c => c.correct);
  if(transferCorrectIndex === -1) errors.push("no correct transfer choice defined");
  const transferChoices = doc.querySelectorAll("#transfer-choices .choice");
  click(transferChoices[transferCorrectIndex]);
  const completeBtn = doc.getElementById("complete-btn");
  if(completeBtn.disabled) errors.push("complete-btn still disabled after correct transfer answer");
  click(completeBtn);

  // Check final state
  const xpText = doc.getElementById("xp-count").textContent;
  const progressText = doc.getElementById("progress-text").textContent;
  if(progressText !== "4 / 4 steps") errors.push("progress not 4/4, got: " + progressText);
  if(xpText !== "40 XP") errors.push("xp not 40, got: " + xpText);

  console.log("=== " + label + " ===");
  if(errors.length === 0){
    console.log("PASS — all 4 steps clicked through cleanly. Final:", xpText, progressText);
  } else {
    console.log("FAIL —", errors.length, "issue(s):");
    errors.forEach(e => console.log("  -", e));
  }
  return errors.length === 0;
}

const target = process.argv[2];
const ok = runTest(target, path.basename(target));
process.exit(ok ? 0 : 1);
