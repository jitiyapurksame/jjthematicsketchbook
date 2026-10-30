const fs = require("fs");
const { JSDOM } = require("jsdom");

function makeDom(html, presetLocalStorage){
  const errors = [];
  const { VirtualConsole } = require("jsdom");
  const vc = new VirtualConsole();
  vc.on("jsdomError", (e) => {
    const msg = e.message || "";
    if(!msg.includes("scrollTo") && !msg.includes("getContext")) errors.push(msg);
  });
  const dom = new JSDOM(html, { runScripts: "outside-only", url: "https://example.com/", virtualConsole: vc, resources: "usable" });
  const { window } = dom;
  window.onerror = (msg) => errors.push("window.onerror: " + msg);

  if(presetLocalStorage){
    Object.keys(presetLocalStorage).forEach(k => window.localStorage.setItem(k, presetLocalStorage[k]));
  }

  const scriptText = fs.readFileSync("index.html", "utf-8").match(/<script>([\s\S]*?)<\/script>/)[1];
  window.eval(scriptText);
  return { window, doc: window.document, errors };
}

const html = fs.readFileSync("index.html", "utf-8");

// ---- Test 1: no progress yet ----
{
  const { doc, errors } = makeDom(html, null);
  const totalXp = doc.getElementById("total-xp").textContent;
  const totalDone = doc.getElementById("total-done").textContent;
  const books = doc.querySelectorAll(".book");
  console.log("=== Test 1: fresh state ===");
  console.log("books rendered:", books.length, "(expect 7)");
  console.log("total XP:", totalXp, "total done:", totalDone, "(expect 0, 0)");
  const lockedBooks = doc.querySelectorAll(".book.locked").length;
  console.log("locked books:", lockedBooks, "(expect 4: ocean, mario, cooking, connections, vst = 5 actually)");
  const titanicLinks = doc.querySelectorAll(".concept-list a");
  console.log("clickable titanic links:", titanicLinks.length, "(expect 4)");
  const titanicLockedRows = doc.querySelectorAll(".locked-row");
  console.log("titanic locked rows:", titanicLockedRows.length, "(expect 8)");
  console.log(errors.length === 0 ? "PASS (no errors)" : "FAIL: " + errors.join(" | "));
}

// ---- Test 2: some progress simulated ----
{
  const preset = {
    "sketchbook-progress::titanic-01-side-view": JSON.stringify({ completed:["observe","label","draw","rotate","compare","connect","explain","predict"], xp: 80 }),
    "sketchbook-progress::titanic-02-top-view": JSON.stringify({ completed:["observe","label"], xp: 20 })
  };
  const { doc, errors } = makeDom(html, preset);
  const totalXp = doc.getElementById("total-xp").textContent;
  const totalDone = doc.getElementById("total-done").textContent;
  console.log("=== Test 2: with progress ===");
  console.log("total XP:", totalXp, "(expect 100)");
  console.log("total done:", totalDone, "(expect 1)");
  const statusIcons = Array.from(doc.querySelectorAll(".concept-list .status")).map(s => s.textContent);
  console.log("status icons for titanic 1-4:", statusIcons.join(" "), "(expect done, inprogress/partial, not-started, not-started)");
  console.log(errors.length === 0 ? "PASS (no errors)" : "FAIL: " + errors.join(" | "));
}
