"""Keyword gap-fill, round 4 (25.11.2026): the last uncovered clusters of the Germany keyword list.

New pages: IPTV Anbieter Liste A–Z (competitor names and app-name typos), IPTV Smarters Pro on Smart TVs,
TiviMate on non-Android devices, Georgian TV. EXTRA_SECTIONS / EXTRA_FAQ deepen existing guides with the
keyword variants that were still missing (English variants, spellings, models, deals). LINK_FROM wires the
new pages into related guides. Statements about third parties stay general and verifiable; no ratings of
named providers, no third-party prices.
"""
from .helpers import steps, checks, tip, table, proscons, chips
from .content_more import community

PAGES = []

TEST_TIP = tip('Ob Ihr Gerät, Ihre App und Ihre Leitung zusammenpassen, sehen Sie am schnellsten im '
               '<a href="/kostenlos-testen/">kostenlosen Test</a> – ohne Zahlungsdaten und auf Ihrem eigenen Gerät.', 'Hinweis')

# ================================================================ ANBIETER LISTE A-Z
PAGES.append(dict(
    slug='iptv-anbieter-liste', parent='ratgeber', kind='guide',
    title='IPTV Anbieter Liste A–Z: bekannte Namen richtig prüfen',
    description='IPTV Anbieter Liste von A bis Z: Hot IPTV, Mega IPTV, Pandar TV, UpIPTV & Co. – welche Namen gesucht werden, welche nur Apps sind und wie Sie jeden prüfen.',
    eyebrow='ANBIETER VON A BIS Z', h1='IPTV Anbieter Liste: bekannte Namen von A bis Z',
    lead='Hot IPTV, UpIPTV, Pandar TV, IPTV365: Wer nach einem IPTV Anbieter sucht, stößt auf Dutzende ähnlich klingende Namen. Diese Liste ordnet die häufigsten Suchbegriffe ein, trennt Anbieternamen von App-Namen und zeigt, wie Sie jeden Dienst mit denselben Fragen prüfen.',
    answer='Eine verlässliche IPTV-Bestenliste gibt es nicht: Viele Anbieternamen wie Hot IPTV, Mega IPTV, Gold IPTV oder IPTV365 werden von wechselnden Wiederverkäufern und unter mehreren Domains genutzt, sodass derselbe Name für unterschiedliche Dienste stehen kann. Andere Suchbegriffe wie „Smarters Pro“, „GSE IPTV“ oder „IPTV Streamplayer“ sind gar keine Anbieter, sondern Apps ohne eigene Sender. Prüfen Sie jeden Namen deshalb mit denselben Kriterien: Impressum, Testzugang, nachvollziehbare Preise, keine Lifetime-Versprechen und erreichbarer Support.',
    sections=[
        ('warum', 'Warum es so viele IPTV-Anbieternamen gibt', '''
<p>Der IPTV-Markt ist anders aufgebaut als der Markt für Kabel- oder Streamingabos. Ein großer Teil der Angebote wird über <strong>Wiederverkäufer</strong> vertrieben: Sie kaufen Kontingente bei einem Großhändler und verkaufen sie unter eigenem Namen weiter. Derselbe Markenname taucht so auf mehreren Websites auf, mit unterschiedlichen Preisen, Laufzeiten und Supportzeiten. Umgekehrt wechseln manche Dienste ihren Namen oder ihre Domain, wenn sie Ärger mit Zahlungsanbietern oder Suchmaschinen haben.</p>
<p>Für Sie als Käufer heißt das: Der Name allein sagt wenig. Zwei Seiten mit dem Logo „Mega IPTV“ können völlig verschiedene Betreiber haben. Ein Erfahrungsbericht auf Reddit oder in einem Forum bezieht sich deshalb oft auf einen ganz anderen Dienst als den, den Sie gerade vor sich haben. Wie Sie solche Berichte lesen, erklärt der Ratgeber <a href="/iptv-erfahrungen/">IPTV Erfahrungen</a>; wie Wiederverkauf technisch funktioniert, steht unter <a href="/iptv-reseller/">IPTV Reseller</a>.</p>'''),
        ('liste', 'Häufig gesuchte Anbieternamen von A bis Z', '''
<p>Die folgende Tabelle listet Namen, nach denen in Deutschland häufig gesucht wird, mit den üblichen Schreibweisen. Die Aufnahme in die Liste ist <strong>keine Bewertung</strong>: Wir sagen weder, dass ein Dienst seriös ist, noch dass er es nicht ist. Über die meisten gibt es keine überprüfbaren Angaben zu Betreiber, Sitz oder Senderrechten.</p>''' + table(['Gesuchter Name', 'Schreibweisen in der Suche'], [
            ['24 IPTV', '24iptv, IPTV24, IPTV 24'],
            ['Ace IPTV', 'ace iptv'],
            ['B1G IPTV / Big IPTV', 'b1g iptv, big iptv'],
            ['Besser IPTV', 'besseriptv, besser iptv'],
            ['Bobres IPTV', 'bobres iptv'],
            ['Crystal IPTV', 'crystaliptv, crystal iptv'],
            ['Dino IPTV', 'dino iptv'],
            ['DLTA 4K', 'dlta 4k'],
            ['Dragon IPTV', 'dragoniptv, dragon iptv'],
            ['Eagle IPTV', 'eagle iptv'],
            ['Euro IPTV', 'euro iptv'],
            ['Xtreme HD IPTV', 'xtreme hd iptv, xtremehd'],
            ['Fast IPTV', 'fastiptv, fast iptv'],
            ['ForeverTV', 'forevertv, forever tv'],
            ['Fox IPTV', 'foxiptv, iptv fox'],
            ['Gold IPTV / Golden IPTV', 'goldiptv, golden iptv'],
            ['Hakuna IPTV', 'hakuna iptv'],
            ['Helix IPTV', 'helix iptv'],
            ['Hot IPTV', 'hotiptv, hot iptv'],
            ['iGate IPTV', 'igate iptv'],
            ['IPTV1, IPTV345, IPTV365, IPTV4less', 'iptv1, iptv345, iptv365, iptv4less'],
            ['IPTV Infinity', 'iptv infinity'],
            ['IPTV Rapid / Rapid Swiss TV', 'iptv rapid, rapid swiss iptv, rapid swiss tv'],
            ['Lion IPTV', 'lion iptv'],
            ['Mango IPTV', 'mangoiptv, mango iptv'],
            ['MaxHD IPTV', 'maxhd iptv'],
            ['Mega IPTV', 'megaiptv, mega ip tv'],
            ['Nord IPTV', 'nord iptv'],
            ['Norago IPTV', 'norago iptv'],
            ['Nova IPTV', 'novaiptv, nova iptv'],
            ['Pandar TV', 'pandar tv'],
            ['Quzu TV', 'quzu tv, quzu iptv'],
            ['Ragnar IPTV', 'ragnar iptv'],
            ['Sebastian IPTV', 'sebastian iptv'],
            ['Sero IPTV', 'sero iptv'],
            ['Slynet TV', 'slynet tv'],
            ['Strong IPTV', 'strong iptv'],
            ['Szenebox IPTV', 'szenebox iptv'],
            ['Trex IPTV', 'trex iptv'],
            ['TV Team IPTV', 'tv team iptv'],
            ['UpIPTV', 'upiptv, up iptv'],
            ['World IPTV / Worldwide IPTV', 'world iptv, worldwide iptv'],
            ['Yu2Go', 'yu2go'],
        ], 'Häufig gesuchte IPTV-Anbieternamen') + '''
<p>Auffällig sind die vielen Namen mit Zahlen oder Superlativen wie „4K“, „8K“, „Premium“ oder „Gold“. Solche Zusätze beschreiben selten eine echte Eigenschaft. Was hinter „IPTV 8K“ steckt, erklärt der Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>.</p>'''),
        ('apps', 'Kein Anbieter, sondern eine App: häufige Verwechslungen', '''
<p>Viele Suchanfragen, die wie ein Anbietername aussehen, meinen in Wahrheit einen Player. Diese Apps enthalten <strong>keine Sender</strong>; sie spielen nur ab, was Ihr IPTV-Abo liefert. Wer „Smarters Pro kaufen“ sucht, braucht also eigentlich ein Abo und die kostenlose App dazu.</p>''' + table(['Suchbegriff', 'Was gemeint ist', 'Ratgeber'], [
            ['SmartersPro, IP Smarter Pro, Smarters TV', 'App IPTV Smarters Pro', '<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>'],
            ['Smart OneIPTV, Smarte One IPTV', 'App SmartOne IPTV', '<a href="/smartone-iptv/">SmartOne IPTV</a>'],
            ['My SIPTV, SIP TV, Smart IP TV', 'App Smart IPTV (SIPTV) und deren „My List“', '<a href="/smart-iptv/">Smart IPTV</a>'],
            ['GSEIPTV', 'App GSE Smart IPTV', '<a href="/gse-smart-iptv/">GSE Smart IPTV</a>'],
            ['IPTV Streamplayer', 'App IPTV Stream Player', '<a href="/iptv-stream-player/">IPTV Stream Player</a>'],
            ['IPTVPro, IPTVApp', 'Apps „IPTV“ und „IPTV Pro“', '<a href="/iptv-pro-app/">IPTV Pro</a>'],
            ['IPTV Extreme, Extreme IPTV', 'App IPTV Extreme für Android (gleichnamige Anbieter gibt es ebenfalls)', '<a href="/iptv-extreme/">IPTV Extreme</a>'],
            ['SimpleIPTV', 'Kodi-Add-on PVR IPTV Simple Client', '<a href="/pvr-iptv-simple-client/">PVR IPTV Simple Client</a>'],
            ['Cody IPTV, Kodi XBMC IPTV', 'Mediacenter Kodi (früher XBMC)', '<a href="/kodi-iptv/">Kodi IPTV</a>'],
            ['Duplecast IPTV', 'App Duplecast', '<a href="/iptv-apps/">IPTV Apps</a>'],
            ['Mu3 IPTV, M.m3u IPTV', 'Tippfehler für M3U-Playlist', '<a href="/m3u-playlist/">M3U Playlist</a>'],
            ['IPTV Portal, IPTVportal', 'Portal-Adresse für MAG-Boxen und STB-Emulatoren', '<a href="/mag-box-iptv/">MAG Box</a>'],
        ], 'Suchbegriffe, die eine App meinen')),
        ('pruefen', 'So prüfen Sie jeden Namen auf der Liste', steps(
            '<b>Impressum und Kontakt:</b> Gibt es eine erreichbare E-Mail-Adresse, und antwortet jemand innerhalb eines Tages?',
            '<b>Testzugang:</b> Ein kostenloser Test ohne Zahlungsdaten ist Standard. Wer nur gegen Vorkasse „testet“, verkauft eigentlich.',
            '<b>Preise:</b> Stehen alle Laufzeiten und Geräteanzahlen klar auf der Seite, inklusive der Frage, ob sich das Abo verlängert?',
            '<b>Keine Lifetime-Versprechen:</b> „Einmal zahlen, für immer schauen“ funktioniert bei laufenden Serverkosten nicht – siehe <a href="/iptv-lifetime/">IPTV Lifetime</a>.',
            '<b>Zahlungsweg:</b> Zahlungen sollten nachvollziehbar sein. Welche Wege es gibt und worauf Sie achten, erklärt <a href="/iptv-bezahlen/">IPTV bezahlen</a>.',
            '<b>Domain vergleichen:</b> Stimmt die Adresse mit der überein, die Sie aus Empfehlungen kennen? Nachahmer-Domains mit Bindestrich oder anderer Endung sind häufig.',
            '<b>Im Test messen:</b> Abends zur Hauptsendezeit einen Fußballsender und einen 4K-Sender je 20 Minuten laufen lassen.')
         + TEST_TIP),
        ('warnsignale', 'Warnsignale, die für jeden Anbieter gelten', table(['Warnsignal', 'Warum es problematisch ist'], [
            ['Nur Kontakt über Telegram, keine E-Mail', 'Bei Problemen fehlt ein verbindlicher Ansprechpartner'],
            ['„Alle Sky- und DAZN-Inhalte für 5 € im Monat“', 'Lizenzierte Pay-TV-Inhalte kosten beim Rechteinhaber ein Vielfaches – siehe <a href="/sky-iptv/">Sky über IPTV</a>'],
            ['Countdown-Timer und Dauer-Rabatt', 'Künstlicher Zeitdruck statt nachvollziehbarer Preise'],
            ['Bewertungen nur auf der eigenen Seite', 'Nicht überprüfbar; unabhängige Stimmen fehlen'],
            ['App-Download nur von unbekannten Seiten', 'Gefahr manipulierter APKs; seriöse Dienste nennen gängige Player'],
        ], 'Warnsignale bei IPTV-Anbietern') + '''
<p>Eine sachliche Gegenüberstellung der Kriterien, inklusive einer Checkliste für den 24-Stunden-Test, finden Sie im <a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>.</p>'''),
        ('iptv-kanal', 'Wo steht IPTV Kanal in dieser Liste?', '''
<p>Wir gehören nicht in die Tabelle oben, weil wir uns nicht selbst bewerten wollen. Messen Sie uns an denselben Kriterien: Unsere Preise stehen vollständig auf der <a href="/preise/">Preisseite</a> (ab 9 € für einen Monat, 49 € für ein Jahr, ohne automatische Verlängerung), der Test ist kostenlos und ohne Zahlungsdaten, und unser deutschsprachiger Support antwortet per E-Mail an kontakt@iptvkanal.de und per WhatsApp. Wenn uns ein anderer Anbieter in Ihrem Test überzeugender erscheint, ist das ein legitimes Ergebnis.</p>'''),
    ],
    faq=[
        ('Welcher IPTV Anbieter ist der beste?', 'Das lässt sich nicht pauschal sagen, weil viele Anbieternamen von mehreren Betreibern genutzt werden. Entscheidend ist, wie stabil der konkrete Zugang auf Ihrem Gerät und Ihrer Leitung läuft. Prüfen Sie das im kostenlosen Test zur Hauptsendezeit.'),
        ('Sind Hot IPTV, Mega IPTV oder UpIPTV seriös?', 'Das können wir nicht beurteilen: Über Betreiber und Rechte dieser Dienste gibt es meist keine überprüfbaren Angaben, und dieselben Namen tauchen auf verschiedenen Websites auf. Prüfen Sie jeden Anbieter mit der Checkliste auf dieser Seite.'),
        ('Was ist eine IPTV Bestenliste wert?', 'Wenig, wenn sie nicht offenlegt, wie getestet wurde. Viele Bestenlisten verdienen an Provisionen der gelisteten Anbieter. Verlassen Sie sich lieber auf einen eigenen Test.'),
        ('Ist IPTV Smarters ein Anbieter?', 'Nein. IPTV Smarters Pro ist eine App ohne eigene Sender. Die Sender kommen aus dem Abo eines IPTV-Anbieters, dessen Zugangsdaten Sie in der App eintragen.'),
        ('Warum finde ich denselben Anbieternamen auf mehreren Websites?', 'Weil Wiederverkäufer Kontingente unter bekannten Namen weiterverkaufen und Nachahmer bekannte Namen kopieren. Vergleichen Sie Domain, Kontakt und Preise, bevor Sie bezahlen.'),
        ('Gibt es IPTV Kanal auch unter anderem Namen?', 'Nein. IPTV Kanal ist nur unter iptvkanal.de erreichbar. Kontakt per E-Mail an kontakt@iptvkanal.de oder per WhatsApp über unsere Website.'),
    ],
    related=['iptv-anbieter-vergleich', 'iptv-erfahrungen', 'iptv-anbieter', 'iptv-lifetime', 'iptv-reseller', 'iptv-bezahlen'],
    card=('IPTV Anbieter Liste A–Z', 'Bekannte Anbieternamen einordnen und richtig prüfen.'),
))

