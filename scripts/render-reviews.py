#!/usr/bin/env python3
"""Render the attributed review archive from assets/reviews.json; no network access."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'assets/reviews.json').read_text())
labels = {'trustpilot': 'Trustpilot laut Quelle', 'whatsapp': 'WhatsApp laut Quelle',
          'google': 'Google laut Quelle', 'metadata': 'Weitere Stimme von mojo4k.de'}


def esc(value):
    return html.escape(str(value), quote=True)


cards = []
for review in data['reviews']:
    title = f'<h3>{esc(review["title"])}</h3>' if review['title'] else ''
    rating = (f'<span class="review-rating" aria-label="{review["rating"]} von 5 Sternen laut Quelle">'
              + '★' * review['rating'] + '</span>') if 'rating' in review else ''
    initials = ''.join(part[0] for part in review['author'].split()[:2])
    cards.append(f'''<article class="review-card" data-review-id="{esc(review['id'])}" data-review-group="{esc(review['group'])}">
<div class="review-card-top"><span class="source-badge {esc(review['group'])}">{esc(labels[review['group']])}</span>{rating}</div>
{title}<blockquote><p>{esc(review['text'])}</p></blockquote>
<footer class="review-author"><span class="avatar" aria-hidden="true">{esc(initials)}</span><div><strong>{esc(review['author'])}</strong><a href="{esc(data['source_url'])}" target="_blank" rel="noopener noreferrer">Quelle: mojo4k.de ↗</a></div></footer></article>''')

page = ROOT / 'index.html'
start, end = '<!-- reviews:start -->', '<!-- reviews:end -->'
before, rest = page.read_text().split(start)
_, after = rest.split(end)
page.write_text(before + start + '\n<div class="review-grid" id="review-grid">\n'
                + '\n'.join(cards) + '\n</div>\n' + end + after)
print(f'Rendered {len(cards)} source-attributed reviews.')
