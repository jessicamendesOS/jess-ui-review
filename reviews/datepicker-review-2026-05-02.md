# DatePicker — Token & Composition Review
**Date:** 2026-05-02
**Score:** 100% · Delightful
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_DatePickerRange

---

## Fix list

**Sem findings.** Todos os critérios avaliáveis estão resolvidos.

---

## Scores

| # | Critério | Score |
|---|---|---|
| 1 | Token integrity | 🟢 Delightful |
| 2 | Scale harmony | 🟢 Delightful |
| 3 | Radius coherence | 🟢 Delightful |
| 4 | Color contract | 🟢 Delightful |
| 5 | Legibility & contrast | 🟢 Delightful |
| 6 | Composition fit | 🟢 Delightful |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | 🟢 Delightful |

**D×9 = 18 / 18 = 100% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final

**Proposed block (visual redesign):**
- `border-radius: var(--token-border-radius-300, 12px)` — surface rounder ✅
- `border: none` + `box-shadow: var(--token-elevation-2, ...)` — floating card ✅
- `width: 288px` — compact footprint ✅
- Header `color: var(--token-text-default, #242424)` — neutral (era primary blue) ✅
- Arrows `stroke: var(--token-text-subtlest, #626262)` — neutral (era primary blue) ✅
- Day cells: `aspect-ratio: 1` + flex + `line-height: var(--token-font-line-height-full, 1)` ✅
- Squircle: `var(--token-border-radius-200, 8px)` em hover/focus/today/selected/startRange/endRange ✅
- Range fill: `color-mix(in srgb, var(--token-semantics-primary-base) 12%, var(--token-bg-surface-default))` ✅
- Input: `height: var(--token-scale-900, 36px)` + `border-radius: var(--token-border-radius-200, 8px)` ✅
- Today button: outline pill com border, padding, `color: var(--token-semantics-primary-base)`, transitions ✅
- AM/PM: outline pill + `transition: background-color var(--token-duration-fast) var(--token-easing-standard)` ✅
- `@media (prefers-reduced-motion: reduce)` para Today button + AM/PM ✅

**Fixes da 2ª análise:**
- `span.flatpickr-weekday` → `var(--token-text-subtlest, #626262)` (era `--token-primitives-neutral-700`) ✅
- `.prevMonthDay/.nextMonthDay` → `var(--token-text-disabled, #a2a2a2)` / hover `var(--token-text-subtlest)` ✅
- `.hasWeeks .weeks .flatpickr-day` → `var(--token-text-default, #242424)` (era `var(--ion-color-medium)`) ✅
- Nav arrows `height/width` → `var(--token-scale-850, 34px)` ✅
- Time widget `height/line-height` (×5) → `var(--token-scale-750, 30px)` ✅
- Focus rings → `color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` ✅
- `.flatpickr-day:focus-visible border-color` → `var(--token-semantics-primary-base, #105cef)` ✅
- `.osui-monthpicker__dropdown` focus → `color-mix(...)` ✅
- `.os-high-contrast` outline/border (12 selectors) → `var(--token-semantics-primary-base, #105cef)` ✅

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 72% | 🟡 Acceptable |
| 2ª análise (final) | 100% | 🟢 Delightful |

### Pending tokens a formalizar

| Token | Valor | Situação |
|---|---|---|
| `--token-scale-750` | 30px | Em uso com fallback (time widget) — formalizar no token system |
| `--token-scale-850` | 34px | Em uso com fallback (nav arrows) — formalizar no token system |
