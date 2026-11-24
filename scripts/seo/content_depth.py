"""Depth additions for the guide pages (SEO audit, 24.11.2026).

Applied by build-seo-pages.py on top of the base page definitions:
  EXTRA_SECTIONS[slug]  extra (id, h2, html) sections appended to the article
  EXTRA_FAQ[slug]       extra visible FAQ entries (mirrored in FAQPage JSON-LD)
  LEAD[slug]            lead paragraph overrides so the primary keyword sits in the first paragraph
  SOURCES[slug]         outbound links to official or authoritative sources
Statements about third-party apps and devices stay general and verifiable; no prices of third parties.
"""
from .helpers import steps, checks, tip, table

# ---------------------------------------------------------------- shared source links
WIKI_IPTV = ('Wikipedia: Internet Protocol Television', 'https://de.wikipedia.org/wiki/Internet_Protocol_Television')
WIKI_M3U = ('Wikipedia: M3U-Dateiformat', 'https://de.wikipedia.org/wiki/M3U')
WIKI_HEVC = ('Wikipedia: High Efficiency Video Coding (HEVC)', 'https://de.wikipedia.org/wiki/High_Efficiency_Video_Coding')
WIKI_TIZEN = ('Wikipedia: Tizen (Samsung)', 'https://de.wikipedia.org/wiki/Tizen')
WIKI_WEBOS = ('Wikipedia: webOS (LG)', 'https://de.wikipedia.org/wiki/WebOS')
WIKI_ANDROIDTV = ('Wikipedia: Android TV und Google TV', 'https://de.wikipedia.org/wiki/Android_TV')
WIKI_ENIGMA2 = ('Wikipedia: Enigma2', 'https://de.wikipedia.org/wiki/Enigma2')
WIKI_AIRPLAY = ('Wikipedia: AirPlay', 'https://de.wikipedia.org/wiki/AirPlay')
WIKI_STB = ('Wikipedia: Set-Top-Box', 'https://de.wikipedia.org/wiki/Set-Top-Box')
WIKI_UHD = ('Wikipedia: Ultra High Definition Television', 'https://de.wikipedia.org/wiki/Ultra_High_Definition_Television')
BREITBAND = ('Breitbandmessung der Bundesnetzagentur', 'https://www.breitbandmessung.de/')
VLC = ('VideoLAN: VLC Media Player (offizielle Website)', 'https://www.videolan.org/vlc/')
KODI = ('Kodi (offizielle Website)', 'https://kodi.tv/')
KODI_WIKI = ('Kodi Wiki: PVR IPTV Simple Client', 'https://kodi.wiki/view/Add-on:PVR_IPTV_Simple_Client')
KODINERDS = ('Kodinerds – deutschsprachige Kodi-Community', 'https://www.kodinerds.net/')
JELLYFIN = ('Jellyfin Dokumentation', 'https://jellyfin.org/docs/')
SMARTERS = ('IPTV Smarters (offizielle Website)', 'https://www.iptvsmarters.com/')
SIPTV = ('Smart IPTV (offizielle Website)', 'https://siptv.app/')
SSIPTV = ('SS IPTV (offizielle Website)', 'https://ss-iptv.com/')
FLIX = ('Flix IPTV (offizielle Website)', 'https://flixiptv.eu/')
SMARTONE = ('SmartOne IPTV (offizielle Website)', 'https://smartone-iptv.com/')
TIVIMATE_PLAY = ('TiviMate im Google Play Store', 'https://play.google.com/store/apps/details?id=ar.tvplayer.tv')
INFOMIR = ('Infomir – Hersteller der MAG-Boxen', 'https://www.infomir.eu/')
MAGENTA = ('Telekom: MagentaTV', 'https://www.telekom.de/magenta-tv')
VODAFONE = ('Vodafone Deutschland', 'https://www.vodafone.de/')
EINSUNDEINS = ('1&1', 'https://www.1und1.de/')
O2 = ('o2 Deutschland', 'https://www.o2online.de/')
VZ = ('Verbraucherzentrale', 'https://www.verbraucherzentrale.de/')
BNETZA = ('Bundesnetzagentur', 'https://www.bundesnetzagentur.de/')
TRUSTPILOT = ('Trustpilot Deutschland', 'https://de.trustpilot.com/')

SOURCES = {
    'was-ist-iptv': [WIKI_IPTV, BREITBAND, BNETZA],
    'iptv-kaufen': [VZ, BREITBAND],
    'iptv-anbieter': [VZ, BNETZA, WIKI_IPTV],
    'iptv-anbieter-vergleich': [VZ, TRUSTPILOT, BREITBAND],
    'iptv-4k': [WIKI_UHD, WIKI_HEVC, BREITBAND],
    'iptv-telekom-vodafone': [MAGENTA, VODAFONE, EINSUNDEINS, O2],
    'm3u-playlist': [WIKI_M3U, VLC],
    'iptv-geraete': [WIKI_STB, WIKI_ANDROIDTV, BREITBAND],
    'iptv-fire-tv-stick': [WIKI_ANDROIDTV, SMARTERS, TIVIMATE_PLAY],
    'iptv-smart-tv': [WIKI_TIZEN, WIKI_WEBOS, WIKI_ANDROIDTV],
    'iptv-samsung-tv': [WIKI_TIZEN, SIPTV, FLIX],
    'iptv-lg-tv': [WIKI_WEBOS, SSIPTV, SIPTV],
    'iptv-android': [WIKI_ANDROIDTV, SMARTERS, TIVIMATE_PLAY],
    'iptv-box': [WIKI_STB, WIKI_ANDROIDTV, WIKI_HEVC],
    'iptv-receiver': [WIKI_ENIGMA2, WIKI_STB, WIKI_HEVC],
    'mag-box-iptv': [INFOMIR, WIKI_STB],
    'iptv-apple-tv-iphone': [WIKI_AIRPLAY, SMARTERS, VLC],
    'iptv-pc-mac': [VLC, SMARTERS, KODI],
    'iptv-stick': [WIKI_ANDROIDTV, BREITBAND],
    'formuler-iptv': [WIKI_ANDROIDTV, WIKI_STB],
    'iptv-apps': [SMARTERS, TIVIMATE_PLAY, VLC, KODI],
    'iptv-smarters-pro': [SMARTERS],
    'iptv-smarters-pro-firestick': [SMARTERS],
    'tivimate': [TIVIMATE_PLAY],
    'tivimate-premium': [TIVIMATE_PLAY],
    'smart-iptv': [SIPTV, WIKI_M3U],
    'ss-iptv': [SSIPTV, WIKI_M3U],
    'set-iptv': [WIKI_M3U, WIKI_TIZEN, WIKI_WEBOS],
    'flix-iptv': [FLIX, WIKI_M3U],
    'smartone-iptv': [SMARTONE, WIKI_M3U],
    'xtream-codes-iptv': [WIKI_M3U, SMARTERS, TIVIMATE_PLAY],
    'kodi-iptv': [KODI, KODI_WIKI, KODINERDS, JELLYFIN],
    'iptv-erfahrungen': [TRUSTPILOT, VZ],
    'iptv-senderliste': [WIKI_M3U, WIKI_IPTV],
    'ratgeber': [WIKI_IPTV, BREITBAND],
}

