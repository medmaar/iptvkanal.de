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
from seo import content_core, content_apps, content_devices, content_extra, content_more, content_depth  # noqa: E402
from seo import content_local, content_devices2, content_apps2  # noqa: E402

DOMAIN = 'https://iptvkanal.de'
UPDATED_ISO = '2026-11-24'
UPDATED_DE = '24.11.2026'
OG_IMAGE = DOMAIN + '/assets/img/og-iptvkanal.jpg'
OG_ALT = 'IPTV Kanal – Fernsehen über das Internet in bis zu 4K'
ORG_ID = DOMAIN + '/#organization'
ORGANIZATION = {'@type': 'Organization', '@id': ORG_ID, 'name': 'IPTV Kanal', 'url': DOMAIN + '/',
                'logo': {'@type': 'ImageObject', 'url': DOMAIN + '/assets/favicon.svg'}, 'email': 'kontakt@iptvkanal.de',
                'contactPoint': {'@type': 'ContactPoint', 'contactType': 'customer support', 'email': 'kontakt@iptvkanal.de',
                                 'availableLanguage': ['de']}}
WEBSITE = {'@type': 'WebSite', '@id': DOMAIN + '/#website', 'name': 'IPTV Kanal', 'url': DOMAIN + '/', 'inLanguage': 'de-DE',
           'publisher': {'@id': ORG_ID}}

home = (ROOT / 'index.html').read_text()


def extract(pattern):
    return re.search(pattern, home, re.S).group(0)


styles = '\n  '.join(re.findall(r'<link rel="stylesheet" href="assets/[^"]+">', home)).replace('href="assets/', 'href="/assets/')
favicon = extract(r'<link rel="icon"[^>]+>').replace('href="assets/', 'href="/assets/')
sprite = extract(r'<svg width="0".*?</svg>')
header = extract(r'<header class="header"[^>]*>.*?</header>')
footer = extract(r'<footer class="footer">.*?</footer>')
script = extract(r'<script src="assets/main\.js[^"]*" defer></script>').replace('src="assets/', 'src="/assets/')

FONT_PRELOAD = ('<link rel="preload" href="/assets/fonts/sora-latin-variable.woff2" as="font" type="font/woff2" crossorigin>\n'
                '  <link rel="preload" href="/assets/fonts/inter-latin-variable.woff2" as="font" type="font/woff2" crossorigin>')

PAGES = (content_core.PAGES + content_apps.PAGES + content_devices.PAGES + content_extra.PAGES + content_more.PAGES
         + content_devices2.PAGES + content_apps2.PAGES + content_local.PAGES)
BY_SLUG = {p['slug']: p for p in PAGES}

HUBS = {
    'ratgeber': ('/ratgeber/', 'Ratgeber'),
    'geraete': ('/iptv-geraete/', 'Geräte'),
    'apps': ('/iptv-apps/', 'Apps'),
    'international': ('/iptv-international/', 'International'),
    'staedte': ('/iptv-staedte/', 'Städte'),
    'regionen': ('/iptv-regionen/', 'Regionen'),
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

# Depth additions from the SEO audit: lead overrides, extra sections and FAQs, outbound sources.
for _page in PAGES:
    _slug = _page['slug']
    if _slug in content_depth.LEAD:
        _page['lead'] = content_depth.LEAD[_slug]
    _page['sections'] = list(_page['sections']) + content_depth.EXTRA_SECTIONS.get(_slug, [])
    _page['faq'] = list(_page['faq']) + content_depth.EXTRA_FAQ.get(_slug, [])
    _page['sources'] = content_depth.SOURCES.get(_slug, [])


SPORT = ['iptv-fussball', 'iptv-sport', 'sky-iptv']


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
            ('Grundlagen &amp; Kauf', [p['slug'] for p in PAGES if p.get('parent') in ('ratgeber', None) and p['kind'] != 'hub' and p['slug'] != 'ratgeber' and p['slug'] not in SPORT]),
            ('Sport &amp; Pay-TV', SPORT),
            ('Geräte', ['iptv-geraete'] + [p['slug'] for p in PAGES if p.get('parent') == 'geraete']),
            ('Apps &amp; Player', ['iptv-apps'] + [p['slug'] for p in PAGES if p.get('parent') == 'apps']),
            ('International', ['iptv-international'] + [p['slug'] for p in PAGES if p.get('parent') == 'international']),
            ('Städte &amp; Regionen', ['iptv-staedte', 'iptv-regionen']),
        ]
    else:
        children = [p for p in PAGES if p.get('parent') == hub]
        names = list(dict.fromkeys(p.get('group') for p in children))
        groups = [(name, [p['slug'] for p in children if p.get('group') == name]) for name in names]
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
    canonical = DOMAIN + url(page['slug'])
    name = strip_tags(page['h1'])
    image = {'@type': 'ImageObject', 'url': OG_IMAGE, 'width': 1200, 'height': 630}
    webpage = {'@type': 'CollectionPage' if page['kind'] == 'hub' else 'WebPage', '@id': canonical + '#webpage',
               'url': canonical, 'name': strip_tags(page['title']), 'description': page['description'], 'inLanguage': 'de-DE',
               'isPartOf': {'@id': DOMAIN + '/#website'}, 'breadcrumb': {'@id': canonical + '#breadcrumb'},
               'primaryImageOfPage': image, 'dateModified': UPDATED_ISO}
    graph = [
        ORGANIZATION, WEBSITE, webpage,
        {'@type': 'BreadcrumbList', '@id': canonical + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': DOMAIN + href}
            for i, (n, href) in enumerate(crumbs)]},
        {'@type': 'FAQPage', '@id': canonical + '#faq', 'isPartOf': {'@id': canonical + '#webpage'}, 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in page['faq']]},
    ]
    if page['kind'] == 'hub':
        children = [s for s in re.findall(r'href="/([a-z0-9-]+)/"', hub_children(page))]
        webpage['mainEntity'] = {'@type': 'ItemList', 'numberOfItems': len(children), 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'url': DOMAIN + url(c), 'name': BY_SLUG[c]['card'][0]}
            for i, c in enumerate(children)]}
    else:
        graph.append({'@type': 'Article', '@id': canonical + '#article', 'headline': name, 'description': page['description'],
                      'inLanguage': 'de-DE', 'mainEntityOfPage': {'@id': canonical + '#webpage'}, 'image': image,
                      'datePublished': UPDATED_ISO, 'dateModified': UPDATED_ISO,
                      'author': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID}})
    if page['kind'] == 'money':
        graph.append({'@type': 'Service', '@id': canonical + '#service', 'name': 'IPTV Abo von IPTV Kanal', 'serviceType': 'IPTV',
                      'description': 'IPTV-Abonnement mit Live-TV, Filmen und Serien in bis zu 4K für 1 bis 5 Geräte, ohne automatische Verlängerung.',
                      'provider': {'@id': ORG_ID}, 'areaServed': {'@type': 'Country', 'name': 'Deutschland'},
                      'offers': {'@type': 'AggregateOffer', 'priceCurrency': 'EUR', 'lowPrice': '9', 'highPrice': '225',
                                 'offerCount': '20', 'url': DOMAIN + '/preise/'}})
    data = {'@context': 'https://schema.org', '@graph': graph}
    return '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=1).replace('</', '<\\/') + '\n</script>'


