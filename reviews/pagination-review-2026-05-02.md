# Pagination — Token & Composition Review
**Date:** 2026-05-02
**Score:** 100% · Delightful
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Pagination

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
- `--osui-pagination-button-background` → `transparent` (CSS keyword) ✅
- `--osui-pagination-button-border-color` → `transparent` ✅
- `--osui-pagination-button-border-width` → `var(--token-border-size-025, 1px)` ✅
- `--osui-pagination-button-color` → `var(--token-text-default, #242424)` ✅
- `--osui-pagination-button-font-weight` → `var(--token-font-weight-medium, 500)` ✅
- `--osui-pagination-button-hover-background` → `var(--token-bg-surface-hover, #f3f3f3)` ✅
- `--osui-pagination-button-size` → `var(--token-scale-900, 36px)` ✅
- `--osui-pagination-active-border-color` → `var(--token-border-default, #d5d5d5)` ✅
- `--osui-pagination-active-color` → `var(--token-text-default, #242424)` ✅
- `--osui-pagination-counter-color` → `var(--token-text-subtlest, #626262)` ✅
- `border-radius` → `var(--token-border-radius-200, 8px)` ✅
- `margin-left` → `var(--token-scale-100, 4px)` ✅
- `margin-top` → `var(--token-scale-600, 24px)` ✅
- `transition` → `background-color + border-color var(--token-duration-fast) var(--token-easing-standard)` ✅
- Tablet/phone size → `var(--token-scale-1000, 40px)` ✅
- `opacity` disabled → `var(--token-opacity-disabled, 0.5)` ✅ (fix: era `0.5` hardcoded)
- Focus ring → `border-color: var(--token-semantics-primary-base)` + `box-shadow: 0 0 0 var(--token-border-size-075, 3px) color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` ✅ (fix: `3px` era hardcoded)
- High-contrast → `outline: var(--token-border-size-075...) solid var(--token-semantics-primary-base, #105cef)` ✅
- `@media (prefers-reduced-motion: reduce)` cobrindo `.pagination-button` ✅

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 94% | 🟢 Delightful |
| 2ª análise (final) | 100% | 🟢 Delightful |

### Pending token a formalizar
| Token | Valor | Situação |
|---|---|---|
| `--token-opacity-disabled` | 0.5 | Em uso com fallback — formalizar no token system |
