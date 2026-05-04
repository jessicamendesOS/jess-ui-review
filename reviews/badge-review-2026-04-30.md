# Badge — Token & Composition Review
**Date:** 2026-04-30
**Score:** 100% · Delightful
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Badge

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
| 8 | Motion & interaction | — N/A |
| 9 | Accessibility | — N/A |

**D×6 = 12 / 12 = 100% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final
- `height/min-width` default → `var(--token-scale-500, 20px)` ✅
- `height/min-width` small → `var(--token-scale-400, 16px)` ✅
- `height/min-width` medium → `var(--token-scale-700, 28px)` ✅
- `padding` default → `var(--token-scale-0, 0) var(--token-scale-150, 6px)` ✅
- `padding` small → `var(--token-scale-0, 0) var(--token-scale-100, 4px)` ✅
- `padding` medium → `var(--token-scale-0, 0) var(--token-scale-200, 8px)` ✅
- `font-size` default → `var(--token-font-size-300, 0.75rem)` ✅
- `font-size` small → `var(--token-font-size-200, 0.625rem)` ✅
- `font-size` medium → `var(--token-font-size-350, 0.875rem)` ✅
- `line-height` → `var(--token-font-line-height-full, 1)` (base + proposed) ✅
- `font-weight` → `var(--token-font-weight-semi-bold, 600)` ✅
- `--osui-badge-color` → `var(--token-text-inverse, ...)` ✅
- `--osui-badge-primary-color` → `var(--token-semantics-primary-base, ...)` ✅
- `--osui-badge-on-light-color` → `var(--token-text-default, ...)` ✅
- `.badge.background-yellow { color: var(--osui-badge-on-light-color) }` → 10.99:1 ✅
- `background-pink` utility → `#C53066` → 5.26:1 ✅
- `background-red` utility → `#BF2222` → 6.06:1 ✅
- `border-radius-full` (999px) via `.border-radius-rounded` — intencional ✅

### Contrast matrix final — 16/16 variantes passam WCAG AA

| Variante | Hex fundo | Rácio | AA |
|---|---|---|---|
| background-primary | #105cef | 5.53:1 | ✅ |
| background-secondary | #303d60 | 10.70:1 | ✅ |
| background-red | #bf2222 | 6.06:1 | ✅ |
| background-yellow | #ffd600 | 10.99:1 | ✅ |
| background-blue | #105cef | 5.53:1 | ✅ |
| background-neutral-7 | #6a7178 | 4.95:1 | ✅ |
| background-indigo | #411bd5 | 8.97:1 | ✅ |
| background-pink | #c53066 | 5.26:1 | ✅ |
| background-primary-lightest | #ffffff | 5.53:1 | ✅ |
| background-secondary-lightest | #ffffff | 10.70:1 | ✅ |
| background-red-lightest | #faeaea | 7.13:1 | ✅ |
| background-yellow-lightest | #fff3d5 | 4.58:1 | ✅ |
| background-blue-lightest | #e9ecfc | 6.36:1 | ✅ |
| background-neutral-7-lightest | #ffffff | 4.95:1 | ✅ |
| background-indigo-lightest | #ebe8ff | 9.33:1 | ✅ |
| background-pink-lightest | #fdeaee | 4.56:1 | ✅ |

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 50% | 🟡 Acceptable |
| 2ª análise | 67% | 🟡 Acceptable |
| 3ª análise | 83% | 🟡 Acceptable |
| 4ª análise | 92% | 🟢 Delightful |
| 5ª análise (final) | 100% | 🟢 Delightful |

### Pending token (não bloqueia score)
- `--token-scale-150` (6px) — em uso com fallback no padding default do badge; formalizar no token system quando possível.
