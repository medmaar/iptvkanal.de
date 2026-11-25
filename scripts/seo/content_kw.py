"""Keyword-cluster pass (25.11.2026) from the Germany keyword list: setup hub, player comparison, TiviMate on
Fire TV, Chromecast, browser playback, Downloader, Plex/Jellyfin. Only clusters without an existing page were
built; everything else maps to existing pages or a redirect alias in _redirects. Prices of third-party apps are
not quoted because they change often; pages point to the official stores and websites instead."""
from .helpers import steps, checks, tip, table, proscons, chips

PAGES = []

LOGIN_TIP = tip('Ihre Zugangsdaten (Benutzername, Passwort, Server-Adresse bzw. M3U-Link) erhalten Sie nach dem '
                '<a href="/kostenlos-testen/">kostenlosen Test</a> oder der <a href="/preise/">Bestellung</a> per E-Mail. '
                'Kopieren Sie sie genau – ein fehlendes Zeichen oder ein Leerzeichen am Ende ist die häufigste Fehlerquelle.',
                'Zugangsdaten')

# ================================================================ IPTV EINRICHTEN (setting iptv)
PAGES.append(dict(
    slug='iptv-einrichten', parent='ratgeber', kind='guide',
    title='IPTV einrichten: Anleitung für jedes Gerät (2026)',
    description='IPTV einrichten in 4 Schritten: Gerät prüfen, passende App wählen, Xtream-Login, M3U-Link oder MAC eintragen und EPG laden – mit Anleitungen für alle Geräte.',
    eyebrow='SCHRITT-FÜR-SCHRITT', h1='IPTV einrichten: so klappt es auf jedem Gerät',
    lead='IPTV einrichten dauert auf den meisten Geräten keine 15 Minuten. Entscheidend sind nur drei Dinge: ein Gerät, auf dem eine passende App läuft, die richtige Login-Art und eine stabile Internetverbindung.',
    answer='So richten Sie IPTV ein: 1. Prüfen Sie, welches Betriebssystem Ihr Gerät hat (Fire OS, Google TV, Tizen, webOS, tvOS, Windows). 2. Installieren Sie eine passende IPTV-App aus dem offiziellen Store. 3. Tragen Sie Ihre Zugangsdaten ein – als Xtream-Codes-Login, M3U-Link oder per MAC-Adresse. 4. Laden Sie den Programmführer (EPG) und prüfen Sie Zeitzone und Bildqualität. Für Live-Sport empfiehlt sich ein LAN-Kabel.',
    sections=[
        ('ueberblick', 'IPTV einrichten in vier Schritten', steps(
            '<b>Gerät bestimmen:</b> Schauen Sie in den Einstellungen nach dem Betriebssystem. Davon hängt ab, welche Apps Sie installieren können – ein Samsung-Fernseher mit Tizen hat andere Apps als ein Fire TV Stick.',
            '<b>App installieren:</b> Wählen Sie einen IPTV-Player aus dem offiziellen Store Ihres Geräts. Ein guter Startpunkt ist unser Vergleich <a href="/bester-iptv-player/">Bester IPTV Player</a>.',
            '<b>Zugang eintragen:</b> Je nach App als Xtream-Codes-Login (Benutzername, Passwort, Server-URL), als M3U-Link oder – bei MAC-basierten Apps – über die Website des App-Entwicklers.',
            '<b>Feinschliff:</b> Programmführer (EPG) laden, Zeitzone prüfen, Hardware-Decoder aktivieren und Lieblingssender als Favoriten speichern.')
         + '<p>Die Reihenfolge ist auf allen Geräten dieselbe. Unterschiede gibt es nur bei der App-Auswahl und beim Weg, auf dem die Zugangsdaten in die App gelangen.</p>' + LOGIN_TIP),
        ('login-arten', 'Xtream Codes, M3U oder MAC: welche Login-Art passt?', table(['Login-Art', 'So funktioniert sie', 'Geeignet für'], [
            ['<a href="/xtream-codes-iptv/">Xtream Codes API</a>', 'Benutzername, Passwort und Server-Adresse direkt in der App', 'TiviMate, IPTV Smarters Pro, IPTVX, OTT Navigator – die komfortabelste Variante mit Filmen, Serien und EPG'],
            ['<a href="/m3u-playlist/">M3U-Link</a>', 'Eine einzige Adresse, die die komplette Senderliste liefert', 'VLC, Kodi, SS IPTV, GSE und Apps ohne Xtream-Unterstützung'],
            ['MAC-Adresse', 'Die App zeigt eine Gerätekennung; die Playlist laden Sie auf der Website des Entwicklers hoch', '<a href="/set-iptv/">SET IPTV</a>, <a href="/smart-iptv/">Smart IPTV</a>, <a href="/ibo-player/">IBO Player</a> auf Samsung und LG'],
            ['Portal (Stalker)', 'Portal-URL im Gerät, Freischaltung über die MAC-Adresse', '<a href="/mag-box-iptv/">MAG-Boxen</a>, <a href="/stbemu/">STBEmu</a>, <a href="/formuler-iptv/">Formuler</a>'],
        ], 'Login-Arten für IPTV im Vergleich') + '''
<p>Wenn Ihre App beides kann, nehmen Sie immer den <strong>Xtream-Codes-Login</strong>. Die App lädt dann Sender, Mediathek und Programmführer getrennt und aktualisiert sie selbstständig. Ein M3U-Link ist dagegen eine starre Liste: Ändert der Anbieter Sender, muss die App die ganze Liste neu laden.</p>'''),
        ('geraete', 'Anleitungen nach Gerät', table(['Gerät', 'Empfohlene Apps', 'Anleitung'], [
            ['Amazon Fire TV Stick (Fire OS)', 'TiviMate, IPTV Smarters Pro', '<a href="/iptv-fire-tv-stick/">Fire TV Stick</a> · <a href="/tivimate-fire-tv-stick/">TiviMate auf Fire TV</a>'],
            ['Samsung Smart TV (Tizen)', 'SET IPTV, Smart IPTV, IBO Player', '<a href="/iptv-samsung-tv/">Samsung TV</a>'],
            ['LG Smart TV (webOS)', 'SET IPTV, SS IPTV, IBO Player', '<a href="/iptv-lg-tv/">LG TV</a>'],
            ['Google TV / Android TV', 'TiviMate, OTT Navigator, IPTV Smarters Pro', '<a href="/iptv-google-tv/">Google TV</a> · <a href="/iptv-android/">Android</a>'],
            ['Apple TV, iPhone, iPad', 'IPTVX, iPlayTV, IPTV Smarters', '<a href="/iptv-apple-tv-iphone/">Apple TV &amp; iPhone</a>'],
            ['Windows-PC, Mac', 'VLC, IPTV Smarters Pro, Kodi, Web-Player', '<a href="/iptv-pc-mac/">PC &amp; Mac</a> · <a href="/iptv-im-browser/">im Browser</a>'],
            ['MAG-Box, Formuler', 'Portal bzw. MyTVOnline', '<a href="/mag-box-iptv/">MAG-Box</a> · <a href="/formuler-iptv/">Formuler</a>'],
            ['Enigma2-Receiver', 'Bouquet-Import oder IPTV-Plugin', '<a href="/iptv-receiver/">IPTV Receiver</a>'],
        ], 'IPTV-Anleitungen nach Gerät') + '''
<p>Alle Geräte und Betriebssysteme mit ihren Besonderheiten finden Sie in der <a href="/iptv-geraete/">Geräteübersicht</a>, alle Player in der <a href="/iptv-apps/">App-Übersicht</a>.</p>'''),
        ('epg', 'Programmführer (EPG) einrichten', '''
<p>Der elektronische Programmführer zeigt, was gerade läuft und was als Nächstes kommt. Bei einem Xtream-Codes-Login wird er meist automatisch mitgeladen. Bei M3U-Listen tragen Sie die <strong>EPG-Adresse</strong> (XMLTV, oft mit der Endung <code>.xml</code> oder <code>.xml.gz</code>) separat in den Playlist-Einstellungen ein.</p>'''
         + checks(
            '<strong>Programm stimmt um eine Stunde nicht:</strong> Zeitzone in der App auf „Europe/Berlin“ stellen oder den EPG-Versatz anpassen.',
            '<strong>EPG bleibt leer:</strong> EPG manuell aktualisieren und die Aktualisierung beim App-Start aktivieren.',
            '<strong>Nur einzelne Sender ohne Programm:</strong> Das liegt an fehlender Zuordnung beim Anbieter, nicht an Ihrem Gerät – melden Sie die Sender dem Support.',
            '<strong>Sommer- und Winterzeit:</strong> Nach der Zeitumstellung den EPG einmal neu laden.')),
        ('qualitaet', 'Die wichtigsten Einstellungen für ein ruhiges Bild', table(['Einstellung', 'Empfehlung', 'Warum'], [
            ['Decoder', 'Hardware (HW oder HW+)', 'Entlastet den Prozessor, vor allem bei 4K und HEVC'],
            ['Puffer', 'Mittel; bei Aussetzern „groß“', 'Überbrückt kurze Schwankungen der Leitung'],
            ['Bildwiederholrate (AFR)', 'An, falls verfügbar', 'Verhindert Mikroruckler bei 50-Hz-Sendern'],
            ['Verbindung', 'LAN-Kabel oder WLAN mit 5 GHz', 'Stabiler als 2,4 GHz, besonders abends'],
            ['Stream-Format', 'TS statt HLS, wenn die App die Wahl bietet', 'Schnelleres Umschalten bei Live-TV'],
        ], 'Empfohlene Einstellungen für IPTV') + '''
<p>Mit Full HD kommen Sie ab etwa 16 Mbit/s pro Gerät gut aus, für 4K sollten es mindestens 25 Mbit/s sein. Mehr zu Bandbreite und HEVC lesen Sie im Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>, mehr zu Ursachen von Aussetzern unter <a href="/iptv-server/">IPTV Server und Puffern</a>.</p>'''),
        ('fehler', 'Wenn es nicht klappt: die fünf häufigsten Fehler', table(['Problem', 'Ursache', 'Lösung'], [
            ['„Ungültige Zugangsdaten“', 'Tippfehler, Leerzeichen, http statt https', 'Daten neu kopieren, Server-URL mit Port übernehmen'],
            ['Senderliste lädt nicht', 'Falsche Login-Art oder Playlist-Format', 'Xtream statt M3U probieren oder umgekehrt'],
            ['Schwarzes Bild, aber Ton', 'Codec wird nicht unterstützt', 'Decoder auf Software umstellen oder andere App testen'],
            ['Ruckeln am Abend', 'Überlastetes WLAN oder Netz', 'LAN-Kabel, Puffer erhöhen, Router neu starten'],
            ['App verlangt Aktivierung', 'Testphase der App abgelaufen', 'App beim Entwickler aktivieren – das ist unabhängig vom IPTV-Zugang'],
        ], 'Fehlerbehebung beim Einrichten')
         + tip('Hängt es trotzdem? Unser deutschsprachiger Support hilft per E-Mail und WhatsApp Schritt für Schritt – auch schon während des kostenlosen Tests.', 'Hilfe')),
    ],
    faq=[
        ('Wie lange dauert es, IPTV einzurichten?', 'Auf Fire TV, Google TV und Smart-TVs meist 10 bis 15 Minuten: App installieren, Zugangsdaten eintragen, Programmführer laden. Bei MAC-basierten Apps kommt das Hochladen der Playlist über die Website des Entwicklers dazu.'),
        ('Was brauche ich, um IPTV einzurichten?', 'Ein internetfähiges Gerät (Smart-TV, Stick, Box, Handy oder PC), eine IPTV-App, Ihre Zugangsdaten und eine Internetleitung mit etwa 16 Mbit/s für Full HD bzw. 25 Mbit/s für 4K.'),
        ('Soll ich Xtream Codes oder M3U nutzen?', 'Wenn die App beides unterstützt, Xtream Codes. Damit lädt die App Sender, Filme, Serien und Programmführer getrennt und hält sie automatisch aktuell. M3U ist die Lösung für Apps ohne Xtream-Unterstützung.'),
        ('Warum zeigt mein Programmführer falsche Zeiten?', 'Meist ist die Zeitzone falsch eingestellt. Stellen Sie in der App „Europe/Berlin“ ein oder passen Sie den EPG-Versatz an und laden Sie den Programmführer neu.'),
        ('Kann ich IPTV auf mehreren Geräten einrichten?', 'Ja. Sie tragen dieselben Zugangsdaten auf jedem Gerät ein. Wie viele Geräte gleichzeitig schauen können, hängt von Ihrem Paket ab – bei IPTV Kanal 1 bis 5 Geräte.'),
        ('Hilft IPTV Kanal bei der Einrichtung?', 'Ja. Der deutschsprachige Support begleitet Sie per E-Mail und WhatsApp durch die Einrichtung auf Ihrem Gerät, auch während des kostenlosen Tests.'),
    ],
    related=['bester-iptv-player', 'iptv-fire-tv-stick', 'iptv-samsung-tv', 'xtream-codes-iptv', 'm3u-playlist', 'iptv-geraete'],
    card=('IPTV einrichten', 'In vier Schritten auf jedem Gerät startklar.'),
    sources=[('VideoLAN – VLC Media Player', 'https://www.videolan.org/vlc/')],
))