# ================================================================ SMARTERS ON SMART TV
PAGES.append(dict(
    slug='iptv-smarters-pro-smart-tv', parent='apps', kind='guide',
    title='IPTV Smarters Pro auf Samsung, LG & Smart TV einrichten',
    description='IPTV Smarters Pro auf dem Smart TV: Samsung (Tizen), LG (webOS), Android TV, Hisense und Roku – wo es die App gibt, Einrichtung und Alternativen.',
    eyebrow='SMARTERS AM FERNSEHER', h1='IPTV Smarters Pro auf Samsung, LG und anderen Smart TVs',
    lead='Am Handy ist IPTV Smarters Pro schnell installiert. Am Fernseher hängt es von Marke, Betriebssystem und Baujahr ab, ob die App im Store steht. Hier sehen Sie für jede Plattform, was geht, wie Sie Smarters einrichten und was Sie tun, wenn die App fehlt.',
    answer='IPTV Smarters Pro läuft auf Fernsehern mit Android TV oder Google TV (etwa Sony, Philips, TCL) direkt aus dem Google Play Store. Auf Samsung (Tizen) und LG (webOS) bietet der Entwickler je nach Modell, Baujahr und Region eine Smarters-App im Store des Herstellers an; fehlt sie, nutzen Sie einen anderen Player wie SET IPTV oder Flix IPTV oder einen Fire TV Stick am HDMI-Anschluss. Für Hisense VIDAA und Roku gibt es keine offizielle Smarters-App. Die Einrichtung ist überall gleich: Login mit Xtream Codes API, Benutzername, Passwort und Server-URL eintragen.',
    sections=[
        ('plattformen', 'Smarters Pro nach Fernseher-Plattform', table(['Fernseher', 'Betriebssystem', 'Smarters verfügbar?', 'Ratgeber'], [
            ['Samsung', 'Tizen', 'Je nach Modell und Region im Samsung-Store', '<a href="/iptv-samsung-tv/">IPTV Samsung TV</a>'],
            ['LG', 'webOS', 'Je nach Modell und Region im LG-Store', '<a href="/iptv-lg-tv/">IPTV LG TV</a>'],
            ['Sony Bravia, Philips, TCL, Xiaomi', 'Android TV / Google TV', 'Ja, Google Play Store', '<a href="/iptv-sony-bravia/">Sony</a>, <a href="/iptv-philips-tv/">Philips</a>, <a href="/iptv-tcl-tv/">TCL</a>'],
            ['Hisense', 'VIDAA (teils Android TV)', 'Auf VIDAA nein, auf Android-Modellen ja', '<a href="/iptv-hisense-tv/">IPTV Hisense</a>'],
            ['Roku-Fernseher und Roku-Player', 'Roku OS', 'Keine offizielle App', '<a href="/iptv-roku/">IPTV Roku</a>'],
            ['Jeder Fernseher mit HDMI', 'Fire TV Stick / Google-TV-Stick', 'Ja, per Downloader bzw. Play Store', '<a href="/iptv-smarters-pro-firestick/">Smarters auf Fire TV</a>'],
        ], 'IPTV Smarters Pro nach Smart-TV-Plattform') + '''
<p>Ob die App im Store Ihres Fernsehers erscheint, prüfen Sie am einfachsten direkt: Store öffnen, nach „Smarters“ suchen. Erscheint nichts, ist sie für Ihr Modell oder Ihre Region nicht freigegeben – auch wenn ein Bekannter sie auf seinem Gerät gleicher Marke hat. Auf älteren Modellen ist die Auswahl im Store oft deutlich kleiner als auf aktuellen Geräten.</p>'''),
        ('samsung-lg', 'IPTV Smarters Pro auf Samsung und LG installieren', steps(
            'Fernseher mit dem Internet verbinden, am besten per LAN-Kabel.',
            'Samsung: <b>Apps</b> öffnen, Lupe wählen. LG: <b>LG Content Store</b> bzw. <b>Apps</b> öffnen und die Suche wählen.',
            '„IPTV Smarters“ eingeben und die App des Entwicklers installieren.',
            'App öffnen, Nutzungsbedingungen bestätigen und <b>„Login mit Xtream Codes API“</b> wählen.',
            'Einen beliebigen Namen, Ihren Benutzernamen, Ihr Passwort und die Server-URL aus der Willkommens-E-Mail eintragen.',
            '<b>Hinzufügen</b> wählen. Sender, Filme, Serien und Programmführer laden automatisch.')
         + tip('Tippen Sie die Server-URL inklusive <code>http://</code> und Port genau ab. Ein vertauschter Buchstabe ist der häufigste Grund für „Ungültige Zugangsdaten“.')),
        ('android-tv', 'Smarters auf Android TV und Google TV', '''
<p>Auf Fernsehern mit Android TV oder Google TV ist es am einfachsten: IPTV Smarters Pro steht im Google Play Store. Suchen Sie per Sprachsuche oder Tastatur nach „IPTV Smarters Pro“, installieren Sie die App und melden Sie sich wie oben beschrieben an. Wenn die Fernbedienung in der App hakt, hilft oft eine Bluetooth-Maus oder die Google-TV-App auf dem Handy als Fernbedienung.</p>
<p>Viele Android-Fernseher haben wenig Arbeitsspeicher. Ruckelt das Bild in 4K, obwohl die Leitung schnell genug ist, liegt es meist am TV-Prozessor. Dann lohnt sich ein externer Stick oder eine Box – siehe <a href="/iptv-stick/">IPTV Stick</a> und <a href="/iptv-box/">IPTV Box</a>.</p>'''),
        ('fehlt', 'Smarters fehlt im Store? Diese Alternativen funktionieren', table(['Alternative', 'Läuft auf', 'Login', 'Kosten'], [
            ['<a href="/set-iptv/">SET IPTV</a>', 'Samsung, LG, Android', 'M3U über MAC-Adresse', 'Aktivierung beim Entwickler'],
            ['<a href="/flix-iptv/">Flix IPTV</a>', 'Samsung, LG, Android', 'M3U oder Xtream', 'Testphase, dann Aktivierung'],
            ['<a href="/ibo-player/">IBO Player</a>', 'Samsung, LG, Android, Fire TV', 'M3U oder Xtream', 'Testphase, dann Aktivierung'],
            ['<a href="/smart-iptv/">Smart IPTV</a>', 'Samsung, LG, Android', 'M3U per „My List“', 'Einmalige Aktivierung'],
            ['<a href="/ss-iptv/">SS IPTV</a>', 'Samsung, LG, Android', 'M3U per Verbindungscode', 'Kostenlos'],
        ], 'Alternativen zu IPTV Smarters Pro am Fernseher') + '''
<p>Für Roku- und VIDAA-Fernseher ist ein <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder ein Google-TV-Stick am HDMI-Anschluss die zuverlässigste Lösung: Dort laufen Smarters, TiviMate und alle anderen Android-Player. Eine Übersicht aller Player finden Sie unter <a href="/bester-iptv-player/">Bester IPTV Player</a>.</p>'''),
        ('einstellungen', 'Die besten Smarters-Einstellungen für den Fernseher', checks(
            '<strong>Player:</strong> Unter Einstellungen → Player-Auswahl zuerst den eingebauten Player testen. Ruckelt es, auf „VLC Player“ bzw. die Alternative wechseln.',
            '<strong>Programmführer:</strong> Einstellungen → EPG-Zeitverschiebung auf 0 lassen, wenn die Zeitzone des Fernsehers Europa/Berlin ist.',
            '<strong>Senderliste:</strong> Unnötige Gruppen über „Kategorien ausblenden“ entfernen – das beschleunigt das Laden spürbar.',
            '<strong>Netzwerk:</strong> LAN statt WLAN; bei WLAN das 5-GHz-Band nutzen.',
            '<strong>Schnellstart:</strong> Den Energiesparmodus „Schnellstart“ ausschalten, wenn die App nach dem Einschalten keine Verbindung findet.')),
        ('probleme', 'Typische Probleme am Smart TV', table(['Problem', 'Ursache', 'Lösung'], [
            ['App startet, aber „Keine Verbindung“', 'Fernseher war im Standby, Netzwerk noch nicht bereit', 'Fernseher einmal komplett vom Strom trennen'],
            ['Sender laden, Bild bleibt schwarz', 'Codec wird vom TV-Player nicht unterstützt', 'In den Einstellungen den Player wechseln'],
            ['Programmführer fehlt', 'EPG noch nicht geladen', 'Einstellungen → EPG aktualisieren, einige Minuten warten'],
            ['App nach Firmware-Update verschwunden', 'App für das Modell nicht mehr freigegeben', 'Alternative Player nutzen oder Stick anschließen'],
        ], 'IPTV Smarters Pro am Smart TV: Fehler') + TEST_TIP),
    ],
    faq=[
        ('Gibt es IPTV Smarters Pro für Samsung TV?', 'Je nach Modell, Baujahr und Region bietet der Entwickler eine Smarters-App im Samsung-Store an. Suchen Sie im Store nach „Smarters“. Fehlt die App, nutzen Sie SET IPTV, Flix IPTV oder einen Fire TV Stick.'),
        ('Gibt es IPTV Smarters Pro für LG TV?', 'Auf vielen neueren LG-Fernsehern mit webOS ist eine Smarters-App im LG Content Store zu finden, abhängig von Modell und Region. Alternativ funktionieren SS IPTV, Smart IPTV und Flix IPTV auf LG.'),
        ('Kann ich IPTV Smarters Pro auf Roku installieren?', 'Nein, für Roku gibt es keine offizielle Smarters-App. Schließen Sie einen Fire TV Stick oder Google-TV-Stick an den Fernseher an; dort läuft Smarters ohne Einschränkungen.'),
        ('Läuft Smarters auf Hisense VIDAA?', 'Auf Hisense-Fernsehern mit VIDAA nicht. Auf Hisense-Modellen mit Android TV oder Google TV installieren Sie Smarters aus dem Play Store.'),
        ('Welche Zugangsdaten brauche ich für Smarters am Fernseher?', 'Benutzername, Passwort und Server-URL Ihres IPTV-Abos für den Login mit Xtream Codes API. Alternativ funktioniert ein M3U-Link.'),
        ('Ist Smarters am Fernseher kostenlos?', 'Die App selbst ist kostenlos; je nach Plattform bietet der Entwickler Zusatzfunktionen gegen Gebühr an. Die Sender kommen immer aus Ihrem IPTV-Abo.'),
    ],
    related=['iptv-smarters-pro', 'iptv-samsung-tv', 'iptv-lg-tv', 'iptv-smart-tv', 'iptv-smarters-pro-firestick', 'set-iptv'],
    card=('Smarters Pro am Smart TV', 'Samsung, LG, Android TV, Hisense und Roku: was geht.'),
    sources=[('IPTV Smarters (offizielle Website)', 'https://www.iptvsmarters.com/'), ('Wikipedia: Tizen (Samsung)', 'https://de.wikipedia.org/wiki/Tizen'), ('Wikipedia: webOS (LG)', 'https://de.wikipedia.org/wiki/WebOS')],
))

