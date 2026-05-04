# Switch — Token & Composition Review
**Date:** 2026-04-30
**Score:** 69% · Acceptable
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Switch

---

## Fix list

### 🟡 Acceptable

| Componente | Propriedade | Actual | → Mudar para | Porquê |
|---|---|---|---|---|
| `:before`/`:after` | `transition duration` | `0.2s` hardcoded (200ms) | `var(--token-duration-natural, 200ms)` | Duration sem token — 200ms não mapeia a nenhum token existente; formalizar |
| `[data-switch]:focus:before` base | `border-color` | `var(--color-focus-inner)` (linha 2530) | `var(--token-semantics-primary-base)` | Token name fora da nomenclatura documentada — mesma issue Button/Accordion |
| `[disabled]:after` | `background` fallback | `rgba(255,255,255,0.6)` em `var(--token-state-disabled, ...)` | Formalizar `--token-state-disabled` | Pending token com alpha-hardcoded fallback |

### 🔵 Pending tokens a formalizar

| Token | Valor | Situação |
|---|---|---|
| `--token-duration-natural` | 200ms | Em uso hardcoded na transition `:before`/`:after` |
| `--token-state-disabled` | `rgba(255,255,255,0.6)` | Em uso com fallback no thumb disabled |
| `--token-elevation-50` | `0 1px 2px rgba(0,0,0,.2)` | Em uso com fallback no thumb activo |
| `--token-elevation-25` | `0 1px 2px rgba(0,0,0,.08)` | Em uso com fallback no thumb disabled |

---

## Scores

| # | Critério | Score |
|---|---|---|
| 1 | Token integrity | 🟡 Acceptable |
| 2 | Scale harmony | 🟢 Delightful |
| 3 | Radius coherence | 🟢 Delightful |
| 4 | Color contract | 🟡 Acceptable |
| 5 | Legibility & contrast | 🟡 Acceptable |
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟡 Acceptable |
| 9 | Accessibility | 🟡 Acceptable |

**D×3 + A×5 = 6 + 5 = 11 / 16 = 69% · Acceptable**

---

## Notas de sessão

### O que estava resolvido na versão final
- `height` track → `var(--token-scale-600, 24px)` ✅
- `width` track → `var(--token-scale-1000, 40px)` ✅
- `height/width` thumb → `var(--token-scale-500, 20px)` ✅
- `border-radius` track → `var(--token-border-radius-full, 9999px)` ✅
- `background` unchecked track → `var(--token-border-default, #d5d5d5)` ✅
- `background` checked track → `var(--token-semantics-primary-base, #105cef)` ✅
- `background` disabled:unchecked track → `var(--token-border-subtle, #f3f3f3)` ✅
- `background` disabled:checked track → `var(--token-semantics-primary-base)` + `opacity: var(--token-opacity-disabled, 0.45)` ✅
- `background` thumb → `var(--osui-switch-thumb-color)` ✅
- `background` disabled thumb → `var(--token-state-disabled, rgba(255,255,255,0.6))` ✅
- `box-shadow` thumb → `var(--token-elevation-50, 0 1px 2px rgba(0,0,0,.2))` ✅
- `box-shadow` disabled thumb → `var(--token-elevation-25, 0 1px 2px rgba(0,0,0,.08))` ✅
- Transition específica: `background, transform` (não mais `all`) ✅
- `@media (prefers-reduced-motion: reduce)` com cobertura de `[data-switch]:before/after` ✅
- Focus ring moderno: `color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` via `:focus-visible` ✅

### Notas de critério

**Critério 5 (Legibility):** Track unchecked `#D5D5D5` vs fundo branco ≈ 1.47:1 — abaixo do WCAG 1.4.11 non-text contrast (3:1). Mantém Acceptable porque a posição do thumb comunica o estado independentemente da cor do track. Decisão de design intencional — não Critical.

**Critério 8 (Motion):** Transitions agora específicas (`background, transform`) em vez de `all` ✅. Reduced-motion confirmado para `[data-switch]` ✅. Duration `0.2s` ainda hardcoded — pending `--token-duration-natural`.

**Critério 9 (Accessibility):** Switch 40×24px < 44px touch target primário. Mitigado pelo label wrapper que estende a área de interacção. Focus ring via `:focus-visible` com `color-mix()` é moderno e correcto ✅. Token `--color-focus-inner` na regra base legada `.has-accessible-features` mantém nomenclatura errada.

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 50% | 🟡 Acceptable |
| 2ª análise | 69% | 🟡 Acceptable |
| 3ª análise (final) | 69% | 🟡 Acceptable |

### Para Delightful (target: 94%)
1. Formalizar `--token-duration-natural: 200ms` e aplicar na transition — resolve critérios 1 e 8
2. Formalizar `--token-state-disabled` — resolve critério 4
3. Substituir `var(--color-focus-inner)` por `var(--token-semantics-primary-base)` na regra base (linha 2530) — resolve critérios 1 e 9

Com as 3 correções: **D×7 + A×1 = 15/16 = 94% · Delightful**
O critério 5 mantém Acceptable (non-text contrast do track é uma decisão de design).
