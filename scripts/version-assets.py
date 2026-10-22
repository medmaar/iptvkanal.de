#!/usr/bin/env python3
"""Keep browser cache keys in sync with scripts, styles, favicon, and wordmark."""
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for asset in ('assets/main.js', 'assets/base.css', 'assets/template.css', 'assets/favicon.svg', 'assets/brand/iptvkanal-supplied-logo.webp'):
    version = hashlib.sha256((ROOT / asset).read_bytes()).hexdigest()[:12]
    pattern = re.compile(r'(?P<prefix>(?:src|href)=")' + re.escape(asset)
                         + r'(?:\?[^"\s]*)?(?P<suffix>")')
    for page in ROOT.glob('*.html'):
        content = page.read_text()
        updated = pattern.sub(lambda match: match['prefix'] + asset + '?v=' + version
                              + match['suffix'], content)
        if updated != content:
            page.write_text(updated)
    print(f'{asset}?v={version}')
