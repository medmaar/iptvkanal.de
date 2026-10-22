#!/usr/bin/env python3
"""Render independent review carousels, with labeled placeholders until supplied."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'assets/review-platforms.json').read_text())
ORDER = ('trustpilot', 'whatsapp', 'google')
PLACEHOLDERS = {'trustpilot': 3, 'whatsapp': 6, 'google': 9}
FLAG = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}')


def esc(value):
    return html.escape(str(value), quote=True)


def author_markup(author):
    """Render supplied flag emoji as local images, independent of system fonts."""
    name, separator, country = author.partition(' — ')
    country_label = FLAG.sub('', country).strip()

    def flag_image(match):
        code = ''.join(chr(ord(char) - 0x1F1E6 + ord('a')) for char in match[0])
        asset = f'assets/flags/{code}.svg'
        if not (ROOT / asset).is_file():
            raise ValueError(f'Missing local flag graphic: {asset}')
        # The adjacent country name provides the accessible label.
        alt = '' if country_label else code.upper()
        return (f'<img class="review-country-flag" src="{asset}" width="20" height="12" '
                f'alt="{alt}" title="{esc(country_label or code.upper())}" data-country="{code}">')

    if separator:
        return esc(name) + ' — <span class="review-author-country">' + FLAG.sub(flag_image, esc(country)) + '</span>'
    return FLAG.sub(flag_image, esc(author))


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
<footer class="platform-review-author"><span>{author_markup(review['author'])}</span></footer></article>'''


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
<div class="review-dots" data-review-dots aria-hidden="true"><span class="review-dots-track" data-review-dots-track>{'<span class="review-dot"></span>' * 9}</span></div>
</div>
<p class="sr-only" data-review-position aria-live="off"></p>
</section>''')

page = ROOT / 'index.html'
start, end = '<!-- reviews:start -->', '<!-- reviews:end -->'
before, rest = page.read_text().split(start)
_, after = rest.split(end)
content = before + start + '\n' + '\n'.join(sections) + '\n' + end + after
if all(platforms[platform]['reviews'] for platform in ORDER):
    content = re.sub(r'<span class="reviews-pending">.*?</span>', '', content)
page.write_text(content)
print('Rendered platform carousels:', {platform: len(platforms[platform]['reviews']) for platform in ORDER})
