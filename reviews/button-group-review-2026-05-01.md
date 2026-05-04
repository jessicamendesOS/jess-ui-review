# Button Group — Token & Composition Review
**Date:** 2026-05-01
**Score:** 94% · Delightful
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_ButtonGroup

---

## Fix list

### 🟡 Acceptable

| Selector | Propriedade | Actual | → Mudar para | Porquê |
|---|---|---|---|---|
| `.layout-native .header-top-content .button-group-item` | `background-color` | `var(--background-color-header, var(--header-color))` | `var(--token-bg-header, ...)` (pending) | Nomenclatura de tema legado fora do sistema `--token-*` |

---

## Scores

| # | Critério | Score |
|---|---|---|
| 1 | Token integrity | 🟡 Acceptable |
| 2 | Scale harmony | 🟢 Delightful |
| 3 | Radius coherence | 🟢 Delightful |
| 4 | Color contract | 🟢 Delightful |
| 5 | Legibility & contrast | 🟢 Delightful |
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | 🟢 Delightful |

**D×7 + A×1 = 14 + 1 = 15 / 16 = 94% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final
- `--osui-button-group-background` → `var(--token-bg-surface-default, #ffffff)` ✅
- `--osui-button-group-border-color` → `var(--token-border-default, #d5d5d5)` ✅
- `--osui-button-group-color` → `var(--token-text-default, #242424)` ✅
- `height` → `var(--token-scale-900, 36px)` ✅
- `padding` → `var(--token-scale-0, 0) var(--token-scale-400, 16px)` ✅
- `font-size` → `var(--token-font-size-350, 0.875rem)` ✅
- `font-weight` → `var(--token-font-weight-semi-bold, 600)` ✅
- `border-radius` first/last → `var(--token-border-radius-200, 8px)` ✅
- `transition` → `background-color var(--token-duration-fast, 100ms) var(--token-easing-standard, ease), border-color var(...)` ✅
- Hover `background-color` → `var(--token-bg-surface-hover, #f3f3f3)` (era `--token-border-subtle` — semantic mismatch corrigido) ✅
- Selected `background-color` → `var(--token-semantics-primary-base, #105cef)` ✅
- Selected `color` → `var(--token-text-inverse, #ffffff)` ✅
- Disabled `color` → `var(--token-text-disabled, #a2a2a2)` ✅
- Disabled selected `background-color` → `var(--token-bg-input-disabled, #f3f3f3)` ✅
- `.tablet/.phone height` → `var(--token-scale-1100, 48px)` ✅
- Focus ring (`.has-accessible-features`) → `color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` ✅
- `@media (prefers-reduced-motion: reduce)` → `.button-group-item { transition: none }` ✅

### Contrast matrix

| Par | Rácio | AA |
|---|---|---|
| Default #242424 / white | 15.52:1 | ✅ |
| Default #242424 / hover #f3f3f3 | 13.99:1 | ✅ |
| White / selected #105cef | 5.53:1 | ✅ |
| Disabled #a2a2a2 / white | 2.55:1 | — (isento) |

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 88% | 🟡 Acceptable |
| 2ª análise (final) | 94% | 🟢 Delightful |

### Para Delightful 100%
Formalizar `--token-bg-header` e aplicar em `.layout-native .header-top-content .button-group-item` em substituição a `var(--background-color-header, var(--header-color))`.

### Pending token
| Token | Situação |
|---|---|
| `--token-bg-surface-hover` | Em uso com fallback `#f3f3f3` — formalizar no token system |
| `--token-bg-header` | Pending — substituir vars de tema legado no contexto native layout |