# ================================================================ TIVIMATE ON OTHER DEVICES
PAGES.append(dict(
    slug='tivimate-andere-geraete', parent='apps', kind='guide',
    title='TiviMate auf PC, Mac, iPhone & Samsung TV: geht das?',
    description='TiviMate auf PC, Mac, iPhone, Apple TV, Samsung, LG und Chromecast: wo TiviMate läuft, wo nicht, Emulator-Lösungen und die besten Alternativen je Gerät.',
    eyebrow='TIVIMATE OHNE ANDROID TV', h1='TiviMate auf PC, Mac, iPhone und Samsung TV',
    lead='TiviMate gilt als einer der komfortabelsten IPTV Player. Viele möchten ihn deshalb auch auf dem Laptop, dem iPhone oder dem Samsung-Fernseher nutzen. Hier steht ehrlich, wo das geht, wo nicht, und welche App jeweils am nächsten an TiviMate herankommt.',
    answer='TiviMate ist eine reine Android-TV-App: Sie läuft auf Fire TV mit Fire OS, Google TV, Android-TV-Fernsehern und Android-TV-Boxen. Für Windows, Mac, iPhone, iPad, Apple TV, Samsung (Tizen), LG (webOS) und Roku gibt es keine TiviMate-Version. Am PC lässt sich TiviMate nur über einen Android-Emulator starten; einfacher sind dort VLC oder IPTV Smarters. Auf Apple-Geräten kommen IPTVX und iPlayTV dem TiviMate-Erlebnis am nächsten, auf Samsung und LG Player wie Flix IPTV oder IBO Player.',
    sections=[
        ('uebersicht', 'Wo läuft TiviMate – und wo nicht?', table(['Gerät', 'TiviMate?', 'Beste Alternative', 'Ratgeber'], [
            ['Fire TV Stick (Fire OS)', 'Ja', '–', '<a href="/tivimate-fire-tv-stick/">TiviMate auf Fire TV</a>'],
            ['Google TV, Android TV, Nvidia Shield', 'Ja, Play Store', '–', '<a href="/tivimate/">TiviMate einrichten</a>'],
            ['Android-Smartphone', 'Nur eingeschränkt (für TV-Bedienung gebaut)', 'IPTV Smarters Pro, OTT Navigator', '<a href="/iptv-android/">IPTV Android</a>'],
            ['Windows-PC, Laptop', 'Nein (nur Emulator)', 'VLC, IPTV Smarters', '<a href="/iptv-pc-mac/">IPTV PC &amp; Mac</a>'],
            ['Mac, MacBook', 'Nein', 'IPTVX, VLC', '<a href="/iptvx/">IPTVX</a>'],
            ['iPhone, iPad', 'Nein', 'IPTVX, iPlayTV, Smarters Player Lite', '<a href="/iptv-apple-tv-iphone/">IPTV iPhone</a>'],
            ['Apple TV', 'Nein', 'IPTVX, iPlayTV', '<a href="/iptv-apple-tv/">IPTV Apple TV</a>'],
            ['Samsung (Tizen), LG (webOS)', 'Nein', 'Flix IPTV, IBO Player, SET IPTV', '<a href="/iptv-samsung-tv/">Samsung</a>, <a href="/iptv-lg-tv/">LG</a>'],
            ['Chromecast mit Google TV', 'Ja, Play Store', '–', '<a href="/iptv-chromecast/">IPTV Chromecast</a>'],
            ['Roku', 'Nein', 'Fire TV Stick anschließen', '<a href="/iptv-roku/">IPTV Roku</a>'],
        ], 'TiviMate nach Gerät') + '''
<p>Der Grund ist einfach: Der Entwickler baut TiviMate gezielt für die Bedienung mit der Fernbedienung auf Android-TV-Systemen. Eine offizielle Version für andere Betriebssysteme ist nicht angekündigt. Angebote, die „TiviMate für iOS“ oder „TiviMate für Windows“ zum Download anbieten, sind deshalb mit Vorsicht zu behandeln.</p>'''),
        ('pc', 'TiviMate am PC und Mac: der Emulator-Weg', '''
<p>Wer TiviMate unbedingt am Rechner nutzen möchte, kann einen Android-Emulator installieren und TiviMate darin aus dem Play Store laden. Das funktioniert, hat aber Nachteile: Der Emulator braucht viel Arbeitsspeicher, die Bedienung ist für Maus und Tastatur nicht gedacht, und Bildfehler oder Ruckler sind häufiger als mit einem nativen Player.</p>''' + proscons(
            ['Gewohnte TiviMate-Oberfläche und Premium-Funktionen', 'Ein Premium-Konto gilt auch im Emulator als eines von bis zu fünf Geräten'],
            ['Hoher Ressourcenbedarf, Lüfter dreht hoch', 'Bedienung mit der Maus umständlich', 'Auf Apple-Silicon-Macs nur eingeschränkt möglich'],
            'Vorteile', 'Nachteile') + '''
<p>Unsere Empfehlung für den Rechner: <a href="/vlc-iptv/">VLC</a> mit Ihrem M3U-Link für den schnellen Einstieg, oder die Desktop-Version von IPTV Smarters mit Programmführer. Alle Optionen stehen im Ratgeber <a href="/iptv-pc-mac/">IPTV am PC und Mac</a>, die browserbasierte Variante unter <a href="/iptv-im-browser/">IPTV im Browser</a>.</p>'''),
        ('apple', 'TiviMate auf iPhone und Apple TV: die nächsten Alternativen', '''
<p>Für Apple-Geräte gibt es keine TiviMate-App. Auch die <strong>TiviMate Companion</strong>-App, mit der Sie Premium verwalten, wird nur für Android angeboten. Wer TiviMate am Fernseher nutzt und das iPhone als zweites Gerät, braucht dort einen anderen Player – die Zugangsdaten Ihres IPTV-Abos funktionieren in jeder App.</p>''' + table(['App', 'Geräte', 'Stärke'], [
            ['<a href="/iptvx/">IPTVX</a>', 'iPhone, iPad, Apple TV, Mac', 'Programmführer-Raster ähnlich wie TiviMate'],
            ['<a href="/iplaytv/">iPlayTV</a>', 'iPhone, iPad, Apple TV', 'Schlanke Oberfläche, schneller Senderwechsel'],
            ['<a href="/smarters-player-lite/">Smarters Player Lite</a>', 'iPhone, iPad, Apple TV', 'Kostenlos, Xtream-Login'],
            ['<a href="/gse-smart-iptv/">GSE Smart IPTV</a>', 'iPhone, iPad, Apple TV', 'Viele Formate, lokale Playlists'],
        ], 'TiviMate-Alternativen für Apple')),
        ('samsung', 'TiviMate auf Samsung und LG: so kommen Sie trotzdem hin', steps(
            'Prüfen, ob Ihr Fernseher ein Android-TV- oder Google-TV-Modell ist. Dann läuft TiviMate direkt aus dem Play Store.',
            'Bei Tizen (Samsung) oder webOS (LG): einen <a href="/iptv-fire-tv-stick/">Fire TV Stick mit Fire OS</a> oder einen Google-TV-Stick an einen freien HDMI-Anschluss stecken.',
            'TiviMate auf dem Stick installieren und Ihre Playlist eintragen.',
            'Optional: Die Fernseher-Fernbedienung per HDMI-CEC für den Stick nutzen, damit Sie nur eine Fernbedienung brauchen.')
         + '''<p>Wer keinen Stick möchte, nutzt direkt auf dem Fernseher <a href="/flix-iptv/">Flix IPTV</a> oder den <a href="/ibo-player/">IBO Player</a>; beide haben einen Programmführer mit Rasteransicht. Für Smarters am Fernseher gibt es einen eigenen Ratgeber: <a href="/iptv-smarters-pro-smart-tv/">IPTV Smarters Pro am Smart TV</a>.</p>'''),
        ('chromecast', 'TiviMate und Chromecast', '''
<p>Beim Chromecast kommt es auf das Modell an. Der <strong>Chromecast mit Google TV</strong> und das Nachfolgegerät Google TV Streamer haben ein eigenes Betriebssystem mit Play Store; TiviMate wird darauf ganz normal installiert. Ältere Chromecast-Modelle ohne Fernbedienung können nur Inhalte vom Handy empfangen. TiviMate selbst bietet keine Funktion zum Streamen an einen Chromecast. Details im Ratgeber <a href="/iptv-chromecast/">IPTV auf Chromecast</a>.</p>''' + TEST_TIP),
    ],
    faq=[
        ('Gibt es TiviMate für den PC?', 'Nein, eine Windows-Version gibt es nicht. TiviMate lässt sich nur über einen Android-Emulator starten. Einfacher sind am PC VLC oder die Desktop-Version von IPTV Smarters.'),
        ('Gibt es TiviMate für Mac oder MacBook?', 'Nein. Auf dem Mac nutzen Sie IPTVX oder VLC. Ein Android-Emulator ist auf Macs mit Apple-Chip nur eingeschränkt möglich.'),
        ('Gibt es TiviMate für iPhone oder Apple TV?', 'Nein, TiviMate ist eine reine Android-TV-App. Auf iPhone, iPad und Apple TV sind IPTVX, iPlayTV und Smarters Player Lite gute Alternativen.'),
        ('Gibt es TiviMate für Samsung TV?', 'Nicht für Samsung-Fernseher mit Tizen. Stecken Sie einen Fire TV Stick oder Google-TV-Stick an den Fernseher, dann läuft TiviMate wie gewohnt.'),
        ('Gibt es die TiviMate Companion App für das iPhone?', 'Nein, die Companion-App für Premium wird nur für Android angeboten. Für den Kauf brauchen Sie ein Android-Handy, Tablet oder Google-TV-Gerät.'),
        ('Funktioniert TiviMate mit Chromecast?', 'Auf dem Chromecast mit Google TV und dem Google TV Streamer ja, dort installieren Sie TiviMate aus dem Play Store. Ältere Chromecast-Modelle ohne Fernbedienung unterstützen TiviMate nicht.'),
    ],
    related=['tivimate', 'tivimate-premium', 'tivimate-fire-tv-stick', 'iptvx', 'iptv-pc-mac', 'bester-iptv-player'],
    card=('TiviMate auf anderen Geräten', 'PC, Mac, iPhone, Samsung und Chromecast: was geht.'),
    sources=[('TiviMate im Google Play Store', 'https://play.google.com/store/apps/details?id=ar.tvplayer.tv')],
))

