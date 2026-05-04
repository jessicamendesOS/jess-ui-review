# Button — Token & Composition Review
**Date:** 2026-04-30
**Score:** 88% · Acceptable
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Button

---

## Fix list

### 🟡 Acceptable

| Componente | Propriedade | Actual | → Mudar para | Porquê |
|---|---|---|---|---|
| `.btn-cancel:hover` | `border-color` | `var(--token-primitives-neutral-500, #9ca3af)` | pending `--token-border-subtle-hover` ou equiv. semântico | Primitivo onde deveria existir alias semântico |
| `.btn:focus` base | `border-color` | `var(--color-focus-inner)` (linha 2971) | `var(--token-semantics-primary-base)` | Token name fora da nomenclatura documentada |

### 🔵 Pending tokens a formalizar

| Token | Valor | Situação |
|---|---|---|
| `--token-semantics-primary-hover` | #0b47b8 | Em uso com fallback em `.btn-primary:hover` |
| `--token-elevation-100` | `0 1px 4px rgba(0,0,0,.08)` | Em uso com fallback em `.btn-cancel:hover box-shadow` |
| `--token-duration-base` | 150ms | Em uso com fallback em `.btn-cancel transition` |
| `--token-opacity-disabled` | 0.45 | Em uso com fallback em todos os `[disabled]` variants |

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
| 9 | Accessibility | 🟡 Acceptable |

**D×6 + A×2 = 12 + 2 = 14 / 16 = 88% · Acceptable**

---

## Notas de sessão

### O que estava resolvido na versão final
- `height` default → `var(--token-scale-900, 36px)` ✅
- `height` small → `var(--token-scale-800, 32px)` ✅
- `height` large → `var(--token-scale-1200, 48px)` ✅
- `border-radius` → `var(--token-border-radius-200, 8px)` ✅
- `font-weight` → `var(--token-font-weight-medium, 500)` ✅
- `line-height` → `var(--token-font-line-height-full, 1)` (base + proposed) ✅
- `padding` → `var(--token-scale-0, 0) var(--token-scale-400/200, ...)` ✅
- `transition` → `background-color var(--token-duration-fast) var(--token-easing-standard), border-color ..., color ...` ✅
- `.btn-cancel transition` → `border-color var(--token-duration-base, 150ms) var(--token-easing-standard, ease), ...` ✅
- `.btn-primary:hover` → `var(--token-semantics-primary-hover, #0b47b8)` ✅
- `.btn-cancel:hover color` → `var(--token-text-default, #374151)` ✅
- `.btn-cancel:hover box-shadow` → `var(--token-elevation-100, 0 1px 4px rgba(0,0,0,.08))` ✅
- `opacity` disabled → `var(--token-opacity-disabled, 0.45)` em todos os variants ✅
- `@media (prefers-reduced-motion: reduce) { .btn, .btn-cancel { transition: none; } }` ✅
- `--osui-btn-success-background` → chains `--token-semantics-success-900` → `#126f23` → **6.32:1** ✅
- `--osui-btn-error-background` → chains `--token-semantics-danger-800` → `#bf2222` → **6.06:1** ✅

### Contrast matrix final

| Variante | Hex fundo | Rácio | AA |
|---|---|---|---|
| btn-primary | #105cef | 5.53:1 | ✅ |
| btn-secondary | #ffffff | 5.53:1 | ✅ |
| btn-success | #126f23 | 6.32:1 | ✅ |
| btn-error | #bf2222 | 6.06:1 | ✅ |
| btn-cancel | #ffffff | 11.20:1 | ✅ |

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 56% | 🟡 Acceptable |
| 2ª análise | 75% | 🟡 Acceptable |
| 3ª análise | 88% | 🟡 Acceptable |

### Para Delightful
Os dois findings Acceptable são o mesmo problema de nomenclatura de token:
1. Substituir `var(--color-focus-inner)` por `var(--token-semantics-primary-base)` na regra base `.has-accessible-features .btn:focus` (linha 2971) — resolve critérios 1 e 9 simultaneamente
2. Formalizar `--token-border-subtle-hover` e aplicar em `.btn-cancel:hover border-color` em substituição ao primitivo `--token-primitives-neutral-500`

Se ambos forem resolvidos: **D×8 = 16/16 = 100% · Delightful**
Se apenas o focus ring for resolvido: **D×7 + A×1 = 15/16 = 93.75% · Delightful**

### Nota sobre touch target (critério 9)
Desktop default height 36px < 44px WCAG 2.5.5. Mitigado pelos overrides de breakpoint:
- `.tablet .btn, .phone .btn { height: 48px }` — contextos touch cobertos ✅
- Desktop usa rato — risco reduzido, não Critical
