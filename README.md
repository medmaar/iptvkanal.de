# iptvkanal.de

Statische Website für iptvkanal.de.

## Entwicklung

Keine Installation und kein Build erforderlich:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

In der vorbereiteten Cloud-Umgebung sind Playwright und Chromium vorhanden.
Bei laufendem Server prüft `node scripts/smoke-test.cjs` Preise, Bestelllinks,
Navigation, responsive Ansichten und das vollständige Bewertungsarchiv.

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

`assets/reviews.json` enthält alle 63 Bewertungsdatensätze aus dem vom Nutzer
bereitgestellten HTML von mojo4k.de: 15 aus der Trustpilot-Gruppe, 20 aus der
WhatsApp-Gruppe, 20 aus der Google-Gruppe sowie 3 aus JSON-LD und 5 aus Microdata.
Letztere werden als „Weitere Stimmen“ angezeigt. Ähnliche Texte mit demselben
Namen werden als eigenständige Datensätze erhalten, wenn ihr Wortlaut abweicht.
Die Namen und Texte sind unverändert; die JSON-Datei dokumentiert die Fundstelle.
Die Vollständigkeit bezieht sich auf den Upload, nicht auf sämtliche Bewertungen
der Live-Seite oder externer Plattformen.

Die Plattformzuordnung stammt aus dem Quelltext und ist nicht unabhängig geprüft.
Die importierten Einträge werden als Erfahrungen mit MOJO4K ausgewiesen, nicht
als Kundenbewertungen oder Gesamtrating von IPTV Kanal. Die ursprünglichen
Gesamtzahlen und Rating-Angaben der Quellseite werden nicht übernommen.

Nach Änderungen an `assets/reviews.json` das statische Archiv regenerieren:

```sh
python3 scripts/render-reviews.py
```

Alle Datensätze stehen ohne JavaScript im HTML. JavaScript ergänzt Filter,
Textsuche und schrittweises Nachladen. Zum Betrieb sind keine externen
Bewertungsdienste erforderlich.