# ---------------------------------------------------------------- lead overrides (primary keyword first)
LEAD = {
    'iptv-geraete': 'IPTV Geräte gibt es für jeden Haushalt: IPTV läuft auf fast jedem Bildschirm, den Sie schon besitzen. Finden Sie Ihr Gerät, die passende App und eine Schritt-für-Schritt-Anleitung.',
    'iptv-receiver': 'Ein IPTV Receiver empfängt Fernsehen über das Internet mit vertrauter Receiver-Bedienung. Viele deutsche Haushalte nutzen ohnehin einen Linux-Receiver für Satellit oder Kabel – mit dem richtigen Plugin empfängt er zusätzlich IPTV.',
    'ratgeber': 'Der IPTV Ratgeber von IPTV Kanal erklärt alles, was Sie über IPTV wissen müssen – von den Grundlagen über die Einrichtung auf Ihrem Gerät bis zur Wahl des passenden Anbieters.',
    'kodi-iptv': 'Kodi IPTV in wenigen Minuten: Kodi verwandelt PC, Box oder Stick in ein Mediacenter. Mit dem offiziellen PVR IPTV Simple Client wird daraus ein vollwertiger IPTV-Empfänger mit Programmführer.',
    'iptv-4k': 'IPTV in 4K zeigt viermal so viele Bildpunkte wie Full HD. Damit das Bild wirklich scharf und flüssig ankommt, müssen Leitung, Gerät und App zusammenpassen.',
    'iptv-pc-mac': 'IPTV am PC und Mac schauen Sie ohne Zusatzgeräte – im Arbeitszimmer, am Laptop oder per HDMI auf dem Fernseher. VLC ist dafür der einfachste Weg.',
    'iptv-android': 'IPTV auf Android ist die flexibelste Lösung: Fast jede IPTV App ist verfügbar, auf dem Handy für unterwegs und auf Google TV für das Wohnzimmer.',
}

# ---------------------------------------------------------------- extra sections
EXTRA_SECTIONS = {}
EXTRA_FAQ = {}

EXTRA_SECTIONS['ratgeber'] = [
    ('aufbau', 'So ist der IPTV Ratgeber aufgebaut', '''
<p>Der Ratgeber folgt dem Weg, den die meisten Leserinnen und Leser gehen: Zuerst verstehen, was IPTV ist, dann das passende Gerät und die passende App wählen und am Ende einen Anbieter finden, der zu den eigenen Ansprüchen passt.</p>
''' + table(['Bereich', 'Was Sie dort finden', 'Einstieg'], [
        ['Grundlagen', 'Begriffe, Technik, Internetgeschwindigkeit, Senderlisten', '<a href="/was-ist-iptv/">Was ist IPTV?</a>'],
        ['Geräte', 'Anleitungen für Smart TV, Fire TV Stick, Boxen, Apple, PC', '<a href="/iptv-geraete/">IPTV Geräte</a>'],
        ['Apps &amp; Player', 'Einrichtung von Smarters, TiviMate, Smart IPTV und weiteren Playern', '<a href="/iptv-apps/">IPTV Apps</a>'],
        ['Kauf &amp; Vergleich', 'Kriterien, Preise, Erfahrungen und Testzugang', '<a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>'],
    ], 'Aufbau des IPTV Ratgebers')),
    ('begriffe', 'Die wichtigsten IPTV-Begriffe kurz erklärt', table(['Begriff', 'Bedeutung'], [
        ['EPG', 'Elektronischer Programmführer mit Sendezeiten, ähnlich einer TV-Zeitschrift'],
        ['<a href="/m3u-playlist/">M3U</a>', 'Textdatei oder Link mit den Adressen aller Sender'],
        ['<a href="/xtream-codes-iptv/">Xtream Codes</a>', 'Login aus Server, Benutzername und Passwort, der Sender, Mediathek und EPG lädt'],
        ['VOD', 'Video on Demand: Filme und Serien zum Abruf'],
        ['Catch-Up', 'Sendungen der letzten Tage nachträglich ansehen, sofern der Sender es anbietet'],
        ['HEVC (H.265)', 'Moderner Videocodec, der <a href="/iptv-4k/">4K</a> mit weniger Bandbreite ermöglicht'],
        ['MAC-Adresse', 'Gerätekennung, mit der Apps wie Smart IPTV oder MAG-Boxen verknüpft werden'],
    ], 'Glossar IPTV') + '''
<p>Sie möchten nicht lange lesen? Dann starten Sie direkt mit dem <a href="/kostenlos-testen/">kostenlosen IPTV-Test</a> und lassen sich die Einrichtung von unserem deutschsprachigen Support per E-Mail oder WhatsApp erklären.</p>'''),
]

EXTRA_SECTIONS['iptv-geraete'] = [
    ('auswahl', 'In drei Schritten zum passenden IPTV-Gerät', steps(
        '<b>Bildschirm festlegen:</b> Wo schauen Sie hauptsächlich – Wohnzimmer-TV, Schlafzimmer, Tablet oder Laptop?',
        '<b>System prüfen:</b> Hat der Fernseher Tizen (Samsung), webOS (LG), Google TV oder ein anderes System? Die Tabelle oben zeigt die passende App.',
        '<b>Komfort entscheiden:</b> Reicht die App am Fernseher, oder möchten Sie TiviMate, Aufnahmen und schnelles Umschalten? Dann lohnt sich ein <a href="/iptv-stick/">IPTV Stick</a> oder eine <a href="/iptv-box/">IPTV Box</a>.') + '''
<p>Testen Sie anschließend genau dieses Gerät mit dem <a href="/kostenlos-testen/">kostenlosen Testzugang</a>. So sehen Sie vor dem Kauf, ob Bild, Ton und Umschaltzeiten passen.</p>'''),
    ('internet', 'Welche Internetgeschwindigkeit braucht jedes Gerät?', table(['Nutzung', 'Empfohlen pro Gerät', 'Verbindung'], [
        ['Smartphone unterwegs (SD/HD)', '5–10 Mbit/s', 'WLAN oder Mobilfunk'],
        ['Smart TV oder Stick in Full HD', '16 Mbit/s', 'WLAN 5 GHz oder LAN'],
        ['Fernseher in 4K', '25 Mbit/s', 'LAN-Kabel empfohlen'],
    ], 'Bandbreite je IPTV-Gerät') + '''
<p>Die Werte gelten pro gleichzeitigem Stream. Ihre tatsächliche Geschwindigkeit messen Sie neutral mit der Breitbandmessung der Bundesnetzagentur (Link unten). Mehr Hintergrund im Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>.</p>'''),
]
EXTRA_FAQ['iptv-geraete'] = [
    ('Funktioniert IPTV auch ohne Smart TV?', 'Ja. Ein Fire TV Stick, ein Google-TV-Stick oder eine Android-Box am HDMI-Anschluss macht jeden Fernseher IPTV-fähig. Alternativ schauen Sie am Smartphone, Tablet oder PC.'),
]

