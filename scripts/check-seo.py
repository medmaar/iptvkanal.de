#!/usr/bin/env python3
"""Static SEO checks: internal links resolve, JSON-LD parses, FAQ schema mirrors visible FAQ,
unique titles/descriptions, one H1, sitemap URLs exist, and every guide has inbound links."""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors, warnings = [], []
pages = {}
for f in ROOT.rglob('*.html'):
    if '.git' in f.parts or 'node_modules' in f.parts:
        continue
    rel = '/' + str(f.relative_to(ROOT)).replace('index.html', '')
    pages[rel] = f.read_text()

def exists(path):
    path = path.split('#')[0].split('?')[0]
    if path in ('', '/go/wa'):
        return True
    p = ROOT / path.lstrip('/')
    return p.is_file() or (p / 'index.html').is_file()

inbound = defaultdict(set)
titles, descs = Counter(), Counter()
for url, text in pages.items():
    for href in re.findall(r'href="(/[^"]*)"', text):
        if not exists(href):
            errors.append(f'{url}: broken link {href}')
        target = href.split('#')[0].split('?')[0]
        if target != url:
            inbound[target].add(url)
    if url == '/404.html':
        continue
    h1 = len(re.findall(r'<h1[\s>]', text))
    if h1 != 1:
        errors.append(f'{url}: {h1} h1 elements')
    t = re.search(r'<title>(.*?)</title>', text)
    d = re.search(r'<meta name="description" content="(.*?)">', text)
    titles[t.group(1) if t else ''] += 1
    descs[d.group(1) if d else ''] += 1
    if t and len(t.group(1)) > 70:
        warnings.append(f'{url}: title {len(t.group(1))} chars')
    if d and not 110 <= len(d.group(1)) <= 175:
        warnings.append(f'{url}: description {len(d.group(1))} chars')
    visible = len(re.findall(r'<details>', text))
    schema_q = 0
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            data = json.loads(block.replace('<\\/', '</'))
        except json.JSONDecodeError as exc:
            errors.append(f'{url}: invalid JSON-LD ({exc})')
            continue
        nodes = data.get('@graph', [data])
        for node in nodes:
            if node.get('@type') == 'FAQPage':
                schema_q += len(node['mainEntity'])
    if visible and schema_q and visible != schema_q:
        errors.append(f'{url}: {visible} visible FAQ vs {schema_q} in schema')
    guide = (ROOT / url.lstrip('/') / 'index.html').is_file() and 'guide-page' in text
    if guide and not schema_q:
        errors.append(f'{url}: missing FAQPage schema')

for k, v in titles.items():
    if v > 1:
        errors.append(f'duplicate title x{v}: {k}')
for k, v in descs.items():
    if v > 1:
        errors.append(f'duplicate description x{v}: {k}')

sitemap = (ROOT / 'sitemap.xml').read_text()
locs = re.findall(r'<loc>https://iptvkanal\.de(/[^<]*)</loc>', sitemap)
for loc in locs:
    if not exists(loc):
        errors.append(f'sitemap: missing page {loc}')
for url, text in pages.items():
    if 'guide-page' in text and url not in locs:
        errors.append(f'{url}: not in sitemap')
    if 'guide-page' in text and len(inbound[url]) < 3:
        errors.append(f'{url}: only {len(inbound[url])} inbound links')

for w in warnings:
    print('WARN', w)
for e in errors:
    print('FAIL', e)
print(f'{len(pages)} pages, {len(locs)} sitemap URLs, {len(errors)} errors, {len(warnings)} warnings')
sys.exit(1 if errors else 0)
