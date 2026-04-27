#!/usr/bin/env python3
"""
For each *-tokens.html in the target dir:
  1. Inject <link> tags for the two scoped CSS files (after <title>)
  2. Strip every top-level CSS rule whose selector starts with
     '#previewWrapper.current-mode' or '#previewWrapper.proposed-mode'
     from the first <style> block.

The point: replace hand-coded replicas of OSUI 2.28 / 2.29 with the real CSS
loaded via <link>, while preserving preview chrome / annotations / token-panel
styles that are NOT scoped to those mode classes.

Usage:  python3 apply-css-links.py DIR_WITH_HTMLS
"""
import os
import re
import sys


LINK_TAGS = (
    '<!-- Phosphor icon font (used by both OSUI 2.28 and 2.29 after FA→Phosphor swap) -->\n'
    '<link rel="stylesheet" href="assets/phosphor/phosphor.css">\n'
    '<!-- Real OSUI CSS — scoped to #previewWrapper.{current-mode,new-tokens-mode,proposed-mode} -->\n'
    '<link rel="stylesheet" href="assets/os-ui/os-ui-228-current-scoped.css">\n'
    '<link rel="stylesheet" href="assets/os-ui/os-ui-229-proposed-scoped.css">\n'
)

MODE_PREFIXES = (
    '#previewWrapper.current-mode',
    '#previewWrapper.proposed-mode',
)


def strip_mode_rules(css: str) -> str:
    """Walk CSS top-level, drop any rule whose selector list contains ONLY
    mode-scoped selectors. If a rule mixes mode and non-mode selectors, keep
    only the non-mode ones."""
    out = []
    i, n = 0, len(css)

    while i < n:
        ch = css[i]

        if ch.isspace():
            out.append(ch)
            i += 1
            continue

        if css[i:i+2] == '/*':
            end = css.find('*/', i+2)
            if end == -1:
                out.append(css[i:])
                break
            out.append(css[i:end+2])
            i = end + 2
            continue

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

            if kw in ('@keyframes', '@-webkit-keyframes', '@font-face',
                     '@counter-style', '@property', '@page', '@viewport'):
                out.append(css[i:block_end])
            elif kw in ('@media', '@supports', '@container', '@layer'):
                inner = strip_mode_rules(body)
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

        sel = css[i:j]
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

        # Split selectors, keep only non-mode ones
        parts = split_top_level(sel)
        kept = [p for p in parts if not is_mode_selector(p)]
        if kept:
            new_sel = ','.join(kept)
            out.append(f'{new_sel}{{{body}}}')
        # else: drop entirely

        i = rule_end

    return ''.join(out)


def split_top_level(text: str):
    parts, depth, cur = [], 0, ''
    for c in text:
        if c in '([': depth += 1; cur += c
        elif c in ')]': depth -= 1; cur += c
        elif c == ',' and depth == 0:
            parts.append(cur); cur = ''
        else:
            cur += c
    if cur: parts.append(cur)
    return parts


def is_mode_selector(sel: str) -> bool:
    s = sel.strip()
    return any(s.startswith(p) for p in MODE_PREFIXES)


def inject_links(html: str) -> str:
    if 'os-ui-228-current-scoped.css' in html:
        return html  # already done
    # Insert after </title>
    m = re.search(r'</title>\s*\n', html)
    if not m:
        # fallback: after charset
        m = re.search(r'(<meta charset[^>]*>\s*\n)', html)
        if not m:
            # last resort: after <head>
            m = re.search(r'<head>\s*\n', html)
            if not m:
                raise RuntimeError('Cannot find insertion point in HTML')
    return html[:m.end()] + LINK_TAGS + html[m.end():]


def transform_file(path: str):
    with open(path) as f:
        html = f.read()
    original = html

    # 1) Inject links
    html = inject_links(html)

    # 2) Strip mode rules from the first <style> block
    m = re.search(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    if m:
        style_content = m.group(1)
        new_content = strip_mode_rules(style_content)
        html = html[:m.start(1)] + new_content + html[m.end(1):]

    if html != original:
        with open(path, 'w') as f:
            f.write(html)
        return True
    return False


if __name__ == '__main__':
    target_dir = sys.argv[1]
    files = sorted(f for f in os.listdir(target_dir) if f.endswith('-tokens.html'))
    changed, skipped = 0, 0
    for f in files:
        path = os.path.join(target_dir, f)
        try:
            if transform_file(path):
                print(f'  updated:  {f}')
                changed += 1
            else:
                print(f'  skipped:  {f}  (no changes needed)')
                skipped += 1
        except Exception as e:
            print(f'  FAILED :  {f}  ({e})')
    print(f'\nTotal: {changed} updated, {skipped} skipped, {len(files)} scanned.')