# ================================================================ BESTER IPTV PLAYER
PAGES.append(dict(
    slug='bester-iptv-player', parent='apps', kind='guide',
    title='Bester IPTV Player 2026: 12 Apps im Vergleich',
    description='Bester IPTV Player 2026: TiviMate, IPTV Smarters Pro, IPTVX, SET IPTV, OTT Navigator, VLC und mehr – nach Gerät, Funktionen und Kosten sortiert.',
    eyebrow='APP-VERGLEICH 2026', h1='Bester IPTV Player 2026: die besten Apps im Vergleich',
    lead='Den einen besten IPTV Player gibt es nicht – aber für jedes Gerät einen klaren Favoriten. Wir haben die gängigen Apps nach Bedienung, Programmführer, Mediathek, Aufnahme und Kostenmodell eingeordnet.',
    answer='Der beste IPTV Player hängt vom Gerät ab: Für Fire TV und Android TV ist TiviMate die erste Wahl, für Apple TV und iPhone IPTVX, für Samsung- und LG-Fernseher SET IPTV oder IBO Player, für den PC VLC bzw. IPTV Smarters Pro. Wer kostenlos starten möchte, nimmt IPTV Smarters Pro oder OTT Navigator. Ein Player liefert übrigens keine Sender – er spielt nur die Zugangsdaten Ihres IPTV-Anbieters ab.',
    sections=[
        ('top-liste', 'Die besten IPTV Player nach Gerät', table(['Gerät', 'Unsere Empfehlung', 'Alternative', 'Kostenlos starten mit'], [
            ['Fire TV Stick, Fire TV Cube', '<a href="/tivimate-fire-tv-stick/">TiviMate</a>', '<a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro</a>', 'IPTV Smarters Pro, TiviMate (Basis)'],
            ['Google TV, Android TV, Nvidia Shield', '<a href="/tivimate/">TiviMate</a>', '<a href="/ott-navigator/">OTT Navigator</a>', 'OTT Navigator'],
            ['Apple TV, iPhone, iPad', '<a href="/iptvx/">IPTVX</a>', '<a href="/iplaytv/">iPlayTV</a>', 'IPTV Smarters (iOS)'],
            ['Samsung Smart TV (Tizen)', '<a href="/set-iptv/">SET IPTV</a>', '<a href="/ibo-player/">IBO Player</a>, <a href="/smart-iptv/">Smart IPTV</a>', 'Testphase der jeweiligen App'],
            ['LG Smart TV (webOS)', '<a href="/set-iptv/">SET IPTV</a>', '<a href="/ss-iptv/">SS IPTV</a>, IBO Player', 'SS IPTV'],
            ['Windows, Mac, Linux', '<a href="/vlc-iptv/">VLC</a>', '<a href="/kodi-iptv/">Kodi</a>, IPTV Smarters Pro', 'VLC, Kodi'],
            ['Android-Smartphone', 'IPTV Smarters Pro', '<a href="/televizo/">Televizo</a>, <a href="/sparkle-tv/">Sparkle</a>', 'IPTV Smarters Pro'],
        ], 'Bester IPTV Player je Gerät') + '''
<p>Stand: November 2026. Verfügbarkeit in den App-Stores kann sich ändern – laden Sie Apps immer aus dem offiziellen Store oder von der Website des Entwicklers.</p>'''),
        ('kriterien', 'So haben wir die Player eingeordnet', checks(
            '<strong>Login-Arten:</strong> Unterstützt die App Xtream Codes, M3U oder nur MAC-Upload? Xtream ist am komfortabelsten.',
            '<strong>Programmführer:</strong> Wie übersichtlich ist das EPG-Raster, lässt sich die Zeitzone einstellen, gibt es eine Vorschau?',
            '<strong>Mediathek:</strong> Werden Filme und Serien mit Staffeln, Covern und Fortsetzen-Funktion angezeigt?',
            '<strong>Live-Funktionen:</strong> Catch-up, Aufnahme, Mehrfachansicht, Favoriten und Kindersicherung.',
            '<strong>Stabilität:</strong> Hardware-Decoder, Puffer-Einstellungen und Bildwiederholraten-Anpassung (AFR).',
            '<strong>Kostenmodell:</strong> kostenlos, Testphase mit Aktivierung pro Gerät oder Premium-Lizenz.')
         + '<p>Wir bewerten Funktionen, die in den offiziellen Beschreibungen und in der App selbst sichtbar sind. Konkrete Preise nennen wir nicht, weil Entwickler sie häufig ändern – die aktuellen Konditionen stehen jeweils im Store.</p>'),
        ('tivimate', 'TiviMate: der Komfort-Player für Fire TV und Android TV', proscons(
            ['Übersichtlichster Programmführer im Fernseher-Layout', 'Mehrere Playlists, Favoriten, Catch-up', 'Aufnahme und Mehrfachansicht mit Premium'],
            ['Nur Android TV, Google TV und Fire OS', 'Viele Komfortfunktionen nur mit Premium', 'Keine Mediathek-Optik wie bei Smarters'])
         + '<p>TiviMate ist der Player, den die meisten nach einer Woche nicht mehr wechseln. Die Basisversion ist kostenlos, <a href="/tivimate-premium/">TiviMate Premium</a> schaltet Aufnahme, mehrere Playlists und weitere Funktionen frei.</p>'),
        ('smarters', 'IPTV Smarters Pro: der Allrounder', proscons(
            ['Auf fast allen Plattformen verfügbar', 'Mediathek mit Filmen und Serien im Streaming-Stil', 'Kostenlos nutzbar'],
            ['Programmführer weniger übersichtlich als TiviMate', 'Auf dem Fire TV meist nur per Downloader', 'Teilweise Werbung bzw. Abo für Zusatzfunktionen'])
         + '<p>Wer Live-TV und eine Mediathek mit Serien in einer App möchte, ist mit <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> gut beraten. Auf dem Fire TV hilft unsere Anleitung zur <a href="/iptv-downloader/">Downloader-App</a>.</p>'),
        ('smart-tv', 'Samsung und LG: SET IPTV, IBO Player, Smart IPTV', '''
<p>Auf Tizen- und webOS-Fernsehern laufen TiviMate und IPTV Smarters Pro in der Regel nicht. Hier arbeiten MAC-basierte Apps: Die App zeigt eine Gerätekennung, Ihre Playlist tragen Sie auf der Website des Entwicklers ein. <strong>SET IPTV</strong> bietet das ausgereifteste EPG, <strong>IBO Player</strong> und seine Alternativen (<a href="/ibo-player-alternativen/">Übersicht</a>) unterstützen auch Xtream-Logins, <strong>Smart IPTV</strong> ist der Klassiker mit einfacher Oberfläche. Alle verlangen nach einer Testphase eine Aktivierung pro Fernseher.</p>
<p>Wenn Ihnen keine dieser Apps gefällt, ist ein günstiger Streaming-Stick am HDMI-Anschluss oft die bessere Lösung als jeder Smart-TV-Player – siehe <a href="/iptv-stick/">IPTV Stick im Vergleich</a>.</p>'''),
        ('apple-pc', 'Apple TV, iPhone und PC', '''
<p>Auf Apple-Geräten überzeugen <a href="/iptvx/">IPTVX</a> (modernes Design, Xtream und M3U, iCloud-Sync) und <a href="/iplaytv/">iPlayTV</a> (stark beim Programmführer). Am Windows-PC und Mac reicht für den Anfang <a href="/vlc-iptv/">VLC</a>: M3U-Link einfügen, fertig. Wer Programmführer und Mediathek möchte, greift zu IPTV Smarters Pro für Windows oder zu <a href="/kodi-iptv/">Kodi</a>. Ohne Installation geht es im <a href="/iptv-im-browser/">Browser</a>.</p>'''),
        ('fire-tv-kostenlos', 'Bester IPTV Player für den Fire TV Stick – kostenlos und auf Deutsch', '''
<p>Eine der häufigsten Suchanfragen lautet „bester IPTV Player für Fire TV Stick kostenlos deutsch“. Unsere Antwort: <strong>TiviMate</strong> in der kostenlosen Basisversion oder <strong>IPTV Smarters Pro</strong>. Beide haben eine deutsche Oberfläche und laufen auf allen Fire-TV-Geräten mit Fire OS. TiviMate gibt es im Amazon Appstore; Smarters laden Sie über die App Downloader von der offiziellen Website. Wichtig: Fire-TV-Geräte mit Vega OS (etwa der Fire TV Stick 4K Select) unterstützen keine Android-Apps außerhalb des Appstores – Details in der Übersicht <a href="/fire-tv-modelle/">Fire-TV-Modelle</a>.</p>'''
         + tip('Testen Sie zwei Player parallel mit demselben Zugang. Nach ein paar Abenden wissen Sie, welche Bedienung Ihnen liegt – die Zugangsdaten funktionieren in jeder App.')),
    ],
    faq=[
        ('Welcher IPTV Player ist der beste?', 'Für Fire TV und Android TV TiviMate, für Apple-Geräte IPTVX, für Samsung und LG SET IPTV oder IBO Player, für den PC VLC. Einen Player für alle Geräte gibt es nicht; IPTV Smarters Pro kommt dem am nächsten.'),
        ('Welcher IPTV Player ist kostenlos?', 'IPTV Smarters Pro, OTT Navigator, VLC, Kodi und SS IPTV sind kostenlos nutzbar. TiviMate hat eine kostenlose Basisversion. MAC-basierte Smart-TV-Apps wie SET IPTV oder IBO Player verlangen nach der Testphase eine Aktivierung.'),
        ('Was ist der beste IPTV Player für den Fire TV Stick?', 'TiviMate – wegen des übersichtlichen Programmführers und der stabilen Wiedergabe. Wer eine Mediathek mit Serien bevorzugt, nimmt IPTV Smarters Pro.'),
        ('Welcher IPTV Player ist der beste für Android?', 'Auf Android-TV-Geräten TiviMate oder OTT Navigator, auf Android-Smartphones IPTV Smarters Pro oder Televizo.'),
        ('Enthält ein IPTV Player Sender?', 'Nein. Ein IPTV Player spielt nur ab. Die Sender kommen von Ihrem IPTV-Anbieter, dessen Zugangsdaten Sie in die App eintragen.'),
        ('Kann ich den Player später wechseln?', 'Ja. Ihre Zugangsdaten funktionieren in jeder kompatiblen App. Sie können mehrere Player parallel installieren und testen.'),
    ],
    related=['tivimate', 'iptv-smarters-pro', 'set-iptv', 'iptvx', 'iptv-apps', 'iptv-einrichten'],
    card=('Bester IPTV Player', 'Die besten IPTV-Apps 2026 nach Gerät verglichen.'),
))