EXTRA_SECTIONS['iptv-smart-tv'] = [
    ('weitere-marken', 'Philips, Panasonic und Toshiba im Detail', '''
<p>Bei <strong>Philips</strong> hängt alles vom Modell ab: Geräte mit Google TV oder Android TV laden IPTV-Apps aus dem Play Store, günstigere Modelle mit Titan OS oder Saphi haben nur eine kleine Auswahl. <strong>Panasonic</strong> setzt bei vielen neueren Fernsehern auf Fire TV als Betriebssystem; die Einrichtung entspricht dann dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>. Ältere Panasonic-Modelle mit my Home Screen bieten kaum IPTV-Player. <strong>Toshiba</strong> verkauft je nach Serie Fernseher mit Fire TV, VIDAA oder Android TV.</p>
<p>Unsicher, was Ihr IPTV Fernseher kann? Senden Sie uns im <a href="/kostenlos-testen/">kostenlosen Test</a> einfach Marke und Modell – unser Support nennt Ihnen die passende App.</p>'''),
]
EXTRA_FAQ['iptv-smart-tv'] = [
    ('Was ist der Unterschied zwischen IPTV Fernseher und Smart TV?', 'Einen eigenen „IPTV Fernseher“ gibt es nicht. Gemeint ist ein Smart TV, auf dem eine IPTV App läuft. Entscheidend ist das Betriebssystem, denn es bestimmt, welche Apps verfügbar sind.'),
]

EXTRA_SECTIONS['iptv-samsung-tv'] = [
    ('modelljahre', 'Samsung Modelljahre und Tizen-Versionen', '''
<p>Samsung nutzt das Betriebssystem Tizen seit etwa 2015. Für IPTV ist vor allem das Modelljahr wichtig: Neuere Geräte haben schnellere Prozessoren, unterstützen HEVC für <a href="/iptv-4k/">4K-Sender</a> und bekommen die aktuellen Versionen der Player. Das Modelljahr erkennen Sie am Buchstaben in der Modellnummer (z. B. „TU“, „AU“, „BU“, „CU“, „DU“) oder unter <b>Einstellungen → Support → Über dieses TV-Gerät</b>.</p>
''' + checks(
        '<strong>Ab ca. 2018:</strong> alle gängigen Tizen-Player wie SET IPTV, Flix IPTV und IBO Player, flüssiges Full HD und 4K.',
        '<strong>2015–2017:</strong> einige Player laufen, Bedienung oft langsamer, nicht jede App ist im Store.',
        '<strong>Vor 2015 (Orsay):</strong> kaum noch IPTV-Apps – hier ist ein <a href="/iptv-stick/">IPTV Stick</a> die beste Lösung.')),
    ('tv-plus', 'Samsung TV Plus oder IPTV?', '''
<p>Auf vielen Samsung-Fernsehern ist <strong>Samsung TV Plus</strong> vorinstalliert, ein kostenloser, werbefinanzierter Dienst mit eigenen Themenkanälen. Er ist praktisch für nebenbei, ersetzt aber kein vollständiges IPTV-Angebot mit deutschen Sendern, Sport, Programmführer und Mediathek. Für IPTV auf dem Samsung Smart TV nutzen Sie deshalb einen der Player oben zusammen mit Ihrem <a href="/iptv-kaufen/">IPTV-Abo</a>.</p>'''),
]
EXTRA_FAQ['iptv-samsung-tv'] = [
    ('Funktioniert IPTV auf Samsung Tizen ohne Zusatzgerät?', 'Ja. Auf Samsung-Fernsehern mit Tizen installieren Sie einen Player wie SET IPTV oder Flix IPTV direkt aus dem Samsung-App-Store. Ein Stick ist nur nötig, wenn Sie TiviMate nutzen möchten oder das Modell sehr alt ist.'),
]

EXTRA_SECTIONS['iptv-lg-tv'] = [
    ('webos-versionen', 'Welche LG-Modelle eignen sich für IPTV?', '''
<p>LG verwendet webOS seit 2014. Neuere Versionen starten Apps schneller, unterstützen HEVC für <a href="/iptv-4k/">IPTV in 4K</a> und bekommen die aktuellen Versionen der Player. Ihre webOS-Version finden Sie unter <b>Einstellungen → Allgemein → Geräteinformationen</b> (je nach Modell auch „Support → TV-Informationen“).</p>
''' + table(['webOS', 'Modelljahre (ca.)', 'IPTV-Eignung'], [
        ['webOS 1–3', '2014–2017', 'SS IPTV und Smart IPTV laufen meist, Bedienung langsamer'],
        ['webOS 4–6', '2018–2021', 'Alle gängigen Player, 4K mit HEVC'],
        ['webOS 22 und neuer', 'ab 2022', 'Beste Leistung, aktuelle App-Versionen'],
    ], 'LG webOS Versionen und IPTV')),
    ('probleme', 'IPTV auf LG TV: häufige Probleme', table(['Problem', 'Lösung'], [
        ['App im LG Content Store nicht gefunden', 'Region des Fernsehers prüfen (Einstellungen → Allgemein → Standort) oder anderen Player wählen'],
        ['Playlist lädt nicht', 'MAC-Adresse bzw. Code erneut prüfen, App vollständig schließen und neu öffnen'],
        ['Bild friert ein', 'LAN-Kabel nutzen, im Player den Puffer erhöhen'],
        ['Kein Ton', 'Audioausgabe auf PCM stellen oder anderen Player-Modus wählen'],
    ], 'LG TV IPTV Problemlösungen') + '''
<p>Wenn Ihr LG-Fernseher sehr alt ist oder Sie TiviMate nutzen möchten, ist ein <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> am HDMI-Anschluss die einfachste Lösung. Über HDMI-CEC (bei LG „SIMPLINK“) bedienen Sie ihn mit der LG-Fernbedienung.</p>'''),
]
EXTRA_FAQ['iptv-lg-tv'] = [
    ('Gibt es IPTV Smarters für LG webOS?', 'Je nach Modell und Region ist eine Smarters-App im LG Content Store verfügbar. Ist sie nicht gelistet, funktionieren SS IPTV, Smart IPTV, Flix IPTV oder SET IPTV mit Ihrem M3U-Link.'),
]

