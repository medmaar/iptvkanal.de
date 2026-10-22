#!/usr/bin/env python3
"""Build the pricing and free-trial pages from the homepage's own markup.

The pricing page embeds the homepage's pricing section verbatim, so the plan
cards can never drift apart. Run this after changing the header, footer, icon
sprite or pricing section in index.html.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
home = (ROOT / 'index.html').read_text()


def between(start, end, text=home, keep=True):
    a = text.index(start)
    b = text.index(end, a) + (len(end) if keep else 0)
    return text[a:b]


def absolute(markup):
    """Make homepage fragments work from a subdirectory."""
    markup = re.sub(r'(<a [^>]*?)href="#(?!main"|top")', r'\1href="/#', markup)
    markup = re.sub(r'(<a class="logo" [^>]*?)href="#top"', r'\1href="/"', markup)
    markup = re.sub(r'(src|href)="(assets/|impressum\.html|datenschutz\.html)', r'\1="/\2', markup)
    return markup


head_links = re.findall(r'<link rel="stylesheet" href="assets/[^"]+">', home)
favicon = re.search(r'<link rel="icon"[^>]+>', home).group(0).replace('href="assets/', 'href="/assets/')
sprite = between('<svg width="0"', '</svg>\n<div class="bg-orbs"', keep=False) + '</svg>'
header = absolute(between('<header class="header"', '</header>'))
footer = absolute(between('<footer class="footer">', '</footer>'))
script = absolute(re.search(r'<script src="assets/main\.js[^"]*" defer></script>', home).group(0))
pricing = between('<section id="preise"', '</section>\n<section id="bewertungen"', keep=False)
pricing = absolute(pricing.rstrip().removesuffix('</section>') ) + '</section>'
pricing = pricing.replace('<span class="chapter">03</span> ', '').replace('<h2 class="display" id="pricing-title">', '<h1 class="display" id="pricing-title">').replace('</span></h2>\n        <p>Einmal', '</span></h1>\n        <p>Einmal')

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

TRIAL = '''<section class="signup-page" aria-labelledby="trial-title">
  <div class="signup-bg" aria-hidden="true"></div>
  <div class="container trial-wrap">
    <div class="trial-summary">
      <span class="eyebrow">KOSTENLOS TESTEN</span>
      <h1 class="display" id="trial-title">Kostenlos testen</h1>
      <div class="trial-price"><b>0</b><span>€</span></div>
      <p class="trial-meta">Voller Zugriff auf Live-TV, Sport, Filme &amp; Serien. Ohne Zahlungsdaten, ohne Vertrag.</p>
      <a class="text-link" href="/preise/">Zu den Paketen &amp; Preisen</a>
    </div>

    <form class="signup-form" data-signup-form novalidate action="/api/trial" method="post">
      <div class="form-row">
        <label class="field"><span>Vorname</span><input type="text" name="first_name" autocomplete="given-name" required></label>
        <label class="field"><span>Nachname</span><input type="text" name="last_name" autocomplete="family-name" required></label>
      </div>
      <label class="field"><span>E-Mail-Adresse</span><input type="email" name="email" autocomplete="email" inputmode="email" required></label>
      <label class="field"><span>WhatsApp-Nummer <small>(optional)</small></span><input type="tel" name="phone" autocomplete="tel" inputmode="tel" placeholder="+49 …"></label>
      <label class="field"><span>Auf welchem Gerät möchten Sie schauen?</span>
        <select name="device" required>
          <option value="">Bitte wählen</option>
          <option>Smart-TV</option><option>Amazon Fire TV Stick</option><option>Android-TV-Box</option><option>MAG-Box</option>
          <option>Apple TV</option><option>iPhone / iPad</option><option>Android-Smartphone / Tablet</option><option>PC / Mac</option>
        </select>
      </label>
      <label class="hp" aria-hidden="true">Bitte leer lassen<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
      <label class="check"><input type="checkbox" name="consent" required><span>Ich habe die <a href="/datenschutz.html" target="_blank" rel="noopener">Datenschutzerklärung</a> gelesen und bin mit der Verarbeitung meiner Angaben zur Bearbeitung der Testanfrage einverstanden.</span></label>
      <p class="form-error" data-trial-error role="alert" hidden></p>
      <button class="btn btn-primary btn-block" type="submit">Kostenlosen Test anfordern <svg><use href="#i-arrow"/></svg></button>
      <p class="form-legal">Ihr Testzugang kommt per E-Mail. Keine Zahlungsdaten nötig. Fragen? <a href="/go/wa" rel="noopener">WhatsApp</a> oder <a href="mailto:kontakt@iptvkanal.de">kontakt@iptvkanal.de</a></p>
    </form>

    <div class="signup-success" data-signup-success tabindex="-1" hidden>
      <div class="success-check" aria-hidden="true"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="46"/><path d="M28 52l16 16 30-34"/></svg></div>
      <h2>Vielen Dank!</h2>
      <p>Ihre Anfrage ist bei uns angekommen. Ihren Testzugang erhalten Sie in Kürze an <b data-trial-email></b>.</p>
      <p class="muted">Keine E-Mail erhalten? Schauen Sie im Spam-Ordner nach oder schreiben Sie uns per <a href="/go/wa" rel="noopener">WhatsApp</a>.</p>
    </div>
  </div>
</section>'''

pages = {
    'preise/index.html': dict(
        path='/preise/',
        title='Preise &amp; Pakete – IPTV Kanal ab 9 €',
        description='Alle IPTV-Kanal-Pakete für 1 bis 5 Geräte: 1, 3, 6 oder 12 Monate. Einmal zahlen, ohne automatische Verlängerung, ab 9 €.',
        body=pricing),
    'kostenlos-testen/index.html': dict(
        path='/kostenlos-testen/',
        title='Kostenlos testen – IPTV Kanal Testzugang',
        description='Testen Sie IPTV Kanal kostenlos: Live-TV, Sport, Filme und Serien in 4K. Formular ausfüllen, Testzugang per E-Mail erhalten.',
        body=TRIAL),
}
styles = '\n  '.join(link.replace('href="assets/', 'href="/assets/') for link in head_links)
for target, page in pages.items():
    out = ROOT / target
    out.parent.mkdir(exist_ok=True)
    out.write_text(PAGE.format(favicon=favicon, styles=styles, sprite=sprite, header=header, footer=footer, script=script, **page))
    print('Built', target)