# ================================================================ TIVIMATE FIRE TV STICK
PAGES.append(dict(
    slug='tivimate-fire-tv-stick', parent='apps', kind='guide',
    title='TiviMate auf dem Fire TV Stick installieren (2026)',
    description='TiviMate auf dem Fire TV Stick: aus dem Appstore oder per Downloader installieren, Playlist eintragen, Premium aktivieren und Ruckler beheben.',
    eyebrow='SCHRITT-FÜR-SCHRITT', h1='TiviMate auf dem Fire TV Stick installieren und einrichten',
    lead='TiviMate und der Fire TV Stick sind die beliebteste IPTV-Kombination in Deutschland. Hier lesen Sie, wie Sie die App installieren, Ihre Playlist eintragen und den Stick so einstellen, dass Live-Sport ruckelfrei läuft.',
    answer='TiviMate auf dem Fire TV Stick installieren: Suchen Sie auf dem Fire TV nach „TiviMate“ und installieren Sie die App aus dem Amazon Appstore. Ist sie dort nicht verfügbar, laden Sie sie über die App Downloader von der offiziellen TiviMate-Website. Danach „Playlist hinzufügen“ wählen, Xtream-Codes-Login oder M3U-Link eintragen und den Programmführer laden. Premium aktivieren Sie über die TiviMate-Companion-App auf dem Handy.',
    sections=[
        ('voraussetzungen', 'Voraussetzungen: welcher Fire TV Stick?', table(['Gerät', 'TiviMate möglich?', 'Hinweis'], [
            ['Fire TV Stick 4K Max (2. Generation)', 'Ja', 'Schnellster Stick, Wi-Fi 6E – ideal für 4K'],
            ['Fire TV Stick 4K (2. Generation)', 'Ja', 'Gute Wahl für 4K-Fernseher'],
            ['Fire TV Stick HD / Lite', 'Ja', 'Für Full-HD-Fernseher, etwas langsamer beim EPG'],
            ['Fire TV Cube', 'Ja', 'LAN-Anschluss eingebaut'],
            ['Fire TV Stick 4K Select und andere Vega-OS-Geräte', 'Nein', 'Keine Android-Apps außerhalb des Appstores'],
        ], 'TiviMate auf Fire-TV-Modellen') + '''
<p>Ihr Betriebssystem sehen Sie unter <b>Einstellungen → Mein Fire TV → Info</b>. Alle Modelle im Detail zeigt die Übersicht <a href="/fire-tv-modelle/">Fire-TV-Modelle</a>.</p>'''),
        ('installieren', 'Schritt 1: TiviMate installieren', '<h3>Variante A: aus dem Amazon Appstore</h3>' + steps(
            'Auf der Fire-TV-Startseite die Suche (Lupe) öffnen.',
            '„TiviMate“ eingeben und <b>TiviMate IPTV Player</b> auswählen.',
            '„Herunterladen“ bzw. „Abrufen“ drücken und die Installation abwarten.')
         + '<h3>Variante B: über Downloader</h3>' + steps(
            'Die App <b>Downloader</b> aus dem Appstore installieren.',
            'In den Entwickleroptionen „Apps unbekannter Herkunft“ für Downloader erlauben (Anleitung: <a href="/iptv-downloader/">Downloader auf Fire TV</a>).',
            'In Downloader die Download-Adresse von der <b>offiziellen TiviMate-Website</b> eingeben, die APK laden und installieren.',
            'Die APK-Datei anschließend in Downloader löschen.')
         + tip('Laden Sie TiviMate nie als „bereits freigeschaltete“ Version aus Foren oder Telegram-Gruppen. Solche Dateien sind häufig manipuliert, und Premium funktioniert damit ohnehin nicht dauerhaft.', 'Sicherheit')),
        ('playlist', 'Schritt 2: Playlist hinzufügen', steps(
            'TiviMate öffnen und „Playlist hinzufügen“ wählen.',
            '<b>„Xtream Codes“</b> antippen (empfohlen) – alternativ „M3U-Playlist“.',
            'Server-Adresse inklusive Port, Benutzername und Passwort eintragen und „Weiter“ drücken.',
            'TiviMate zählt Sender, Filme und Serien. Einen Namen für die Playlist vergeben und „Fertig“ wählen.',
            'Unter <b>Einstellungen → EPG</b> die Aktualisierung beim Start einschalten und einmal manuell aktualisieren.') + LOGIN_TIP),
        ('premium', 'Schritt 3: TiviMate Premium aktivieren (optional)', '''
<p>Die Basisversion reicht zum Fernsehen. Premium schaltet unter anderem Aufnahme, mehrere Playlists, Favoriten-Verwaltung, Catch-up und Bild-in-Bild frei. Gekauft wird Premium in der <strong>TiviMate-Companion-App</strong> auf einem Android-Handy. Mit demselben Konto melden Sie sich danach in TiviMate auf dem Stick an (<b>Einstellungen → Premium → Konto</b>). Eine Lizenz gilt für mehrere Geräte. Was Premium kostet und welche Varianten es gibt, steht im Ratgeber <a href="/tivimate-premium/">TiviMate Premium</a>.</p>'''),
        ('einstellungen', 'Die besten TiviMate-Einstellungen für den Fire TV Stick', table(['Einstellung', 'Wo', 'Empfehlung'], [
            ['Decoder', 'Einstellungen → Wiedergabe', 'Hardware; bei Bildfehlern einzelner Sender „Software“ testen'],
            ['Bildwiederholrate', 'Einstellungen → Wiedergabe → AFR', 'Einschalten – wichtig für 50-Hz-Fußball'],
            ['Puffergröße', 'Einstellungen → Wiedergabe', 'Mittel, bei Aussetzern groß'],
            ['Sendergruppen', 'Einstellungen → Playlists → Gruppen verwalten', 'Ungenutzte Länder ausblenden – EPG lädt schneller'],
            ['Start mit letztem Sender', 'Einstellungen → Allgemein', 'Einschalten – TiviMate startet wie ein Fernseher'],
        ], 'Empfohlene TiviMate-Einstellungen') + '''
<p>Der Fire TV Stick hat wenig Speicher. Löschen Sie gelegentlich den Cache unter <b>Einstellungen → Anwendungen → Installierte Anwendungen verwalten → TiviMate</b>. Für dauerhaft stabile Wiedergabe lohnt ein USB-LAN-Adapter – mehr Tipps im Ratgeber <a href="/iptv-fire-tv-stick/">IPTV auf dem Fire TV Stick</a>.</p>'''),
        ('probleme', 'Häufige Probleme mit TiviMate auf dem Fire TV', table(['Problem', 'Lösung'], [
            ['TiviMate nicht im Appstore', 'Über Downloader von der offiziellen Website installieren'],
            ['„Keine Playlist gefunden“', 'Server-URL mit „http://“ und Port prüfen, auf Leerzeichen achten'],
            ['Programmführer leer', 'EPG manuell aktualisieren, Zeitzone prüfen'],
            ['Ruckeln bei Fußball', 'AFR einschalten, LAN-Adapter nutzen, Puffer erhöhen'],
            ['Premium wird nicht erkannt', 'In TiviMate mit demselben Konto wie in der Companion-App anmelden'],
        ], 'TiviMate-Fehler auf Fire TV')),
    ],
    faq=[
        ('Gibt es TiviMate im Amazon Appstore?', 'TiviMate ist im Amazon Appstore für Fire-TV-Geräte gelistet. Sollte die App in Ihrem Land oder auf Ihrem Gerät fehlen, installieren Sie sie über die App Downloader von der offiziellen TiviMate-Website.'),
        ('Ist TiviMate auf dem Fire TV Stick kostenlos?', 'Die Basisversion ist kostenlos. Aufnahme, mehrere Playlists und weitere Komfortfunktionen gibt es mit TiviMate Premium, das in der Companion-App gekauft wird.'),
        ('Funktioniert TiviMate auf dem Fire TV Stick 4K Select?', 'Nein. Der Fire TV Stick 4K Select nutzt Vega OS. Darauf laufen keine Android-Apps außerhalb des Amazon Appstores.'),
        ('Wie aktiviere ich TiviMate Premium auf dem Fire TV?', 'Kaufen Sie Premium in der TiviMate-Companion-App auf einem Android-Handy und melden Sie sich in TiviMate unter Einstellungen → Premium mit demselben Konto an.'),
        ('Warum ruckelt TiviMate auf meinem Fire TV Stick?', 'Häufige Ursachen sind überlastetes WLAN, ein zu kleiner Puffer oder eine nicht angepasste Bildwiederholrate. Schalten Sie AFR ein, erhöhen Sie den Puffer und nutzen Sie möglichst einen LAN-Adapter.'),
    ],
    related=['tivimate', 'tivimate-premium', 'iptv-fire-tv-stick', 'iptv-downloader', 'iptv-smarters-pro-firestick', 'fire-tv-modelle'],
    card=('TiviMate auf Fire TV', 'TiviMate auf dem Fire TV Stick installieren und einstellen.'),
))

