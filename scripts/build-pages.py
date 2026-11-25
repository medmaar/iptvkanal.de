#!/usr/bin/env python3
"""Build pricing, trial and individual order pages with shared navigation."""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
home = (ROOT / 'index.html').read_text()
sys.path.insert(0, str(ROOT / 'scripts'))
from seo.helpers import steps, checks, table  # noqa: E402

DOMAIN = 'https://iptvkanal.de'
OG_IMAGE = DOMAIN + '/assets/img/og-iptvkanal.jpg'
OG_ALT = 'IPTV Kanal – Fernsehen über das Internet in bis zu 4K'
# Same prices as assets/main.js (PRICES) and the homepage plan cards.
PRICES = {1: [9, 29, 39, 49], 2: [18, 50, 69, 89], 3: [27, 75, 105, 135], 4: [36, 99, 140, 180], 5: [45, 120, 175, 225]}
TERMS = [(1, '1-monat', '1 Monat'), (3, '3-monate', '3 Monate'), (6, '6-monate', '6 Monate'), (12, '1-jahr', '1 Jahr')]
ORG = {'@type': 'Organization', '@id': DOMAIN + '/#organization', 'name': 'IPTV Kanal', 'url': DOMAIN + '/',
       'logo': {'@type': 'ImageObject', 'url': DOMAIN + '/assets/favicon.svg'}, 'email': 'kontakt@iptvkanal.de'}
TRUST = ('<ul class="trust-row" aria-label="Ihre Vorteile bei IPTV Kanal">'
         + ''.join(f'<li><svg aria-hidden="true"><use href="#i-check-c"/></svg><span>{t}</span></li>' for t in (
             '<b>Kostenlos testen</b> ohne Zahlungsdaten',
             '<b>Einmal zahlen</b>, keine automatische Verlängerung',
             '<b>Deutscher Support</b> per E-Mail &amp; WhatsApp',
             '<b>1 bis 5 Geräte</b>, 4K inklusive'))
         + '</ul>')


def euro(value):
    return f'{value:.2f}'.replace('.', ',') + ' €'


def ld(graph):
    return ('<script type="application/ld+json">'
            + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('</', '<\\/')
            + '</script>')


