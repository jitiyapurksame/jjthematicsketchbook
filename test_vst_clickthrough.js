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
  function setValue(el, val){
    if(!el){ errors.push("tried to set value on a null element"); return; }
    el.value = val;
    el.dispatchEvent(new window.Event("input", { bubbles: true }));
  }

  const data = window.CONCEPT_DATA;
  if(!data) errors.push("window.CONCEPT_DATA missing");

  // Step 1: Notice — click correct choice, then Next
  const noticeCorrectIndex = data.notice.choices.findIndex(c => c.correct);
  if(noticeCorrectIndex === -1) errors.push("no correct notice choice defined");
  const noticeChoices = doc.querySelectorAll("#notice-choices .choice");
  click(noticeChoices[noticeCorrectIndex]);
  const noticeNext = doc.getElementById("notice-next");
  if(noticeNext.disabled) errors.push("notice-next still disabled after correct answer");
  click(noticeNext);

  // Step 2: Practice — mode-dependent
  const practiceNext = doc.getElementById("practice-next");
  if(data.practice.mode === "draw"){
    const drawBlock = doc.getElementById("practice-draw-block");
    if(drawBlock.hasAttribute("hidden")) errors.push("draw block should be visible in draw mode");
    click(doc.getElementById("draw-finished-btn"));
  } else {
    const textBlock = doc.getElementById("practice-text-block");
    if(textBlock.hasAttribute("hidden")) errors.push("text block should be visible in text mode");
    if(practiceNext.disabled) errors.push("practice-next should be enabled by default in text mode (self-paced)");
    const starterChip = doc.querySelector("#practice-starters .chip");
    if(starterChip) click(starterChip);
    const practiceTextEl = doc.getElementById("practice-text");
    if(!practiceTextEl.value || practiceTextEl.value.length < 3) errors.push("practice textarea not populated by starter chip");
  }
  if(practiceNext.disabled) errors.push("practice-next still disabled after completing practice step");
  click(practiceNext);

  // Step 3: Predict — type something, then Next (ungated)
  setValue(doc.getElementById("predict-text"), "I predict things change because of the pattern.");
  click(doc.getElementById("predict-next"));

  // Step 4: Test — click a self-check choice, then Next
  const testChoice = doc.querySelector("#test-choices .choice");
  click(testChoice);
  click(doc.getElementById("test-next"));

  // Step 5: Fix — click an error chip (gates next), type improved idea, then Next
  const fixChip = doc.querySelector("#fix-error-chips .chip");
  click(fixChip);
  const fixNext = doc.getElementById("fix-next");
  if(fixNext.disabled) errors.push("fix-next still disabled after selecting an error chip");
  setValue(doc.getElementById("fix-text"), "My better idea is to check the variable I missed.");
  click(fixNext);

  // Step 6: Level up — click a level chip, then complete
  const levelChip = doc.querySelector("#level-row .level-chip");
  click(levelChip);
  const completeBtn = doc.getElementById("complete-btn");
  if(completeBtn.disabled) errors.push("complete-btn still disabled after selecting a level");
  click(completeBtn);

  // Check final state
  const xpText = doc.getElementById("xp-count").textContent;
  const progressText = doc.getElementById("progress-text").textContent;
  if(progressText !== "6 / 6 steps") errors.push("progress not 6/6, got: " + progressText);
  if(xpText !== "60 XP") errors.push("xp not 60, got: " + xpText);

  console.log("=== " + label + " (practice mode: " + data.practice.mode + ") ===");
  if(errors.length === 0){
    console.log("PASS — all 6 steps clicked through cleanly. Final:", xpText, progressText);
  } else {
    console.log("FAIL —", errors.length, "issue(s):");
    errors.forEach(e => console.log("  -", e));
  }
  return errors.length === 0;
}

const target = process.argv[2];
const ok = runTest(target, path.basename(target));
process.exit(ok ? 0 : 1);