EXTRA_SECTIONS['iptv-android'] = [
    ('einstellungen', 'Die richtigen Einstellungen auf Android', checks(
        '<strong>Energiesparmodus:</strong> für die IPTV App deaktivieren, sonst bricht der Stream im Hintergrund ab.',
        '<strong>Player:</strong> in Smarters oder XCIPTV den Hardware-Decoder wählen; bei Bildfehlern auf Software umschalten.',
        '<strong>Bild-in-Bild:</strong> in den Android-Einstellungen für die App erlauben, um nebenbei weiterzuschauen.',
        '<strong>Speicher:</strong> regelmäßig den App-Cache leeren, besonders auf Geräten mit wenig Speicher.',
        '<strong>Updates:</strong> Apps nur aus dem Play Store oder von der offiziellen Website des Entwicklers aktualisieren.')),
    ('probleme', 'IPTV auf Android funktioniert nicht? Lösungen', table(['Problem', 'Lösung'], [
        ['App lädt keine Sender', 'Zugangsdaten mit http:// und Port prüfen, mobile Daten/WLAN wechseln'],
        ['Stream bricht ab', 'Akkuoptimierung für die App ausschalten, Puffer erhöhen'],
        ['Cast-Symbol fehlt', 'Handy und Fernseher müssen im selben WLAN sein'],
        ['Ruckeln auf dem Tablet', 'Qualitätsstufe senken oder näher an den Router gehen'],
    ], 'Android IPTV Problemlösungen') + '''
<p>Für Android-Fernseher gelten dieselben Tipps wie für <a href="/iptv-box/">Android-TV-Boxen</a>. Welche Android IPTV App am besten zu Ihrem Gerät passt, zeigt die Übersicht <a href="/iptv-apps/">IPTV Apps</a>.</p>'''),
]
EXTRA_FAQ['iptv-android'] = [
    ('Gibt es einen kostenlosen IPTV Player für Android?', 'Ja. IPTV Smarters Pro, XCIPTV, VLC und Kodi sind kostenlos. Einige Apps bieten Zusatzfunktionen gegen Gebühr. Die Sender kommen immer aus Ihrem IPTV-Abo.'),
]

EXTRA_SECTIONS['iptv-apple-tv-iphone'] = [
    ('modelle', 'Welche Apple-Geräte eignen sich für IPTV?', table(['Gerät', 'Eignung', 'Hinweis'], [
        ['Apple TV 4K', 'Sehr gut', 'HEVC und 4K-Wiedergabe, LAN beim Modell mit Ethernet'],
        ['Apple TV HD', 'Gut für Full HD', 'Kein 4K'],
        ['iPhone und iPad', 'Sehr gut', 'Aktuelles iOS bzw. iPadOS empfohlen'],
        ['Mac', 'Gut', 'VLC, IPTVX oder Smarters Desktop – siehe <a href="/iptv-pc-mac/">PC &amp; Mac</a>'],
    ], 'Apple-Geräte für IPTV') + '''
<p>Für <a href="/iptv-4k/">4K-Sender</a> brauchen Sie ein Apple TV 4K und einen Fernseher mit HDCP 2.2. Ältere Apple-TV-Generationen ohne App Store sind für IPTV nicht geeignet.</p>'''),
    ('probleme', 'Typische Probleme auf iPhone und Apple TV', table(['Problem', 'Lösung'], [
        ['Login schlägt fehl', 'Server-URL mit http:// und Port prüfen; Autokorrektur kann Großbuchstaben einfügen'],
        ['AirPlay ruckelt', 'Apple TV per LAN anschließen und Handy nahe am Router nutzen'],
        ['Kein Programmführer', 'EPG in den App-Einstellungen aktivieren und neu laden'],
        ['App nicht mehr im App Store', 'Alternative App wählen, z. B. IPTVX statt Smarters Player Lite'],
    ], 'Apple IPTV Problemlösungen')),
]
EXTRA_FAQ['iptv-apple-tv-iphone'] = [
    ('Brauche ich ein Apple TV 4K für IPTV?', 'Nur für 4K-Sender. Für Full HD reicht auch ein Apple TV HD. Wichtig ist ein Modell mit App Store, damit Sie einen IPTV Player installieren können.'),
]

EXTRA_SECTIONS['iptv-pc-mac'] = [
    ('vlc-probleme', 'VLC und IPTV: häufige Probleme', table(['Problem', 'Lösung'], [
        ['Stream startet nicht', 'M3U-Link im Browser testen; Leerzeichen am Ende entfernen'],
        ['Bild ruckelt', 'Unter Werkzeuge → Einstellungen → „Alle“ → Eingang/Codecs den Netzwerk-Zwischenspeicher erhöhen (z. B. 3000 ms)'],
        ['Kein Ton', 'Unter Audio → Audiospur eine andere Spur wählen'],
        ['Playlist sehr lang', 'Gruppen in der Wiedergabeliste nutzen oder eine gefilterte Playlist anfordern'],
    ], 'VLC IPTV Problemlösungen') + '''
<p>Für ein TV-Raster mit Programmführer bleiben IPTV Smarters Desktop und <a href="/kodi-iptv/">Kodi</a> die komfortablere Wahl. Wie eine Playlist aufgebaut ist, erklärt der Ratgeber <a href="/m3u-playlist/">M3U Playlist</a>.</p>'''),
    ('laptop', 'Tipps für IPTV am Laptop und MacBook', checks(
        'Netzteil anschließen: Videowiedergabe in HD und 4K verbraucht viel Akku.',
        'Im Büro- oder Hotel-WLAN können Firmen-Firewalls Streaming-Ports blockieren – testen Sie dann einen Hotspot.',
        'Mit einem zweiten Monitor läuft der Stream nebenbei, während Sie arbeiten.',
        'Den Browser-Webplayer nur für Links ohne persönliche Zugangsdaten nutzen.')),
]
EXTRA_FAQ['iptv-pc-mac'] = [
    ('Ist IPTV im Webbrowser sicher?', 'Webplayer sind bequem, sehen aber Ihren Link samt Zugangsdaten. Für persönliche Zugänge sind lokale Programme wie VLC, IPTV Smarters Desktop oder Kodi die sicherere Wahl.'),
]