# ================================================================ CHROMECAST
PAGES.append(dict(
    slug='iptv-chromecast', parent='geraete', kind='guide',
    title='IPTV auf Chromecast: Casting & Google TV Streamer',
    description='IPTV auf Chromecast schauen: vom Handy casten mit IPTV Smarters, VLC oder GSE – oder TiviMate direkt auf Chromecast mit Google TV und Google TV Streamer nutzen.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf Chromecast: casten oder direkt installieren',
    lead='Chromecast ist nicht gleich Chromecast. Ob Sie IPTV vom Handy auf den Fernseher schicken müssen oder eine App direkt auf dem Gerät nutzen können, hängt vom Modell ab.',
    answer='IPTV auf Chromecast funktioniert auf zwei Wegen: Beim Chromecast mit Google TV und dem Google TV Streamer installieren Sie eine IPTV-App wie TiviMate direkt aus dem Play Store – das ist die stabilste Lösung. Ältere Chromecasts ohne Fernbedienung empfangen nur Streams, die Sie vom Handy aus senden („casten“), etwa mit IPTV Smarters Pro, VLC oder GSE Smart IPTV. TiviMate selbst kann nicht casten.',
    sections=[
        ('modelle', 'Welcher Chromecast kann was?', table(['Gerät', 'Eigene Apps?', 'IPTV-Weg'], [
            ['Chromecast (1.–3. Generation), Chromecast Ultra', 'Nein', 'Nur Casting vom Handy, Tablet oder Chrome-Browser'],
            ['Chromecast mit Google TV (HD und 4K)', 'Ja (Google TV)', 'IPTV-App direkt installieren – Casting zusätzlich möglich'],
            ['Google TV Streamer (seit 2024)', 'Ja (Google TV)', 'IPTV-App direkt installieren, LAN-Anschluss eingebaut'],
            ['Fernseher mit „Chromecast built-in“', 'Je nach System', 'Google-TV-Fernseher: App installieren; sonst Casting'],
        ], 'Chromecast-Modelle und IPTV') + '''
<p>Google verkauft seit 2024 keine klassischen Chromecasts mehr; bestehende Geräte erhalten aber weiter Sicherheitsupdates. Der Nachfolger ist der Google TV Streamer. Eine Einordnung aller Sticks finden Sie unter <a href="/iptv-stick/">IPTV Stick im Vergleich</a>, die Einrichtung auf Google TV unter <a href="/iptv-google-tv/">IPTV auf Google TV</a>.</p>'''),
        ('casting-apps', 'Diese IPTV-Apps können casten', table(['App', 'Plattform', 'Chromecast-Unterstützung'], [
            ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'Android, iPhone', 'Cast-Symbol im Player (Live-TV, Filme, Serien)'],
            ['<a href="/vlc-iptv/">VLC</a>', 'Android, iPhone', '„Wiedergabe auf Gerät“ – spielt M3U-Sender auf dem Chromecast'],
            ['<a href="/gse-smart-iptv/">GSE Smart IPTV</a>', 'Android, iPhone', 'Cast-Funktion eingebaut'],
            ['<a href="/tivimate/">TiviMate</a>', 'Android TV', 'Kein Casting – läuft nur direkt auf Google-TV-Geräten'],
            ['Chrome-Browser', 'PC, Mac', 'Tab casten – funktioniert, aber mit geringerer Qualität'],
        ], 'IPTV-Apps mit Chromecast-Funktion') + '''
<p>Welche App Ihnen liegt, hängt von der Bedienung ab. Einen Überblick über alle Player gibt unser Vergleich <a href="/bester-iptv-player/">Bester IPTV Player</a>.</p>'''),
        ('casten', 'So casten Sie IPTV vom Handy', steps(
            'Handy und Chromecast mit <b>demselben WLAN</b> verbinden (am besten 5 GHz).',
            'IPTV Smarters Pro oder VLC öffnen und mit Ihren Zugangsdaten anmelden.',
            'Einen Sender starten und auf das <b>Cast-Symbol</b> (Rechteck mit Funkwellen) tippen.',
            'Ihren Chromecast auswählen. Der Stream läuft jetzt auf dem Fernseher; das Handy dient als Fernbedienung.',
            'Zum Umschalten den nächsten Sender auf dem Handy wählen – der Chromecast übernimmt automatisch.')
         + tip('Beim Casting holt der Chromecast den Stream selbst aus dem Internet. Das Handy kann also in den Ruhezustand gehen. Bricht die Wiedergabe trotzdem ab, deaktivieren Sie den Energiesparmodus für die App.')),
        ('direkt', 'Besser: IPTV-App direkt auf Google TV', '''
<p>Beim Chromecast mit Google TV und beim Google TV Streamer lohnt sich Casting nicht – installieren Sie die App direkt. Öffnen Sie den Play Store auf dem Gerät, suchen Sie nach <strong>TiviMate</strong>, <strong>IPTV Smarters Pro</strong> oder <strong>OTT Navigator</strong> und tragen Sie Ihre Zugangsdaten ein. Vorteile: Fernbedienung statt Handy, schnelleres Umschalten, Programmführer auf dem Fernseher und keine Abbrüche, wenn das Handy klingelt. Die Schritt-für-Schritt-Anleitung finden Sie unter <a href="/tivimate/">TiviMate einrichten</a>.</p>'''),
        ('probleme', 'Typische Chromecast-Probleme', table(['Problem', 'Ursache', 'Lösung'], [
            ['Cast-Symbol fehlt', 'Handy in anderem WLAN oder Gastnetz', 'Beide Geräte ins selbe Netz, kein Gast-WLAN'],
            ['Stream startet nicht', 'Format wird vom Chromecast nicht unterstützt', 'In der App HLS (m3u8) statt TS wählen oder VLC nutzen'],
            ['Ton, aber kein Bild', 'Codec wie HEVC auf altem Chromecast', 'Chromecast Ultra oder Google TV Streamer nutzen'],
            ['Ruckeln', 'Schwaches 2,4-GHz-WLAN', '5-GHz-WLAN oder Google TV Streamer mit LAN'],
        ], 'Chromecast-Fehlerbehebung')),
    ],
    faq=[
        ('Kann ich IPTV auf Chromecast schauen?', 'Ja. Auf Chromecast mit Google TV und dem Google TV Streamer installieren Sie eine IPTV-App direkt. Ältere Chromecasts empfangen IPTV per Casting vom Handy, etwa mit IPTV Smarters Pro oder VLC.'),
        ('Kann TiviMate auf Chromecast casten?', 'Nein. TiviMate hat keine Casting-Funktion. Es läuft aber direkt auf Chromecast mit Google TV und dem Google TV Streamer.'),
        ('Welche IPTV-App unterstützt Chromecast?', 'IPTV Smarters Pro, VLC und GSE Smart IPTV können auf den Chromecast casten. Für Google-TV-Geräte sind TiviMate und OTT Navigator die bessere Wahl, weil sie direkt auf dem Gerät laufen.'),
        ('Warum ruckelt IPTV auf meinem Chromecast?', 'Meist wegen eines schwachen WLANs. Nutzen Sie 5 GHz, stellen Sie den Router näher an den Fernseher oder wechseln Sie zum Google TV Streamer mit LAN-Anschluss.'),
        ('Gibt es den Chromecast noch?', 'Google verkauft seit 2024 keine klassischen Chromecasts mehr. Nachfolger ist der Google TV Streamer. Vorhandene Chromecasts funktionieren weiter.'),
    ],
    related=['iptv-google-tv', 'iptv-stick', 'iptv-smarters-pro', 'vlc-iptv', 'tivimate', 'iptv-geraete'],
    card=('IPTV auf Chromecast', 'Casten vom Handy oder App direkt auf Google TV.'),
    sources=[('Google Chromecast-Hilfe', 'https://support.google.com/chromecast/')],
))

