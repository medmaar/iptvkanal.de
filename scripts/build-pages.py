#!/usr/bin/env python3
"""Build pricing, trial and individual order pages with shared navigation."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
home = (ROOT / 'index.html').read_text()


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
  <link rel="canonical" href="https://iptvkanal.de{path}">
  <meta name="theme-color" content="#0d0e14">
  {favicon}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="de_DE">
  <meta property="og:site_name" content="IPTV Kanal">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="https://iptvkanal.de{path}">
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
      <p class="form-legal">Ihre Angaben verwenden wir zur Bearbeitung Ihrer Anfrage. Mehr dazu in der <a href="/datenschutz.html">Datenschutzerklärung</a>.</p>
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
TRIAL_JSONLD = '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': [
    {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in TRIAL_FAQ]},
    {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Start', 'item': 'https://iptvkanal.de/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'IPTV kostenlos testen', 'item': 'https://iptvkanal.de/kostenlos-testen/'}]}]}, ensure_ascii=False) + '</script>'


trial = '''<section class="signup-page" aria-labelledby="trial-title">
  <div class="container trial-wrap">
    <div class="trial-summary">
      <span class="eyebrow">IHR KOSTENLOSER TESTZUGANG</span>
      <h1 class="display" id="trial-title">IPTV kostenlos testen</h1>
      <div class="trial-price"><b>0</b><span>€</span></div>
      <p class="trial-meta">Live-TV, Sport, Filme und Serien kennenlernen. Ohne Zahlungsdaten.</p>
      <p class="order-instructions">Formular ausfüllen und absenden. Ihren Testzugang erhalten Sie anschließend per E-Mail oder WhatsApp.</p>
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
<section class="faq-section" id="faq" aria-labelledby="faq-title">
  <div class="container container--narrow">
    <header class="section-head"><p class="eyebrow">FAQ</p><h2 class="display" id="faq-title">Häufige Fragen zum IPTV-Test</h2></header>
    <div class="faq">''' + ''.join(f'<details><summary>{q}<i aria-hidden="true"></i></summary><p>{a}</p></details>' for q, a in TRIAL_FAQ) + '''</div>
  </div>
</section>'''

pricing_page = '''<section class="page-intro" aria-labelledby="pricing-page-title">
  <div class="container trial-wrap trial-summary">
    <span class="eyebrow">IHR PAKET. IHRE WAHL.</span>
    <h1 class="display" id="pricing-page-title">Preise &amp; Pakete</h1>
    <div class="trial-price"><small>ab</small><b data-starting-price>9</b><span>€</span></div>
    <p class="trial-meta">Einmal zahlen. Keine automatische Verlängerung.</p>
    <p class="order-instructions">Wählen Sie die Anzahl Ihrer Geräte und klicken Sie auf Ihr Wunschpaket. Auf der eigenen Paketseite können Sie Ihre Bestellung absenden.</p>
  </div>
</section>
''' + pricing


def plan_page(months, term, price):
    return f'''<section class="signup-page" data-order-page data-months="{months}" aria-labelledby="order-page-title">
  <div class="container trial-wrap">
    <div class="trial-summary">
      <span class="eyebrow">IHR AUSGEWÄHLTES PAKET</span>
      <h1 class="display" id="order-page-title"><span data-selected-term>{term}</span> IPTV</h1>
      <div class="trial-price"><b data-selected-price>{price}</b><span>€</span></div>
      <p class="trial-meta"><span data-selected-devices>1 Gerät</span> gleichzeitig · Einmaliger Paketpreis.<br>Keine automatische Verlängerung.</p>
      <p class="order-instructions">Senden Sie das Formular für dieses Paket ab. Wir melden uns per E-Mail oder WhatsApp mit den Angaben zu Ihrem Zugang und zur Bezahlung.</p>
      <a class="text-link" href="/preise/">Zur Paketübersicht</a>
    </div>''' + request_form('order', months, term, price) + '''
  </div>
</section>'''


pages = {
    'preise/index.html': dict(path='/preise/', title='IPTV Preise &amp; Pakete ab 9 € – ohne Vertrag | IPTV Kanal',
        description='IPTV Preise im Überblick: 1, 3, 6 oder 12 Monate für 1 bis 5 Geräte, ab 9 €. Einmal zahlen, keine automatische Verlängerung. Paket wählen und direkt bestellen.', body=pricing_page),
    'kostenlos-testen/index.html': dict(path='/kostenlos-testen/', title='IPTV kostenlos testen – Testline ohne Zahlungsdaten | IPTV Kanal',
        description='IPTV kostenlos testen: Testline für Smart TV, Fire TV, Handy und PC anfragen – ohne Zahlungsdaten und ohne Abo. Sender, 4K und EPG vor dem Kauf prüfen.', body=trial, extra_head=TRIAL_JSONLD),
}
# Initial prices come directly from the homepage's plan cards.
for months, slug, term in [(1, '1-monat', '1 Monat'), (3, '3-monate', '3 Monate'), (6, '6-monate', '6 Monate'), (12, '1-jahr', '1 Jahr')]:
    card = re.search(r'<article class="plan[^>]*data-months="' + str(months) + r'".*?</article>', pricing, re.S).group(0)
    price = re.search(r'class="plan-price[^>]*><b>(\d+)</b>', card).group(1)
    pages[f'bestellen/{slug}/index.html'] = dict(
        path=f'/bestellen/{slug}/', title=f'{term} IPTV bestellen – IPTV Kanal',
        description=f'{term} IPTV bestellen: 20.000+ Sender, Filme und Serien in bis zu 4K für 1 bis 5 Geräte. Einmalig bezahlt, keine automatische Verlängerung.',
        body=plan_page(months, term, price))

for target, page in pages.items():
    out = ROOT / target
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(line.rstrip() for line in PAGE.format(favicon=favicon, styles=styles, sprite=sprite, header=header, footer=footer, script=script, **{'extra_head': '', **page}).splitlines()) + "\n")
    print('Built', target)

# The legal/error pages keep their content and share the same navigation and footer.
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
    if 'assets/main.js' not in text:
        text = text.replace('</body>', script + '\n</body>')
    else:
        text = re.sub(r'<script src="/?assets/main\.js[^"]*" defer></script>', lambda _: script, text)
    out.write_text(text)
    print('Synced navigation', target)

# Guide pages and sitemap share the same header and footer.
subprocess.run([sys.executable, str(ROOT / 'scripts' / 'build-seo-pages.py')], check=True)
