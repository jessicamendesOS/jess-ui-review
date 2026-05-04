# Checkbox — Token & Composition Review
**Date:** 2026-05-01
**Score:** 100% · Delightful
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Checkbox

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
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | 🟢 Delightful |

**D×8 = 16 / 16 = 100% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final
- `--osui-checkbox-background` → `var(--token-bg-input-default, #ffffff)` ✅
- `--osui-checkbox-border-color` → `var(--token-border-input-default, #8c8c8c)` ✅
- `--osui-checkbox-border-radius` → `var(--token-border-radius-200, 8px)` ✅
- `--osui-checkbox-checked-color` → `var(--token-semantics-primary-base, #105cef)` ✅
- `[data-checkbox]` `height/width` → `var(--token-scale-600, 24px)` ✅
- `[data-checkbox]:before` `height/width` → `calc(var(--token-scale-600, 24px) - 2px)` ✅
- `[data-checkbox]:before` `transition` → `background-color var(--token-duration-fast, 100ms) var(--token-easing-standard, ease), border-color var(...)` (era `all`) ✅
- `.tablet/.phone [data-checkbox]` `height/width` → `var(--token-scale-800, 32px)` ✅
- `.tablet/.phone [data-checkbox]:before` `height/width` → `calc(var(--token-scale-800, 32px) - 2px)` ✅
- Hover border → `var(--token-border-input-press)` ✅
- Checkmark color → `var(--token-text-inverse)` ✅
- Disabled background/border → `var(--token-bg-input-disabled)` / `var(--token-border-default)` ✅
- Disabled checkmark → `var(--token-text-disabled)` ✅
- Error state → `var(--token-semantics-danger-base)` ✅
- Focus ring (`.has-accessible-features`) → `color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` ✅
- `@media (prefers-reduced-motion: reduce)` com cobertura de `[data-checkbox]:before` ✅

### Contrast matrix

| Par | Rácio | AA |
|---|---|---|
| Checkmark branco / checked #105cef | 5.53:1 | ✅ |
| Border unchecked #8c8c8c / white | 3.35:1 | ✅ (non-text) |
| Disabled checkmark #a2a2a2 / disabled bg #f3f3f3 | 2.30:1 | — (disabled isento) |

### Nota sobre checkmark (5px × 10px)
As dimensões do checkmark (`:checked:after height: 5px; width: 10px`) são constantes geométricas que definem a proporção do traço — não mapeiam para tokens de escala. Tratamento intencional.

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 81% | 🟡 Acceptable |
| 2ª análise (final) | 100% | 🟢 Delightful |
