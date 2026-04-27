#!/usr/bin/env python3
"""
For each *-tokens.html in the target dir:
  1. Set the initial wrapper class to include 'new-tokens-mode' so the page
     always renders with a selected theme active (no unscoped fallback).
  2. Strip unscoped OSUI component-level CSS rules from the inline <style>
     block. Specifically: any rule whose selector list, after splitting on
     top-level commas, contains ONLY component-level selectors of the form
     '[data-X]' or '.radio-button' (with optional pseudo-class/element/
     attribute suffix). Mixed rules keep only their non-component selectors.

Page-chrome rules, CSS variables, demo helpers, and rules already scoped
to '#previewWrapper.X-mode' are preserved.

Usage: python3 clean-inline-styles.py DIR_WITH_HTMLS
"""
import os
import re
import sys


# Component selectors that must be removed when unscoped.
# Match: '[data-switch]', '[data-switch]:hover', '[data-switch][disabled]', etc.
DATA_ATTR_RE = re.compile(r'^\[data-[\w-]+\]')

# Class-based unscoped components (matches '.radio-button', '.radio-button:checked', etc.,
# but NOT '.radio-button-foo' or '.radio-group').
CLASS_COMPONENT_RES = [
    re.compile(r'^\.radio-button(?:[:.\[]|$|\s)'),
]


def is_unscoped_component_selector(sel: str) -> bool:
    s = sel.strip()
    if not s:
        return False
    # Already scoped to wrapper -> not "unscoped component" (keep)
    if s.startswith('#previewWrapper'):
        return False
    if DATA_ATTR_RE.match(s):
        return True
    for r in CLASS_COMPONENT_RES:
        if r.match(s):
            return True
    return False


def split_top_level(text: str):
    parts, depth, cur = [], 0, ''
    for c in text:
        if c in '([':
            depth += 1; cur += c
        elif c in ')]':
            depth -= 1; cur += c
        elif c == ',' and depth == 0:
            parts.append(cur); cur = ''
        else:
            cur += c
    if cur:
        parts.append(cur)
    return parts


def strip_unscoped_rules(css: str) -> str:
    """Walk CSS top-level. Drop rules whose selector list contains ONLY unscoped
    component selectors. For mixed rules, keep only non-component selectors."""
    out = []
    i, n = 0, len(css)

    while i < n:
        ch = css[i]

        if ch.isspace():
            out.append(ch); i += 1; continue

        if css[i:i+2] == '/*':
            end = css.find('*/', i+2)
            if end == -1:
                out.append(css[i:]); break
            out.append(css[i:end+2]); i = end + 2; continue

        if ch == '@':
            m = re.match(r'@[\w-]+', css[i:])
            if not m:
                out.append(ch); i += 1; continue
            kw = m.group(0)
            j = i + len(kw)
            while j < n and css[j] not in '{;':
                j += 1
            if j >= n:
                out.append(css[i:]); break
            if css[j] == ';':
                out.append(css[i:j+1]); i = j + 1; continue
            depth = 1; k = j + 1
            while k < n and depth > 0:
                c = css[k]
                if c == '{': depth += 1
                elif c == '}': depth -= 1
                elif c in '"\'':
                    q = c; k += 1
                    while k < n and css[k] != q:
                        if css[k] == '\\': k += 2
                        else: k += 1
                k += 1
            block_end = k
            prelude = css[i:j]
            body = css[j+1:block_end-1]

            if kw in ('@media', '@supports', '@container', '@layer'):
                inner = strip_unscoped_rules(body)
                if inner.strip():
                    out.append(f'{prelude}{{{inner}}}')
            else:
                out.append(css[i:block_end])
            i = block_end
            continue

        # Regular rule
        j = i; pd = 0
        while j < n:
            c = css[j]
            if c in '([': pd += 1
            elif c in ')]': pd -= 1
            elif c == '{' and pd == 0: break
            elif c in '"\'':
                q = c; j += 1
                while j < n and css[j] != q:
                    if css[j] == '\\': j += 2
                    else: j += 1
            j += 1
        if j >= n:
            out.append(css[i:]); break

        sel_text = css[i:j]
        depth = 1; k = j + 1
        while k < n and depth > 0:
            c = css[k]
            if c == '{': depth += 1
            elif c == '}': depth -= 1
            elif c in '"\'':
                q = c; k += 1
                while k < n and css[k] != q:
                    if css[k] == '\\': k += 2
                    else: k += 1
            k += 1
        rule_end = k
        body = css[j+1:k-1]

        parts = split_top_level(sel_text)
        kept = [p for p in parts if not is_unscoped_component_selector(p)]
        if not kept:
            # Whole rule removed
            pass
        elif len(kept) == len(parts):
            # Nothing to drop — keep the rule verbatim
            out.append(css[i:rule_end])
        else:
            new_sel = ','.join(kept)
            out.append(f'{new_sel}{{{body}}}')

        i = rule_end

    return ''.join(out)


def set_initial_mode(html: str) -> str:
    """Make the wrapper render with new-tokens-mode by default."""
    # Case 1: <div id="previewWrapper" class="hide-annotations">
    html, n1 = re.subn(
        r'(<div\s+id="previewWrapper"\s+class=")hide-annotations(")',
        r'\1hide-annotations new-tokens-mode\2',
        html,
    )
    if n1:
        return html
    # Case 2: <div id="previewWrapper"> (no class)
    html, n2 = re.subn(
        r'<div\s+id="previewWrapper"\s*>',
        '<div id="previewWrapper" class="new-tokens-mode">',
        html,
    )
    return html


def transform_file(path: str) -> bool:
    with open(path) as f:
        html = f.read()
    original = html

    html = set_initial_mode(html)

    m = re.search(r'(<style[^>]*>)(.*?)(</style>)', html, re.DOTALL)
    if m:
        opener, content, closer = m.group(1), m.group(2), m.group(3)
        new_content = strip_unscoped_rules(content)
        html = html[:m.start()] + opener + new_content + closer + html[m.end():]

    if html != original:
        with open(path, 'w') as f:
            f.write(html)
        return True
    return False


if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    files = sorted(f for f in os.listdir(target_dir) if f.endswith('-tokens.html'))
    changed, skipped = 0, 0
    for f in files:
        path = os.path.join(target_dir, f)
        try:
            if transform_file(path):
                print(f'  updated:  {f}')
                changed += 1
            else:
                print(f'  skipped:  {f}')
                skipped += 1
        except Exception as e:
            print(f'  FAILED :  {f}  ({e})')
            import traceback; traceback.print_exc()
    print(f'\nTotal: {changed} updated, {skipped} skipped, {len(files)} scanned.')
