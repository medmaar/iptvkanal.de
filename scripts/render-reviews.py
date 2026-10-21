#!/usr/bin/env python3
"""Render independent review carousels, with labeled placeholders until supplied."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'assets/review-platforms.json').read_text())
ORDER = ('trustpilot', 'whatsapp', 'google')
PLACEHOLDERS = {'trustpilot': 3, 'whatsapp': 6, 'google': 9}


def esc(value):
    return html.escape(str(value), quote=True)


def icon(platform):
    if platform == 'trustpilot':
        return '<svg class="platform-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="#00b67a" d="m12 1 2.8 8.2H23l-6.7 5 2.6 8L12 17.3l-6.9 4.9 2.6-8L1 9.2h8.2Z"/><path fill="#005128" d="m12 17.3 4.3-3.1 2.6 8Z"/></svg>'
    if platform == 'whatsapp':
        return '<span class="platform-icon whatsapp-icon"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-wa"/></svg></span>'
    return '<span class="google-wordmark" aria-hidden="true"><span>G</span><span>o</span><span>o</span><span>g</span><span>l</span><span>e</span></span>'


def placeholder(platform, index):
    stars = '<div class="preview-stars" aria-hidden="true">☆☆☆☆☆</div>'
    top = ('<div class="message-card-label">' + icon(platform) + '<span>WhatsApp</span></div>') if platform == 'whatsapp' else stars
    return f'''<article class="platform-review-card" data-review-card data-placeholder="true" aria-label="{esc(platform)}: Platzhalter {index + 1}, noch keine Bewertung">
<div class="card-preview-label">Platzhalter</div>{top}
<h4>Bewertung folgt in Kürze</h4>
<div class="review-skeleton" aria-hidden="true"><span></span><span></span><span></span></div>
<footer class="platform-review-author"><span class="review-placeholder-avatar" aria-hidden="true"></span><span>Kundenstimme folgt</span></footer></article>'''


def review_card(review, platform):
    title = f'<h4>{esc(review["title"])}</h4>' if review.get('title') else ''
    rating = review.get('rating')
    if rating is not None and (type(rating) is not int or not 1 <= rating <= 5):
        raise ValueError('Review ratings must be integers from 1 to 5.')
    stars = (f'<div class="platform-review-stars" aria-label="{rating} von 5 Sternen">'
             + '★' * rating + '☆' * (5 - rating) + '</div>') if rating else ''
    top = ('<div class="message-card-label">' + icon(platform) + '<span>WhatsApp</span></div>') if platform == 'whatsapp' else stars
    return f'''<article class="platform-review-card" data-review-card>
{top}{title}<blockquote><p>{esc(review['text'])}</p></blockquote>
<footer class="platform-review-author"><span>{esc(review['author'])}</span></footer></article>'''


platforms = {item['id']: item for item in data['platforms']}
if set(platforms) != set(ORDER) or len(data['platforms']) != len(ORDER):
    raise ValueError('Exactly one Trustpilot, WhatsApp and Google configuration is required.')
sections = []
for platform in ORDER:
    item = platforms[platform]
    label = esc(item['label'])
    cards = ([review_card(review, platform) for review in item['reviews']] if item['reviews']
             else [placeholder(platform, index) for index in range(PLACEHOLDERS[platform])])
    heading = (icon(platform) + f'<h3 id="{platform}-reviews-title">{label}</h3>') if platform != 'google' else (icon(platform) + f'<h3 id="{platform}-reviews-title"><span class="sr-only">Google </span>Bewertungen</h3>')
    sections.append(f'''<section class="review-platform review-platform--{platform}" data-review-platform="{platform}" aria-labelledby="{platform}-reviews-title">
<header class="review-platform-heading">{heading}</header>
<div class="platform-review-viewport" data-review-viewport tabindex="0" aria-label="{label}: Bewertungen horizontal durchblättern">
{chr(10).join(cards)}
</div>
<div class="review-platform-controls" data-review-controls hidden>
<button type="button" class="review-arrow" data-review-prev aria-label="{label}: vorherige Seite"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button>
<div class="review-pagination" data-review-dots role="group" aria-label="{label}: Seite auswählen"></div>
<button type="button" class="review-arrow" data-review-next aria-label="{label}: nächste Seite"><svg aria-hidden="true"><use href="#i-arrow"/></svg></button>
<button type="button" class="review-pause" data-review-pause aria-pressed="false" aria-label="{label}: automatischen Wechsel pausieren"><span data-review-pause-icon data-icon="pause" aria-hidden="true"></span><span data-review-pause-text>Pause</span></button>
</div>
<p class="sr-only" data-review-position aria-live="off"></p>
</section>''')

page = ROOT / 'index.html'
start, end = '<!-- reviews:start -->', '<!-- reviews:end -->'
before, rest = page.read_text().split(start)
_, after = rest.split(end)
page.write_text(before + start + '\n' + '\n'.join(sections) + '\n' + end + after)
print('Rendered three independent platform carousels; empty platforms use labeled placeholders.')
