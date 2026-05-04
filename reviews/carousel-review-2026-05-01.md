# Carousel — Token & Composition Review
**Date:** 2026-05-01
**Score:** 81% · Acceptable
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Carousel

---

## Fix list

### 🟡 Acceptable

| Selector | Propriedade | Actual | → Mudar para | Porquê |
|---|---|---|---|---|
| `.osui-carousel` (linha 54787) | `--osui-carousel-pagination-rest-color` | `var(--token-border-default, #d5d5d5)` | `var(--token-bg-neutral-subtle, #d5d5d5)` (pending) | Token de border usado para cor de indicador — semantic mismatch |
| `.osui-carousel` (linha 54785) | `--osui-carousel-arrow-size` | `38px` | `var(--token-scale-950, 38px)` (pending) | Sem token de escala correspondente — formalizar `--token-scale-950` |
| `.osui-carousel` (linha 54789) | `--osui-carousel-pagination-margin` | `30px` | `var(--token-scale-750, 30px)` (pending) | Sem token de escala correspondente — formalizar `--token-scale-750` |

### 🔵 Pending tokens a formalizar

| Token | Valor | Situação |
|---|---|---|
| `--token-scale-750` | 30px | Em uso hardcoded em `--osui-carousel-pagination-margin` |
| `--token-scale-950` | 38px | Em uso hardcoded em `--osui-carousel-arrow-size` |
| `--token-bg-neutral-subtle` | `#d5d5d5` | Pending — substituir `--token-border-default` usado como cor de indicador |

---

## Scores

| # | Critério | Score |
|---|---|---|
| 1 | Token integrity | 🟡 Acceptable |
| 2 | Scale harmony | 🟡 Acceptable |
| 3 | Radius coherence | 🟢 Delightful |
| 4 | Color contract | 🟡 Acceptable |
| 5 | Legibility & contrast | 🟢 Delightful |
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | 🟢 Delightful |

**D×5 + A×3 = 10 + 3 = 13 / 16 = 81% · Acceptable**

---

## Notas de sessão

### O que estava resolvido na versão final
- `--osui-carousel-arrow-background` → `var(--token-bg-surface-default, #ffffff)` ✅
- `--osui-carousel-arrow-shadow` → `var(--token-elevation-2, ...)` ✅
- `--osui-carousel-arrow-icon-color` → `var(--token-text-default, #242424)` ✅
- `--osui-carousel-pagination-active-color` → `var(--token-semantics-primary-base, #105cef)` ✅
- Arrow `transition` → `opacity var(--token-duration-fast, 100ms) var(--token-easing-standard, ease)` ✅
- Arrow SVG `height/width` → `var(--token-scale-500, 20px)` ✅
- Pagination gap → `var(--token-scale-150, 6px)` ✅
- Pagination dot `height/width` → `var(--token-scale-200, 8px)` ✅
- Active pagination `width` → `var(--token-scale-700, 28px)` ✅
- Active pagination `border-radius` → `var(--token-border-radius-100, 4px)` ✅
- Pagination transition → `width/border-radius var(--token-duration-moderate, 200ms) var(--token-easing-expressive, ...)` + `background-color var(--token-duration-fast, 100ms) var(--token-easing-standard, ease)` ✅
- Focus `outline` → `var(--token-border-size-075) solid var(--token-semantics-primary-base)` ✅
- `.os-high-contrast` outline → `var(--token-semantics-primary-base, ...)` (era `--color-focus-outer`) ✅
- `@media (prefers-reduced-motion: reduce)` cobrindo arrow + pagination ✅

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 75% | 🟡 Acceptable |
| 2ª análise (final) | 81% | 🟡 Acceptable |

### Para Delightful — 100%
1. Substituir `var(--token-border-default)` por `var(--token-bg-neutral-subtle, #d5d5d5)` em `--osui-carousel-pagination-rest-color` → C4 🟢 (87.5%)
2. Formalizar `--token-scale-950` (38px) e aplicar em `--osui-carousel-arrow-size` → C1+C2 melhora
3. Formalizar `--token-scale-750` (30px) e aplicar em `--osui-carousel-pagination-margin` → C1+C2 🟢 (100%)