EXTRA_SECTIONS['iptv-receiver'] = [
    ('plugins', 'Enigma2 IPTV Plugins im Vergleich', table(['Plugin', 'Login', 'Stärken'], [
        ['XStreamity', 'Xtream Codes', 'Live-TV, Filme, Serien und Catch-Up in eigener Oberfläche'],
        ['Jedi Maker Xtream', 'Xtream Codes, M3U', 'Erzeugt Bouquets für die normale Kanalliste'],
        ['E2m3u2bouquet', 'M3U', 'Wandelt M3U-Listen in Bouquets mit EPG-Zuordnung um'],
    ], 'Enigma2 IPTV Plugins') + '''
<p>Welches Plugin verfügbar ist, hängt vom Image ab. Bei OpenATV und OpenPLi finden Sie die gängigen Plugins im Plugin-Browser. Für Xtream-Zugänge ist XStreamity am einfachsten; wer IPTV direkt neben Sat-Sendern in der Kanalliste möchte, wählt Jedi Maker Xtream. Grundlagen zum Login lesen Sie unter <a href="/xtream-codes-iptv/">Xtream Codes</a>.</p>'''),
    ('kaufen', 'Worauf Sie beim Kauf eines IPTV Receivers achten', checks(
        '<strong>HEVC/H.265-Decoder:</strong> Pflicht für 4K und spart Bandbreite bei Full HD.',
        '<strong>Gigabit-LAN:</strong> stabiler als WLAN, besonders bei 4K und mehreren Aufnahmen.',
        '<strong>Arbeitsspeicher:</strong> mindestens 1 GB, besser 2 GB für große Senderlisten.',
        '<strong>Aktive Images:</strong> Das Modell sollte von OpenATV oder OpenPLi unterstützt werden.',
        '<strong>4K IPTV Receiver:</strong> nur sinnvoll mit 4K-Fernseher und mindestens 25 Mbit/s.')),
]
EXTRA_FAQ['iptv-receiver'] = [
    ('Welcher IPTV Receiver ist für 4K geeignet?', 'Achten Sie auf HEVC-Decoder, Gigabit-LAN und aktuelle Image-Unterstützung. Aktuelle 4K-Modelle von GigaBlue, VU+ oder Edision sowie 4K-MAG-Boxen eignen sich. Wer keinen Sat-Empfang braucht, ist mit einer Android-TV-Box oft günstiger dran.'),
]

EXTRA_SECTIONS['mag-box-iptv'] = [
    ('fehler', 'MAG Box Fehlermeldungen und Lösungen', table(['Meldung', 'Bedeutung', 'Lösung'], [
        ['„Portal nicht gefunden“ / Ladebalken hängt', 'Portal-URL falsch oder nicht erreichbar', 'URL exakt mit http:// und abschließendem Schrägstrich eintragen, Box neu starten'],
        ['„STB blockiert“ / „Ihr STB ist gesperrt“', 'MAC-Adresse nicht freigeschaltet oder Zugang abgelaufen', 'MAC-Adresse beim Anbieter prüfen lassen'],
        ['Kein EPG', 'Zeitzone oder NTP-Server falsch', 'Einstellungen → System → Zeit: Europa/Berlin wählen'],
        ['Bild ruckelt', 'Netzwerk zu langsam oder WLAN schwach', 'LAN-Kabel nutzen, Router neu starten'],
    ], 'MAG Box Fehler')),
    ('upgrade', 'MAG 254, 256 und 322: lohnt sich ein Upgrade?', '''
<p>Die Infomir MAG 254 und MAG 256 sind robuste, aber ältere Boxen ohne HEVC. Viele Sender werden heute effizient in H.265 übertragen; ohne passenden Decoder fallen diese Streams aus oder laufen nur in reduzierter Qualität. Die MAG 322 und MAG 324 unterstützen HEVC und genügen für Full HD. Wer eine MAG TV Box für 4K sucht, wählt ein Modell der 4xx- oder 5xx-Serie. Alternativ ist eine <a href="/iptv-box/">Android-TV-Box</a> mit STBEmu flexibler, weil zusätzlich Apps wie TiviMate laufen.</p>'''),
]
EXTRA_FAQ['mag-box-iptv'] = [
    ('Was bedeutet „STB blockiert“ auf der MAG Box?', 'Das Portal erkennt die MAC-Adresse nicht als freigeschaltet oder der Zugang ist abgelaufen. Lassen Sie die MAC-Adresse vom Anbieter prüfen und starten Sie die Box neu.'),
]

EXTRA_SECTIONS['iptv-4k'] = [
    ('hdr', 'HDR, HDR10 und Dolby Vision bei 4K-IPTV', '''
<p>Neben der Auflösung bestimmt der Dynamikumfang (HDR) die Bildwirkung. Bei IPTV in 4K kommt HDR meist als HDR10 oder HLG an. Damit HDR sichtbar wird, müssen Fernseher, HDMI-Anschluss und Abspielgerät es unterstützen. Ein Fire TV Stick 4K Max, Apple TV 4K oder eine aktuelle Android-TV-Box geben HDR korrekt aus; ältere Sticks zeigen dieselbe Quelle nur in SDR.</p>
<p>Wichtig: HDR verbraucht kaum zusätzliche Bandbreite. Entscheidend für ein ruckelfreies Bild bleibt eine stabile Leitung mit mindestens 25 Mbit/s pro 4K-Stream.</p>'''),
    ('checkliste', 'Checkliste: Ist Ihr Zuhause bereit für 4K-IPTV?', checks(
        'Internet: mindestens 25 Mbit/s frei pro gleichzeitigem 4K-Stream – messen Sie direkt am Fernseher.',
        'Gerät: HEVC-Decoder, HDMI 2.0 und HDCP 2.2 (z. B. <a href="/iptv-stick/">aktuelle IPTV Sticks</a>).',
        'Verbindung: LAN-Kabel oder 5-GHz-WLAN mit gutem Signal.',
        'App: Hardware-Decoder aktiviert, z. B. in <a href="/tivimate/">TiviMate</a>.',
        'Paket: 4K ist bei IPTV Kanal in allen <a href="/preise/">Paketen</a> enthalten.')),
]
EXTRA_FAQ['iptv-4k'] = [
    ('Brauche ich für 4K-IPTV einen neuen Fernseher?', 'Nur wenn Ihr Fernseher kein 4K kann. Bei einem 4K-Fernseher reicht oft ein aktueller Stick oder eine Box mit HEVC-Decoder am HDMI-Anschluss mit HDCP 2.2.'),
]

