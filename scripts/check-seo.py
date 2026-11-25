#!/usr/bin/env python3
"""Static SEO checks: internal links resolve, JSON-LD parses, FAQ schema mirrors visible FAQ,
unique titles/descriptions, one H1 and no skipped heading levels, sitemap URLs exist, every guide has
inbound links, indexable pages carry canonical/hreflang/Open Graph/Twitter tags, guides have depth."""
import html
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
    # Cloudflare Pages serves /impressum for impressum.html (clean URLs).
    return p.is_file() or (p / 'index.html').is_file() or p.with_name(p.name + '.html').is_file()

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
    if d and not 120 <= len(html.unescape(d.group(1))) <= 160:
        warnings.append(f'{url}: description {len(d.group(1))} chars')
    head = text.split('</head>')[0]
    indexable = 'noindex' not in head
    if indexable:
        canonical = re.search(r'<link rel="canonical" href="([^"]+)">', head)
        if not canonical or canonical.group(1) != 'https://iptvkanal.de' + url:
            errors.append(f'{url}: canonical missing or not self-referencing')
        for tag in ('hreflang="de-DE"', 'hreflang="de-AT"', 'hreflang="de-CH"', 'hreflang="x-default"', 'property="og:image"', 'property="og:title"',
                    'property="og:description"', 'name="twitter:card"', 'name="twitter:title"', 'name="robots"'):
            if tag not in head:
                errors.append(f'{url}: missing {tag}')
        if t and len(html.unescape(t.group(1))) > 65:
            warnings.append(f'{url}: title {len(html.unescape(t.group(1)))} chars')
    main = re.search(r'<main.*?</main>', text, re.S)
    levels = [int(h) for h in re.findall(r'<h([1-6])[\s>]', main.group(0) if main else '')]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1:
            errors.append(f'{url}: heading jumps from h{a} to h{b}')
            break
    if 'guide-page' in text and '"CollectionPage"' not in text:  # hubs carry card lists instead
        prose = re.search(r'<section class="article".*?</section>', text, re.S).group(0)
        words = len(html.unescape(re.sub(r'<[^>]+>', ' ', prose)).split())
        if words < 450:
            errors.append(f'{url}: only {words} words in the article body')
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