# ================================================================ IPTV IM BROWSER
PAGES.append(dict(
    slug='iptv-im-browser', parent='apps', kind='guide',
    title='IPTV im Browser schauen: Web Player für PC & Laptop',
    description='IPTV im Browser schauen ohne Installation: wie Web Player mit M3U und Xtream funktionieren, wo ihre Grenzen liegen und wann VLC besser ist.',
    eyebrow='WEB PLAYER', h1='IPTV im Browser: Fernsehen ohne App am PC und Laptop',
    lead='Am Arbeitsplatz, auf dem Firmenlaptop oder auf dem Chromebook dürfen Sie oft nichts installieren. Dann bleibt der Browser. Wir zeigen, was IPTV im Browser kann, wo die Grenzen liegen und wie Sie Ihre Zugangsdaten schützen.',
    answer='IPTV im Browser funktioniert mit sogenannten Web Playern: Sie öffnen eine Website, tragen Ihren M3U-Link oder Xtream-Codes-Login ein und schauen direkt in Chrome, Edge, Firefox oder Safari. Weil Browser nicht jedes Streamformat abspielen, laufen manche Sender nur, wenn der Anbieter HLS (m3u8) liefert. Für den Alltag sind VLC oder IPTV Smarters Pro am PC stabiler – und Ihre Zugangsdaten bleiben auf Ihrem Gerät.',
    sections=[
        ('so-gehts', 'So funktioniert IPTV im Browser', '''
<p>Ein Web Player ist eine Website, die IPTV-Streams mit den Bordmitteln des Browsers abspielt. Sie geben dort Ihre Zugangsdaten ein, der Player lädt die Senderliste und startet den Stream im Browserfenster. Technisch kann ein Browser ohne Zusatzsoftware vor allem <strong>HLS-Streams</strong> (Endung <code>.m3u8</code>) wiedergeben. Klassische <strong>MPEG-TS-Streams</strong> (<code>.ts</code>) müssen erst umgewandelt werden – manche Web Player tun das per JavaScript, andere über einen eigenen Server.</p>'''
         + steps(
            'Web Player öffnen und „Playlist hinzufügen“ bzw. „Login“ wählen.',
            'Xtream-Codes-Login (Server, Benutzername, Passwort) oder M3U-Link eintragen.',
            'Bei M3U-Listen in der Adresse <code>output=ts</code> durch <code>output=m3u8</code> ersetzen, falls Ihr Anbieter beides liefert.',
            'Sender auswählen – bei Problemen einen anderen Browser testen (Chrome und Edge sind am kompatibelsten).')),
        ('vergleich', 'Browser, VLC oder App: was ist am PC besser?', table(['Weg', 'Installation', 'Formate', 'Programmführer', 'Datenschutz'], [
            ['Web Player im Browser', 'Keine', 'Vor allem HLS', 'Je nach Player', 'Zugangsdaten gehen an die Website'],
            ['<a href="/vlc-iptv/">VLC</a>', 'Ja', 'Nahezu alle', 'Nein', 'Bleibt lokal'],
            ['IPTV Smarters Pro (Windows/Mac)', 'Ja', 'Nahezu alle', 'Ja', 'Bleibt lokal'],
            ['<a href="/kodi-iptv/">Kodi</a>', 'Ja', 'Nahezu alle', 'Ja', 'Bleibt lokal'],
        ], 'IPTV am PC im Vergleich') + '''
<p>Für einen schnellen Blick ist der Browser praktisch. Wer regelmäßig am Computer schaut, ist mit einer installierten App besser bedient – siehe <a href="/iptv-pc-mac/">IPTV auf PC und Mac</a>.</p>'''),
        ('sicherheit', 'Zugangsdaten schützen: worauf Sie achten sollten', checks(
            '<strong>Nur bekannte Web Player nutzen.</strong> Ein Web Player, der über einen eigenen Server streamt, sieht Ihre Zugangsdaten und Ihren Datenverkehr.',
            '<strong>Keine Zugangsdaten in öffentlichen Rechnern speichern.</strong> Nach der Nutzung abmelden und den Browserverlauf löschen.',
            '<strong>Keine Erweiterungen aus unbekannten Quellen.</strong> „IPTV-Erweiterungen“ für Chrome verlangen oft Zugriff auf alle Websites.',
            '<strong>Smarters Web und Anbieter-Portale:</strong> Manche IPTV-Anbieter stellen einen eigenen Web Player bereit – das ist die sicherste Browser-Variante, weil die Daten beim Anbieter bleiben.')
         + tip('Ihren IPTV-Kanal-Zugang können Sie jederzeit auch in VLC testen: M3U-Link einfügen, Sender starten. So prüfen Sie ohne fremde Website, ob alles läuft.')),
        ('grenzen', 'Grenzen von IPTV im Browser', '''
<p>Browser sind für Live-TV nicht gebaut. Typische Grenzen: kein oder nur einfacher Programmführer, langsames Umschalten, kein Hardware-Decoding für jeden Codec und kein Vollbild auf dem Fernseher, ohne den Laptop per HDMI anzuschließen. HEVC-Streams (H.265), die bei <a href="/iptv-4k/">4K</a> üblich sind, spielen viele Browser gar nicht ab. Auch Firmennetzwerke blockieren Streaming-Ports oft – dann helfen weder Browser noch App.</p>
<p>Am Fernseher ist ein Stick wie der <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder ein <a href="/iptv-chromecast/">Chromecast mit Google TV</a> die deutlich bessere Lösung. Und wer vom Laptop auf den Fernseher möchte, kann den Browser-Tab auf einen Chromecast streamen.</p>'''),
        ('chromebook', 'Sonderfall Chromebook', '''
<p>Auf Chromebooks laufen Android-Apps aus dem Play Store. Statt eines Web Players installieren Sie dort einfach <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder VLC für Android – das ist stabiler und unterstützt mehr Formate. Nur auf verwalteten Schul- und Firmen-Chromebooks ohne Play Store bleibt der Browser die einzige Option.</p>'''),
    ],
    faq=[
        ('Kann ich IPTV im Browser schauen?', 'Ja, mit einem Web Player. Sie tragen dort Ihren M3U-Link oder Xtream-Login ein und schauen direkt im Browser. Am zuverlässigsten funktionieren HLS-Streams (m3u8).'),
        ('Warum spielt mein Browser manche Sender nicht ab?', 'Browser unterstützen ohne Zusatzsoftware vor allem HLS. MPEG-TS-Streams oder HEVC-Codecs laufen oft nicht. Stellen Sie im M3U-Link auf m3u8 um oder nutzen Sie VLC.'),
        ('Ist IPTV im Browser sicher?', 'Das hängt vom Web Player ab. Fremde Websites sehen Ihre Zugangsdaten. Nutzen Sie bevorzugt den Web Player Ihres Anbieters oder eine lokal installierte App wie VLC.'),
        ('Gibt es IPTV Smarters als Web-Version?', 'Es gibt Web-Player-Varianten auf Smarters-Basis, die IPTV-Anbieter für ihre Kunden bereitstellen. Eine allgemeine Web-App für beliebige Zugänge sollten Sie nur nutzen, wenn Sie dem Betreiber vertrauen.'),
        ('Was ist besser: Browser oder VLC?', 'VLC. Es spielt nahezu alle Formate, ist kostenlos und Ihre Zugangsdaten bleiben auf Ihrem Gerät. Der Browser ist nur sinnvoll, wenn Sie nichts installieren dürfen.'),
    ],
    related=['iptv-pc-mac', 'vlc-iptv', 'm3u-playlist', 'iptv-smarters-pro', 'iptv-chromecast', 'bester-iptv-player'],
    card=('IPTV im Browser', 'Web Player ohne Installation – und ihre Grenzen.'),
))

