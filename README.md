# iptvkanal.de

Statische Website für IPTV Kanal mit lokal gespeicherten Bildern, Schriftarten,
Stylesheets, JavaScript und Länderflaggen.

## Entwicklung

Keine Installation und kein Build erforderlich:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

In der vorbereiteten Cloud-Umgebung sind Playwright und Chromium vorhanden.
Bei laufendem Server prüft `node scripts/smoke-test.cjs` Preise, Bestelllinks,
Navigation, responsive Ansichten und die unabhängigen Bewertungs-Karussells.
Die Prüfung schlägt auch bei externen Ressourcenanfragen fehl.

Nach Änderungen an JavaScript, Stylesheets oder dem Favicon vor den Tests
`python3 scripts/version-assets.py` ausführen. Die HTML-Dateien verwenden dann
den aktuellen Inhalts-Hash als Cache-Version. `_headers` lässt die Startseite
und veränderliche Bundles revalidieren.

Änderungen werden nach bestandenen Prüfungen auf `main` gepusht. Das verbundene
Cloudflare-Pages-Projekt übernimmt automatisch das Deployment.

## Lokale Assets und Darstellung

- `assets/base.css`: grundlegendes Layout und lokale Schriftdefinitionen.
- `assets/template.css`: Farbthema und Komponenten.
- `assets/main.js`: Geräteauswahl, Navigation und Karussell-Steuerung.
- `assets/img/`: lokal gespeicherte Fotos und VOD-Poster.
- `assets/fonts/`: lokale variable WOFF2-Schriften und vollständige Font-Lizenzen.
- `assets/flags/`: lokale Länderflaggen als SVG-Grafiken.
- `assets/brand/iptvkanal-logo.svg`: reine Wortmarke mit weißer und goldener Sora-Schrift.

Die Schriften Inter und Sora werden lokal aus den Paketen
`@fontsource-variable/inter@5.3.0` und `@fontsource-variable/sora@5.2.8`
bereitgestellt. Die jeweiligen SIL-Open-Font-Lizenzen und Urheberangaben liegen
bei den Font-Dateien. Es werden keine externen Font- oder Bilddienste benötigt.
Technische Namensräume in SVG, Sitemap und strukturierten Daten sind keine
externen Ressourcenanfragen.

Die Gestaltung verbindet Anthrazit (`#0D0E14`) mit Lavendel (`#D3C6FA`),
Mauve und hellen Film- und Bewertungsbereichen. Der gerahmte Hero nutzt
`assets/img/hero-carnival.webp`: eine mit dem Bildwerkzeug aufbereitete Variante
des gelieferten Karnevalsfotos, lokal als WebP mit ca. 209 KB gespeichert.
Die Datei ist eine verarbeitete Fassung, nicht die ursprüngliche Upload-Datei.

Auf Mobilgeräten erhält das Foto einen eigenen Bereich im 16:9-Format;
das Preisangebot steht darunter und verdeckt keine Gesichter. Der Start-Button
und die Geräteauswahl bleiben erreichbar. Preiskarten lassen sich per
Wischgeste vergleichen. Eine lokale Bildschirm-Illustration zeigt TV und Handy.
Animationen respektieren die Einstellung für reduzierte Bewegung.

Die Aktionsbuttons verwenden dunkle Bronze-Gold-Flächen mit hellgoldener
Beschriftung, dezenten Konturen und weich gerundeten Ecken. Das Jahrespaket setzt
sich mit einem dunklen, goldschimmernden Hintergrund ab. Die Preiskarten
wechseln beim Hover weich zwischen Position und Schatten. Der Bewertungsbereich
verwendet denselben dunklen Hintergrund wie die übrige Seitenfläche;
Trustpilot-Sterne bleiben grün und Google-Sterne gelb. Logo und Favicon sind
lokal als SVG gespeichert und verwenden Inhalts-Hashes als Cache-Versionen.
Die reine Wortmarke verwendet kompakte, leicht geneigte Sora-Buchstaben als
Vektorpfade in Weiß und Gold. Sie benötigt keine zusätzlichen Schriftanfragen
und enthält kein Bildsymbol. Das Favicon zeigt ein typografisches K.

## Bewertungsbereiche

Trustpilot zeigt eine große Karte, WhatsApp zwei Nachrichtenkarten und Google
drei Karten. Alle drei Bereiche verwenden denselben kompakten Seitenzähler
mit zwei dezenten Pfeilen. Auf schmalen Bildschirmen wird eine Karte angezeigt;
Touch-Scrolling und Tastatursteuerung sind möglich. Sichtbare Karussells wechseln
alle sieben Sekunden. Hover, Tastaturfokus und ausgeblendete Tabs halten den
Wechsel an. Ein sichtbarer Pause-Button wird nicht angezeigt. Bei reduzierter
Bewegung ist Autoplay aus.

Die gelieferten 60 Rezensionen stehen in `assets/review-platforms.json`:
20 Einträge pro Plattform. Texte, Namen, Länderangaben und Sterne entsprechen
der bereitgestellten Liste. Zusätzliche Verifizierungs- oder Rating-Gesamtangaben
werden nicht ergänzt.

Länderflaggen werden beim Rendern aus den gelieferten Emoji-Codes in lokale
SVG-Bilder umgewandelt. Dadurch sind sie auch auf Systemen ohne Flaggen-Emoji-
Schrift als Grafik sichtbar. Bei neuen Ländern die entsprechende SVG-Datei
unter dem ISO-Ländercode ergänzen; fehlende Dateien führen zu einem Renderfehler.

Jeder Eintrag hat `author` und `text`, optional `title` und `rating`
(ganze Zahl von 1 bis 5). Leere Plattformen erhalten markierte Platzhalter.
Nach Änderungen an den Inhalten:

```sh
python3 scripts/render-reviews.py
python3 scripts/version-assets.py
```

Alle Karten sind statisches HTML und ohne JavaScript horizontal scrollbar.
JavaScript ergänzt die getrennte Seitensteuerung und automatische Bewegung.
