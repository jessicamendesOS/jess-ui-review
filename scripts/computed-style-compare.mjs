/**
 * Proposed mode: measure target elements on isolated *-tokens.html vs form-tokens.html
 * Run: LAB_BASE=http://127.0.0.1:8765 node scripts/computed-style-compare.mjs
 * (http.server must be running in project root)
 */
import { chromium } from "playwright";

const BASE = process.env.LAB_BASE || "http://127.0.0.1:8765";

const PROPS = [
  "width",
  "height",
  "border-radius",
  "background",
  "background-color",
  "box-sizing",
];

const CONFIG = {
  input: {
    file: "input-tokens.html",
    sel: "input#inp1",
  },
  textarea: { file: "textarea-tokens.html", sel: "textarea#ta1" },
  dropdown: {
    file: "dropdown-tokens.html",
    sel: "div.dropdown-display.annotate-display",
  },
  button: {
    file: "button-tokens.html",
    sel: "button.annotate-primary",
  },
  checkbox: { file: "checkbox-tokens.html", sel: "input#cb1" },
  switch: { file: "switch-tokens.html", sel: "input#sw2" },
  /* No .annotate-dot — compare OSUI-only radio */
  radio: { file: "radio-tokens.html", sel: "input#rg2-0" },
};

const FORM = {
  /* Full-width field like input lab preview width context */
  input: "input#fm-email",
  textarea: "textarea#fm-bio",
  dropdown: "form .dropdown-container .dropdown-display",
  button: "form[data-form] button.btn.btn-primary",
  checkbox: "input#fm-terms",
  switch: "input#fm-notify",
  radio: "input#fm-role-0",
};

async function measure(page, file, targetSelector) {
  await page.goto(`${BASE}/${file}`, { waitUntil: "networkidle" });
  await page.locator("button.ptab:has-text('Proposed')").first().click();
  await page.waitForTimeout(200);
  return page.evaluate((targetSelector) => {
    const PROPS = [
      "width",
      "height",
      "border-radius",
      "background",
      "background-color",
      "box-sizing",
    ];
    function collectMatchingStyleRules(element) {
      const out = [];
      const tryPush = (rule) => {
        if (!rule.selectorText) return;
        for (const part of rule.selectorText.split(",")) {
          const sel = part.trim();
          try {
            if (element.matches(sel)) {
              out.push({
                href:
                  (rule.parentStyleSheet && rule.parentStyleSheet.href) ||
                  "(inline)",
                selector: rule.selectorText,
                css: rule.cssText,
              });
              return;
            }
          } catch (e) {}
        }
      };
      const walk = (sheet) => {
        let list;
        try {
          list = sheet.cssRules;
        } catch (e) {
          return;
        }
        for (let i = 0; i < list.length; i++) {
          const r = list[i];
          if (r.type === CSSRule.IMPORT_RULE) {
            if (r.styleSheet) walk(r.styleSheet);
            continue;
          }
          if (r.type === CSSRule.MEDIA_RULE) {
            try {
              if (matchMedia(r.media.mediaText).matches) {
                for (let j = 0; j < r.cssRules.length; j++) {
                  const r2 = r.cssRules[j];
                  if (r2.type === CSSRule.STYLE_RULE) tryPush(r2);
                }
              }
            } catch (e) {}
            continue;
          }
          if (r.type === CSSRule.STYLE_RULE) tryPush(r);
        }
      };
      for (const sheet of document.styleSheets) {
        try {
          walk(sheet);
        } catch (e) {}
      }
      return out;
    }
    function collectPseudoStyleRules(element, pseudo) {
      const needle = pseudo === "before" ? /::before/i : /::after/i;
      const out = [];
      const tryRule = (rule) => {
        if (rule.type !== CSSRule.STYLE_RULE || !rule.selectorText) return;
        if (!needle.test(rule.selectorText)) return;
        for (const part of rule.selectorText.split(",")) {
          const sel = part.trim();
          const m = sel.match(/^(.*)(::before|::after)$/i);
          if (!m) continue;
          const host = m[1].trim();
          if (!host) continue;
          try {
            if (element.matches(host)) {
              out.push({
                href:
                  (rule.parentStyleSheet && rule.parentStyleSheet.href) ||
                  "(inline)",
                selector: rule.selectorText,
                css: rule.cssText,
              });
              return;
            }
          } catch (e) {}
        }
      };
      const walk = (sheet) => {
        let list;
        try {
          list = sheet.cssRules;
        } catch (e) {
          return;
        }
        for (let i = 0; i < list.length; i++) {
          const r = list[i];
          if (r.type === CSSRule.IMPORT_RULE) {
            if (r.styleSheet) walk(r.styleSheet);
            continue;
          }
          if (r.type === CSSRule.MEDIA_RULE) {
            try {
              if (matchMedia(r.media.mediaText).matches) {
                for (let j = 0; j < r.cssRules.length; j++)
                  tryRule(r.cssRules[j]);
              }
            } catch (e) {}
            continue;
          }
          tryRule(r);
        }
      };
      for (const sheet of document.styleSheets) {
        try {
          walk(sheet);
        } catch (e) {}
      }
      return out;
    }
    const T = targetSelector
      .split(",")
      .map((s) => s.trim())
      .map((s) => document.querySelector(s))
      .find(Boolean);
    if (!T) return { err: "no element: " + targetSelector };
    const snap = (pseudo) => {
      const p = pseudo || undefined;
      const cs = getComputedStyle(T, p);
      const o = { pseudo: pseudo || "element" };
      for (const pr of PROPS) o[pr] = cs.getPropertyValue(pr);
      if (pseudo) o.content = cs.getPropertyValue("content");
      return o;
    };
    return {
      el:
        T.tagName.toLowerCase() +
        (T.id ? "#" + T.id : "") +
        (T.className
          ? "." +
            String(T.className)
              .split(" ")
              .filter(Boolean)
              .slice(0, 3)
              .join(".")
          : ""),
      main: snap(),
      before: snap("::before"),
      after: snap("::after"),
      mainRules: collectMatchingStyleRules(T),
      beforeRules: collectPseudoStyleRules(T, "before"),
      afterRules: collectPseudoStyleRules(T, "after"),
    };
  }, targetSelector);
}

function diffSnapshots(a, b) {
  const keys = ["main", "before", "after"];
  const d = [];
  for (const k of keys) {
    if (!a[k] || !b[k]) continue;
    for (const p of [...PROPS, "content"].filter(
      (x) => x === "content" ? k !== "main" : true
    )) {
      const av = a[k][p] || "";
      const bv = b[k][p] || "";
      if (av !== bv) {
        d.push({ layer: k, prop: p, isolated: av.trim(), form: bv.trim() });
      }
    }
  }
  return d;
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  const out = { meta: { base: BASE }, components: {} };

  for (const [name, { file, sel }] of Object.entries(CONFIG)) {
    const iso = await measure(page, file, sel);
    const f = await measure(page, "form-tokens.html", FORM[name]);
    out.components[name] = {
      isolated: iso,
      form: f,
      diff: !iso.err && !f.err ? diffSnapshots(iso, f) : { error: iso.err || f.err },
    };
  }

  console.log(JSON.stringify(out, null, 2));
  await browser.close();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