# ================================================================ GEORGISCH (iptv ge)
PAGES.append(community(
    'iptv-georgisch', 'IPTV Georgisch: georgische Sender in Deutschland',
    'Georgisches Fernsehen per IPTV in Deutschland: Imedi, Rustavi 2, 1TV und weitere Sender, Zeitzone, georgische Schrift im Programmführer und Einrichtung.',
    'IPTV Georgisch: georgisches Fernsehen in Deutschland',
    'Sie suchen Imedi oder Rustavi 2 in Deutschland? Per IPTV kommen Programme aus Georgien über Ihre Internetleitung auf Fernseher, Handy und Tablet – mit Programmführer in deutscher Zeit.',
    'Mit IPTV schauen Sie georgische Sender wie 1TV, Imedi oder Rustavi 2 in Deutschland über Ihre Internetleitung, ohne Satellitenschüssel. In der IPTV-App öffnen Sie die georgischen Sendergruppen, legen Favoriten an und lassen den Programmführer in deutscher Zeit anzeigen. Welche georgischen Kanäle Ihr Zugang enthält, sehen Sie im kostenlosen Test.',
    '''<p><strong>კეთილი იყოს თქვენი მობრძანება!</strong> Suchanfragen wie „IPTV GE“, „Imedi TV live“ oder „Rustavi 2 IPTV“ zeigen: Auch in Deutschland möchten viele Menschen georgische Nachrichten, Talkshows und Serien sehen. „IPTV.ge“ ist dabei der Name eines Angebots aus Georgien – IPTV Kanal ist damit nicht verbunden. Per IPTV kommen georgische Programme ohne zusätzliche Hardware in dieselbe App wie Ihre deutschen Sender.</p>
<p>Georgien liegt in der Zeitzone UTC+4 und stellt die Uhr nicht um. Im Winter ist es dort drei Stunden später als in Deutschland, im Sommer zwei. Gute IPTV-Apps rechnen das automatisch um, wenn die Zeitzone auf Europa/Berlin steht.</p>''',
    [['1TV (Erster Kanal, GPB)', 'Öffentlich-rechtlicher Rundfunk Georgiens'], ['Imedi TV', 'Privatsender: Nachrichten, Shows, Serien'],
     ['Rustavi 2', 'Privatsender: Nachrichten und Unterhaltung'], ['Formula TV', 'Privatsender: Nachrichten und Talk'],
     ['TV Pirveli', 'Privatsender: Nachrichten und Politik'], ['POS TV', 'Privatsender'], ['Adjara TV', 'Öffentlich-rechtlicher Sender der Autonomen Republik Adscharien']],
    ('tipps', 'Tipps für georgische Sender'), checks(
        'Sendergruppen heißen oft „GE“, „GEO“ oder „Georgia“ – suchen Sie in der App nach diesen Kürzeln.',
        'Die georgische Schrift (Mchedruli) wird korrekt angezeigt, wenn die Playlist als M3U8 mit UTF-8 geladen wird oder Sie einen Xtream-Codes-Login nutzen.',
        'Für Nachrichten am Abend lohnt sich Catch-Up: Die Hauptnachrichten laufen in Georgien, wenn es in Deutschland noch Nachmittag ist.',
        'Legen Sie eine eigene Favoritenliste an, damit georgische und deutsche Sender schnell erreichbar sind.') + '''
<p>Wie Sie Gruppen und Favoriten in der App sortieren, zeigt der Ratgeber <a href="/iptv-senderliste/">IPTV Senderliste</a>. Russischsprachige Programme, die in Georgien ebenfalls verbreitet sind, behandelt <a href="/iptv-russisch/">IPTV Russisch</a>.</p>''',
    [('Kann ich georgische Sender in Deutschland per IPTV schauen?', 'Ja. Per IPTV kommen georgische Programme über Ihre Internetleitung. Welche Kanäle wie Imedi oder Rustavi 2 Ihr Zugang enthält, zeigt der kostenlose Test.'),
     ('Was ist IPTV GE?', 'Mit „IPTV GE“ oder „iptv.ge“ suchen viele nach georgischem Fernsehen per IPTV oder nach einem gleichnamigen Angebot aus Georgien. IPTV Kanal ist mit diesem Angebot nicht verbunden.'),
     ('Warum stimmen die Sendezeiten georgischer Sender nicht?', 'Georgien liegt im Winter drei, im Sommer zwei Stunden vor Deutschland. Stellen Sie die Zeitzone in der App auf Europa/Berlin, dann rechnet der Programmführer automatisch um.'),
     ('Wird die georgische Schrift im Programmführer angezeigt?', 'Ja, wenn Sie die Playlist als M3U8 mit UTF-8 laden oder einen Xtream-Codes-Login nutzen. Bei einer alten M3U-Datei können Zeichen falsch erscheinen.')],
    ('IPTV Georgisch', 'Imedi, Rustavi 2 und 1TV per IPTV in Deutschland.'),
    ['iptv-international', 'iptv-russisch', 'iptv-senderliste', 'iptv-smarters-pro', 'tivimate', 'm3u-playlist']))


