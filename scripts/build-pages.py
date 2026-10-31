#!/usr/bin/env python3
"""Build pricing, trial and individual order pages with shared navigation."""
import re
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


def request_form(kind, months=1):
    order = kind == 'order'
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


trial = '''<section class="signup-page" aria-labelledby="trial-title">
  <div class="container trial-wrap">
    <div class="trial-summary">
      <span class="eyebrow">IHR KOSTENLOSER TESTZUGANG</span>
      <h1 class="display" id="trial-title">Kostenlos testen</h1>
      <div class="trial-price"><b>0</b><span>€</span></div>
      <p class="trial-meta">Live-TV, Sport, Filme und Serien kennenlernen. Ohne Zahlungsdaten.</p>
      <p class="order-instructions">Formular ausfüllen und absenden. Ihren Testzugang erhalten Sie anschließend per E-Mail oder WhatsApp.</p>
    </div>''' + request_form('trial') + '''
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
    </div>''' + request_form('order', months) + '''
  </div>
</section>'''


pages = {
    'preise/index.html': dict(path='/preise/', title='Preise &amp; Pakete – IPTV Kanal ab 9 €',
        description='Die gleichen IPTV-Kanal-Pakete wie auf der Startseite. Geräteanzahl und Paket wählen und direkt auf der eigenen Paketseite bestellen.', body=pricing_page),
    'kostenlos-testen/index.html': dict(path='/kostenlos-testen/', title='Kostenlos testen – IPTV Kanal Testzugang',
        description='IPTV Kanal kostenlos anfragen. Name, E-Mail, WhatsApp und Notiz sind freiwillig – auch ein leeres Formular lässt sich absenden.', body=trial),
}
# Initial prices come directly from the homepage's plan cards.
for months, slug, term in [(1, '1-monat', '1 Monat'), (3, '3-monate', '3 Monate'), (6, '6-monate', '6 Monate'), (12, '1-jahr', '1 Jahr')]:
    card = re.search(r'<article class="plan[^>]*data-months="' + str(months) + r'".*?</article>', pricing, re.S).group(0)
    price = re.search(r'class="plan-price[^>]*><b>(\d+)</b>', card).group(1)
    pages[f'bestellen/{slug}/index.html'] = dict(
        path=f'/bestellen/{slug}/', title=f'{term} IPTV bestellen – IPTV Kanal',
        description=f'{term} IPTV für die gewählte Geräteanzahl bestellen. Name, E-Mail, WhatsApp und Notiz sind freiwillig.',
        body=plan_page(months, term, price))

for target, page in pages.items():
    out = ROOT / target
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(line.rstrip() for line in PAGE.format(favicon=favicon, styles=styles, sprite=sprite, header=header, footer=footer, script=script, **page).splitlines()) + "\n")
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
