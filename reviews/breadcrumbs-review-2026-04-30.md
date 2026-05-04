# Breadcrumbs — Token & Composition Review
**Date:** 2026-04-30
**Score:** 94% · Delightful
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Breadcrumbs

---

## Fix list

### 🟡 Acceptable

| Componente | Propriedade | Actual | → Mudar para | Porquê |
|---|---|---|---|---|
| `.breadcrumbs-item a` | `:focus-visible` ring | Browser default | `box-shadow: 0 0 0 3px color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent)` + `border-radius: var(--token-border-radius-50, 2px)` | Sem regra personalizada — inconsistente com Button/Switch |

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
| 9 | Accessibility | 🟡 Acceptable |

**D×7 + A×1 = 14 + 1 = 15 / 16 = 94% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final
- `font-size` item → `var(--token-font-size-350, 0.875rem)` ✅
- `font-weight` item → `var(--token-font-weight-regular, 400)` ✅
- `line-height` item → `var(--token-font-line-height-full, 1)` ✅
- `color` item → `var(--token-text-subtle, #3b3b3b)` ✅
- `color` link → `var(--token-text-subtlest, #626262)` ✅
- `line-height` link → `var(--token-font-line-height-full, 1)` ✅
- `text-decoration` link → `none` ✅
- `transition` link → `color var(--token-duration-fast, 100ms) var(--token-easing-standard, ease)` ✅
- `color` link:hover → `var(--token-text-default, #242424)` ✅
- `color` last item → `var(--token-text-default, #242424)` ✅
- `font-weight` last item → `var(--token-font-weight-semi-bold, 600)` ✅
- `color` icon → `var(--token-text-subtlest, #626262)` ✅
- `font-size` separator icon → `var(--token-font-size-300, 0.75rem)` ✅
- `line-height` separator icon → `var(--token-font-line-height-full, 1)` ✅
- `font-size` link icon → `var(--token-font-size-400, 1rem)` ✅
- `line-height` link icon → `var(--token-font-line-height-full, 1)` ✅
- `padding` ellipsis → `var(--token-scale-0, 0)` ✅
- `border-radius` ellipsis → `var(--token-border-radius-0, 0)` ✅
- `color` ellipsis:hover → `var(--token-text-default, #242424)` ✅
- `@media (prefers-reduced-motion: reduce)` com cobertura de `.breadcrumbs-item a` ✅

### Contrast matrix final — todos os pares passam WCAG AA

| Par de cores | Rácio | AA (4.5:1) |
|---|---|---|
| Link #626262 / white | 6.10:1 | ✅ |
| Item #3b3b3b / white | 11.20:1 | ✅ |
| Hover / current #242424 / white | 15.52:1 | ✅ |

### Progressão de score ao longo da sessão

| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | — | (pré-sessão) |
| 2ª análise (final) | 94% | 🟢 Delightful |

### Para Delightful 100%
Adicionar regra `:focus-visible` nos links do breadcrumb, consistente com Button e Switch:

```css
.breadcrumbs-item a:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--token-semantics-primary-base) 22%, transparent);
  border-radius: var(--token-border-radius-50, 2px);
}
```

Com esta correção: **D×8 = 16/16 = 100% · Delightful**