# ================================================================ DEPTH: missing variants on existing guides
EXTRA_SECTIONS = {
    'iptv-georgisch': [
        ('schrift', 'Georgische Schrift wird als Kästchen angezeigt? So lösen Sie das', '''
<p>Die georgische Schrift hat ein eigenes Alphabet. Nicht jedes Gerät bringt dafür eine Schriftart mit: Vor allem ältere Smart-TVs und manche günstige Boxen zeigen georgische Sendernamen und Programminfos dann als leere Kästchen oder Fragezeichen an. Das Bild selbst ist davon nicht betroffen, nur die Texte.</p>''' + table(['Gerät', 'Georgische Schrift', 'Tipp'], [
            ['Android TV, Google TV, Fire TV', 'In der Regel ja', 'App mit eigener Schriftart wie TiviMate oder Smarters nutzen'],
            ['iPhone, iPad, Apple TV', 'Ja', 'Keine Einstellung nötig'],
            ['Neuere Samsung- und LG-Fernseher', 'Meist ja', 'Playlist als M3U8 laden'],
            ['Ältere Smart-TVs, MAG-Boxen', 'Teilweise nein', 'Sender in der App umbenennen oder auf einen Stick wechseln'],
        ], 'Georgische Schrift nach Gerät') + '''
<p>Wenn mehrere Familienmitglieder gleichzeitig schauen, etwa georgische Nachrichten im Wohnzimmer und Bundesliga im Kinderzimmer, brauchen Sie ein Paket mit zwei oder mehr Geräten. Die Preise je Geräteanzahl stehen unter <a href="/preise/">IPTV Preise</a>; Geräte-Anleitungen finden Sie in der <a href="/iptv-geraete/">Geräteübersicht</a>.</p>'''),
    ],
    'iptv-smarters-pro': [
        ('kosten-support', 'Kostet IPTV Smarters Pro etwas? Premium, Abo und Support', '''
<p>Die App IPTV Smarters Pro (oft auch „SmartersPro“, „IP TV Smarters“ oder „Smarters TV“ geschrieben) ist im Kern kostenlos. Je nach Plattform und Version bietet der Entwickler Zusatzfunktionen oder eine werbefreie Variante gegen Gebühr an; Preise dafür legt der Entwickler fest, sie ändern sich, deshalb nennen wir hier keine Beträge. Wichtig ist der Unterschied zwischen zwei Dingen, die gern verwechselt werden:</p>''' + table(['Begriff', 'Was es ist', 'Wer es verkauft'], [
            ['„IPTV Smarters Pro Premium“', 'Optionale Zusatzfunktionen der App', 'Der App-Entwickler, im jeweiligen App-Store'],
            ['„IPTV Smarters Subscription / Abo“', 'In der Regel ein IPTV-Abo mit Sendern, das in Smarters eingetragen wird', 'Ein IPTV-Anbieter, nicht der App-Entwickler'],
            ['„IPTV Smarters Pro Live“', 'Der Bereich „Live TV“ in der App', 'Inhalte kommen aus Ihrem Abo'],
        ], 'Smarters: App, Premium und Abo') + '''
<p>Die offizielle Website des Entwicklers ist iptvsmarters.com. Dort gibt es die Downloads für Windows, Mac und Android sowie den App-Support. Der <strong>Kundenservice von IPTV Smarters</strong> hilft bei App-Fehlern, nicht bei Sendern oder Zugangsdaten. Für Fragen zu Ihrem Zugang ist Ihr IPTV-Anbieter zuständig – bei IPTV Kanal per E-Mail und WhatsApp. Auf Reddit und in Foren finden Sie zu „IPTV Smarters“ viele Tipps; achten Sie dort darauf, ob jemand über die App oder über einen Anbieter schreibt.</p>
<p>Smarters am Fernseher einrichten: <a href="/iptv-smarters-pro-smart-tv/">IPTV Smarters Pro auf Samsung, LG und Smart TV</a>.</p>'''),
    ],
    'iptv-kaufen': [
        ('angebote', 'IPTV Angebote, Deals und Preisvergleich', '''
<p>Rund um Black Friday und Jahreswechsel tauchen viele „IPTV Deals“, „IPTV Sale“ und „IPTV Promotions“ auf. Ein echter Preisvergleich gelingt nur, wenn Sie dieselbe Einheit vergleichen: <strong>Preis pro Monat und pro Gerät</strong>, bei gleicher Laufzeit. Bei IPTV Kanal sieht das so aus:</p>''' + table(['Paket (1 Gerät)', 'Preis', 'Pro Monat', 'Verlängerung'], [
            ['1 Monat', '9 €', '9,00 €', 'Keine automatische Verlängerung'],
            ['3 Monate', '29 €', '9,67 €', 'Keine automatische Verlängerung'],
            ['6 Monate', '39 €', '6,50 €', 'Keine automatische Verlängerung'],
            ['12 Monate (1 Jahr)', '49 €', '4,08 €', 'Keine automatische Verlängerung'],
        ], 'IPTV Kanal: Preis pro Monat') + checks(
            '<strong>IPTV Abo 12 Monate:</strong> Das Jahrespaket ist pro Monat am günstigsten. Ob Sie es als M3U-Link oder Xtream-Login nutzen, ist egal – beides ist enthalten („IPTV M3U 1 Jahr“ ist dasselbe Paket).',
            '<strong>Pakete und Pläne:</strong> „IPTV Packages“ oder „IPTV Plans“ unterscheiden sich bei uns nur in Laufzeit und Geräteanzahl, nicht im Senderumfang.',
            '<strong>IPTV Lines:</strong> Eine „Line“ ist ein Zugang mit einer bestimmten Zahl gleichzeitiger Verbindungen. Für zwei Fernseher brauchen Sie zwei Verbindungen.',
            '<strong>Vorsicht bei Dauer-Rabatten:</strong> Ein „-80 %“-Preis, der seit Monaten gilt, ist kein Angebot, sondern der normale Preis mit erfundenem Streichpreis.',
            '<strong>IPTV Shop mit Lifetime-Paket:</strong> Siehe <a href="/iptv-lifetime/">IPTV Lifetime</a> – einmalige Zahlung gegen dauerhafte Serverkosten geht selten gut.')
         + '<p>Alle 20 Paketpreise für 1 bis 5 Geräte stehen auf der <a href="/preise/">Preisseite</a>. Wie andere Dienste einzuordnen sind, zeigt die <a href="/iptv-anbieter-liste/">IPTV Anbieter Liste</a>.</p>'),
    ],
    'iptv-box': [
        ('wlan', 'IPTV Box mit WLAN oder LAN? Und was ist mit Ugoos AM7?', '''
<p>Fast jede IPTV Box hat WLAN („IPTV Box WiFi“), aber nicht jede WLAN-Verbindung reicht für 4K. Ein 4K-Stream braucht dauerhaft rund 25 Mbit/s; im 2,4-GHz-Band bricht das bei Wänden und Nachbarnetzen schnell ein. Faustregel: Box per LAN-Kabel an den Router, wenn möglich. Geht das nicht, achten Sie auf WLAN 5 (ac) oder WLAN 6 (ax) und nutzen Sie das 5-GHz-Band.</p>''' + table(['Verbindung', 'Für HD', 'Für 4K', 'Hinweis'], [
            ['LAN (100 Mbit/s)', 'Ja', 'Ja', 'Reicht für jeden IPTV-Stream'],
            ['LAN (Gigabit)', 'Ja', 'Ja', 'Vorteil vor allem bei großen Downloads'],
            ['WLAN 5 / WLAN 6, 5 GHz', 'Ja', 'Meist ja', 'Abstand zum Router entscheidend'],
            ['WLAN 2,4 GHz', 'Meist ja', 'Oft nein', 'Störanfällig in Mehrfamilienhäusern'],
        ], 'IPTV Box: LAN oder WLAN') + '''
<p>Nach Boxen wie der <strong>Ugoos AM7</strong> oder der <strong>Homatics Box Q</strong> wird oft gesucht, weil es zertifizierte Android-TV- bzw. Google-TV-Geräte mit Play Store sind: TiviMate, Smarters und Kodi lassen sich dort direkt installieren. Einen eigenen „IPTV Box Test“ machen Sie am besten mit Ihrem Zugang: zwei Abende lang Fußball und einen 4K-Sender laufen lassen. Eine Box bei Amazon zu kaufen ist dabei sicherer als ein No-Name-Gerät, weil Sie es innerhalb der Rückgabefrist zurückschicken können.</p>'''),
    ],
    'formuler-iptv': [
        ('aeltere-modelle', 'Ältere Formuler-Modelle: Z7, Z8, Z+ und Co.', '''
<p>Viele Suchanfragen betreffen Formuler-Boxen, die schon einige Jahre im Wohnzimmer stehen. Grundsätzlich funktionieren auch ältere Modelle mit IPTV, solange MyTVOnline startet und Ihr Login angenommen wird. Die Einordnung:</p>''' + table(['Modell', 'Generation', 'Für IPTV heute'], [
            ['Formuler Z+ und Z Neo', 'Frühe Android-Generation', 'Nur noch für einfache HD-Nutzung; neue Apps laufen oft nicht'],
            ['Formuler Z Nano', 'Kompaktes Einstiegsmodell', 'HD ja; für 4K nicht gedacht'],
            ['Formuler Z7 und Z7+', 'Mittlere Generation', 'Für HD brauchbar, kaum noch Updates'],
            ['Formuler Z8 und Z8 Pro', 'Mittlere Generation', 'HD und teils 4K; Leistung für große Listen knapp'],
            ['Formuler Z10 Pro 4K und Z10 Pro Max 4K', 'Vorgängergeneration', 'Für 4K und große Senderlisten weiterhin gut'],
            ['Formuler Z11 Pro und Z11 Pro Max', 'Aktuelle Generation', 'Empfehlung für Neukauf'],
        ], 'Formuler-Modelle nach Generation') + '''
<p>Wenn eine ältere Formuler-Box Ihre Senderliste nur langsam lädt, blenden Sie in MyTVOnline ungenutzte Gruppen aus und deaktivieren Sie VOD-Kategorien, die Sie nicht brauchen. Hilft das nicht, ist ein Wechsel auf eine aktuelle <a href="/iptv-box/">IPTV Box</a> sinnvoller als lange Fehlersuche.</p>'''),
    ],
    'was-ist-iptv': [
        ('begriffe', 'IPTV, IP TV, IP Television: die Begriffe auf einen Blick', table(['Begriff', 'Bedeutung'], [
            ['Internet Protocol Television', 'Die englische Langform von IPTV: Fernsehen, das per Internetprotokoll übertragen wird'],
            ['IP TV, IP Television, IPTV TV', 'Andere Schreibweisen für dasselbe'],
            ['IP televizija', 'IPTV auf Bosnisch, Kroatisch und Serbisch – siehe <a href="/iptv-balkan/">IPTV Balkan</a>'],
            ['Television and Internet', 'Kombi-Angebote der Netzbetreiber aus Internet und TV, etwa MagentaTV – siehe <a href="/iptv-telekom-vodafone/">Telekom &amp; Vodafone</a>'],
            ['IPTV Stream / IPTV Live', 'Ein einzelner Live-Sender, der als Datenstrom übertragen wird'],
            ['IPTV Provider / Internet Protocol TV Providers', 'Anbieter, die Sender per IPTV bereitstellen – siehe <a href="/iptv-anbieter/">IPTV Anbieter</a>'],
        ], 'IPTV-Begriffe') + '''
<p>Wer auf Englisch „What is Internet Protocol Television?“ fragt, bekommt dieselbe Antwort wie oben: Fernsehen, das nicht über Antenne, Kabel oder Satellit, sondern als Datenstrom über eine Internetverbindung kommt und mit einer App oder Box abgespielt wird.</p>'''),
    ],
}

