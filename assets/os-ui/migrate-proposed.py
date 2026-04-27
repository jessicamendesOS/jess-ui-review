#!/usr/bin/env python3
"""
Migrate bespoke proposed-mode CSS from HTML inline styles into the proposed scoped CSS file.

For each *-tokens.html:
  1. Extract all CSS rules whose selector contains '#previewWrapper.proposed-mode'
  2. Append them (with a per-component section comment) to os-ui-229-proposed-scoped.css
  3. Remove those rules from the inline <style> block
  4. Replace the os-ui-229-proposed-scoped.css link with the new split links

Usage: python3 migrate-proposed.py DIR_WITH_HTMLS
"""
import os
import re
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEW_TOKENS_CSS = os.path.join(BASE_DIR, 'os-ui-229-new-tokens-scoped.css')
PROPOSED_BASE_CSS = os.path.join(BASE_DIR, 'os-ui-229-proposed-scoped-base.css')
PROPOSED_OUT_CSS = os.path.join(BASE_DIR, 'os-ui-229-proposed-scoped.css')

OLD_LINK = '<link rel="stylesheet" href="assets/os-ui/os-ui-229-proposed-scoped.css">'
NEW_LINKS = (
    '<link rel="stylesheet" href="assets/os-ui/os-ui-229-new-tokens-scoped.css">\n'
    '<link rel="stylesheet" href="assets/os-ui/os-ui-229-proposed-scoped.css">'
)


def split_top_level(text):
    parts, depth, cur = [], 0, ''
    for c in text:
        if c in '([': depth += 1; cur += c
        elif c in ')]': depth -= 1; cur += c
        elif c == ',' and depth == 0:
            parts.append(cur); cur = ''
        else:
            cur += c
    if cur:
        parts.append(cur)
    return parts


def is_proposed_selector(sel):
    return '#previewWrapper.proposed-mode' in sel.strip()


def partition_style(css):
    """Split inline CSS into (proposed_rules_text, remaining_css_text)."""
    proposed_chunks = []
    remaining_chunks = []
    i, n = 0, len(css)

    while i < n:
        ch = css[i]

        if ch.isspace():
            remaining_chunks.append(ch)
            i += 1
            continue

        if css[i:i+2] == '/*':
            end = css.find('*/', i+2)
            if end == -1:
                remaining_chunks.append(css[i:])
                break
            comment = css[i:end+2]
            # Comments before proposed blocks go to proposed
            remaining_chunks.append(comment)
            i = end + 2
            continue

        if ch == '@':
            m = re.match(r'@[\w-]+', css[i:])
            if not m:
                remaining_chunks.append(ch); i += 1; continue
            kw = m.group(0)
            j = i + len(kw)
            while j < n and css[j] not in '{;':
                j += 1
            if j >= n:
                remaining_chunks.append(css[i:]); break
            if css[j] == ';':
                remaining_chunks.append(css[i:j+1]); i = j+1; continue
            depth = 1; k = j+1
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
            remaining_chunks.append(css[i:k])
            i = k
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
            remaining_chunks.append(css[i:]); break

        sel_text = css[i:j]
        depth = 1; k = j+1
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
        full_rule = css[i:rule_end]

        parts = split_top_level(sel_text)
        proposed_parts = [p for p in parts if is_proposed_selector(p)]
        other_parts = [p for p in parts if not is_proposed_selector(p)]

        if proposed_parts and not other_parts:
            # Entire rule is proposed — move to proposed
            proposed_chunks.append(full_rule)
        elif proposed_parts and other_parts:
            # Mixed — split
            proposed_chunks.append(','.join(proposed_parts) + '{' + body + '}')
            remaining_chunks.append(','.join(other_parts) + '{' + body + '}')
        else:
            remaining_chunks.append(full_rule)

        i = rule_end

    return ''.join(proposed_chunks), ''.join(remaining_chunks)


def get_component_name(filename):
    """accordion-tokens.html -> Accordion"""
    base = os.path.basename(filename)
    name = base.replace('-tokens.html', '').replace('-', ' ').title()
    return name


def transform_html(path, proposed_collector):
    with open(path) as f:
        html = f.read()
    original = html

    # Extract and partition the inline style block
    m = re.search(r'(<style[^>]*>)(.*?)(</style>)', html, re.DOTALL)
    if m:
        style_open, style_content, style_close = m.group(1), m.group(2), m.group(3)
        proposed_css, remaining_css = partition_style(style_content)

        if proposed_css.strip():
            component = get_component_name(path)
            proposed_collector.append(
                f'\n/* ── {component} ─────────────────────────────────────── */\n'
                + proposed_css.strip()
                + '\n'
            )

        html = html[:m.start(1)] + style_open + remaining_css + style_close + html[m.end(3):]

    # Update the CSS link: replace old single link with split links
    if OLD_LINK in html:
        html = html.replace(OLD_LINK, NEW_LINKS)
    elif 'os-ui-229-proposed-scoped.css' in html and 'os-ui-229-new-tokens-scoped.css' not in html:
        # Partial match fallback
        html = re.sub(
            r'<link[^>]*os-ui-229-proposed-scoped\.css[^>]*>',
            NEW_LINKS,
            html
        )

    if html != original:
        with open(path, 'w') as f:
            f.write(html)
        return True
    return False


if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else '.'

    # Read base proposed CSS
    with open(PROPOSED_BASE_CSS) as f:
        base_css = f.read()

    files = sorted(f for f in os.listdir(target_dir) if f.endswith('-tokens.html'))
    proposed_collector = []
    changed, skipped = 0, 0

    for fname in files:
        path = os.path.join(target_dir, fname)
        try:
            if transform_html(path, proposed_collector):
                print(f'  updated:  {fname}')
                changed += 1
            else:
                print(f'  skipped:  {fname}')
                skipped += 1
        except Exception as e:
            print(f'  FAILED :  {fname}  ({e})')
            import traceback; traceback.print_exc()

    # Write final proposed scoped CSS
    bespoke_block = ''
    if proposed_collector:
        bespoke_block = (
            '\n\n/* ══════════════════════════════════════════════════════════\n'
            '   BESPOKE PROPOSED-MODE OVERRIDES (per component)\n'
            '   These extend / override the OSUI 2.29 base above.\n'
            '══════════════════════════════════════════════════════════ */\n'
            + ''.join(proposed_collector)
        )

    with open(PROPOSED_OUT_CSS, 'w') as f:
        f.write(base_css + bespoke_block)

    print(f'\nWrote {PROPOSED_OUT_CSS}')
    print(f'  Base CSS:    {len(base_css):,} chars')
    print(f'  Bespoke CSS: {len(bespoke_block):,} chars')
    print(f'\nTotal: {changed} HTMLs updated, {skipped} skipped.')
