# Accordion — Token & Composition Review
**Date:** 2026-04-29
**Score:** 56% · Acceptable
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Accordion

---

## Fix list

### 🟡 Acceptable

| Component | Property | Linha | Actual | → Change to | Why |
|---|---|---|---|---|---|
| Accordion item | `--osui-accordion-item-border-color` | 6930 | `var(--token-primitives-neutral-200)` (primitivo) | pending semantic `--token-border-subtle` | Primitivo onde deveria existir alias semântico — surface-safe mas fora da layer correcta |
| Accordion title hover | `background` | 6961 | `var(--token-primitives-neutral-100)` (primitivo) | pending semantic `--token-bg-neutral-subtle-hover` | Idem |
| Accordion item icon (base) | `transition` | 6825 | `all 300ms ease-in-out` (base, não proposto) | `var(--token-duration-slow) var(--token-easing-standard)` | Regra base não actualizada: ícone roda em 300ms, conteúdo abre em 400ms via `--token-duration-slow` — timing mismatch na mesma interacção |
| Focus ring | `outline color` | 6910 | `var(--color-focus-outer)` | `var(--token-semantics-primary-base)` | Token name fora da nomenclatura documentada |

### 🔵 Pending tokens a formalizar

| Token | Valor | Situação |
|---|---|---|
| `--token-border-subtle` | equiv. `neutral-200` (#eae9e9) | Em uso como primitivo — formalizar alias semântico |
| `--token-bg-neutral-subtle-hover` | equiv. `neutral-100` (#f3f3f3) | Em uso como primitivo — formalizar alias semântico |
| `--token-scale-350` | 14px | Em uso com fallback — formalizar |
| `--token-opacity-disabled` | 0.4 | Em uso com fallback — formalizar |

---

## Scores

| # | Critério | Score |
|---|---|---|
| 1 | Token integrity | 🟡 Acceptable |
| 2 | Scale harmony | 🟡 Acceptable |
| 3 | Radius coherence | 🟢 Delightful |
| 4 | Color contract | 🟡 Acceptable |
| 5 | Legibility & contrast | 🟡 Acceptable |
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟡 Acceptable |
| 8 | Motion & interaction | 🟡 Acceptable |
| 9 | Accessibility | 🟡 Acceptable |

**D×2 + A×1 + C×0 = 2 + 7 + 0 = 9 / 16 = 56% · Acceptable**

---

## Notas de sessão

### O que estava resolvido na versão final
- `--acc-proposed-dur` → `var(--token-duration-slow, 400ms)` ✅
- `--acc-proposed-ease` → `var(--token-easing-expressive, cubic-bezier(...))` ✅
- `font-size` item e title → `var(--token-font-size-400, 1rem)` ✅
- `color` item e title → `var(--token-text-default)` ✅
- `border-radius: 0` → `var(--token-border-radius-0)` + comment a documentar dividers-only ✅
- First/last items com `var(--token-border-radius-200)` explícito no bloco proposto ✅
- Title padding `scale-300 (12px)` → `scale-350 (14px)` — touch target 44px ✅
- Disabled `a` e `button` → `opacity: var(--token-opacity-disabled, 0.4)` ✅
- `rgba(0, 0, 0, .07)` → `var(--token-primitives-neutral-200)` ✅
- `rgba(0, 0, 0, .04)` → `var(--token-primitives-neutral-100)` ✅
- Caret `width/height` → `var(--token-scale-500, 20px)` ✅
- Caret `font-size` → `var(--token-font-size-500, 1.25rem)` ✅
- Caret SVG `width/height` → `var(--token-scale-500, 20px)` ✅
- Disabled Action elements visualmente correctos ✅

### Progressão de score ao longo da sessão
| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 14% | 🔴 Critical |
| 2ª análise | 18.75% | 🔴 Critical |
| 3ª análise | 50% | 🟡 Acceptable |
| 4ª análise (final) | 56% | 🟡 Acceptable |

### Para Delightful
1. Criar `--token-border-subtle` (alias semântico para `neutral-200`) e aplicar na linha 6930
2. Criar `--token-bg-neutral-subtle-hover` (alias semântico para `neutral-100`) e aplicar na linha 6961
3. Actualizar a regra base `.osui-accordion-item__icon` (linha 6825): `transition: all 300ms ease-in-out` → `var(--token-duration-slow) var(--token-easing-standard)`
4. Formalizar `--token-scale-350`, `--token-opacity-disabled` no sistema de tokens
