#!/usr/bin/env python3
"""Build the German guide pages (Ratgeber) with the shared header, footer and sprite from index.html.

Content lives in scripts/seo/content_*.py. Every page gets BreadcrumbList + FAQPage JSON-LD that mirrors
the visible FAQ, related links, and the shared CTA. Also writes sitemap.xml.
Run after scripts/build-pages.py (which calls this script automatically).
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from seo import content_core, content_apps, content_devices, content_extra  # noqa: E402

DOMAIN = 'https://iptvkanal.de'
UPDATED_ISO = '2026-11-24'
UPDATED_DE = '24.11.2026'
OG_IMAGE = DOMAIN + '/assets/img/og-iptvkanal.jpg'

home = (ROOT / 'index.html').read_text()


def extract(pattern):
    return re.search(pattern, home, re.S).group(0)


styles = '\n  '.join(re.findall(r'<link rel="stylesheet" href="assets/[^"]+">', home)).replace('href="assets/', 'href="/assets/')
favicon = extract(r'<link rel="icon"[^>]+>').replace('href="assets/', 'href="/assets/')
sprite = extract(r'<svg width="0".*?</svg>')
header = extract(r'<header class="header"[^>]*>.*?</header>')
footer = extract(r'<footer class="footer">.*?</footer>')
script = extract(r'<script src="assets/main\.js[^"]*" defer></script>').replace('src="assets/', 'src="/assets/')

PAGES = content_core.PAGES + content_apps.PAGES + content_devices.PAGES + content_extra.PAGES
BY_SLUG = {p['slug']: p for p in PAGES}

HUBS = {
    'ratgeber': ('/ratgeber/', 'Ratgeber'),
    'geraete': ('/iptv-geraete/', 'Geräte'),
    'apps': ('/iptv-apps/', 'Apps'),
}

# The Ratgeber hub lists every guide.
RATGEBER = dict(
    slug='ratgeber', parent=None, kind='hub', hub='ratgeber',
    title='IPTV Ratgeber: Anleitungen, Apps, Geräte & Vergleiche',
    description='Der IPTV Ratgeber von IPTV Kanal: Was ist IPTV, beste IPTV Apps, Anleitungen für Fire TV, Samsung, LG, MAG und PC, M3U-Listen, 4K und Anbieter-Vergleich.',
    eyebrow='IPTV RATGEBER', h1='IPTV Ratgeber',
    lead='Alles, was Sie über IPTV wissen müssen – von den Grundlagen über die Einrichtung auf Ihrem Gerät bis zur Wahl des passenden Anbieters.',
    answer='Hier finden Sie alle Anleitungen von IPTV Kanal: Grundlagen wie „Was ist IPTV?“ und M3U-Listen, Schritt-für-Schritt-Anleitungen für Fire TV Stick, Samsung, LG, Android, Apple, MAG und PC, App-Anleitungen für IPTV Smarters Pro, TiviMate, Smart IPTV und weitere Player sowie Kaufhilfen zu Anbietern, 4K und Preisen.',
    sections=[],
    faq=[
        ('Wo fange ich als IPTV-Einsteiger an?', 'Lesen Sie zuerst „Was ist IPTV?“, wählen Sie dann in der Geräteübersicht Ihr Gerät und folgen Sie der Anleitung. Mit dem kostenlosen Test können Sie alles sofort ausprobieren.'),
        ('Welche IPTV App soll ich nehmen?', 'Das hängt vom Gerät ab: TiviMate oder IPTV Smarters Pro für Fire TV und Android TV, SET IPTV oder Flix IPTV für Samsung und LG, VLC für den PC. Die App-Übersicht zeigt alle Optionen.'),
        ('Hilft IPTV Kanal bei der Einrichtung?', 'Ja. Unser deutschsprachiger Support hilft per E-Mail und WhatsApp Schritt für Schritt bei der Einrichtung auf Ihrem Gerät.'),
    ],
    related=['was-ist-iptv', 'iptv-kaufen', 'iptv-fire-tv-stick', 'iptv-smarters-pro', 'tivimate', 'm3u-playlist'],
    card=('IPTV Ratgeber', 'Alle Anleitungen und Vergleiche auf einen Blick.'),
)
PAGES.append(RATGEBER)
BY_SLUG['ratgeber'] = RATGEBER


def url(slug):
    return f'/{slug}/'


def strip_tags(text):
    return html.unescape(re.sub(r'<[^>]+>', '', text)).strip()


def breadcrumb(page):
    trail = [('Start', '/')]
    parent = page.get('parent')
    chain = []
    while parent:
        hub_url, hub_name = HUBS[parent]
        chain.insert(0, (hub_name if parent != 'ratgeber' else 'Ratgeber', hub_url))
        parent = BY_SLUG[hub_url.strip('/')].get('parent')
    trail += chain
    trail.append((strip_tags(page['h1']), url(page['slug'])))
    return trail


def card_html(slug):
    target = BY_SLUG[slug]
    title, text = target['card']
    return (f'<a class="card" href="{url(slug)}"><h3>{title}</h3><p>{text}</p>'
            f'<span>Weiterlesen <svg aria-hidden="true" width="14" height="14"><use href="#i-arrow"/></svg></span></a>')


def hub_children(page):
    hub = page.get('hub')
    if hub == 'ratgeber':
        groups = [
            ('Grundlagen &amp; Kauf', [p['slug'] for p in PAGES if p.get('parent') in ('ratgeber', None) and p['kind'] != 'hub' and p['slug'] != 'ratgeber']),
            ('Geräte', ['iptv-geraete'] + [p['slug'] for p in PAGES if p.get('parent') == 'geraete']),
            ('Apps &amp; Player', ['iptv-apps'] + [p['slug'] for p in PAGES if p.get('parent') == 'apps']),
        ]
    else:
        groups = [(None, [p['slug'] for p in PAGES if p.get('parent') == hub])]
    out = ['<section class="related hub-list" aria-label="Alle Anleitungen"><div class="container">']
    for title, slugs in groups:
        if title:
            out.append(f'<h2 class="hub-title">{title}</h2>')
        out.append('<div class="link-grid">' + ''.join(card_html(s) for s in slugs) + '</div>')
    out.append('</div></section>')
    return '\n'.join(out)


def faq_section(page):
    items = ''.join(f'''
          <details>
            <summary>{html.escape(q, quote=False)}<i aria-hidden="true"></i></summary>
            <p>{html.escape(a, quote=False)}</p>
          </details>''' for q, a in page['faq'])
    return f'''<section class="faq-section" id="faq" aria-labelledby="faq-title">
      <div class="container container--narrow">
        <header class="section-head">
          <p class="eyebrow">FAQ</p>
          <h2 class="display" id="faq-title">Häufige Fragen</h2>
        </header>
        <div class="faq">{items}
        </div>
      </div>
    </section>'''


def jsonld(page):
    crumbs = breadcrumb(page)
    graph = [
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': name, 'item': DOMAIN + href}
            for i, (name, href) in enumerate(crumbs)]},
        {'@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in page['faq']]},
    ]
    canonical = DOMAIN + url(page['slug'])
    if page['kind'] == 'hub':
        graph.append({'@type': 'CollectionPage', 'name': strip_tags(page['h1']), 'url': canonical, 'inLanguage': 'de-DE',
                      'description': page['description']})
    else:
        graph.append({'@type': 'Article', 'headline': strip_tags(page['h1']), 'description': page['description'],
                      'inLanguage': 'de-DE', 'mainEntityOfPage': canonical, 'image': OG_IMAGE,
                      'datePublished': UPDATED_ISO, 'dateModified': UPDATED_ISO,
                      'author': {'@type': 'Organization', 'name': 'IPTV Kanal', 'url': DOMAIN + '/'},
                      'publisher': {'@type': 'Organization', 'name': 'IPTV Kanal', 'url': DOMAIN + '/'}})
    data = {'@context': 'https://schema.org', '@graph': graph}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1).replace('</', '<\\/') + '\n</script>'


def body(page):
    crumbs = breadcrumb(page)
    crumb_html = ''.join(
        f'<li><a href="{href}">{html.escape(name, quote=False)}</a></li>' if i < len(crumbs) - 1
        else f'<li aria-current="page">{html.escape(name, quote=False)}</li>' for i, (name, href) in enumerate(crumbs))
    words = len(strip_tags(' '.join(s[2] for s in page['sections']) + page['answer'] + ' '.join(q + a for q, a in page['faq'])).split())
    minutes = max(2, round(words / 200))
    parts = [f'''<section class="page-hero seo-hero" aria-labelledby="page-title">
  <div class="container">
    <nav aria-label="Brotkrümelnavigation"><ol class="breadcrumb">{crumb_html}</ol></nav>
    <span class="eyebrow">{page['eyebrow']}</span>
    <h1 class="display" id="page-title">{page['h1']}</h1>
    <p class="lead">{page['lead']}</p>
    <div class="hero-actions cta-pair"><a class="btn btn-primary" href="/kostenlos-testen/">Kostenlos testen <svg aria-hidden="true"><use href="#i-arrow"/></svg></a><a class="btn btn-ghost" href="/preise/">Preise</a></div>
    <p class="page-meta">Aktualisiert am <time datetime="{UPDATED_ISO}">{UPDATED_DE}</time> · Lesezeit ca. {minutes} Min.</p>
  </div>
</section>''']
    toc = ''
    if len(page['sections']) >= 3:
        toc = ('<nav class="toc" aria-label="Inhaltsverzeichnis"><b>Inhalt</b><ol>'
               + ''.join(f'<li><a href="#{sid}">{strip_tags(h2)}</a></li>' for sid, h2, _ in page['sections'])
               + '<li><a href="#faq">Häufige Fragen</a></li></ol></nav>')
    prose = ''.join(f'\n<h2 id="{sid}">{h2}</h2>\n{content.strip()}\n' for sid, h2, content in page['sections'])
    parts.append(f'''<section class="article" aria-label="Ratgeber">
  <div class="container">
    <div class="answer-box"><b>Kurz erklärt</b><p>{page['answer']}</p></div>
    {toc}
    <div class="prose">{prose}</div>
  </div>
</section>''')
    if page.get('pricing'):
        parts.append(PRICING_SECTION)
    if page['kind'] == 'hub':
        parts.append(hub_children(page))
    parts.append(faq_section(page))
    related = [s for s in page['related'] if s in BY_SLUG and s != page['slug']]
    parts.append(f'''<section class="related" aria-labelledby="related-title"><div class="container">
  <div class="section-head"><span class="eyebrow">WEITERLESEN</span><h2 class="display" id="related-title">Passende Ratgeber</h2></div>
  <div class="link-grid">{''.join(card_html(s) for s in related)}</div>
</div></section>''')
    parts.append(CTA)
    return '\n'.join(parts)


PRICING_SECTION = re.sub(r'<div class="section-head reveal">.*?</div>\s*', '', extract(r'<section id="preise".*?</section>'), count=1, flags=re.S)
CTA = re.search(r'<section id="kontakt">.*?</section>', home, re.S).group(0).replace('<section id="kontakt">', '<section class="cta-section">')

PAGE = '''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#0d0e14">
  {favicon}
  <meta property="og:type" content="{og_type}">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="IPTV Kanal">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="IPTV Kanal – Fernsehen über das Internet">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image}">
  {styles}
  {jsonld}
</head>
<body class="subpage guide-page">
<a class="skip" href="#main">Zum Inhalt springen</a>
{sprite}
{header}
<main id="main">
{body}
</main>
{footer}
{script}
</body>
</html>
'''

for page in PAGES:
    out = ROOT / page['slug'] / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    text = PAGE.format(
        title=html.escape(strip_tags(page['title'])), description=html.escape(page['description']),
        canonical=DOMAIN + url(page['slug']), og_type='website' if page['kind'] in ('hub', 'money') else 'article',
        og_image=OG_IMAGE, favicon=favicon, styles=styles, jsonld=jsonld(page), sprite=sprite, header=header,
        footer=footer, script=script, body=body(page))
    out.write_text('\n'.join(line.rstrip() for line in text.splitlines()) + '\n')
print(f'Built {len(PAGES)} guide pages')

# Sitemap: every indexable URL. lastmod only for pages changed in this build.
static = [('/', '1.0', 'weekly'), ('/preise/', '0.9', 'weekly'), ('/kostenlos-testen/', '0.9', 'monthly'),
          ('/bestellen/1-monat/', '0.6', 'monthly'), ('/bestellen/3-monate/', '0.6', 'monthly'),
          ('/bestellen/6-monate/', '0.6', 'monthly'), ('/bestellen/1-jahr/', '0.7', 'monthly')]
priority = {'money': '0.9', 'hub': '0.8', 'guide': '0.7'}
entries = static + [(url(p['slug']), priority[p['kind']], 'monthly') for p in PAGES]
lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc, prio, freq in entries:
    lines.append(f'  <url><loc>{DOMAIN}{loc}</loc><lastmod>{UPDATED_ISO}</lastmod><changefreq>{freq}</changefreq><priority>{prio}</priority></url>')
lines.append('</urlset>')
(ROOT / 'sitemap.xml').write_text('\n'.join(lines) + '\n')
print(f'Wrote sitemap.xml with {len(entries)} URLs')