EXTRA_SECTIONS['iptv-anbieter'] = [
    ('kundenservice', 'IPTV Kundenservice: So prüfen Sie den Support', '''
<p>Der Support entscheidet, ob ein IPTV-Dienst im Alltag funktioniert. Prüfen Sie ihn deshalb schon im Test: Stellen Sie eine konkrete Frage zur Einrichtung Ihres Geräts und achten Sie darauf, wie schnell und verständlich die Antwort kommt. Ein guter IPTV Service nennt Ihnen die passende App, hilft bei Zugangsdaten und Programmführer und ist auch abends erreichbar, wenn die meisten Menschen fernsehen.</p>
''' + checks(
        'Kontaktwege: E-Mail und ein Messenger wie WhatsApp, nicht nur ein Bot.',
        'Sprache: Antworten auf Deutsch, ohne Übersetzungsprogramm-Kauderwelsch.',
        'Einrichtungshilfe: konkrete Schritte für Ihr Gerät statt Standardtexte.',
        'Transparenz: klare Angaben zu Laufzeit, Geräteanzahl und Preis vor dem Kauf.')),
    ('zahlung', 'Transparente Preise und Zahlung', '''
<p>Seriöse IPTV Anbieter nennen den Gesamtpreis vor der Bestellung und bestätigen ihn schriftlich. Achten Sie auf eine feste Laufzeit ohne automatische Verlängerung und darauf, dass Sie die Zahlungsangaben erst nach einer klaren Bestätigung erhalten. Bei IPTV Kanal sehen Sie alle Paketpreise öffentlich auf der Seite <a href="/preise/">IPTV Preise</a>; nach Ihrer Anfrage erhalten Sie die Angaben zur Bezahlung per E-Mail oder WhatsApp. Weitere Kriterien zeigt der <a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>.</p>'''),
]
EXTRA_FAQ['iptv-anbieter'] = [
    ('Was ist der Unterschied zwischen IPTV Anbieter und IPTV App?', 'Der IPTV Anbieter liefert die Sender und Zugangsdaten. Die IPTV App ist nur der Player, in den Sie diese Zugangsdaten eintragen. Apps wie IPTV Smarters oder TiviMate enthalten selbst keine Sender.'),
]

EXTRA_SECTIONS['iptv-telekom-vodafone'] = [
    ('technik', 'Technik: Multicast, Unicast und Streaming-Apps', '''
<p>Beim klassischen Provider-IPTV wie MagentaTV am Telekom-Anschluss werden Livesender per <strong>Multicast</strong> verteilt: Ein Datenstrom versorgt viele Haushalte gleichzeitig, das Netz wird geschont. Streaming-Apps und unabhängige IPTV-Dienste nutzen dagegen <strong>Unicast</strong> über das offene Internet – jeder Zuschauer bekommt seinen eigenen Stream. Deshalb funktionieren sie an jedem Anschluss, auch über Mobilfunk oder im Ausland innerhalb der EU.</p>
<p>Für Sie heißt das: Provider-TV ist an den Anschluss gebunden, unabhängiges IPTV an Ihre Zugangsdaten. Wie viel Bandbreite Sie pro Gerät brauchen, zeigt der Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>.</p>'''),
    ('kosten', 'Was kostet Fernsehen über den Internetanbieter?', '''
<p>TV-Pakete der Internetanbieter werden in der Regel als monatlicher Aufpreis zum Internettarif berechnet, oft mit Mindestlaufzeit und gegebenenfalls zusätzlicher Gebühr für Receiver oder Zusatzpakete. Die aktuellen Konditionen nennen Telekom, Vodafone, 1&amp;1 und o2 auf ihren Websites (Links unten). Unabhängiges IPTV kostet bei IPTV Kanal ab 9 € für einen Monat, ohne Vertrag und ohne automatische Verlängerung – die Übersicht steht unter <a href="/preise/">IPTV Preise</a>.</p>'''),
]
EXTRA_FAQ['iptv-telekom-vodafone'] = [
    ('Kann ich MagentaTV und unabhängiges IPTV parallel nutzen?', 'Ja. Beide laufen über dieselbe Internetleitung, solange genug Bandbreite frei ist. Viele testen unabhängiges IPTV zuerst parallel, bevor sie ein TV-Zusatzpaket kündigen.'),
]

EXTRA_SECTIONS['smart-iptv'] = [
    ('geraete', 'Smart IPTV auf Android TV, Fire TV, Sony, Philips und Hisense', table(['Gerät', 'Smart IPTV', 'Bessere Alternative'], [
        ['<a href="/iptv-samsung-tv/">Samsung (Tizen)</a>', 'Je nach Modell und Store', '<a href="/set-iptv/">SET IPTV</a>, <a href="/flix-iptv/">Flix IPTV</a>'],
        ['<a href="/iptv-lg-tv/">LG (webOS)</a>', 'Ja, LG Content Store', '<a href="/ss-iptv/">SS IPTV</a> (kostenlos)'],
        ['Sony, Philips (Android/Google TV)', 'APK von der offiziellen Website', '<a href="/tivimate/">TiviMate</a>, <a href="/iptv-smarters-pro/">Smarters</a>'],
        ['<a href="/iptv-fire-tv-stick/">Fire TV Stick</a> (Fire OS)', 'APK per Downloader', 'TiviMate, Smarters'],
        ['Hisense VIDAA', 'Verfügbarkeit wechselt', '<a href="/iptv-stick/">IPTV Stick</a> am HDMI-Anschluss'],
    ], 'Smart IPTV nach Gerät') + '''
<p>Laden Sie die Android-Version (APK) nur von der offiziellen Smart-IPTV-Website herunter. Angebote mit „Smart IPTV Pro“, „Smart IPTV Premium“ oder fertigen „Smart IPTV Listen“ stammen in der Regel nicht vom Entwickler; Aktivierung und Playlist-Upload laufen ausschließlich über die offizielle Seite.</p>'''),
]
EXTRA_FAQ['smart-iptv'] = [
    ('Gibt es Smart IPTV für den Fire TV Stick?', 'Ja, auf Fire-TV-Geräten mit Fire OS lässt sich die Android-Version von der offiziellen Website über die App Downloader installieren. Auf dem Fire TV Stick bieten TiviMate oder IPTV Smarters aber deutlich mehr Komfort.'),
]

