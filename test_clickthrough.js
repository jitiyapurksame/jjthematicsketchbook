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

  function click(el){ el.dispatchEvent(new window.MouseEvent("click", { bubbles: true })); }

  // Mission 1: Observe — click the correct choice, then Next
  const observeChoices = doc.querySelectorAll("#observe-choices .choice");
  const observeCorrect = Array.from(observeChoices).find(b => b.classList.contains("choice") && false); // placeholder
  // find correct by checking CONCEPT_DATA order
  const data = window.CONCEPT_DATA;
  const observeCorrectIndex = data.observe.choices.findIndex(c => c.correct);
  click(observeChoices[observeCorrectIndex]);
  const observeNext = doc.getElementById("observe-next");
  if(observeNext.disabled) errors.push("observe-next still disabled after correct answer");
  click(observeNext);

  // Mission 2: Label — match all pairs in correct order
  const items = data.label.items;
  items.forEach(item => {
    const picBtn = Array.from(doc.querySelectorAll(".match-picture")).find(b => b.dataset.id === item.id);
    click(picBtn);
    const nameBtn = Array.from(doc.querySelectorAll(".match-name")).find(b => b.dataset.id === item.id);
    click(nameBtn);
  });
  const labelNext = doc.getElementById("label-next");
  if(labelNext.disabled) errors.push("label-next still disabled after all matches made");
  click(labelNext);

  // Mission 3: Draw — click finished, then Next
  click(doc.getElementById("draw-finished-btn"));
  const drawNext = doc.getElementById("draw-next");
  if(drawNext.disabled) errors.push("draw-next still disabled after marking finished");
  click(drawNext);

  // Mission 4: Rotate — rotate then Next
  click(doc.getElementById("rotate-right"));
  const rotateNextBtn = Array.from(doc.querySelectorAll('[data-mission="rotate"] .next-mission'))[0];
  click(rotateNextBtn);

  // Mission 5: Compare — click correct picture, then Next
  const compareCorrectIndex = data.compare.choices.findIndex(c => c.correct);
  const compareChoices = doc.querySelectorAll("#compare-choices .choice");
  click(compareChoices[compareCorrectIndex]);
  const compareNext = doc.getElementById("compare-next");
  if(compareNext.disabled) errors.push("compare-next still disabled after correct picture");
  click(compareNext);

  // Mission 6: Connect — tap chain in order, then Next
  const connectButtons = doc.querySelectorAll("#connect-chain .choice");
  connectButtons.forEach(b => click(b));
  const connectFeedback = doc.getElementById("connect-feedback");
  if(!connectFeedback.textContent.includes("whole chain")) errors.push("connect chain did not complete correctly");
  const connectNextBtn = Array.from(doc.querySelectorAll('[data-mission="connect"] .next-mission'))[0];
  click(connectNextBtn);

  // Mission 7: Explain — click a starter chip and a keyword chip, check textarea updates
  const starterChip = doc.querySelector("#explain-starters .chip");
  const keywordChip = doc.querySelector("#explain-keywords .chip");
  click(starterChip);
  click(keywordChip);
  const explainTextEl = doc.getElementById("explain-text");
  if(!explainTextEl.value || explainTextEl.value.length < 3) errors.push("explain textarea not populated by chips");
  click(doc.getElementById("explain-next"));

  // Mission 8: Predict — click correct choice, then complete
  const predictCorrectIndex = data.predict.choices.findIndex(c => c.correct);
  const predictChoices = doc.querySelectorAll("#predict-choices .choice");
  click(predictChoices[predictCorrectIndex]);
  const completeBtn = doc.getElementById("complete-btn");
  if(completeBtn.disabled) errors.push("complete-btn still disabled after correct prediction");
  click(completeBtn);

  // Check final state
  const xpText = doc.getElementById("xp-count").textContent;
  const progressText = doc.getElementById("progress-text").textContent;
  if(progressText !== "8 / 8 missions") errors.push("progress not 8/8, got: " + progressText);
  if(xpText !== "80 XP") errors.push("xp not 80, got: " + xpText);

  console.log("=== " + label + " ===");
  if(errors.length === 0){
    console.log("PASS — all 8 missions clicked through cleanly. Final:", xpText, progressText);
  } else {
    console.log("FAIL —", errors.length, "issue(s):");
    errors.forEach(e => console.log("  -", e));
  }
  return errors.length === 0;
}

const target = process.argv[2];
runTest(target, path.basename(target));
