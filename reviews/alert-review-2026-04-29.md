# Alert — Token & Composition Review
**Date:** 2026-04-29
**Score:** 93% · Delightful
**CSS source:** `assets/os-ui/OutsystemsUI_2.29-proposed.css`
**Test page:** https://eng-starter-apps-dev.outsystems.app/MakeGreatUI_FunctionalTests/Tests_Alert

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
| 5 | Legibility & contrast | 🟡 Acceptable |
| 6 | Composition fit | — N/A |
| 7 | Visual quality | 🟢 Delightful |
| 8 | Motion & interaction | 🟢 Delightful |
| 9 | Accessibility | — N/A |

**D×2 + A×1 = 12 + 1 = 13 / 14 = 93% · Delightful**

---

## Notas de sessão

### O que estava resolvido na versão final
- Border-left accent removida ✅
- `--osui-alert-border-radius` → `var(--token-border-radius-200, 8px)` via override intencional (documentado com comment) ✅
- `gap` → `var(--token-scale-200, 8px)` ✅
- `padding` → `var(--token-scale-300, 12px) var(--token-scale-400, 16px)` ✅
- `font-size` mensagem → `var(--token-font-size-350, 0.875rem)` ✅
- `font-weight` mensagem → `var(--token-font-weight-medium, 500)` ✅
- `line-height` mensagem → `var(--token-line-height-body, 1.4)` ✅
- `transition` → `var(--token-duration-fast, 120ms) var(--token-easing-standard, ease)` ✅
- Cores semânticas todas correctas por variante ✅
- ARIA roles correctos: `role="alert"` para error/warning, `role="status"` para info/success ✅
- `.alert-icon` base `width/height` → `var(--token-scale-500, 20px)` ✅
- `.alert .alert-icon` override `width/height` → `var(--token-scale-500, 20px)` ✅
- `.alert-icon:after` `font-size` → `var(--token-font-size-500, 1.25rem)` ✅

### Progressão de score ao longo da sessão
| Iteração | Score | Tier |
|---|---|---|
| 1ª análise | 50% | 🟡 Acceptable |
| 2ª análise | 56% | 🟡 Acceptable |
| 3ª análise | 62.5% | 🟡 Acceptable |
| 4ª análise | 68.75% | 🟡 Acceptable |
| 5ª análise | 75% | 🟡 Acceptable |
| 6ª análise (final) | 93% | 🟢 Delightful |

### Notas de critério 5
Legibility & contrast mantém Acceptable porque os rácios de contraste não foram medidos formalmente — apenas inferidos pelos tokens semânticos (-900 texto sobre -100 fundo). Para Delightful seria necessário medir os 4 pares de cor com ferramenta de contraste.