# ================================================================ DOWNLOADER
PAGES.append(dict(
    slug='iptv-downloader', parent='apps', kind='guide',
    title='Downloader App auf Fire TV: IPTV-Apps sicher laden',
    description='Downloader App auf dem Fire TV Stick: installieren, Entwickleroptionen freischalten und IPTV-Apps sicher von der offiziellen Website laden.',
    eyebrow='FIRE TV &amp; ANDROID TV', h1='Downloader App: IPTV-Apps sicher auf den Fire TV Stick laden',
    lead='Viele IPTV-Apps stehen nicht im Amazon Appstore. Mit der kostenlosen App Downloader laden Sie sie trotzdem auf den Fire TV Stick – vorausgesetzt, Sie wissen, welche Quellen sicher sind.',
    answer='Downloader ist eine kostenlose App im Amazon Appstore, mit der Sie Dateien und Android-Apps (APK) aus dem Internet auf Fire TV und Android TV laden. So geht es: Downloader installieren, in den Entwickleroptionen „Apps unbekannter Herkunft“ für Downloader erlauben, die Download-Adresse von der offiziellen Website des App-Entwicklers eintippen und installieren. Kurzcodes aus Videos und Foren sollten Sie meiden – sie können auf manipulierte Apps verweisen.',
    sections=[
        ('was-ist', 'Was ist die Downloader App?', '''
<p><strong>Downloader</strong> stammt vom Betreiber der Fire-TV-Fachseite AFTVnews und ist seit Jahren das Standardwerkzeug, um Apps außerhalb des Appstores auf Fire-TV-Geräte zu bringen. Die App kombiniert einen einfachen Browser mit einem Dateimanager: Sie geben eine Adresse ein, Downloader lädt die Datei und startet bei APK-Dateien die Installation. Zusätzlich gibt es <strong>Downloader-Codes</strong> – Zahlenkürzel, die auf eine längere Adresse verweisen.</p>
<p>Downloader selbst ist unbedenklich. Entscheidend ist, <em>was</em> Sie damit laden.</p>'''),
        ('installieren', 'Downloader installieren und freischalten', steps(
            'Auf dem Fire TV die Suche öffnen, „Downloader“ eingeben und die App mit dem orangefarbenen Symbol installieren.',
            '<b>Einstellungen → Mein Fire TV → Info</b> öffnen und siebenmal auf den Gerätenamen klicken, bis „Sie sind jetzt Entwickler“ erscheint.',
            'Zurück zu <b>Mein Fire TV → Entwickleroptionen</b>.',
            '<b>Apps unbekannter Herkunft installieren</b> öffnen und Downloader auf „Ein“ stellen.',
            'Downloader starten und den Zugriff auf Dateien erlauben.')
         + '<p>Auf Google-TV- und Android-TV-Geräten heißt die Option „Unbekannte Apps installieren“ und liegt unter <b>Einstellungen → Apps → Sicherheit &amp; Einschränkungen</b>. Downloader gibt es dort im Play Store.</p>'),
        ('iptv-apps', 'IPTV-Apps mit Downloader installieren', table(['App', 'Im Amazon Appstore?', 'Anleitung'], [
            ['IPTV Smarters Pro', 'Meist nicht', '<a href="/iptv-smarters-pro-firestick/">Smarters auf Fire TV</a>'],
            ['TiviMate', 'Ja, sonst per Downloader', '<a href="/tivimate-fire-tv-stick/">TiviMate auf Fire TV</a>'],
            ['XCIPTV', 'Nein', '<a href="/xciptv/">XCIPTV</a>'],
            ['OTT Navigator', 'Nein', '<a href="/ott-navigator/">OTT Navigator</a>'],
            ['VLC, Kodi', 'Ja', '<a href="/vlc-iptv/">VLC</a> · <a href="/kodi-iptv/">Kodi</a>'],
        ], 'IPTV-Apps auf Fire TV') + steps(
            'Downloader öffnen und in das Feld „Enter a URL“ die Download-Adresse von der <b>offiziellen Website</b> des Entwicklers eingeben.',
            '„Go“ drücken, Download abwarten und „Installieren“ wählen.',
            'Nach „Fertig“ die APK-Datei in Downloader löschen, um Speicher freizugeben.',
            'Die App unter <b>Einstellungen → Anwendungen</b> auf die Startseite legen.')),
        ('sicherheit', 'Downloader-Codes und Sicherheit', '''
<p>In Videos und Foren kursieren Downloader-Codes, die angeblich „die beste IPTV-App“ oder eine „freigeschaltete Premium-Version“ installieren. Dahinter stecken oft veränderte Apps mit fest eingebauten, nicht lizenzierten Senderlisten, Werbung oder Schadcode, der Zugangsdaten abgreift. Mit Ihrer Fire-TV-Anmeldung ist auch Ihr Amazon-Konto auf dem Gerät hinterlegt.</p>'''
         + checks(
            'Nur Adressen von der offiziellen Website des App-Entwicklers verwenden – auf dem Handy aufrufen und abgleichen.',
            'Keine Apps installieren, die Sender „kostenlos“ mitbringen. Seriöse IPTV-Player enthalten nie eigene Sender.',
            'Nach der Installation „Apps unbekannter Herkunft“ wieder ausschalten, wenn Sie nichts mehr laden.',
            'Bei verdächtigem Verhalten (Pop-ups, Fremd-Apps) die App löschen und das Gerät zurücksetzen.')
         + tip('Mehr zu riskanten Apps lesen Sie im Ratgeber <a href="/cloudstream/">CloudStream</a>. Was einen seriösen IPTV-Anbieter ausmacht, zeigt der <a href="/iptv-anbieter-vergleich/">Anbieter-Vergleich</a>.', 'Hinweis')),
        ('vega', 'Downloader auf Fire TV mit Vega OS', '''
<p>Amazon stellt neue Geräte schrittweise auf <strong>Vega OS</strong> um, zuerst den Fire TV Stick 4K Select. Vega OS basiert nicht mehr auf Android, deshalb lassen sich dort keine APK-Dateien installieren – auch nicht mit Downloader. Auf diesen Geräten sind Sie auf Apps aus dem Amazon Appstore beschränkt. Welche Modelle betroffen sind, zeigt die Übersicht <a href="/fire-tv-modelle/">Fire-TV-Modelle</a>.</p>'''),
    ],
    faq=[
        ('Ist die Downloader App legal und sicher?', 'Ja. Downloader ist eine kostenlose App aus dem Amazon Appstore. Sicher bleibt sie, solange Sie nur Apps von den offiziellen Websites der Entwickler laden.'),
        ('Warum kann ich mit Downloader nichts installieren?', 'Meist ist „Apps unbekannter Herkunft“ für Downloader nicht erlaubt. Schalten Sie es unter Einstellungen → Mein Fire TV → Entwickleroptionen ein. Auf Geräten mit Vega OS ist die Installation von APK-Dateien grundsätzlich nicht möglich.'),
        ('Wo finde ich die Entwickleroptionen auf dem Fire TV?', 'Unter Einstellungen → Mein Fire TV → Info siebenmal auf den Gerätenamen klicken. Danach erscheinen die Entwickleroptionen im Menü „Mein Fire TV“.'),
        ('Sind Downloader-Codes gefährlich?', 'Der Code selbst nicht, aber er kann auf jede beliebige Datei verweisen. Codes aus Videos und Foren führen häufig zu veränderten Apps. Nutzen Sie lieber die vollständige Adresse von der offiziellen Website.'),
        ('Welche IPTV-Apps brauchen Downloader?', 'Auf Fire TV vor allem IPTV Smarters Pro, XCIPTV und OTT Navigator. TiviMate, VLC und Kodi gibt es im Amazon Appstore.'),
    ],
    related=['iptv-fire-tv-stick', 'iptv-smarters-pro-firestick', 'tivimate-fire-tv-stick', 'fire-tv-modelle', 'cloudstream', 'iptv-apps'],
    card=('Downloader App', 'IPTV-Apps sicher auf Fire TV und Android TV laden.'),
    sources=[('AFTVnews (Entwickler der Downloader-App)', 'https://www.aftvnews.com/')],
))