EXTRA_SECTIONS['ss-iptv'] = [
    ('geraete', 'SS IPTV auf Samsung, LG und Android', '''
<p>Auf <a href="/iptv-lg-tv/">LG-Fernsehern</a> finden Sie SS IPTV direkt im LG Content Store – dort ist die App am weitesten verbreitet. Auf <a href="/iptv-samsung-tv/">Samsung-Modellen</a> hängt die Verfügbarkeit vom Modelljahr und der Region ab. Die Android-Version (SSIPTV Android) läuft auf Smartphones, Tablets und Android-TV-Geräten; dort sind <a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> allerdings komfortabler.</p>'''),
    ('m3u8', 'SSIPTV Liste: M3U oder M3U8?', '''
<p>SS IPTV liest beide Formate. <strong>M3U8</strong> ist dieselbe Liste in UTF-8-Kodierung, was Umlaute in Sendernamen korrekt darstellt. Für eine übersichtliche SSIPTV Liste fordern Sie bei Ihrem Anbieter am besten eine Playlist im Format <code>m3u_plus</code> an: Sie enthält Gruppen und Senderlogos, die SS IPTV als Kategorien anzeigt. Wie eine Playlist aufgebaut ist, erklärt der Ratgeber <a href="/m3u-playlist/">M3U Playlist</a>.</p>
''' + tip('Speichern Sie im Playlist-Editor nur Links, die Sie selbst von Ihrem Anbieter erhalten haben. Öffentlich verbreitete „SSIPTV Listen“ sind meist veraltet und rechtlich problematisch.', 'Achtung')),
]
EXTRA_FAQ['ss-iptv'] = [
    ('Wie lade ich eine M3U-Liste in SS IPTV?', 'Code in den App-Einstellungen unter „Allgemein“ erzeugen, im Playlist-Editor auf der SS-IPTV-Website eingeben, den M3U-Link als externe Playlist hinzufügen und speichern. Danach die App neu laden.'),
]

EXTRA_SECTIONS['set-iptv'] = [
    ('geraete', 'SET IPTV auf Samsung, LG und Android', '''
<p>Auf <a href="/iptv-samsung-tv/">Samsung-Fernsehern mit Tizen</a> und <a href="/iptv-lg-tv/">LG-Fernsehern mit webOS</a> installieren Sie SET IPTV aus dem jeweiligen App-Store. Die Verfügbarkeit kann je nach Modelljahr und Region schwanken. Auf Android-Geräten läuft die App ebenfalls, dort gibt es mit <a href="/tivimate/">TiviMate</a> und <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> aber komfortablere Alternativen.</p>
<p>Die Aktivierung ist an die MAC-Adresse des Geräts gebunden. Wechseln Sie den Fernseher, müssen Sie die App auf dem neuen Gerät erneut aktivieren und die Playlist mit der neuen MAC-Adresse hochladen.</p>'''),
    ('fehler', 'SET IPTV: typische Fehler und Lösungen', table(['Problem', 'Lösung'], [
        ['Playlist erscheint nicht', 'MAC-Adresse exakt prüfen (Ziffer 0 und Buchstabe O verwechselt?), App neu starten'],
        ['Programmführer leer', 'EPG-Adresse auf der Upload-Seite ergänzen und App neu laden'],
        ['„Expired“ nach der Testphase', 'App über die Website des Entwicklers aktivieren'],
        ['Ruckeln', 'Fernseher per LAN verbinden, Player-Modus in den Einstellungen wechseln'],
    ], 'SET IPTV Problemlösungen')),
]
EXTRA_FAQ['set-iptv'] = [
    ('Muss ich SET IPTV bei einem neuen Fernseher neu aktivieren?', 'Ja. Die Aktivierung gilt für die MAC-Adresse eines Geräts. Auf einem neuen Fernseher aktivieren Sie die App erneut und laden die Playlist mit der neuen MAC-Adresse hoch.'),
]

EXTRA_SECTIONS['flix-iptv'] = [
    ('fire-tv', 'Flix IPTV auf Fire TV Stick und Android', steps(
        'Auf dem <a href="/iptv-fire-tv-stick/">Fire TV Stick mit Fire OS</a> die App <b>Downloader</b> aus dem Amazon Appstore installieren.',
        'Unter <b>Einstellungen → Mein Fire TV → Entwickleroptionen</b> die Installation unbekannter Apps für Downloader erlauben.',
        'In Downloader die APK-Adresse von der offiziellen Flix-IPTV-Website eingeben und installieren.',
        'Flix IPTV öffnen, MAC-Adresse notieren und die Playlist wie oben beschrieben hochladen.') + '''
<p>Auf Android-Smartphones und Android-TV-Geräten erhalten Sie Flix IPTV in der Regel direkt aus dem Play Store. Fire-TV-Modelle mit Vega OS unterstützen keine APK-Installation.</p>'''),
    ('fehler', 'Flix IPTV: häufige Fehler', table(['Problem', 'Lösung'], [
        ['Playlist leer', 'M3U-Link im Browser testen, MAC-Adresse erneut vergleichen'],
        ['Filme ohne Poster', 'Playlist im Format m3u_plus verwenden'],
        ['Untertitel fehlen', 'Im Player über das Untertitel-Symbol eine Spur wählen, sofern vorhanden'],
        ['Testphase abgelaufen', 'Aktivierung über die Website des Entwicklers abschließen'],
    ], 'Flix IPTV Problemlösungen') + '''
<p>Sie möchten mehrere Player vergleichen? Die Übersicht <a href="/iptv-apps/">IPTV Apps</a> zeigt Stärken und Grenzen aller gängigen Apps für Samsung, LG und Fire TV.</p>'''),
]
EXTRA_FAQ['flix-iptv'] = [
    ('Warum ist meine Playlist in Flix IPTV leer?', 'Meist stimmt die MAC-Adresse nicht exakt oder der M3U-Link ist fehlerhaft. Prüfen Sie beides auf der Manage-Playlist-Seite und starten Sie die App danach vollständig neu.'),
]