def crumbs(*items):
    return {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': name, 'item': DOMAIN + path} for i, (name, path) in enumerate(items)]}


def faq_ld(items):
    return {'@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}


def faq_html(items, title):
    return ('<section class="faq-section" id="faq" aria-labelledby="faq-title">\n  <div class="container container--narrow">\n'
            f'    <header class="section-head"><p class="eyebrow">FAQ</p><h2 class="display" id="faq-title">{title}</h2></header>\n'
            '    <div class="faq">' + ''.join(f'<details><summary>{html.escape(q, quote=False)}<i aria-hidden="true"></i></summary><p>{html.escape(a, quote=False)}</p></details>' for q, a in items)
            + '</div>\n  </div>\n</section>')


def extract(pattern):
    return re.search(pattern, home, re.S).group(0)


styles = '\n  '.join(re.findall(r'<link rel="stylesheet" href="assets/[^"]+">', home)).replace('href="assets/', 'href="/assets/')
favicon = extract(r'<link rel="icon"[^>]+>').replace('href="assets/', 'href="/assets/')
sprite = extract(r'<svg width="0".*?</svg>')
header = extract(r'<header class="header"[^>]*>.*?</header>')
footer = extract(r'<footer class="footer">.*?</footer>')
script = extract(r'<script src="assets/main\.js[^"]*" defer></script>').replace('src="assets/', 'src="/assets/')
pricing = extract(r'<section id="preise".*?</section>')

PAGE = '''<!doctype html>
<html lang="de">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <link rel="canonical" href="https://iptvkanal.de{path}">
  <link rel="alternate" hreflang="de-DE" href="https://iptvkanal.de{path}">
  <link rel="alternate" hreflang="de-AT" href="https://iptvkanal.de{path}">
  <link rel="alternate" hreflang="de-CH" href="https://iptvkanal.de{path}">
  <link rel="alternate" hreflang="x-default" href="https://iptvkanal.de{path}">
  <meta name="theme-color" content="#0d0e14">
  {favicon}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="IPTV Kanal">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://iptvkanal.de{path}">
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
  <link rel="preload" href="/assets/fonts/sora-latin-variable.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/inter-latin-variable.woff2" as="font" type="font/woff2" crossorigin>
  {styles}
  {extra_head}
</head>
<body class="subpage">
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


def request_form(kind, months=1, term='', price=0):
    order = kind == 'order'
    subject = f'iptvkanal.de - {term} - 1 Gerät — {price} €' if order else 'iptvkanal.de - Kostenloser Test — 0 €'
    fields = '''
      <label class="field"><span>Name</span><input type="text" name="name" autocomplete="name" maxlength="160"></label>
      <label class="field"><span>E-Mail-Adresse</span><input type="email" name="email" autocomplete="email" inputmode="email" maxlength="254"></label>
      <label class="field"><span>WhatsApp-Nummer</span><input type="tel" name="phone" autocomplete="tel" inputmode="tel" placeholder="+49 …" maxlength="80"></label>
      <label class="field"><span>Notiz</span><textarea name="note" rows="4" maxlength="4000" placeholder="Ihre Wünsche oder Fragen"></textarea></label>'''
    return f'''
    <form id="request-form" class="signup-form" data-request-form {'data-order-form' if order else ''} novalidate action="https://api.emailjs.com/api/v1.0/email/send-form" method="post" enctype="multipart/form-data" aria-describedby="request-help">
      <p class="form-help" id="request-help">Alle Angaben sind freiwillig. Für die Zusendung Ihres Zugangs können Sie E-Mail oder WhatsApp angeben.</p>
      {f'<input type="hidden" name="devices" value="1"><input type="hidden" name="months" value="{months}">' if order else ''}
      <input type="hidden" name="service_id" value="service_ehcnxxv">
      <input type="hidden" name="template_id" value="template_bfl916q">
      <input type="hidden" name="user_id" value="uTqKLVjvvwWeSZxdN">
      <input type="hidden" name="to_email" value="kontakt@iptvkanal.de">
      <input type="hidden" name="reply_to" value="kontakt@iptvkanal.de">
      <input type="hidden" name="subject" value="{subject}">
      <input type="hidden" name="title" value="{subject}">
      {fields}
      <label class="hp" aria-hidden="true">Bitte leer lassen<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
      <p class="form-error" data-form-error role="alert" hidden></p>
      <div class="request-fallback" data-request-fallback hidden><p>Alternativ können Sie Ihre Anfrage per E-Mail übermitteln:</p><a data-mail-fallback href="mailto:kontakt@iptvkanal.de">Anfrage per E-Mail senden</a></div>
      <button class="btn btn-primary btn-block" type="submit"><span>{'Paket anfragen' if order else 'Kostenlosen Test anfragen'}</span> <svg aria-hidden="true"><use href="#i-arrow"/></svg></button>
      <p class="form-legal">Ihre Angaben verwenden wir zur Bearbeitung Ihrer Anfrage. Mehr dazu in der <a href="/datenschutz">Datenschutzerklärung</a>.</p>
    </form>
    <div class="signup-success" data-request-success tabindex="-1" hidden>
      <div class="success-check" aria-hidden="true"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46"/><path d="M28 52l16 16 30-34"/></svg></div>
      <h2>Anfrage erhalten</h2>
      <p>Vielen Dank! Ihre Anfrage wurde übermittelt.</p>
      <p class="muted">Wenn Sie E-Mail oder WhatsApp angegeben haben, melden wir uns darüber bei Ihnen.</p>
    </div>'''


TRIAL_FAQ = [
    ('Ist der IPTV-Test wirklich kostenlos?', 'Ja. Der Testzugang kostet nichts, und Sie geben keine Zahlungsdaten an. Es entsteht kein Abo.'),
    ('Wie lange dauert der IPTV-Test?', 'Der Testzugang ist zeitlich begrenzt und reicht, um Sender, Bildqualität und Stabilität auf Ihrem Gerät zu prüfen. Die genaue Dauer nennen wir Ihnen mit den Zugangsdaten.'),
    ('Welche Apps kann ich für die Testline nutzen?', 'Alle gängigen IPTV-Apps wie IPTV Smarters Pro, TiviMate, Smart IPTV, SET IPTV, Flix IPTV, VLC sowie MAG-Boxen.'),
    ('Verlängert sich der Test automatisch in ein Abo?', 'Nein. Nach dem Test entscheiden Sie selbst, ob Sie ein Paket bestellen. Auch die Pakete verlängern sich nicht automatisch.'),
    ('Was ist eine IPTV Testline?', 'Eine IPTV Testline ist ein zeitlich begrenzter Testzugang mit echten Zugangsdaten. Sie tragen ihn wie ein normales Abo in Ihre App ein und prüfen Sender, Bildqualität und Stabilität, bevor Sie kaufen.'),
    ('Gibt es einen IPTV 24h Test?', 'Viele Anbieter nennen ihren Test „24h Test“ oder „Test 24“. Unser Testzugang ist ebenfalls zeitlich begrenzt und reicht für einen vollständigen Abend zur Hauptsendezeit. Die genaue Dauer nennen wir Ihnen mit den Zugangsdaten.'),
    ('Kann ich 4K im Test ausprobieren?', 'Ja. 4K-Sender sind auch im Test enthalten. Für flüssiges 4K empfehlen wir mindestens 25 Mbit/s.'),
]
TRIAL_JSONLD = ld([
    {'@type': 'WebPage', '@id': DOMAIN + '/kostenlos-testen/#webpage', 'url': DOMAIN + '/kostenlos-testen/',
     'name': 'IPTV kostenlos testen', 'inLanguage': 'de-DE', 'isPartOf': {'@id': DOMAIN + '/#website'}},
    faq_ld(TRIAL_FAQ),
    crumbs(('Start', '/'), ('IPTV kostenlos testen', '/kostenlos-testen/'))])


trial = '''<section class="signup-page" aria-labelledby="trial-title">
  <div class="container trial-wrap">
    <div class="trial-summary">
      <span class="eyebrow">IHR KOSTENLOSER TESTZUGANG</span>
      <h1 class="display" id="trial-title">IPTV kostenlos testen</h1>
      <div class="trial-price"><b>0</b><span>€</span></div>
      <p class="trial-meta">Live-TV, Sport, Filme und Serien kennenlernen. Ohne Zahlungsdaten.</p>
      <p class="order-instructions">Formular ausfüllen und absenden. Ihren Testzugang erhalten Sie anschließend per E-Mail oder WhatsApp.</p>
      ''' + TRUST + '''
    </div>''' + request_form('trial') + '''
  </div>
</section>
<section class="article trial-info" aria-labelledby="trial-info-title">
  <div class="container">
    <div class="answer-box"><b>Kurz erklärt</b><p>Der IPTV-Test von IPTV Kanal ist kostenlos und ohne Zahlungsdaten. Sie erhalten eine Testline mit Zugangsdaten für Ihre App und prüfen Sender, Bildqualität bis 4K, Programmführer und Stabilität auf Ihrem eigenen Gerät, bevor Sie ein Paket wählen.</p></div>
    <div class="prose">
      <h2 id="trial-info-title">So läuft Ihr kostenloser IPTV-Test ab</h2>
      <ol class="howto">
        <li><b>Anfrage senden:</b> Formular oben ausfüllen. Name, E-Mail oder WhatsApp genügen.</li>
        <li><b>Testline erhalten:</b> Sie bekommen Zugangsdaten als Xtream-Codes-Login oder <a href="/m3u-playlist/">M3U-Link</a>.</li>
        <li><b>App einrichten:</b> zum Beispiel <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>, <a href="/tivimate/">TiviMate</a> oder <a href="/smart-iptv/">Smart IPTV</a>.</li>
        <li><b>Testen:</b> Live-TV, Filme, Serien und <a href="/iptv-4k/">4K-Sender</a> auf Ihrem Gerät ausprobieren.</li>
      </ol>
      <h2 id="testline">IPTV Testline, 24h Test oder Free Trial: was ist der Unterschied?</h2>
      <p>Ob „IPTV Testline“, „Test Line“, „IPTV 24h Test“, „Free Trial“ oder „IPTV gratis testen“: Gemeint ist fast immer dasselbe – ein kurzer, kostenloser Zugang mit echten Zugangsdaten. Bei IPTV Kanal ist die Testline technisch identisch mit einem bezahlten Paket. Sie sehen also genau die Senderliste, die Bildqualität bis 4K und den Programmführer, die Sie später bekommen. Welche Sendergruppen enthalten sind und wie Sie sie sortieren, erklärt der Ratgeber <a href="/iptv-senderliste/">IPTV Senderliste</a>.</p>
      <p>Seien Sie bei Angeboten vorsichtig, die für einen „Premium-Test“ eine Gebühr oder Zahlungsdaten verlangen. Ein seriöser IPTV-Test ist kostenlos und verlängert sich nicht in ein Abo. Wie Sie Erfahrungsberichte anderer Nutzer einordnen, steht unter <a href="/iptv-erfahrungen/">IPTV Erfahrungen</a>.</p>
      <h2 id="test-tipps">Worauf Sie beim IPTV-Test achten sollten</h2>
      <ul>
        <li>Testen Sie abends zur Hauptsendezeit – dann zeigt sich, wie stabil ein IPTV-Anbieter wirklich ist.</li>
        <li>Prüfen Sie die Umschaltzeit zwischen Sendern und den Programmführer.</li>
        <li>Verbinden Sie Ihr Gerät möglichst per LAN-Kabel, besonders für 4K.</li>
        <li>Nutzen Sie die Bewertungsmatrix aus unserem <a href="/iptv-anbieter-vergleich/">IPTV-Anbieter-Vergleich</a>.</li>
      </ul>
      <h2 id="test-geraete">Anleitungen für Ihr Gerät</h2>
      <p>Schritt-für-Schritt-Hilfe finden Sie für den <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, andere <a href="/iptv-stick/">IPTV Sticks</a>, <a href="/formuler-iptv/">Formuler-Boxen</a>, <a href="/iptv-samsung-tv/">Samsung TV</a>, <a href="/iptv-lg-tv/">LG TV</a>, <a href="/iptv-android/">Android</a>, <a href="/iptv-apple-tv-iphone/">Apple TV und iPhone</a>, <a href="/mag-box-iptv/">MAG-Boxen</a> und den <a href="/iptv-pc-mac/">PC</a>. Nach dem Test wählen Sie Ihr Paket unter <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>
    </div>
  </div>
</section>
''' + faq_html(TRIAL_FAQ, 'Häufige Fragen zum IPTV-Test')

PRICE_FAQ = [
    ('Was kostet IPTV bei IPTV Kanal?', 'Ab 9 € für einen Monat mit einem Gerät. 3 Monate kosten 29 €, 6 Monate 39 € und 1 Jahr 49 €. Für 2 bis 5 gleichzeitige Geräte gibt es eigene Paketpreise, zum Beispiel 89 € für ein Jahr mit 2 Geräten.'),
    ('Verlängert sich mein IPTV-Paket automatisch?', 'Nein. Sie zahlen einmalig für die gewählte Laufzeit. Es gibt kein Abo und keine Kündigungsfrist; nach Ablauf entscheiden Sie selbst, ob Sie verlängern.'),
    ('Wie bezahle ich mein Paket?', 'Sie senden auf der Paketseite eine Anfrage. Wir melden uns per E-Mail oder WhatsApp mit Ihren Zugangsdaten und den Angaben zur Bezahlung. Eine Zahlung wird erst nach dieser Bestätigung fällig.'),
    ('Kann ich vor dem Kauf testen?', 'Ja. Der kostenlose Testzugang funktioniert ohne Zahlungsdaten. So prüfen Sie Sender, Bildqualität und Stabilität auf Ihrem eigenen Gerät, bevor Sie ein Paket wählen.'),
    ('Was bedeutet „Geräte gleichzeitig“?', 'Die Geräteanzahl legt fest, wie viele Streams parallel laufen dürfen. Installieren können Sie die App auf beliebig vielen eigenen Geräten; gleichzeitig schauen so viele, wie Ihr Paket erlaubt.'),
    ('Ist 4K in allen Paketen enthalten?', 'Ja. 20.000+ Sender, Filme und Serien, 4K-Qualität, Programmführer (EPG) und Catch-Up sind in jedem Paket enthalten – unabhängig von Laufzeit und Geräteanzahl.'),
]

price_rows = [[f'{d} {"Gerät" if d == 1 else "Geräte"}'] + [f'{v} €' for v in PRICES[d]] for d in PRICES]
monthly_rows = [[term, f'{PRICES[1][i]} €', euro(PRICES[1][i] / months),
                 '–' if months == 1 else f'{round((1 - PRICES[1][i] / (PRICES[1][0] * months)) * 100)} %']
                for i, (months, _, term) in enumerate(TERMS)]

pricing_info = ('''<section class="article trial-info" aria-labelledby="price-info-title">
  <div class="container">
    <div class="answer-box"><b>Kurz erklärt</b><p>IPTV bei IPTV Kanal kostet ab 9 € für einen Monat und ein Gerät. Im Jahrespaket zahlen Sie 49 €, umgerechnet 4,08 € pro Monat. Jedes Paket enthält 20.000+ Sender, Filme und Serien in bis zu 4K, Programmführer und deutschsprachigen Support. Sie zahlen einmalig, ohne Vertrag und ohne automatische Verlängerung.</p></div>
    <div class="prose">
      <h2 id="price-info-title">IPTV Preise für alle Laufzeiten und Geräte</h2>
      <p>Der Preis hängt von zwei Dingen ab: der Laufzeit und der Anzahl der Geräte, die gleichzeitig schauen. Längere Laufzeiten sind deutlich günstiger pro Monat. Die Tabelle zeigt alle 20 Paketpreise auf einen Blick.</p>
      ''' + table(['Geräte gleichzeitig', '1 Monat', '3 Monate', '6 Monate', '1 Jahr'], price_rows, 'IPTV-Kanal-Preise nach Laufzeit und Geräteanzahl') + '''
      <h2 id="pro-monat">Was kostet IPTV pro Monat?</h2>
      ''' + table(['Laufzeit (1 Gerät)', 'Paketpreis', 'Pro Monat', 'Ersparnis ggü. Monatspaket'], monthly_rows, 'IPTV Preis pro Monat') + '''
      <p>Das <a href="/bestellen/1-jahr/">Jahrespaket</a> ist die günstigste Wahl für alle, die dauerhaft schauen. Wer nach dem Test erst einmal im Alltag ausprobieren möchte, startet mit <a href="/bestellen/1-monat/">einem Monat</a>. Warum seriöse Anbieter keine „Lifetime“-Angebote machen, erklärt der Ratgeber <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>
      <h2 id="enthalten">Das ist in jedem IPTV-Paket enthalten</h2>
      ''' + checks('<strong>20.000+ Sender</strong> aus Deutschland und aller Welt – siehe <a href="/iptv-senderliste/">IPTV Senderliste</a>',
                   '<strong>Filme und Serien</strong> auf Abruf (VOD)',
                   '<strong>4K Ultra HD</strong> bei passenden Sendern – mehr unter <a href="/iptv-4k/">IPTV in 4K</a>',
                   '<strong>Programmführer (EPG) und Catch-Up</strong>',
                   '<strong>Alle gängigen Geräte und Apps</strong>: Smart TV, <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, Android, Apple, MAG und PC',
                   '<strong>Deutschsprachiger Support</strong> per E-Mail und WhatsApp, inklusive Einrichtungshilfe') + '''
      <h2 id="ablauf">Bestellung und Bezahlung in drei Schritten</h2>
      ''' + steps('<b>Paket wählen:</b> Geräteanzahl oben einstellen und auf Ihr Wunschpaket klicken.',
                  '<b>Anfrage senden:</b> Auf der Paketseite Name und E-Mail oder WhatsApp angeben – alle Felder sind freiwillig.',
                  '<b>Zugang erhalten:</b> Wir melden uns mit Ihren Zugangsdaten und den Angaben zur Bezahlung. Danach richten Sie Ihre <a href="/iptv-apps/">IPTV App</a> ein.') + '''
      <p>Noch unsicher? Mit dem <a href="/kostenlos-testen/">kostenlosen IPTV-Test</a> prüfen Sie alles vorab auf Ihrem eigenen Gerät – ohne Zahlungsdaten und ohne Abo.</p>
    </div>
  </div>
</section>
''' + faq_html(PRICE_FAQ, 'Häufige Fragen zu Preisen und Bezahlung'))

pricing_page = '''<section class="page-intro" aria-labelledby="pricing-page-title">
  <div class="container trial-wrap trial-summary">
    <span class="eyebrow">IHR PAKET. IHRE WAHL.</span>
    <h1 class="display" id="pricing-page-title">IPTV Preise &amp; Pakete</h1>
    <div class="trial-price"><small>ab</small><b data-starting-price>9</b><span>€</span></div>
    <p class="trial-meta">Einmal zahlen. Keine automatische Verlängerung.</p>
    <p class="order-instructions">Wählen Sie die Anzahl Ihrer Geräte und klicken Sie auf Ihr Wunschpaket. Auf der eigenen Paketseite können Sie Ihre Bestellung absenden.</p>
    ''' + TRUST + '''
  </div>
</section>
''' + pricing + '\n' + pricing_info

PRICING_JSONLD = ld([
    ORG,
    {'@type': 'WebPage', '@id': DOMAIN + '/preise/#webpage', 'url': DOMAIN + '/preise/', 'name': 'IPTV Preise & Pakete',
     'inLanguage': 'de-DE', 'isPartOf': {'@id': DOMAIN + '/#website'}, 'mainEntity': {'@id': DOMAIN + '/preise/#product'}},
    {'@type': 'Product', '@id': DOMAIN + '/preise/#product', 'name': 'IPTV Kanal Abonnement',
     'description': 'IPTV-Paket mit 20.000+ Sendern, Filmen und Serien in bis zu 4K für 1 bis 5 Geräte. Einmalig bezahlt, ohne automatische Verlängerung.',
     'image': OG_IMAGE, 'brand': {'@type': 'Brand', 'name': 'IPTV Kanal'},
     'offers': [{'@type': 'Offer', 'name': f'{term} IPTV – 1 Gerät', 'price': str(PRICES[1][i]), 'priceCurrency': 'EUR',
                 'availability': 'https://schema.org/InStock', 'url': f'{DOMAIN}/bestellen/{slug}/', 'seller': {'@id': DOMAIN + '/#organization'}}
                for i, (_, slug, term) in enumerate(TERMS)]},
    faq_ld(PRICE_FAQ),
    crumbs(('Start', '/'), ('IPTV Preise', '/preise/'))])

# Plan-specific copy keeps the four order pages distinct from each other.
PLAN_COPY = {
    1: ('Für wen eignet sich 1 Monat IPTV?',
        'Das Monatspaket ist ideal, wenn Sie IPTV nach dem kostenlosen Test im Alltag ausprobieren möchten oder nur für einen bestimmten Zeitraum schauen – etwa während eines Turniers, eines Urlaubs oder bis zum Umzug. Sie zahlen einmalig 9 € für ein Gerät und gehen keine Verpflichtung ein. Wer danach weiterschauen möchte, wechselt einfach auf ein längeres Paket und spart pro Monat.'),
    3: ('Für wen eignet sich 3 Monate IPTV?',
        'Drei Monate sind der Einstieg für alle, die nach dem Test über mehrere Wochen und viele Abende prüfen möchten, ob Sender, Mediathek und Stabilität dauerhaft passen. Das Paket kostet 29 € für ein Gerät, läuft ohne Unterbrechung und passt gut zu einer Sport-Saisonphase oder zum Start in Herbst und Winter, wenn mehr ferngesehen wird.'),
    6: ('Für wen eignet sich 6 Monate IPTV?',
        'Das Halbjahrespaket richtet sich an alle, die IPTV bereits kennen und regelmäßig schauen. Mit 39 € für ein Gerät zahlen Sie umgerechnet 6,50 € pro Monat und sparen rund 28 % gegenüber sechs Monatspaketen. Gleichzeitig legen Sie sich nicht für ein ganzes Jahr fest.'),
    12: ('Für wen eignet sich 1 Jahr IPTV?',
         'Das Jahrespaket ist unser bester Preis: 49 € für ein Gerät, umgerechnet 4,08 € pro Monat und rund 55 % günstiger als zwölf Monatspakete. Es lohnt sich für alle, die IPTV als festen Ersatz für Kabel, Satellit oder das TV-Paket ihres Internetanbieters nutzen – eine komplette Saison inklusive, ohne Vertrag und ohne automatische Verlängerung.'),
}
PLAN_FAQ = {
    1: ('Kann ich nach einem Monat auf ein längeres Paket wechseln?', 'Ja. Nach Ablauf wählen Sie einfach ein neues Paket, zum Beispiel 6 Monate oder 1 Jahr. Ihre App-Einrichtung bleibt in der Regel unverändert.'),
    3: ('Lohnt sich 3 Monate gegenüber dem Monatspaket?', 'Das 3-Monats-Paket läuft für 29 € (1 Gerät) ohne Unterbrechung und ohne erneute Bestellung. Deutlich günstiger pro Monat sind das 6-Monats-Paket (6,50 €) und das Jahrespaket (4,08 €).'),
    6: ('Wie viel spare ich mit dem 6-Monats-Paket?', 'Für ein Gerät zahlen Sie 39 € statt 54 € für sechs Monatspakete. Das entspricht 6,50 € pro Monat und rund 28 % Ersparnis.'),
    12: ('Wie viel spare ich mit dem Jahrespaket?', 'Für ein Gerät zahlen Sie 49 € statt 108 € für zwölf Monatspakete. Das entspricht 4,08 € pro Monat und rund 55 % Ersparnis.'),
}
PLAN_COMMON_FAQ = [
    ('Verlängert sich das Paket automatisch?', 'Nein. Sie zahlen einmalig für die gewählte Laufzeit. Es gibt keine automatische Verlängerung und keine Kündigungsfrist.'),
    ('Wie geht es nach dem Absenden weiter?', 'Wir melden uns per E-Mail oder WhatsApp mit Ihren Zugangsdaten und den Angaben zur Bezahlung. Bei der Einrichtung auf Ihrem Gerät hilft unser deutschsprachiger Support.'),
]


def plan_info(months, term, index):
    heading, copy = PLAN_COPY[months]
    rows = [[f'{d} {"Gerät" if d == 1 else "Geräte"}', f'{PRICES[d][index]} €', euro(PRICES[d][index] / months)] for d in PRICES]
    faq = [PLAN_FAQ[months]] + PLAN_COMMON_FAQ
    others = ' · '.join(f'<a href="/bestellen/{s}/">{t}</a>' for m, s, t in TERMS if m != months)
    body = (f'''<section class="article trial-info" aria-labelledby="plan-info-title">
  <div class="container">
    <div class="prose">
      <h2 id="plan-info-title">{heading}</h2>
      <p>{copy}</p>
      <h2 id="plan-preise">{term} IPTV: Preise für 1 bis 5 Geräte</h2>
      ''' + table(['Geräte gleichzeitig', f'Preis {term}', 'Pro Monat'], rows, f'{term} IPTV Preise nach Geräteanzahl') + f'''
      <p>Die Geräteanzahl stellen Sie auf der <a href="/preise/">Preisübersicht</a> ein. Andere Laufzeiten: {others}.</p>
      <h2 id="plan-inklusive">Im Paket enthalten</h2>
      ''' + checks('20.000+ Sender, Filme und Serien (VOD)', '4K Ultra HD, Programmführer (EPG) und Catch-Up',
                   'Alle gängigen Geräte: Smart TV, Fire TV Stick, Android, Apple, MAG und PC – siehe <a href="/iptv-geraete/">IPTV Geräte</a>',
                   'Deutschsprachiger Support per E-Mail und WhatsApp mit Einrichtungshilfe') + '''
    </div>
  </div>
</section>
''' + faq_html(faq, f'Häufige Fragen zu {term} IPTV'))
    return body, faq


def plan_page(months, term, price):
    return f'''<section class="signup-page" data-order-page data-months="{months}" aria-labelledby="order-page-title">
  <div class="container trial-wrap">
    <div class="trial-summary">
      <nav aria-label="Brotkrümelnavigation"><ol class="breadcrumb"><li><a href="/">Start</a></li><li><a href="/preise/">Preise</a></li><li aria-current="page">{term}</li></ol></nav>
      <span class="eyebrow">IHR AUSGEWÄHLTES PAKET</span>
      <h1 class="display" id="order-page-title"><span data-selected-term>{term}</span> IPTV</h1>
      <div class="trial-price"><b data-selected-price>{price}</b><span>€</span></div>
      <p class="trial-meta"><span data-selected-devices>1 Gerät</span> gleichzeitig · Einmaliger Paketpreis.<br>Keine automatische Verlängerung.</p>
      <p class="order-instructions">Senden Sie das Formular für dieses Paket ab. Wir melden uns per E-Mail oder WhatsApp mit den Angaben zu Ihrem Zugang und zur Bezahlung.</p>
      {TRUST}
      <a class="text-link" href="/preise/">Zur Paketübersicht</a>
    </div>''' + request_form('order', months, term, price) + '''
  </div>
</section>'''


pages = {
    'preise/index.html': dict(path='/preise/', title='IPTV Preise &amp; Pakete ab 9 € – ohne Vertrag | IPTV Kanal',
        description='IPTV Preise im Überblick: 1, 3, 6 oder 12 Monate für 1 bis 5 Geräte, ab 9 €. Einmal zahlen, keine automatische Verlängerung. Paket wählen und bestellen.',
        body=pricing_page, extra_head=PRICING_JSONLD),
    'kostenlos-testen/index.html': dict(path='/kostenlos-testen/', title='IPTV kostenlos testen – Testline ohne Zahlungsdaten',
        description='IPTV kostenlos testen: Testline für Smart TV, Fire TV, Handy und PC anfragen – ohne Zahlungsdaten und ohne Abo. Sender, 4K und EPG vor dem Kauf prüfen.', body=trial, extra_head=TRIAL_JSONLD),
}
# Initial prices come directly from the homepage's plan cards and must match PRICES.
for index, (months, slug, term) in enumerate(TERMS):
    card = re.search(r'<article class="plan[^>]*data-months="' + str(months) + r'".*?</article>', pricing, re.S).group(0)
    price = re.search(r'class="plan-price[^>]*><b>(\d+)</b>', card).group(1)
    assert int(price) == PRICES[1][index], f'{term}: homepage card {price} € differs from PRICES'
    info, faq = plan_info(months, term, index)
    path = f'/bestellen/{slug}/'
    pages[f'bestellen/{slug}/index.html'] = dict(
        path=path, title=f'{term} IPTV bestellen – ab {price} € ohne Vertrag | IPTV Kanal',
        description=f'{term} IPTV bestellen: 20.000+ Sender, Filme und Serien in bis zu 4K für 1 bis 5 Geräte, ab {price} €. Einmalig bezahlt, keine automatische Verlängerung.',
        body=plan_page(months, term, price) + '\n' + info,
        extra_head=ld([
            ORG,
            {'@type': 'Product', '@id': DOMAIN + path + '#product', 'name': f'IPTV Kanal {term}',
             'description': f'IPTV-Paket für {term} mit 20.000+ Sendern, Filmen und Serien in bis zu 4K. Einmalig bezahlt, keine automatische Verlängerung.',
             'image': OG_IMAGE, 'brand': {'@type': 'Brand', 'name': 'IPTV Kanal'},
             'offers': {'@type': 'AggregateOffer', 'priceCurrency': 'EUR', 'lowPrice': str(PRICES[1][index]),
                        'highPrice': str(PRICES[5][index]), 'offerCount': '5', 'url': DOMAIN + path,
                        'availability': 'https://schema.org/InStock', 'seller': {'@id': DOMAIN + '/#organization'}}},
            faq_ld(faq),
            crumbs(('Start', '/'), ('IPTV Preise', '/preise/'), (f'{term} IPTV', path))]))

for target, page in pages.items():
    out = ROOT / target
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(line.rstrip() for line in PAGE.format(
        favicon=favicon, styles=styles, sprite=sprite, header=header, footer=footer, script=script,
        og_image=OG_IMAGE, og_alt=OG_ALT, **{'extra_head': '', **page}).splitlines()) + "\n")
    print('Built', target)

# The legal/error pages keep their content and share the same navigation and footer.
LEGAL_META = {
    'impressum.html': dict(path='/impressum', title='Impressum | IPTV Kanal – iptvkanal.de'),
    'datenschutz.html': dict(path='/datenschutz', title='Datenschutzerklärung | IPTV Kanal – iptvkanal.de'),
    '404.html': dict(title='Seite nicht gefunden (404) | IPTV Kanal',
                     description='Diese Seite gibt es nicht (mehr). Zur Startseite, zu den IPTV Preisen, zum kostenlosen Test oder zum IPTV Ratgeber von IPTV Kanal.'),
}
for target in ('impressum.html', 'datenschutz.html', '404.html'):
    out = ROOT / target
    text = out.read_text()
    text = re.sub(r'<header class="header"[^>]*>.*?</header>', lambda _: header, text, count=1, flags=re.S)
    text = re.sub(r'<footer class="footer">.*?</footer>', lambda _: footer, text, count=1, flags=re.S)
    if '<svg width="0"' in text:
        text = re.sub(r'<svg width="0".*?</svg>', lambda _: sprite, text, count=1, flags=re.S)
    else:
        text = text.replace('<body>', '<body>\n' + sprite, 1)
    text = text.replace('<main class="legal">', '<main id="main" class="legal">')
    # Absolute asset paths: the 404 page is served for nested URLs, where relative paths break.
    text = re.sub(r'(href|src)="assets/', r'\1="/assets/', text)
    meta = LEGAL_META[target]
    text = re.sub(r'<title>.*?</title>', lambda _: f'<title>{meta["title"]}</title>', text, count=1)
    if '<meta name="description"' not in text:
        text = text.replace('  <meta name="robots"', f'  <meta name="description" content="{meta["description"]}">\n  <meta name="robots"', 1)
    if meta.get('path') and 'rel="canonical"' not in text:
        social = (f'  <link rel="canonical" href="{DOMAIN}{meta["path"]}">\n'
                  '  <meta property="og:type" content="website">\n  <meta property="og:locale" content="de_DE">\n'
                  '  <meta property="og:site_name" content="IPTV Kanal">\n'
                  f'  <meta property="og:title" content="{meta["title"]}">\n'
                  f'  <meta property="og:url" content="{DOMAIN}{meta["path"]}">\n'
                  f'  <meta property="og:image" content="{OG_IMAGE}">\n'
                  '  <meta name="twitter:card" content="summary_large_image">\n')
        text = text.replace('  <meta name="theme-color"', social + '  <meta name="theme-color"', 1)
    if 'assets/main.js' not in text:
        text = text.replace('</body>', script + '\n</body>')
    else:
        text = re.sub(r'<script src="/?assets/main\.js[^"]*" defer></script>', lambda _: script, text)
    out.write_text(text)
    print('Synced navigation', target)

# Guide pages and sitemap share the same header and footer.
subprocess.run([sys.executable, str(ROOT / 'scripts' / 'build-seo-pages.py')], check=True)
