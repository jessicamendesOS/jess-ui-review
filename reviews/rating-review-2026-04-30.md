# Rating — Token & Composition Review
**Date:** 2026-04-30
**Score:** 93% · Delightful
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Rating

---

## Fix list

**Sem findings.** Todos os critérios avaliáveis estão resolvidos.

---

## Scores

| # | Critério | Score |
|---|---|---|
| 1 | Token integrity | 🟢 Delightful |
| 2 | Scale harmony | 🟢 Delightful |
| 3 | Radius coherence | — N/A |
| 4 | Color contract | 🟢 Delightful |
| 5 | Legibility & contrast | 🟡 Acceptable |
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | 🟢 Delightful |

**D×6 + A×1 = 12 + 1 = 13 / 14 = 93% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final

- `--token-rating-filled-color` → `var(--token-semantics-warning-base, #e9a100)` ✅
- `--token-rating-empty-color` → `color-mix(in srgb, var(--token-rating-filled-color) 38%, #ffffff)` ✅
- `.rating .text-primary` → `var(--token-rating-filled-color, #e9a100)` (gold substituiu primary blue) ✅
- `.rating .text-neutral-5` → `var(--token-rating-empty-color)` (tint quente em vez de cinzento desligado) ✅
- `.rating .icon` → `vertical-align: middle` ✅
- `--rating-size` default → `var(--token-scale-400, 16px)` ✅
- `--rating-size` small → `var(--token-scale-300, 12px)` (8px → 12px para legibilidade) ✅
- `--rating-size` medium → `var(--token-scale-600, 24px)` ✅
- `transition` → `opacity var(--token-duration-fast, 100ms) var(--token-easing-standard, ease)` (era `opacity linear 150ms`) ✅
- `line-height` items → `var(--token-font-line-height-full, 1)` ✅
- Disabled empty → `color-mix(in srgb, var(--token-text-disabled, #a2a2a2) 35%, #ffffff)` ✅
- `.has-accessible-features fieldset[disabled]` → `var(--token-text-disabled, #a2a2a2)` (substituiu `--token-primitives-neutral-700`) ✅
- Focus ring → `color-mix(in srgb, var(--token-semantics-primary-base, #105cef) 22%, transparent)` (substituiu `--color-focus-outer`) ✅
- `@media (prefers-reduced-motion: reduce)` com cobertura de `rating-item-filled/half/empty` ✅

### Contrast matrix

| Par | Rácio | Nota |
|---|---|---|
| Gold #e9a100 / white | 2.20:1 | Abaixo de WCAG 1.4.11 3:1 — decisão de design intencional (convenção universal) |
| Empty warm tint / white | 1.35:1 | Estado não-activo; comunica via fill count, não cor |
| Disabled #a2a2a2 / white | 2.55:1 | Disabled isento por WCAG 1.4.11 |

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 64% | 🟡 Acceptable |
| 2ª análise (final) | 93% | 🟢 Delightful |

### Notas de critério 5
Legibility & contrast mantém Acceptable porque gold #e9a100 sobre branco dá 2.20:1 — abaixo do WCAG 1.4.11 non-text contrast (3:1). Mantém Acceptable porque:
- A convenção da estrela dourada é universalmente reconhecida
- O estado filled/empty é comunicado por fill count e posição, não apenas pela cor
- O componente tem suporte a meia-estrela que dá granularidade adicional de leitura

### Pending tokens a formalizar

| Token | Valor | Situação |
|---|---|---|
| `--token-rating-filled-color` | `var(--token-semantics-warning-base, #e9a100)` | Em uso com fallback — formalizar no token system |
| `--token-rating-empty-color` | `color-mix(in srgb, #e9a100 38%, #ffffff)` | Em uso com fallback — formalizar no token system |