EXTRA_SECTIONS['smartone-iptv'] = [
    ('android', 'SmartOne IPTV auf Android und Fire TV', '''
<p>Neben Samsung und LG läuft SmartOne IPTV auch auf Android-Geräten. Auf dem <a href="/iptv-fire-tv-stick/">Fire TV Stick mit Fire OS</a> installieren Sie die Android-Version über die App Downloader von der offiziellen Website. Die Verknüpfung erfolgt dort genauso über die MAC-Adresse. Auf Android-TV-Geräten bieten <a href="/tivimate/">TiviMate</a> und <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> jedoch mehr Funktionen, etwa Xtream-Login und ein komfortableres EPG.</p>'''),
    ('fehler', 'SmartOne IPTV: typische Probleme', table(['Problem', 'Lösung'], [
        ['App im Store nicht gefunden', 'Auf älteren Modellen nicht immer gelistet – <a href="/set-iptv/">SET IPTV</a> oder <a href="/flix-iptv/">Flix IPTV</a> nutzen'],
        ['Playlist lädt nicht', 'MAC-Adresse und M3U-Link prüfen, App komplett beenden und neu starten'],
        ['Kein Programmführer', 'Playlist mit EPG-Zuordnung (tvg-id) verwenden'],
        ['Verwechslung mit Smart IPTV', 'Zugangsdaten auf der richtigen Website eintragen – beide Apps haben eigene Seiten'],
    ], 'SmartOne IPTV Problemlösungen')),
    ('vor-aktivierung', 'Checkliste vor der Aktivierung', checks(
        'Testphase nutzen: Läuft die App auf Ihrem Modell flüssig und startet sie schnell?',
        'Sender prüfen: Mit Ihrem M3U-Link aus dem <a href="/kostenlos-testen/">IPTV-Test</a> Live-TV, Filme und Programmführer ausprobieren.',
        'Netzwerk testen: Abends zur Hauptsendezeit per LAN und WLAN vergleichen.',
        'Alternativen vergleichen: Auf demselben Fernseher <a href="/set-iptv/">SET IPTV</a> oder <a href="/flix-iptv/">Flix IPTV</a> testen – die Aktivierung gilt jeweils nur für eine App und ein Gerät.',
        'Erst dann aktivieren: Die Gebühr zahlen Sie direkt beim App-Entwickler, nicht bei Ihrem IPTV-Anbieter.')),
    ('fuer-wen', 'Für wen eignet sich SmartOne IPTV?', '''
<p>SmartOne IPTV (oft auch als „Smart One IPTV“ gesucht) passt zu allen, die eine schlanke App direkt am Fernseher möchten und mit M3U-Links arbeiten. Wer Filme und Serien mit Postern, Aufnahmen oder mehrere Profile braucht, ist mit Flix IPTV oder einem Stick mit TiviMate besser bedient. Testen Sie die App am besten mit dem <a href="/kostenlos-testen/">kostenlosen IPTV-Test</a>, bevor Sie sie aktivieren.</p>'''),
]

EXTRA_SECTIONS['xtream-codes-iptv'] = [
    ('fehler', 'Xtream-Login: Fehlermeldungen verstehen', table(['Meldung', 'Häufige Ursache', 'Lösung'], [
        ['„Invalid credentials“ / ungültige Zugangsdaten', 'Tippfehler, Leerzeichen, falscher Port', 'Daten aus der E-Mail kopieren statt abtippen'],
        ['„Max connections reached“', 'Mehr Geräte gleichzeitig als im Paket gebucht', 'Ein Gerät schließen oder Paket mit mehr Geräten wählen'],
        ['„Account expired“', 'Laufzeit beendet', 'Paket verlängern – siehe <a href="/preise/">Preise</a>'],
        ['Keine Verbindung zum Server', 'Server-URL ohne http:// oder VPN/DNS-Filter', 'URL vollständig eintragen, Filter testweise deaktivieren'],
    ], 'Xtream Codes Fehlermeldungen') + '''
<p>Bei IPTV Kanal wählen Sie 1 bis 5 gleichzeitig nutzbare Geräte. Die Geräteanzahl entspricht den erlaubten parallelen Verbindungen Ihres Xtream-Logins.</p>'''),
    ('sicherheit', 'Xtream-Zugangsdaten sicher nutzen', checks(
        'Zugangsdaten nur in vertrauenswürdigen Apps aus offiziellen Stores eintragen.',
        'Keine Online-Konverter nutzen, die Ihren Xtream-Login in einen M3U-Link umwandeln – sie sehen Ihre Daten.',
        'Login nicht in Foren oder Gruppen teilen; geteilte Zugänge führen zu „Max connections“-Fehlern.',
        'Bei Verdacht auf Missbrauch neue Zugangsdaten beim Anbieter anfordern.')),
]
EXTRA_FAQ['xtream-codes-iptv'] = [
    ('Was bedeutet „Max connections reached“?', 'Mit Ihrem Login schauen mehr Geräte gleichzeitig, als Ihr Paket erlaubt. Schließen Sie die App auf einem Gerät oder wählen Sie ein Paket mit mehr gleichzeitigen Geräten.'),
]

EXTRA_SECTIONS['kodi-iptv'] = [
    ('fire-tv', 'Kodi auf dem Fire TV Stick installieren', steps(
        'Auf dem <a href="/iptv-fire-tv-stick/">Fire TV Stick mit Fire OS</a> die App <b>Downloader</b> installieren und unbekannte Apps erlauben.',
        'In Downloader die offizielle Download-Seite von kodi.tv öffnen und die Android-Version (ARMV7A, 32-Bit) wählen.',
        'Kodi installieren, starten und den PVR IPTV Simple Client wie oben beschrieben einrichten.') + '''
<p>Auf Fire-TV-Modellen mit Vega OS ist das nicht möglich. Für Android-TV-Boxen und Google TV gibt es Kodi direkt im Play Store.</p>'''),
    ('live-tv', 'Kodi Live-TV: Programmführer, Aufnahme und Favoriten', '''
<p>Nach der Einrichtung zeigt Kodi unter <b>TV</b> eine Kanalliste, das <b>EPG-Raster</b> und eine Suche nach Sendungen. Aufnahmen sind mit einem PVR-Backend wie TVHeadend möglich; der Simple Client allein nimmt nicht auf. Favoriten legen Sie als eigene Kanalgruppe an, damit Sie nicht durch tausende Sender scrollen müssen. Hilfe zu Skins, Add-ons und Einstellungen finden Sie in der deutschsprachigen Community Kodinerds (Link unten).</p>'''),
]
EXTRA_FAQ['kodi-iptv'] = [
    ('Kann Kodi IPTV-Sendungen aufnehmen?', 'Der PVR IPTV Simple Client selbst nimmt nicht auf. Aufnahmen sind mit einem zusätzlichen Backend wie TVHeadend oder mit Jellyfin möglich.'),
]

EXTRA_SECTIONS['iptv-senderliste'] = []