EXTRA_FAQ = {
    'iptv-smarters-pro': [
        ('Gibt es ein IPTV Smarters Pro Abo?', 'Die App selbst verkauft keine Sender. Was als „IPTV Smarters Subscription“ angeboten wird, ist in der Regel das Abo eines IPTV-Anbieters, das Sie in Smarters eintragen. Optionale Zusatzfunktionen der App verkauft der Entwickler im jeweiligen App-Store.'),
        ('Was ist iptvsmarters.com?', 'Die offizielle Website des App-Entwicklers. Dort gibt es Downloads für Windows, Mac und Android sowie den App-Support. Sender und Zugangsdaten bekommen Sie dort nicht.'),
    ],
    'iptv-kaufen': [
        ('Gibt es IPTV Angebote zum Black Friday?', 'Unsere aktuellen Preise stehen immer vollständig auf der Preisseite: 9 € für einen Monat, 49 € für ein Jahr bei einem Gerät. Erfundene Streichpreise gibt es bei uns nicht.'),
        ('Was ist eine IPTV Line?', 'Eine IPTV Line ist ein Zugang mit einer festgelegten Anzahl gleichzeitiger Verbindungen. Für zwei Geräte, die gleichzeitig schauen, brauchen Sie zwei Verbindungen.'),
    ],
    'iptv-box': [
        ('Lohnt sich eine IPTV Box mit WLAN?', 'Ja, wenn WLAN 5 oder WLAN 6 mit 5 GHz zur Verfügung steht und der Router nicht weit entfernt ist. Für stabiles 4K ist ein LAN-Kabel die sicherere Wahl.'),
        ('Ist die Ugoos AM7 für IPTV geeignet?', 'Ja. Als zertifiziertes Android-TV-Gerät mit Play Store installieren Sie TiviMate, IPTV Smarters Pro oder Kodi direkt. Für die meisten Nutzer reicht auch eine günstigere Google-TV-Box.'),
    ],
    'formuler-iptv': [
        ('Funktioniert IPTV noch auf der Formuler Z7?', 'Für HD-Sender meist ja, solange MyTVOnline startet und Ihren Login annimmt. Updates gibt es kaum noch; für 4K und große Senderlisten ist die Z11-Serie besser.'),
    ],
    'was-ist-iptv': [
        ('Was bedeutet Internet Protocol Television auf Deutsch?', 'Wörtlich „Fernsehen über das Internetprotokoll“. Gemeint ist Fernsehen, das als Datenstrom über eine Internetverbindung kommt statt über Antenne, Kabel oder Satellit.'),
    ],
    'iptv-telekom-vodafone': [
        ('Ist MagentaTV IPTV?', 'Ja. MagentaTV der Telekom wird über die Internetleitung übertragen und ist damit IPTV, auch wenn es als Magenta IPTV oder Telekom IP TV gesucht wird. Gleiches gilt für Vodafone TV über Glasfaser oder DSL.'),
    ],
    'kodi-iptv': [
        ('Was ist der Unterschied zwischen Kodi und XBMC?', 'Keiner: Kodi hieß bis 2014 XBMC. Anleitungen für „Kodi XBMC IPTV“ beziehen sich auf dieselbe Software. Auch „Cody IPTV“ ist meist ein Tippfehler für Kodi.'),
        ('Wie schaue ich Live-TV in Kodi?', 'Mit dem Add-on PVR IPTV Simple Client: M3U-Link und EPG-Adresse eintragen, Kodi neu starten, dann erscheinen die Sender unter „TV“ mit Programmführer.'),
    ],
    'm3u-playlist': [
        ('Was ist eine „Mu3“ oder „M.m3u“ Liste?', 'Beides sind Tippfehler für M3U. Gemeint ist eine M3U- oder M3U8-Playlist (auf Spanisch und Portugiesisch „M3U lista“), die Sender-Adressen enthält.'),
        ('Was ist der Unterschied zwischen M3U-Liste und M3U8-Liste?', 'M3U8 ist eine M3U-Datei in UTF-8-Kodierung. Sie zeigt Umlaute und Sonderzeichen korrekt an und ist für deutsche und internationale Senderlisten die bessere Wahl.'),
    ],
    'iptv-receiver': [
        ('Welcher IPTV Receiver eignet sich für 4K?', 'Ein Enigma2-Receiver mit 4K-HEVC-Unterstützung, etwa aktuelle Modelle von Vu+, GigaBlue oder Dreambox, oder eine Android-TV-Box. Ältere HD-Receiver und Dreamlink T2 sind für 4K nicht ausgelegt.'),
    ],
    'iptv-einrichten': [
        ('Wo finde ich die IPTV Settings in meiner App?', 'Fast jede App hat ein Zahnrad-Symbol oder den Menüpunkt „Einstellungen“ bzw. „Settings“. Dort tragen Sie Zugangsdaten ein, wählen den Player und stellen die EPG-Zeitzone ein.'),
    ],
    'iptv-pc-mac': [
        ('Welcher IPTV Player für Windows ist am einfachsten?', 'VLC: installieren, „Medien → Netzwerkstream öffnen“ wählen und den M3U-Link einfügen. Wer Programmführer und Mediathek möchte, nimmt die Windows-Version von IPTV Smarters von der offiziellen Website.'),
    ],
    'ss-iptv': [
        ('Was ist ss-iptv.com?', 'Die offizielle Website der App SS IPTV. Dort laden Sie Ihre Playlist hoch und erhalten den Verbindungscode für den Fernseher. Sender enthält die Website nicht.'),
    ],
    'smart-iptv': [
        ('Wo kann ich Smart IPTV herunterladen?', 'Smart IPTV installieren Sie aus dem App-Store Ihres Fernsehers oder als Android-App von der offiziellen Website siptv.app. Dort finden Sie auch „My List“ zum Hochladen der Playlist.'),
    ],
    'smartone-iptv': [
        ('Ist „Smart OneIPTV“ dieselbe App wie SmartOne IPTV?', 'Ja. „Smart OneIPTV“ und „Smarte One IPTV“ sind häufige Schreibweisen für SmartOne IPTV. Mit Smart IPTV (SIPTV) ist die App nicht identisch.'),
    ],
    'gse-smart-iptv': [
        ('Was ist GSEIPTV?', 'Eine verkürzte Schreibweise für GSE Smart IPTV, einen Player für iPhone, iPad, Apple TV und Android. Die App enthält keine Sender.'),
    ],
    'xciptv': [
        ('Gibt es XCIPTV für Samsung oder LG?', 'Nein. XCIPTV ist eine Android-App für Fire TV, Android TV und Android-Handys. Auf Samsung und LG nutzen Sie andere Player wie SET IPTV oder Flix IPTV.'),
        ('Ist XCIPTV kostenlos?', 'Die App ist kostenlos erhältlich. Manche Anbieter verteilen eigene, vorkonfigurierte Versionen, die als „XCIPTV Pro“ oder ähnlich auftauchen. Laden Sie XCIPTV nur aus vertrauenswürdigen Quellen.'),
    ],
    'iptv-stream-player': [
        ('Ist „IPTV Streamplayer“ dieselbe App?', 'Ja, „IPTV Streamplayer“ ist eine häufige Schreibweise für IPTV Stream Player. Die App enthält keine Sender; Sie tragen die Zugangsdaten Ihres Abos ein.'),
    ],
    'iptv-pro-app': [
        ('Was ist mit „IPTVPro“ oder „IPTV App“ gemeint?', 'Meist die Apps „IPTV“ und „IPTV Pro“ von Alexander Sofronov für Android. Beide spielen M3U-Playlists ab und enthalten keine Sender.'),
    ],
    'iptv-stick': [
        ('Ist der Amazon Fire Stick ein IPTV Stick?', 'Ja, der Amazon Fire TV Stick ist der meistgenutzte IPTV Stick. Auf Modellen mit Fire OS installieren Sie IPTV Smarters Pro oder TiviMate; neuere Modelle mit Vega OS unterstützen keine APK-Installation.'),
    ],
    'iptv-server': [
        ('Was bedeutet „IPTV Servers“ in Angeboten?', 'Damit ist die Infrastruktur des Anbieters gemeint, die die Streams ausliefert. Mehrere Server-Standorte und Ersatzserver sorgen dafür, dass Sender bei Ausfällen weiterlaufen.'),
    ],
    'iptv-erfahrungen': [
        ('Wie erreiche ich den Kundenservice eines IPTV Anbieters?', 'Seriöse Anbieter nennen mindestens eine E-Mail-Adresse und antworten innerhalb eines Tages. Testen Sie den Support schon während des kostenlosen Tests mit einer Frage zur Einrichtung.'),
    ],
    'iptv-vod': [
        ('Kann ich discovery+ oder HBO in einer IPTV-App schauen?', 'Nein. discovery+, HBO Max und andere Streamingdienste laufen nur in ihren eigenen Apps. Die Apps lassen sich aber auf demselben Gerät wie Ihr IPTV-Player installieren.'),
        ('Was bedeutet „IPTV Series“?', 'Der Serienbereich einer IPTV-App, in dem Serien nach Staffeln und Folgen sortiert zum Abruf bereitstehen.'),
    ],
    'iptv-fussball': [
        ('Was ist mit „IPTV Soccer“ gemeint?', 'Die englische Suche nach Fußball per IPTV. Welche Sender in Deutschland Bundesliga, Champions League, Premier League und WM-Spiele zeigen, steht in den Tabellen oben.'),
    ],
    'iptv-albanisch': [
        ('Was ist IPTV Iliria?', 'Mit „IPTV Iliria“ suchen viele nach albanischen Programmen bzw. nach einem gleichnamigen Angebot. IPTV Kanal ist damit nicht verbunden; welche albanischen Sender Ihr Zugang enthält, zeigt der Test.'),
    ],
    'iptv-rumaenisch': [
        ('Was bedeutet „canale romanesti IPTV“?', 'Die Suche nach rumänischen Fernsehkanälen per IPTV, oft ohne Sonderzeichen geschrieben. Gemeint sind Sender wie TVR, Pro TV oder Antena 1.'),
    ],
    'iptv-balkan': [
        ('Was heißt „IPTV programa“?', '„Programa“ steht in mehreren Balkan-Sprachen für Programme bzw. Sender. Gemeint ist die Senderliste eines IPTV-Zugangs mit Programmen aus der Region.'),
    ],
    'mag-box-iptv': [
        ('Was ist ein IPTV Portal bei der MAG Box?', 'Die Portal-Adresse (Stalker-Portal) ist die Server-Adresse, die Sie in der MAG Box unter „Portale“ eintragen. Der Anbieter schaltet dafür die MAC-Adresse Ihrer Box frei.'),
    ],
    'sky-iptv': [
        ('Was kostet die Sky Q IPTV Box heute?', 'Die Sky Q IPTV Box wird nicht mehr neu vermarktet. Neue Internetkunden erhalten Sky Stream; aktuelle Preise und Pakete nennt Sky auf sky.de. Die UHD-Inhalte von Sky laufen dort ebenfalls.'),
    ],
}

# New pages appear in the related links of these existing guides (3+ inbound links each).
LINK_FROM = {
    'iptv-anbieter-liste': ['iptv-anbieter-vergleich', 'iptv-erfahrungen', 'iptv-anbieter', 'iptv-kaufen', 'iptv-reseller'],
    'iptv-smarters-pro-smart-tv': ['iptv-smarters-pro', 'iptv-samsung-tv', 'iptv-lg-tv', 'iptv-smart-tv', 'iptv-roku'],
    'tivimate-andere-geraete': ['tivimate', 'tivimate-premium', 'iptv-pc-mac', 'iptv-apple-tv-iphone', 'iptvx'],
    'iptv-georgisch': ['iptv-international', 'iptv-russisch', 'iptv-senderliste'],
}
