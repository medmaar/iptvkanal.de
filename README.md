# iptvkanal.de

Statische Website für iptvkanal.de.

## Entwicklung

Keine Installation und kein Build erforderlich:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

In der vorbereiteten Cloud-Umgebung sind Playwright und Chromium vorhanden.
Bei laufendem Server prüft `node scripts/smoke-test.cjs` Preise, Bestelllinks,
Navigation, responsive Ansichten und die unabhängigen Bewertungs-Karussells.

Nach Änderungen an JavaScript, eigenem CSS oder dem Favicon vor den Tests
`python3 scripts/version-assets.py` ausführen. Die HTML-Dateien verwenden dann
den aktuellen Inhalts-Hash als Cache-Version. `_headers` lässt Cloudflare die
Startseite und veränderliche Bundles revalidieren, damit ältere Browser-Caches
die Geräteauswahl nach einem Deployment nicht außer Funktion setzen.

## Vorlage und Bewertungen

Die Startseite übernimmt die Struktur aus dem bereitgestellten HTML von
iptvweltpremium.de. Das Original-Stylesheet wurde am 21.10.2026 direkt heruntergeladen
und liegt unverändert in `assets/reference/style.css`. Die verwendeten Fotos und
Poster liegen lokal unter `assets/img/`. Herkunft, Größe und SHA-256-Prüfsummen
stehen in `assets/reference/sources.json`. Der Betrieb benötigt keinen Zugriff
auf die Quellseite. `assets/template.css` ergänzt die Integration der eigenen
Marke, das Bewertungsarchiv und die Zugänglichkeit ohne JavaScript.

Die Startseite verwendet auch die originalen Hintergrundbilder, die Highlights
und die VOD-Posterreihen. Die bestehenden IPTV-Kanal-Preise und Kontaktdaten
bleiben erhalten. Fremde Checkout-, WhatsApp- und Tracking-Verbindungen werden
nicht übernommen. Das JavaScript für die eigene Navigation und Preiswahl bleibt
lokal; das fremde Anwendungsskript wird nicht eingebunden.

Das eigene Farbthema „Wisteria Bloom“ verwendet die vorgegebene Palette
`#D3D3FF` (Lavendel), `#9400D3` (Violett), `#D8BFD8` (Mauve) und
`#ED80E9` (Pink). Die Theme-Overrides in `assets/template.css` gestalten helle
Flächen, dunkle Pflaumentöne für Text und violette Aktionen; Bildunterschriften
bleiben weiß auf dunklen Fotoverläufen. Das Original-CSS bleibt unverändert.

## Bewertungsbereiche

Die aktuelle Gestaltung folgt dem vom Nutzer bereitgestellten HTML von maple4k.ca:
Trustpilot mit einer großen Karte, WhatsApp mit zwei Nachrichtenkarten, Google
mit drei Karten. Jeder Bereich hat eigene Pfeile, Seitenpunkte und eine
Seitensteuerung. Auf schmalen Bildschirmen wird eine Karte angezeigt;
Touch-Scrolling und Tastatursteuerung sind möglich. Sichtbare Karussells wechseln
alle sieben Sekunden. Hover, Tastaturfokus und ausgeblendete Tabs halten den Wechsel an.
Ein sichtbarer Pause-Button wird nicht angezeigt. Bei reduzierter Bewegung ist Autoplay zunächst aus.

Die bereitgestellten 60 Rezensionen sind eingepflegt: 20 Kundenbewertungen im
Trustpilot-Bereich, 20 WhatsApp-Nachrichten und 20 Google-Bewertungen. Wortlaut,
Titel, Namen, Länderangaben und mitgelieferte Sterne bleiben erhalten.
Platzhalter und der Hinweis auf kommende Bewertungen werden nicht angezeigt.
Das alte MOJO4K-Archiv in `assets/reviews.json` bleibt erhalten, wird aber nicht
mehr auf der Seite angezeigt. Die neuen Inhalte stammen aus der Nutzerdatei;
zusätzliche Verifizierungs- oder Rating-Gesamtangaben werden nicht ergänzt.

Weitere Einträge werden in `assets/review-platforms.json` unter der passenden
Plattform ergänzt. Jeder Eintrag hat `author` und `text`, optional `title` und
`rating` (ganze Zahl von 1 bis 5). Leere Plattformen erhalten Platzhalter.

Nach dem Eintragen der gelieferten Inhalte:

```sh
python3 scripts/render-reviews.py
python3 scripts/version-assets.py
```

Alle Karten sind statisches HTML und ohne JavaScript horizontal scrollbar.
JavaScript ergänzt getrennte Seitensteuerung und automatische Bewegung. Die
fremden Next.js-Anwendungsskripte, Bewertungen und Rating-Gesamtzahlen werden
nicht übernommen.
