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

## Vorlage und Bewertungen

Die Startseite übernimmt die Struktur aus dem bereitgestellten HTML von
iptvweltpremium.de und verwendet lokale Styles in `assets/template.css`.
Das externe Original-CSS, JavaScript und die Fotos waren nicht im Upload enthalten.
Direkter Zugriff auf beide Quellseiten wurde vom Netzwerk-Proxy mit HTTP 403
abgewiesen. Deshalb ist die Gestaltung eine lokale Rekonstruktion; die
Stadion-Illustration ist ein lokales SVG. Ein exakter visueller Abgleich mit der
Live-Seite steht noch aus. Die bestehenden IPTV-Kanal-Preise und Kontaktdaten
bleiben erhalten. Fremde Checkout-, WhatsApp- und Tracking-Verbindungen werden
nicht übernommen.

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