TRUST = ('<ul class="trust-row" aria-label="Ihre Vorteile bei IPTV Kanal">'
         + ''.join(f'<li><svg aria-hidden="true"><use href="#i-check-c"/></svg><span>{t}</span></li>' for t in (
             '<b>Kostenlos testen</b> ohne Zahlungsdaten',
             '<b>Einmal zahlen</b>, keine automatische Verlängerung',
             '<b>Deutscher Support</b> per E-Mail &amp; WhatsApp',
             '<b>1 bis 5 Geräte</b>, 4K inklusive'))
         + '</ul>')

INLINE_CTA = ('<div class="inline-cta"><p><strong>Direkt auf Ihrem Gerät ausprobieren:</strong> Testen Sie IPTV Kanal kostenlos und ohne '
              'Zahlungsdaten. Unser Support hilft per E-Mail oder WhatsApp bei der Einrichtung.</p>'
              '<div class="cta-pair"><a class="btn btn-primary" href="/kostenlos-testen/">Kostenlos testen <svg aria-hidden="true"><use href="#i-arrow"/></svg></a>'
              '<a class="btn btn-ghost" href="/preise/">Preise</a></div></div>')


def sources_html(page):
    if not page.get('sources'):
        return ''
    items = ''.join(f'<li><a href="{href}" rel="noopener" target="_blank">{html.escape(label, quote=False)}</a></li>'
                    for label, href in page['sources'])
    return ('\n<h2 id="quellen">Quellen und offizielle Websites</h2>\n'
            '<p>Weiterführende Informationen direkt bei Herstellern, Behörden und Nachschlagewerken:</p>'
            f'<ul class="source-list">{items}</ul>\n')


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
    {TRUST}
    <p class="page-meta">Aktualisiert am <time datetime="{UPDATED_ISO}">{UPDATED_DE}</time> · Lesezeit ca. {minutes} Min.</p>
  </div>
</section>''']
    toc = ''
    if len(page['sections']) >= 3:
        toc = ('<nav class="toc" aria-label="Inhaltsverzeichnis"><b>Inhalt</b><ol>'
               + ''.join(f'<li><a href="#{sid}">{strip_tags(h2)}</a></li>' for sid, h2, _ in page['sections'])
               + '<li><a href="#faq">Häufige Fragen</a></li></ol></nav>')
    prose = ''
    for i, (sid, h2, content) in enumerate(page['sections']):
        prose += f'\n<h2 id="{sid}">{h2}</h2>\n{content.strip()}\n'
        if i == 1 and len(page['sections']) >= 4:
            prose += INLINE_CTA + '\n'
    prose += sources_html(page)
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
  <link rel="alternate" hreflang="de" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">
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
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:alt" content="{og_alt}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og_image}">
  <meta name="twitter:image:alt" content="{og_alt}">
  {preload}
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
        og_image=OG_IMAGE, og_alt=OG_ALT, preload=FONT_PRELOAD, favicon=favicon, styles=styles, jsonld=jsonld(page), sprite=sprite, header=header,
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