# ================================================================ PLEX & JELLYFIN
PAGES.append(dict(
    slug='plex-jellyfin-iptv', parent='apps', kind='guide',
    title='IPTV in Plex & Jellyfin: Live-TV mit M3U und EPG',
    description='IPTV in Plex und Jellyfin einrichten: M3U-Tuner und XMLTV-EPG in Jellyfin, Threadfin für Plex Live-TV & DVR – mit Aufnahmen und Vergleich.',
    eyebrow='MEDIASERVER', h1='IPTV in Plex und Jellyfin einrichten',
    lead='Sie haben bereits einen Mediaserver für Filme und Serien? Dann können Sie dort auch Live-TV einbinden – mit Programmführer, Aufnahmen und Zugriff von jedem Gerät im Haushalt.',
    answer='Jellyfin unterstützt IPTV direkt: Im Dashboard unter „Live-TV“ fügen Sie Ihren M3U-Link als Tuner und eine XMLTV-Adresse als Programmführer hinzu – fertig. Plex erwartet dagegen einen echten TV-Tuner; ein Vermittler wie Threadfin stellt die M3U-Liste als virtuellen Tuner bereit. Live-TV & DVR in Plex setzt zudem einen Plex Pass voraus. Für reines Fernsehen ohne Server ist TiviMate einfacher.',
    sections=[
        ('wann', 'Für wen lohnt sich IPTV im Mediaserver?', proscons(
            ['Live-TV, Filme und Aufnahmen in einer Oberfläche', 'Aufnahmen landen zentral auf der Festplatte des Servers', 'Zugriff von Fernseher, Handy, Tablet und Browser', 'Ein Zugang, viele Geräte im Haushalt'],
            ['Ein dauerhaft laufender Server (PC, NAS, Mini-PC) nötig', 'Einrichtung aufwendiger als eine App', 'Server zählt beim Anbieter als ein Gerät, Transcoding braucht Leistung', 'Umschalten etwas langsamer als in TiviMate'],
            'Vorteile', 'Zu beachten')
         + '<p>Wenn Sie nur fernsehen möchten, ist ein Player wie <a href="/tivimate/">TiviMate</a> schneller eingerichtet. Ein Mediaserver lohnt sich vor allem, wenn Sie <a href="/iptv-aufnehmen/">Sendungen aufnehmen</a> und auf mehreren Geräten abspielen möchten.</p>'),
        ('jellyfin', 'IPTV in Jellyfin einrichten', steps(
            'Jellyfin-Dashboard öffnen und <b>Live-TV</b> wählen.',
            'Unter „Tuner-Geräte“ auf <b>+</b> klicken und als Typ <b>M3U-Tuner</b> wählen.',
            'Ihren M3U-Link einfügen. Bei „Gleichzeitige Streams begrenzen“ die Zahl Ihrer erlaubten Verbindungen eintragen.',
            'Unter „TV-Programm-Datenanbieter“ <b>XMLTV</b> wählen und die EPG-Adresse Ihres Anbieters eintragen.',
            'Sender zuordnen lassen und <b>„Programmdaten aktualisieren“</b> starten.',
            'In jeder Jellyfin-App erscheint jetzt der Bereich „Live-TV“ mit Programmführer und Aufnahmefunktion.')
         + '<p>Jellyfin ist kostenlos und quelloffen. Aufnahmen speichert der Server in einem Ordner, den Sie unter Live-TV → „Aufnahmepfad“ festlegen.</p>'),
        ('plex', 'IPTV in Plex mit Threadfin', steps(
            'Prüfen, ob Ihr Plex-Konto einen <b>Plex Pass</b> hat – Live-TV &amp; DVR ist daran gebunden.',
            '<b>Threadfin</b> (Nachfolger von xTeVe) auf dem Server oder per Docker installieren.',
            'In Threadfin M3U-Link und XMLTV-Adresse hinzufügen und die gewünschten Sender auswählen.',
            'In Plex unter <b>Einstellungen → Live-TV &amp; DVR → Gerät einrichten</b> Threadfin als Tuner hinzufügen (wird meist automatisch gefunden).',
            'Als Programmführer die XMLTV-Datei von Threadfin wählen und die Sender zuordnen.')
         + tip('Begrenzen Sie in Threadfin die Anzahl gleichzeitiger Streams auf die Zahl der Geräte in Ihrem IPTV-Paket. Sonst versucht Plex bei mehreren Aufnahmen mehr Verbindungen, als Ihr Zugang erlaubt.')),
        ('vergleich', 'Plex, Jellyfin, Emby und Kodi im Vergleich', table(['', 'Jellyfin', 'Plex', 'Emby', 'Kodi'], [
            ['IPTV direkt per M3U', 'Ja', 'Nur über Threadfin', 'Ja', 'Ja (PVR IPTV Simple Client)'],
            ['Programmführer (XMLTV)', 'Ja', 'Ja', 'Ja', 'Ja'],
            ['Aufnahmen', 'Ja, kostenlos', 'Mit Plex Pass', 'Mit Emby Premiere', 'Nur mit Backend (z. B. TVHeadend)'],
            ['Kosten', 'Kostenlos', 'Plex Pass für Live-TV', 'Premiere für DVR', 'Kostenlos'],
            ['Server nötig', 'Ja', 'Ja', 'Ja', 'Nein'],
        ], 'Mediaserver für IPTV im Vergleich') + '''
<p>Kodi ist kein Server, sondern ein Player – dafür ohne Einrichtungsaufwand auf einem Gerät. Die Anleitung finden Sie unter <a href="/kodi-iptv/">Kodi IPTV</a> und <a href="/pvr-iptv-simple-client/">PVR IPTV Simple Client</a>.</p>'''),
        ('hardware', 'Welche Hardware braucht der Server?', '''
<p>Für Live-TV ohne Umwandlung („Direct Stream“) reicht fast jeder Rechner, auch ein NAS von Synology oder QNAP. Sobald der Server Streams für schwächere Geräte umwandeln muss (Transcoding), braucht er eine CPU mit Hardware-Beschleunigung, etwa Intel Quick Sync. Ein Mini-PC mit aktuellem Intel-Prozessor schafft mehrere Full-HD-Streams gleichzeitig. Schließen Sie den Server per LAN an den Router an – über WLAN leidet die Stabilität bei Aufnahmen und mehreren Zuschauern.</p>'''),
    ],
    faq=[
        ('Kann Jellyfin IPTV abspielen?', 'Ja. Jellyfin bindet M3U-Listen als Tuner und XMLTV-Programmführer direkt ein. Live-TV, Programmführer und Aufnahmen sind kostenlos.'),
        ('Brauche ich für IPTV in Plex einen Plex Pass?', 'Ja. Live-TV & DVR in Plex ist an den Plex Pass gebunden. Zusätzlich brauchen Sie einen Vermittler wie Threadfin, der die M3U-Liste als Tuner bereitstellt.'),
        ('Was ist Threadfin?', 'Threadfin ist ein kostenloser M3U-Proxy und Nachfolger von xTeVe. Er stellt IPTV-Listen als virtuellen HDHomeRun-Tuner bereit, den Plex und Emby erkennen.'),
        ('Kann ich mit Jellyfin IPTV aufnehmen?', 'Ja. Jellyfin nimmt Sendungen direkt auf die Festplatte des Servers auf, auch als Serienaufnahme. Die Aufnahmen stehen danach in allen Jellyfin-Apps bereit.'),
        ('Zählt der Mediaserver als Gerät bei meinem IPTV-Anbieter?', 'Jeder gleichzeitig laufende Stream zählt als Verbindung. Schauen zwei Personen über Jellyfin verschiedene Sender, belegt das zwei Verbindungen Ihres Pakets.'),
    ],
    related=['kodi-iptv', 'iptv-aufnehmen', 'pvr-iptv-simple-client', 'tivimate', 'm3u-playlist', 'iptv-apps'],
    card=('Plex & Jellyfin', 'Live-TV mit M3U und EPG im eigenen Mediaserver.'),
    sources=[('Jellyfin Dokumentation – Live TV', 'https://jellyfin.org/docs/'), ('Plex Support – Live TV & DVR', 'https://support.plex.tv/')],
))
