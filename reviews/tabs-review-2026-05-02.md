# Tabs — Token & Composition Review
**Date:** 2026-05-02
**Score:** 100% · Delightful
**CSS source:** `OSUI_NewTheme/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Tabs

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
| 5 | Legibility & contrast | 🟢 Delightful |
| 6 | Composition fit | 🟢 Delightful |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | 🟢 Delightful |

**D×8 = 16 / 16 = 100% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final
- `--osui-tabs-border-color` → `var(--token-border-default, ...)` ✅
- `--osui-tabs-header-item-color` → `var(--token-text-subtlest, ...)` ✅
- `--osui-tabs-header-item-color-active` → `var(--token-semantics-primary-base, ...)` ✅
- `--osui-tabs-header-item-color-hover` → `var(--token-text-default, ...)` ✅
- `--osui-tabs-header-item-color-disabled` → `var(--token-text-disabled, ...)` ✅
- `--osui-tabs-indicator-color` → `var(--token-semantics-primary-base, ...)` ✅
- Indicator thickness → `var(--token-border-size-050, 2px)` ✅
- Indicator transition → `transform var(--token-duration-moderate) var(--token-easing-standard)` ✅
- `min-height` → `var(--token-scale-1100, 44px)` ✅
- Todos os paddings tokenizados ✅
- Focus ring → `inset color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` ✅
- High-contrast → `var(--token-semantics-primary-base, #105cef)` sem `--color-focus-outer` ✅
- `z-index` → `var(--token-layer-local-tier-1, 1)` ✅ (fix: era `var(--layer-local-tier-1)` sem fallback)
- `indicator[disabled] background-color` → `var(--token-bg-neutral-base-default, #a2a2a2)` ✅ (fix: era `--token-text-disabled`)
- `.osui-tabs__header-item` → `transition: background-color var(--token-duration-fast) var(--token-easing-standard)` ✅ (fix: ausente)
- `@media (prefers-reduced-motion: reduce)` → cobre `.osui-tabs__header__indicator` + `.osui-tabs__header-item` ✅ (fix: header-item em falta)

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 81% | 🟡 Acceptable |
| 2ª análise (final) | 100% | 🟢 Delightful |

### Pending token a formalizar
| Token | Valor | Situação |
|---|---|---|
| `--token-layer-local-tier-1` | 1 | Em uso com fallback no indicator z-index — formalizar no token system |
