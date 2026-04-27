#!/usr/bin/env python3
"""
Scope a CSS file by prefixing every selector with a scope selector.

Special cases:
  :root { ... }        -> scope { ... }        (tokens inherit to descendants)
  html { ... }         -> scope { ... }        (treat the scope root as "html")
  body { ... }         -> scope { ... }        (same)
  * { ... }            -> scope *, scope { ... }  (resets for all descendants)
  html, body, ...      -> scope, ...           (deduplicate root-level hits)

Recurses into @media, @supports, @container, @layer.
Leaves @keyframes, @font-face, @counter-style, @property, @page untouched.

Usage:  python3 scope-css.py INPUT.css OUTPUT.css "#previewWrapper.current-mode"
        python3 scope-css.py INPUT.css OUTPUT.css "#a, #b"   (multi-scope: rule matches either)
"""

import re
import sys


def scope_css(css: str, scope) -> str:
    out = []
    i, n = 0, len(css)

    while i < n:
        ch = css[i]

        # Pass through whitespace
        if ch.isspace():
            out.append(ch)
            i += 1
            continue

        # Comments
        if css[i:i+2] == '/*':
            end = css.find('*/', i+2)
            if end == -1:
                out.append(css[i:])
                break
            out.append(css[i:end+2])
            i = end + 2
            continue

        # @-rules
        if ch == '@':
            m = re.match(r'@[\w-]+', css[i:])
            if not m:
                out.append(ch)
                i += 1
                continue
            kw = m.group(0)

            # Find end: either ';' (simple @-rule) or '{' (block @-rule)
            j = i + len(kw)
            while j < n and css[j] not in '{;':
                j += 1
            if j >= n:
                out.append(css[i:])
                break

            if css[j] == ';':
                # @charset, @import, @namespace — pass through
                out.append(css[i:j+1])
                i = j + 1
                continue

            # Block @-rule — find matching '}'
            depth = 1
            k = j + 1
            while k < n and depth > 0:
                c2 = css[k]
                if c2 == '{':
                    depth += 1
                elif c2 == '}':
                    depth -= 1
                elif c2 == '"' or c2 == "'":
                    # Skip strings
                    quote = c2
                    k += 1
                    while k < n and css[k] != quote:
                        if css[k] == '\\':
                            k += 2
                        else:
                            k += 1
                k += 1
            block_end = k

            prelude = css[i:j]
            body = css[j+1:block_end-1]

            if kw in ('@keyframes', '@-webkit-keyframes', '@font-face',
                     '@counter-style', '@property', '@page', '@viewport'):
                # Leave untouched
                out.append(css[i:block_end])
            elif kw in ('@media', '@supports', '@container', '@layer',
                       '@-moz-document', '@document'):
                scoped_body = scope_css(body, scope)
                out.append(f'{prelude}{{{scoped_body}}}')
            else:
                # Unknown — pass through
                out.append(css[i:block_end])

            i = block_end
            continue

        # Regular rule: selector {...}
        # Find '{' at depth 0 (considering parens/brackets for :is(), [attr=","])
        j = i
        pdepth = 0
        while j < n:
            c = css[j]
            if c == '(' or c == '[':
                pdepth += 1
            elif c == ')' or c == ']':
                pdepth -= 1
            elif c == '{' and pdepth == 0:
                break
            elif c == '"' or c == "'":
                q = c
                j += 1
                while j < n and css[j] != q:
                    if css[j] == '\\':
                        j += 2
                    else:
                        j += 1
            j += 1

        if j >= n:
            out.append(css[i:])
            break

        selector_text = css[i:j]

        # Find matching '}'
        depth = 1
        k = j + 1
        while k < n and depth > 0:
            c2 = css[k]
            if c2 == '{':
                depth += 1
            elif c2 == '}':
                depth -= 1
            elif c2 == '"' or c2 == "'":
                q = c2
                k += 1
                while k < n and css[k] != q:
                    if css[k] == '\\':
                        k += 2
                    else:
                        k += 1
            k += 1
        rule_end = k

        body = css[j+1:rule_end-1]
        scoped_sel = scope_selector_list(selector_text, scope)

        if scoped_sel is not None:
            out.append(f'{scoped_sel}{{{body}}}')
        # else: drop the rule

        i = rule_end

    return ''.join(out)


def split_top_level_commas(text: str):
    parts, depth, cur = [], 0, ''
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c == '(' or c == '[':
            depth += 1
            cur += c
        elif c == ')' or c == ']':
            depth -= 1
            cur += c
        elif c == ',' and depth == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += c
        i += 1
    if cur:
        parts.append(cur)
    return parts


def scope_selector_list(selector_text: str, scope):
    # Accept either a single scope string or a list of scope strings
    scopes = scope if isinstance(scope, list) else [scope]
    parts = split_top_level_commas(selector_text)
    scoped = []
    for p in parts:
        s = p.strip()
        if not s:
            continue
        for sc in scopes:
            t = scope_one(s, sc)
            if t:
                scoped.append(t)
    if not scoped:
        return None
    return ', '.join(scoped)


# Anchored patterns for root-level pseudo/tag selectors we need to rewrite
_root_pat = re.compile(r'^:root(?=$|[\s.:\[#,])')
_html_pat = re.compile(r'^html(?=$|[\s.:\[#,])')
_body_pat = re.compile(r'^body(?=$|[\s.:\[#,])')
_star_pat = re.compile(r'^\*(?=$|[\s.:\[#,])')


def scope_one(sel: str, scope: str):
    """
    Rewrite one selector.
    :root / html / body acting as the *document root* get replaced by `scope`
    (so tokens + resets land on the scope element).
    `*` gets mapped to descendants of scope so resets like box-sizing still apply.
    Everything else gets prefixed with `scope `.
    """
    # :root.something  ->  scope.something
    m = _root_pat.match(sel)
    if m:
        return scope + sel[m.end():]
    # html.something   ->  scope.something
    m = _html_pat.match(sel)
    if m:
        return scope + sel[m.end():]
    # body.something   ->  scope.something
    m = _body_pat.match(sel)
    if m:
        return scope + sel[m.end():]
    # *                 ->  scope *  (applies to descendants only; resets like box-sizing work)
    m = _star_pat.match(sel)
    if m:
        return scope + ' *' + sel[m.end():]
    # Everything else: prefix
    return f'{scope} {sel}'


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: scope-css.py INPUT.css OUTPUT.css SCOPE_SELECTOR[,SCOPE_SELECTOR,...]', file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1]) as f:
        css = f.read()
    raw_scope = sys.argv[3]
    # Split on comma at depth 0 so selectors like "#a.b, #a.c" become ["#a.b", "#a.c"]
    scopes = [s.strip() for s in split_top_level_commas(raw_scope) if s.strip()]
    scope_arg = scopes[0] if len(scopes) == 1 else scopes
    out = scope_css(css, scope_arg)
    with open(sys.argv[2], 'w') as f:
        f.write(out)
    print(f'Wrote {sys.argv[2]} ({len(out):,} chars) with {len(scopes)} scope(s)')
