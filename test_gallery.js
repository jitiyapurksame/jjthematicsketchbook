const fs = require("fs");
const { JSDOM } = require("jsdom");

function makeDom(presetLocalStorage){
  const html = fs.readFileSync("sketchbook-gallery.html", "utf-8");
  const errors = [];
  const { VirtualConsole } = require("jsdom");
  const vc = new VirtualConsole();
  vc.on("jsdomError", (e) => {
    const msg = e.message || "";
    if(!msg.includes("scrollTo") && !msg.includes("getContext")) errors.push(msg);
  });
  const dom = new JSDOM(html, { runScripts: "outside-only", resources: "usable", url: "https://example.com/", virtualConsole: vc });
  const { window } = dom;
  window.onerror = (msg) => errors.push("window.onerror: " + msg);
  if(presetLocalStorage){
    Object.keys(presetLocalStorage).forEach(k => window.localStorage.setItem(k, presetLocalStorage[k]));
  }
  const scriptText = html.match(/<script>([\s\S]*?)<\/script>/)[1];
  window.eval(scriptText);
  return { window, doc: window.document, errors };
}

// tiny 1x1 png as a stand-in data URL
const FAKE_PNG = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=";

// ---- Test 1: empty state ----
{
  const { doc, errors } = makeDom(null);
  const countLabel = doc.getElementById("count-label").textContent;
  const hasEmptyState = !!doc.querySelector(".empty-state");
  console.log("=== Test 1: empty gallery ===");
  console.log("count label:", countLabel);
  console.log("shows empty state:", hasEmptyState);
  console.log(errors.length === 0 ? "PASS" : "FAIL: " + errors.join(" | "));
}

// ---- Test 2: two saved drawings ----
{
  const preset = {
    "sketchbook-gallery::titanic-01-side-view": JSON.stringify({ conceptId:"titanic-01-side-view", title:"Titanic: Side View", dataUrl: FAKE_PNG, savedAt: "2026-08-10T10:00:00.000Z" }),
    "sketchbook-gallery::titanic-03-cross-section": JSON.stringify({ conceptId:"titanic-03-cross-section", title:"Titanic: Cross Section ⭐", dataUrl: FAKE_PNG, savedAt: "2026-08-12T09:30:00.000Z" }),
    "sketchbook-progress::titanic-01-side-view": JSON.stringify({ completed: ["observe"], xp: 10 }) // unrelated key, should be ignored
  };
  const { doc, errors } = makeDom(preset);
  const cards = doc.querySelectorAll(".card");
  const countLabel = doc.getElementById("count-label").textContent;
  const firstTitle = doc.querySelector(".card-title").textContent;
  const exportLinks = doc.querySelectorAll(".card-actions a");
  console.log("=== Test 2: two drawings ===");
  console.log("cards rendered:", cards.length, "(expect 2)");
  console.log("count label:", countLabel);
  console.log("most recent first:", firstTitle, "(expect Cross Section, since it was saved later)");
  console.log("export links:", exportLinks.length, "(expect 2)");
  console.log("export link 1 download attr:", exportLinks[0].getAttribute("download"));
  console.log(errors.length === 0 ? "PASS" : "FAIL: " + errors.join(" | "));
}
