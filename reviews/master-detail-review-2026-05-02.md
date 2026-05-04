# Master Detail — Token & Composition Review
**Date:** 2026-05-02
**Score:** 100% · Delightful
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_MasterDetail

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
- `--osui-master-detail-background` → `var(--token-bg-surface-default, #ffffff)` ✅
- `--osui-master-detail-border-color` → `var(--token-border-default, #d5d5d5)` ✅
- `--osui-master-detail-border-radius` → `var(--token-border-radius-0, 0)` ✅ (fix: era `0` directo)
- `.split-left .list-item` padding → `var(--token-scale-300, 12px) var(--token-scale-600, 24px)` ✅
- `.list-item` transition → `background-color var(--token-duration-fast, 100ms) var(--token-easing-standard, ease)` ✅
- Chevron icon `font-size` → `var(--token-scale-400, 16px)` ✅
- Hover → `var(--token-bg-surface-hover, #f3f3f3)` ✅
- Active → `var(--token-bg-surface-active, color-mix(in srgb, var(--token-semantics-primary-base, #105cef) 8%, transparent))` ✅
- Active icon → `var(--token-semantics-primary-base, #105cef)` ✅
- `.split-right` padding → `var(--token-scale-1000, 40px)` ✅
- Border → `var(--token-border-size-025, 1px) solid var(--osui-master-detail-border-color)` ✅
- Phone slide transition → `transform var(--token-duration-fast, 100ms) var(--token-easing-standard, ease)` ✅
- Phone open transition → `transform var(--token-duration-slow, 300ms) var(--token-easing-expressive, ...)` ✅
- `.android .split-right-close top` calc offset → `var(--token-scale-250, 10px)` ✅ (fix: era `10px` hardcoded)
- Focus ring (`.has-accessible-features`) → `inset box-shadow color-mix(in srgb, var(--token-semantics-primary-base) 100%, transparent)` ✅
- `@media (prefers-reduced-motion: reduce)` cobrindo `.split-left .list-item` + `.phone .split-right` + `.phone .split-right.open` ✅

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 94% | 🟢 Delightful |
| 2ª análise (final) | 100% | 🟢 Delightful |

### Pending token a formalizar
| Token | Valor | Situação |
|---|---|---|
| `--token-scale-250` | 10px | Em uso com fallback em `.android .split-right-close` — formalizar no token system |
