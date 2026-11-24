"""App / player pages (protected app keywords). Statements about third-party apps are kept general and verifiable;
prices of third-party apps are deliberately not quoted because they change."""
from .helpers import steps, checks, tip, table, proscons

PAGES = []

LOGIN_TIP = tip('Ihre Zugangsdaten von IPTV Kanal funktionieren in dieser App. Fragen Sie im <a href="/kostenlos-testen/">kostenlosen Test</a> direkt nach dem passenden Format (Xtream Codes oder M3U).', 'Hinweis')

# ---------------------------------------------------------------- Hub
PAGES.append(dict(
    slug='iptv-apps', parent='ratgeber', kind='hub', hub='apps',
    title='Beste IPTV Apps & Player 2026: Übersicht für jedes Gerät',
    description='Die besten IPTV Apps und Player 2026: IPTV Smarters Pro, TiviMate, Smart IPTV, SET IPTV, Flix IPTV, Kodi & VLC – welche App zu welchem Gerät passt.',
    eyebrow='IPTV APPS & PLAYER', h1='Beste IPTV Apps und Player',
    lead='Eine IPTV-App ist Ihre Fernbedienung für Senderliste, Programmführer und Mediathek. Hier finden Sie den besten IPTV Player für jedes Gerät – mit Anleitungen.',
    answer='Die beste IPTV App hängt vom Gerät ab: Auf Fire TV und Android-TV sind TiviMate und IPTV Smarters Pro erste Wahl, auf Samsung- und LG-Fernsehern Player wie Smart IPTV, SET IPTV oder Flix IPTV, auf iPhone und Apple TV Apps aus dem App Store und am PC VLC. Alle Apps sind leere Player – die Sender kommen aus Ihrem IPTV-Abo.',
    sections=[
        ('uebersicht', 'Welche IPTV App für welches Gerät?', table(['App', 'Geräte', 'Login', 'Besonderheit'], [
            ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'Android, Fire TV, iOS, Windows, Mac', 'Xtream, M3U', 'Einfacher Einstieg, viele Plattformen'],
            ['<a href="/tivimate/">TiviMate</a>', 'Android TV, Fire TV, Google TV', 'Xtream, M3U', 'Bester EPG, Aufnahme mit Premium'],
            ['<a href="/smart-iptv/">Smart IPTV</a>', 'Samsung, LG, Android', 'M3U per MAC', 'Einmalige Aktivierung pro Gerät'],
            ['<a href="/ss-iptv/">SS IPTV</a>', 'Samsung, LG', 'M3U per Code', 'Kostenlos mit Werbung'],
            ['<a href="/set-iptv/">SET IPTV</a>', 'Samsung, LG, Android', 'M3U per MAC', 'Playlist über Website'],
            ['<a href="/flix-iptv/">Flix IPTV</a>', 'Samsung, LG, Android, Fire TV', 'M3U per MAC', 'Moderne Oberfläche'],
            ['<a href="/smartone-iptv/">SmartOne IPTV</a>', 'Samsung, LG, Android', 'M3U per MAC', 'Leichtgewichtig'],
            ['<a href="/xtream-codes-iptv/">XCIPTV</a>', 'Android, Fire TV', 'Xtream', 'Für Xtream-Codes-Logins'],
            ['<a href="/kodi-iptv/">Kodi</a>', 'Alle außer Smart-TV', 'M3U + EPG', 'Mediacenter mit Add-ons'],
            ['<a href="/iptv-pc-mac/">VLC</a>', 'Windows, Mac, Linux, Handy', 'M3U', 'Universell, ohne EPG-Raster'],
            ['<a href="/mag-box-iptv/">STBEmu</a>', 'Android', 'MAG-Portal', 'Emuliert eine MAG-Box'],
        ], 'IPTV Apps im Überblick')),
        ('auswahl', 'So wählen Sie den besten IPTV Player', checks(
            '<strong>Gerät zuerst:</strong> Nicht jede App gibt es für jedes System. TiviMate etwa läuft nur auf Android-TV-Geräten.',
            '<strong>Login-Typ:</strong> Xtream-Codes-Apps laden Mediathek und EPG automatisch; M3U-Apps brauchen manchmal eine separate EPG-Adresse.',
            '<strong>Programmführer:</strong> Wer viel linear schaut, profitiert von einem guten EPG-Raster.',
            '<strong>Kosten:</strong> Viele Player sind nach einer Testphase einmalig oder jährlich kostenpflichtig. Diese Gebühr geht an den App-Entwickler, nicht an den IPTV-Anbieter.')),
        ('weitere', 'Weitere bekannte IPTV Apps', table(['App', 'Geräte', 'Hinweis'], [
            ['IBO Player', 'Samsung, LG, Android, Fire TV', 'Verknüpfung per MAC-Adresse, Aktivierung nach Testphase'],
            ['Duplecast', 'Samsung, LG, Android', 'Playlist über die Website verknüpfen'],
            ['iMPlayer', 'Android, Fire TV, Smart-TVs', 'Moderne Oberfläche, Xtream und M3U'],
            ['OTT Navigator', 'Android, Google TV, Fire TV', 'Sehr anpassbar, Premium-Funktionen optional'],
            ['GSE Smart IPTV', 'iPhone, iPad, Apple TV, Android', 'Klassiker für Apple-Geräte'],
            ['IPTVX', 'iPhone, iPad, Apple TV, Mac', 'Elegante App für Apple – siehe <a href="/iptv-apple-tv-iphone/">Apple-Ratgeber</a>'],
            ['IPTV Pro / IPTV Stream Player', 'Android', 'Einfache M3U-Player für Handy und Tablet'],
            ['My IPTV Player', 'Windows', 'Desktop-Player für M3U – siehe <a href="/iptv-pc-mac/">IPTV am PC</a>'],
            ['<a href="/cloudstream/">CloudStream</a>', 'Android, Fire TV', 'Keine eigenen Inhalte, Erweiterungen von Drittanbietern – Risiken beachten'],
        ], 'Weitere IPTV Apps') + '''
<p>Sie funktionieren nach demselben Prinzip: App installieren, Gerät per MAC-Adresse oder Code verknüpfen, Playlist oder Xtream-Login eintragen. Für Fire-TV-Geräte wird zur Installation von Apps außerhalb des Amazon Appstores häufig die App <strong>Downloader</strong> verwendet – siehe <a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro auf dem Fire TV Stick</a>.</p>'''),
        ('kostenlos', 'Bester IPTV Player für Fire TV Stick – kostenlos und auf Deutsch?', '''
<p>Eine häufige Suche lautet „bester IPTV Player für Fire TV Stick kostenlos deutsch“. Die ehrliche Antwort: <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> ist kostenlos und auf Deutsch nutzbar, <a href="/tivimate/">TiviMate</a> ist in der Grundversion kostenlos und mit Premium deutlich komfortabler. Beide sind empfehlenswert – wichtiger als die App ist ein stabiler Zugang.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Welche ist die beste IPTV App?', 'Für Fire TV und Android-TV sind TiviMate und IPTV Smarters Pro am beliebtesten, für Samsung und LG Fernseher Smart IPTV, SET IPTV und Flix IPTV, am PC VLC. Die beste App ist die, die auf Ihrem Gerät stabil läuft und Ihren Login-Typ unterstützt.'),
        ('Sind IPTV Apps kostenlos?', 'Einige sind kostenlos (IPTV Smarters Pro, SS IPTV, VLC, Kodi). Andere bieten eine Testphase und verlangen danach eine einmalige oder jährliche Aktivierungsgebühr an den Entwickler.'),
        ('Enthalten IPTV Apps Sender?', 'Nein. IPTV-Apps sind reine Abspielprogramme. Sender, Filme und Serien kommen aus Ihrem IPTV-Abo, dessen Zugangsdaten Sie in der App eintragen.'),
        ('Welche IPTV App gibt es für Android?', 'Auf Android-Smartphones und Android-TV laufen IPTV Smarters Pro, TiviMate (nur TV-Geräte), XCIPTV, OTT Navigator, Kodi, VLC und STBEmu.'),
    ],
    related=['iptv-geraete', 'm3u-playlist', 'iptv-fire-tv-stick', 'iptv-smart-tv', 'iptv-android', 'iptv-kaufen'],
    card=('IPTV Apps & Player', 'Die beste App für jedes Gerät – mit Anleitungen.'),
))

# ---------------------------------------------------------------- Smarters
PAGES.append(dict(
    slug='iptv-smarters-pro', parent='apps', kind='guide',
    title='IPTV Smarters Pro: Download, Einrichtung & Tipps (Deutsch)',
    description='IPTV Smarters Pro einrichten auf Fire TV Stick, Samsung TV, Android, iPhone und Windows: Download, Xtream-Login, M3U, Einstellungen und Fehlerlösungen.',
    eyebrow='APP-ANLEITUNG', h1='IPTV Smarters Pro: Anleitung auf Deutsch',
    lead='IPTV Smarters Pro ist einer der meistgenutzten IPTV Player. Wir zeigen Download und Einrichtung für jedes Gerät, die besten Einstellungen und was bei Fehlern hilft.',
    answer='IPTV Smarters Pro ist ein kostenloser IPTV Player für Android, Fire TV, iPhone/iPad, Windows und Mac. Nach der Installation wählen Sie „Login mit Xtream Codes API“, tragen Name, Benutzername, Passwort und Server-URL Ihres IPTV-Abos ein und laden Live-TV, Filme, Serien und EPG automatisch. Die App selbst enthält keine Sender.',
    sections=[
        ('was', 'Was ist IPTV Smarters Pro?', '''
<p>IPTV Smarters Pro (oft kurz „Smarters“ oder „Smarters Pro“ genannt) ist ein Abspielprogramm für IPTV-Zugänge. Es unterstützt Xtream-Codes-Logins und <a href="/m3u-playlist/">M3U-Playlists</a>, zeigt Live-TV mit Programmführer, eine Mediathek für Filme und Serien sowie Catch-Up. Auf iPhone und iPad heißt die App „Smarters Player Lite“ – oft als „IPTV Smarters Lite“ gesucht.</p>
''' + proscons(['Kostenlos und auf Deutsch', 'Für fast alle Plattformen', 'Xtream-Login lädt alles automatisch', 'Mehrere Nutzerprofile'],
               ['EPG-Raster schlichter als bei TiviMate', 'Nicht überall im offiziellen App-Store', 'Keine eigenen Sender – nur mit Abo nutzbar'])),
        ('download', 'IPTV Smarters Pro Download nach Gerät', table(['Gerät', 'Bezugsquelle'], [
            ['Android-Smartphone / Android-TV', 'Google Play Store oder APK von der offiziellen Website'],
            ['<a href="/iptv-fire-tv-stick/">Fire TV Stick</a>', 'Über die App Downloader mit der APK-Adresse der offiziellen Website (nur Geräte mit Fire OS) – <a href="/iptv-smarters-pro-firestick/">Anleitung für Fire TV</a>'],
            ['Chromecast mit Google TV / Google TV Streamer', 'Google Play Store, alternativ vom Handy casten – siehe <a href="/iptv-stick/">IPTV Stick</a>'],
            ['<a href="/iptv-apple-tv-iphone/">iPhone, iPad, Apple TV</a>', 'App Store („Smarters Player Lite“)'],
            ['<a href="/iptv-samsung-tv/">Samsung</a> / <a href="/iptv-lg-tv/">LG</a>', 'Je nach Modell und Region im App-Store des Fernsehers'],
            ['<a href="/iptv-pc-mac/">Windows &amp; Mac</a>', 'Desktop-Version von der offiziellen Website'],
        ], 'Bezugsquellen für IPTV Smarters Pro') + tip('Laden Sie APK-Dateien ausschließlich von der offiziellen Smarters-Website. Kopien von Drittseiten können Schadsoftware enthalten.')),
        ('einrichten', 'IPTV Smarters Pro einrichten: Schritt für Schritt', steps(
            'App öffnen, Nutzungsbedingungen akzeptieren und Gerätetyp (Mobil oder TV) wählen.',
            '<b>„Login mit Xtream Codes API“</b> antippen.',
            'Beliebigen Namen eingeben, z. B. „IPTV Kanal“.',
            'Benutzername, Passwort und Server-URL aus Ihrer Zugangs-E-Mail exakt übernehmen – inklusive <code>http://</code> und Port.',
            '<b>„Nutzer hinzufügen“</b> wählen. Die App lädt Live-TV, Filme, Serien und EPG.',
            'Unter „Live-TV“ eine Kategorie öffnen und lostschauen.') + '''
<p>Mit M3U-Link wählen Sie in Schritt 2 stattdessen „M3U-URL laden“. Xtream Codes ist komfortabler, weil Mediathek und Programmführer automatisch kommen (<a href="/xtream-codes-iptv/">Unterschiede erklärt</a>).</p>'''.replace('lostschauen', 'losschauen')),
        ('einstellungen', 'Empfohlene Einstellungen', checks(
            '<strong>Player:</strong> unter Einstellungen → Player-Auswahl den internen Player mit Hardware-Decoder nutzen; bei Problemen VLC-Player testen.',
            '<strong>EPG:</strong> unter Einstellungen → EPG die Zeitzone auf Europa/Berlin setzen und EPG einmal neu laden.',
            '<strong>Puffer:</strong> bei Rucklern die Puffergröße auf „mittel“ oder „groß“ stellen.',
            '<strong>Kindersicherung:</strong> Kategorien per PIN sperren.')),
        ('fehler', 'IPTV Smarters Pro funktioniert nicht? Lösungen', table(['Problem', 'Lösung'], [
            ['„Ungültige Zugangsdaten“', 'Server-URL mit http:// und Port prüfen, keine Leerzeichen am Ende'],
            ['Sender laden nicht', 'Anderen Player in den Einstellungen wählen, App-Cache leeren'],
            ['Programmführer leer', 'EPG unter Einstellungen neu laden, Zeitzone prüfen'],
            ['Ruckeln', 'LAN statt WLAN, Puffer erhöhen, siehe <a href="/iptv-4k/">4K-Tipps</a>'],
            ['App startet nicht auf Fire TV', 'Prüfen, ob Ihr Modell Vega OS nutzt (keine APK-Installation möglich)'],
        ], 'Fehlerbehebung IPTV Smarters Pro') + '''
<p>Wichtig: Der Kundendienst von IPTV Smarters betreut nur die App, nicht Ihre Sender. Bei Fragen zum Zugang hilft Ihr IPTV-Anbieter – bei IPTV Kanal per E-Mail und WhatsApp.</p>'''),
        ('alternativen', 'Alternativen zu IPTV Smarters Pro', '''
<p>Wer mehr Komfort beim Programmführer möchte, wechselt auf Android-TV-Geräten oft zu <a href="/tivimate/">TiviMate</a>. Auf Samsung und LG sind <a href="/flix-iptv/">Flix IPTV</a> und <a href="/set-iptv/">SET IPTV</a> beliebt. Alle Optionen: <a href="/iptv-apps/">IPTV Apps im Vergleich</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Ist IPTV Smarters Pro kostenlos?', 'Ja, die App ist kostenlos. Sie enthält aber keine Sender; Sie benötigen zusätzlich ein IPTV-Abo mit Zugangsdaten.'),
        ('Wie installiere ich IPTV Smarters Pro auf dem Fire TV Stick?', 'Auf Fire-OS-Geräten installieren Sie die App Downloader aus dem Amazon Appstore, erlauben unbekannte Quellen und laden die APK von der offiziellen Smarters-Website. Neuere Modelle mit Vega OS unterstützen keine APK-Installation.'),
        ('Gibt es IPTV Smarters Pro für Samsung TV?', 'Je nach Modell und Region ist eine Smarters-App im Samsung-Store verfügbar. Alternativ nutzen Sie Player wie Smart IPTV, SET IPTV oder Flix IPTV oder einen Fire TV Stick am Fernseher.'),
        ('Kann ich IPTV Smarters Pro auf Windows nutzen?', 'Ja, es gibt eine Desktop-Version für Windows und Mac auf der offiziellen Website. Alternativ funktioniert VLC mit einem M3U-Link.'),
        ('Was ist der Unterschied zwischen Smarters Pro und Smarters Lite?', 'Smarters Player Lite ist die Version für iPhone, iPad und Apple TV im App Store. Funktionen und Login-Möglichkeiten sind sehr ähnlich.'),
        ('Wer hilft, wenn IPTV Smarters Pro nicht funktioniert?', 'Bei App-Fehlern helfen die Tipps oben. Bei Fragen zu Zugangsdaten und Sendern hilft Ihr IPTV-Anbieter; IPTV Kanal erreichen Sie per E-Mail und WhatsApp.'),
    ],
    related=['iptv-smarters-pro-firestick', 'tivimate', 'iptv-fire-tv-stick', 'iptv-samsung-tv', 'xtream-codes-iptv', 'iptv-apps'],
    card=('IPTV Smarters Pro', 'Download und Einrichtung auf Fire TV, Android, iPhone und PC.'),
))

# ---------------------------------------------------------------- TiviMate
PAGES.append(dict(
    slug='tivimate', parent='apps', kind='guide',
    title='TiviMate: Einrichtung, Premium & Tipps für Fire TV (Deutsch)',
    description='TiviMate IPTV Player auf Fire TV Stick und Android TV einrichten: Playlist hinzufügen, TiviMate Premium freischalten, EPG, Aufnahme und Lösungen bei Problemen.',
    eyebrow='APP-ANLEITUNG', h1='TiviMate: der IPTV Player für Fire TV &amp; Android TV',
    lead='TiviMate gilt als komfortabelster IPTV Player für den Fernseher. Wir zeigen Installation, Playlist, Premium-Freischaltung und die Einstellungen, die den Unterschied machen.',
    answer='TiviMate ist ein IPTV Player für Android TV, Google TV und Fire TV. Sie installieren die App, wählen „Playlist hinzufügen“, tragen Ihren Xtream-Codes-Login oder M3U-Link ein und erhalten einen übersichtlichen Programmführer. TiviMate Premium schaltet Aufnahmen, mehrere Playlists und Favoriten frei und wird über die TiviMate-Companion-App gekauft.',
    sections=[
        ('geraete', 'Auf welchen Geräten läuft TiviMate?', table(['Gerät', 'TiviMate verfügbar?'], [
            ['<a href="/iptv-fire-tv-stick/">Fire TV Stick / Fire TV Cube</a> (Fire OS)', 'Ja'],
            ['Fire-TV-Modelle mit Vega OS', 'Nein – keine Android-Apps'],
            ['<a href="/iptv-box/">Android-TV-Boxen</a>, Nvidia Shield, Google TV Streamer', 'Ja'],
            ['Smart-TVs mit Google TV (Sony, Philips, TCL u. a.)', 'Ja'],
            ['<a href="/iptv-samsung-tv/">Samsung (Tizen)</a> und <a href="/iptv-lg-tv/">LG (webOS)</a>', 'Nein'],
            ['<a href="/iptv-apple-tv-iphone/">Apple TV, iPhone</a>', 'Nein'],
            ['<a href="/iptv-pc-mac/">Windows / Mac</a>', 'Nein (nur per Android-Emulator)'],
        ], 'TiviMate Geräteunterstützung') + '''
<p>Wer TiviMate auf Samsung, LG oder Apple TV sucht, nutzt am einfachsten einen Fire TV Stick oder Google TV Streamer am HDMI-Anschluss.</p>'''),
        ('einrichten', 'TiviMate einrichten: Schritt für Schritt', steps(
            'TiviMate aus dem Google Play Store installieren; auf Fire TV über den Amazon Appstore, falls gelistet, sonst per Downloader.',
            'App öffnen und <b>„Playlist hinzufügen“</b> wählen.',
            '<b>„Xtream Codes“</b> wählen und Server-URL, Benutzername und Passwort eingeben – oder „M3U-Playlist“ mit Link.',
            'Playlist benennen und Sender, Filme und Serien laden lassen.',
            'EPG-Quelle prüfen: Bei Xtream Codes kommt sie automatisch, bei M3U ggf. eine XMLTV-Adresse ergänzen.',
            'Fertig – mit der Taste nach links öffnen Sie das Menü, mit OK den Programmführer.')),
        ('premium', 'TiviMate Premium: Kosten und Freischaltung', '''
<p>Die Grundversion ist kostenlos. <strong>TiviMate Premium</strong> schaltet unter anderem Aufnahmen, mehrere Playlists, Favoritenverwaltung, Catch-Up-Komfort und Anpassungen der Oberfläche frei. Gekauft wird Premium in der App <strong>TiviMate Companion</strong> auf einem Android-Smartphone; anschließend melden Sie sich mit dem Companion-Konto in TiviMate an. Ein Premium-Konto lässt sich auf mehreren eigenen Geräten nutzen. Die aktuellen Preise für Jahres- und Einmal-Lizenz zeigt die Companion-App. Kauf, Geräteanzahl und Freischaltung erklärt unser Ratgeber <a href="/tivimate-premium/">TiviMate Premium</a>.</p>
''' + tip('„TiviMate Premium APK“ von Drittseiten ist eine geknackte Version. Sie verstößt gegen die Lizenz, bekommt keine Updates und kann Schadcode enthalten. Die offizielle Lizenz kostet nur wenige Euro im Jahr.', 'Achtung')),
        ('einstellungen', 'Die besten TiviMate-Einstellungen', checks(
            '<strong>Wiedergabe → Decoder:</strong> Hardware; bei Bildfehlern Software testen.',
            '<strong>Wiedergabe → AFR (Bildwiederholrate anpassen):</strong> aktivieren, damit Sport flüssiger läuft.',
            '<strong>EPG → Aktualisierung:</strong> beim Start und alle 12 Stunden.',
            '<strong>Playlist → Gruppen:</strong> nicht benötigte Länderkategorien ausblenden – die Senderliste wird übersichtlich.',
            '<strong>Allgemein → Beim Start:</strong> letzten Sender öffnen.')),
        ('probleme', 'Häufige TiviMate-Probleme', table(['Problem', 'Lösung'], [
            ['Kein EPG', 'Playlist → EPG-Quellen → aktualisieren; Zeitverschiebung prüfen'],
            ['„Playlist konnte nicht geladen werden“', 'Server-URL und Port prüfen, auf Fire TV VPN/DNS-Filter testen'],
            ['Ruckeln bei 4K', 'LAN-Kabel nutzen, Puffer erhöhen, siehe <a href="/iptv-4k/">IPTV in 4K</a>'],
            ['Premium nicht aktiv', 'In TiviMate unter Einstellungen → Konto mit Companion-Daten anmelden'],
        ], 'TiviMate Problemlösungen')),
        ('alternativen', 'TiviMate oder IPTV Smarters?', '''
<p>TiviMate punktet mit Programmführer und Aufnahme, <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> mit Plattformvielfalt und Kostenfreiheit. Viele nutzen beide: Smarters auf dem Handy, TiviMate am Fernseher. Mehr Apps im <a href="/iptv-apps/">IPTV-App-Vergleich</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Was kostet TiviMate Premium?', 'TiviMate Premium wird als Jahresabo oder Einmal-Lizenz in der TiviMate-Companion-App verkauft. Die aktuellen Preise zeigt die App; sie liegen im Bereich weniger Euro pro Jahr.'),
        ('Gibt es TiviMate für Samsung TV oder Apple TV?', 'Nein. TiviMate läuft nur auf Android-TV-Systemen wie Fire TV (Fire OS), Google TV und Android-TV-Boxen. Für Samsung, LG oder Apple TV nehmen Sie einen Fire TV Stick oder eine andere App.'),
        ('Funktioniert TiviMate auf dem PC?', 'Nicht direkt. Es gibt keine Windows- oder Mac-Version; nur über einen Android-Emulator. Am PC ist VLC oder IPTV Smarters die einfachere Wahl.'),
        ('Wie bekomme ich TiviMate auf den Fire TV Stick?', 'Über den Amazon Appstore, wenn verfügbar, oder mit der App Downloader und der offiziellen Quelle. Modelle mit Vega OS unterstützen TiviMate nicht.'),
        ('Ist TiviMate ein IPTV Anbieter?', 'Nein. TiviMate ist nur ein Player und enthält keine Sender. Die Inhalte kommen aus Ihrem IPTV-Abo.'),
    ],
    related=['tivimate-premium', 'iptv-smarters-pro', 'iptv-fire-tv-stick', 'iptv-box', 'iptv-4k', 'iptv-apps'],
    card=('TiviMate', 'Einrichtung, Premium und beste Einstellungen für Fire TV und Android TV.'),
))

# ---------------------------------------------------------------- Smart IPTV (SIPTV)
PAGES.append(dict(
    slug='smart-iptv', parent='apps', kind='guide',
    title='Smart IPTV (SIPTV): My List hochladen & aktivieren',
    description='Smart IPTV (SIPTV) auf Samsung & LG Smart TV: App installieren, MAC-Adresse finden, Playlist über „My List“ hochladen, aktivieren und typische Fehler beheben.',
    eyebrow='APP-ANLEITUNG', h1='Smart IPTV (SIPTV): Anleitung für Samsung &amp; LG',
    lead='Smart IPTV – kurz SIPTV – ist einer der bekanntesten IPTV Player für Smart-TVs. Die Playlist wird nicht in der App, sondern auf der Website des Entwicklers hochgeladen.',
    answer='Smart IPTV (SIPTV) ist ein IPTV Player für Samsung, LG und Android. Nach dem Start zeigt die App die MAC-Adresse Ihres Fernsehers. Auf der „My List“-Seite des Entwicklers geben Sie diese MAC-Adresse und Ihren M3U-Link ein; nach einem Neustart der App erscheinen Ihre Sender. Nach der Testphase ist eine einmalige Aktivierung pro Gerät fällig.',
    sections=[
        ('installieren', 'Smart IPTV installieren', '''
<p>Auf LG-Fernsehern finden Sie Smart IPTV im LG Content Store. Auf Samsung-Modellen ist die App nicht in jedem Store und auf jedem Baujahr gelistet; ältere Geräte lassen sich teilweise per USB installieren, was aber umständlich ist. Für Android-Geräte gibt es eine APK auf der Entwickler-Website.</p>
''' + tip('Findet Ihr Samsung-TV die App nicht, ist <a href="/set-iptv/">SET IPTV</a>, <a href="/flix-iptv/">Flix IPTV</a> oder ein <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> meist schneller eingerichtet.')),
        ('my-list', 'Smart IPTV My List: Playlist hochladen', steps(
            'Smart IPTV am Fernseher öffnen und die angezeigte <b>MAC-Adresse</b> notieren.',
            'Am Handy oder PC die „My List“-Seite auf der offiziellen Smart-IPTV-Website öffnen.',
            'MAC-Adresse eintragen und Ihren <a href="/m3u-playlist/">M3U-Link</a> in das URL-Feld einfügen.',
            'Bei Bedarf „Save online“ bzw. Speichern aktivieren und hochladen.',
            'App am Fernseher komplett schließen und neu öffnen – die Senderliste erscheint.')),
        ('aktivierung', 'Smart IPTV aktivieren und kaufen', '''
<p>Smart IPTV bietet eine kostenlose Testphase. Danach verlangt der Entwickler eine <strong>einmalige Aktivierungsgebühr pro Gerät</strong>, die über die Website mit der MAC-Adresse bezahlt wird. Den aktuellen Preis nennt die Entwickler-Website. Diese Gebühr gilt nur für die App; Ihr IPTV-Abo mit den Sendern ist davon getrennt.</p>'''),
        ('probleme', 'Typische Smart-IPTV-Fehler', table(['Meldung / Problem', 'Lösung'], [
            ['Keine Sender nach Upload', 'App vollständig beenden und neu starten, MAC-Adresse vergleichen'],
            ['„Playlist not found“', 'Link prüfen, ob er im Browser eine Datei lädt'],
            ['Kein Programmführer', 'Smart IPTV nutzt EPG nur bei passender tvg-id in der Playlist'],
            ['Ton fehlt', 'In den App-Einstellungen anderen Player-Modus wählen'],
        ], 'Smart IPTV Fehlerbehebung')),
        ('fernseher', 'Smart IPTV nach Fernsehermarke', '''
<p>Ausführliche Anleitungen pro Marke: <a href="/iptv-samsung-tv/">IPTV auf Samsung TV</a>, <a href="/iptv-lg-tv/">IPTV auf LG TV</a> und für Hisense, Philips und Sony in der Übersicht <a href="/iptv-smart-tv/">IPTV auf dem Smart TV</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Was ist SIPTV?', 'SIPTV ist die Kurzform von Smart IPTV, einem IPTV Player für Samsung, LG und Android. Die Playlist wird über die My-List-Seite des Entwicklers mit der MAC-Adresse des Fernsehers verknüpft.'),
        ('Ist Smart IPTV kostenlos?', 'Nur in der Testphase. Danach ist eine einmalige Aktivierungsgebühr pro Gerät fällig, die direkt an den App-Entwickler geht.'),
        ('Wo finde ich die MAC-Adresse für Smart IPTV?', 'Die App zeigt die MAC-Adresse beim Start auf dem Bildschirm an. Sie besteht aus sechs Zeichenpaaren, zum Beispiel 00:1a:2b:3c:4d:5e.'),
        ('Warum zeigt Smart IPTV nach dem Upload keine Sender?', 'Meist muss die App vollständig neu gestartet werden. Prüfen Sie außerdem, ob die eingegebene MAC-Adresse mit der in der App übereinstimmt und der M3U-Link funktioniert.'),
        ('Kann ich bei Smart IPTV Xtream Codes nutzen?', 'Smart IPTV arbeitet mit M3U-Links. Aus Xtream-Zugangsdaten lässt sich ein M3U-Link erstellen; IPTV Kanal sendet Ihnen auf Wunsch direkt den passenden Link.'),
    ],
    related=['ss-iptv', 'set-iptv', 'flix-iptv', 'iptv-samsung-tv', 'iptv-lg-tv', 'm3u-playlist'],
    card=('Smart IPTV (SIPTV)', 'My List hochladen und aktivieren auf Samsung und LG.'),
))

# ---------------------------------------------------------------- SS IPTV
PAGES.append(dict(
    slug='ss-iptv', parent='apps', kind='guide',
    title='SS IPTV: Playlist laden mit Verbindungscode (Anleitung)',
    description='SS IPTV (Simple Smart IPTV) auf LG und Samsung einrichten: Verbindungscode erzeugen, M3U-Liste über den Playlist-Editor laden und häufige Probleme lösen.',
    eyebrow='APP-ANLEITUNG', h1='SS IPTV: Anleitung für LG &amp; Samsung',
    lead='SS IPTV (Simple Smart IPTV) ist ein kostenloser IPTV Player für Smart-TVs. Externe Playlists verbinden Sie über einen Code, den die App am Fernseher erzeugt.',
    answer='SS IPTV ist ein kostenloser, werbefinanzierter IPTV Player für LG- und Samsung-Fernseher. In den App-Einstellungen erzeugen Sie unter „Allgemein“ einen Verbindungscode, geben ihn im Playlist-Editor auf der SS-IPTV-Website ein und laden dort Ihren M3U-Link hoch. Alternativ fügen Sie den Link direkt in der App als externe Playlist hinzu.',
    sections=[
        ('was', 'Was ist SS IPTV?', '''
<p>SS IPTV gehört zu den ältesten IPTV-Apps für Smart-TVs. Sie ist kostenlos, finanziert sich über Werbung und unterstützt <a href="/m3u-playlist/">M3U- und M3U8-Listen</a>. Besonders verbreitet ist sie auf LG-Fernsehern mit webOS, sie ist aber auch für Samsung und Android erhältlich.</p>
''' + proscons(['Kostenlos', 'Einfache Verknüpfung per Code', 'Läuft auch auf älteren Modellen'],
               ['Werbeeinblendungen', 'Weniger Komfort beim EPG', 'Keine Xtream-Codes-Anmeldung'])),
        ('code', 'SS IPTV Playlist per Verbindungscode laden', steps(
            'SS IPTV am Fernseher öffnen und das <b>Zahnrad (Einstellungen)</b> wählen.',
            'Unter <b>„Allgemein“</b> auf „Code erhalten“ klicken. Der Code ist 24 Stunden gültig.',
            'Am PC oder Handy den Playlist-Editor auf der offiziellen SS-IPTV-Website öffnen und den Code eingeben.',
            'Ihren M3U-Link als externe Playlist hinzufügen und speichern.',
            'App am Fernseher neu laden – die Playlist erscheint als eigene Kachel.')),
        ('direkt', 'Alternative: Link direkt in der App', '''
<p>In den Einstellungen unter „Inhalte → Extern“ können Sie eine Playlist auch direkt per Fernbedienung hinzufügen. Das Tippen langer Links ist allerdings mühsam – der Weg über den Verbindungscode ist schneller.</p>'''),
        ('probleme', 'SS IPTV funktioniert nicht?', checks(
            'Code abgelaufen: einen neuen Code erzeugen.',
            'Playlist leer: Link im Browser testen und auf Tippfehler prüfen.',
            'Bild hängt: in den Einstellungen den Player wechseln oder auf <a href="/iptv-lg-tv/">LG</a> die App neu installieren.',
            'Mehr Komfort gewünscht: <a href="/flix-iptv/">Flix IPTV</a> oder <a href="/set-iptv/">SET IPTV</a> bieten ein moderneres EPG.') + LOGIN_TIP),
    ],
    faq=[
        ('Ist SS IPTV kostenlos?', 'Ja. SS IPTV ist kostenlos und finanziert sich über Werbung. Für die Sender benötigen Sie ein IPTV-Abo mit M3U-Link.'),
        ('Wie lange ist der SS-IPTV-Code gültig?', 'Der Verbindungscode aus den Einstellungen ist 24 Stunden gültig. Danach erzeugen Sie einfach einen neuen.'),
        ('Unterstützt SS IPTV Xtream Codes?', 'Nein, SS IPTV arbeitet mit M3U- und M3U8-Links. IPTV Kanal stellt Ihnen dafür einen passenden M3U-Link bereit.'),
        ('Gibt es SS IPTV für Android?', 'Ja, SS IPTV ist auch für Android erhältlich. Auf Android-TV-Geräten bieten TiviMate oder IPTV Smarters jedoch mehr Komfort.'),
    ],
    related=['smart-iptv', 'iptv-lg-tv', 'iptv-samsung-tv', 'm3u-playlist', 'set-iptv', 'iptv-apps'],
    card=('SS IPTV', 'Playlist mit Verbindungscode laden – kostenlos für LG und Samsung.'),
))

# ---------------------------------------------------------------- SET IPTV
PAGES.append(dict(
    slug='set-iptv', parent='apps', kind='guide',
    title='SET IPTV: Playlist hochladen & aktivieren (Anleitung)',
    description='SET IPTV auf Samsung, LG und Android einrichten: MAC-Adresse finden, M3U-Playlist über die Website hochladen, EPG nutzen und Aktivierung verstehen.',
    eyebrow='APP-ANLEITUNG', h1='SET IPTV: Einrichtung Schritt für Schritt',
    lead='SET IPTV ist ein Player für Smart-TVs, bei dem Sie die Playlist bequem am Computer hochladen. So richten Sie die App in wenigen Minuten ein.',
    answer='SET IPTV ist ein IPTV Player für Samsung, LG und Android. Die App zeigt beim Start eine MAC-Adresse. Auf der Upload-Seite der offiziellen SET-IPTV-Website tragen Sie diese MAC-Adresse und Ihren M3U-Link ein. Nach dem Neustart der App sind Sender und EPG da. Nach der Testphase wird die App per einmaliger Gebühr aktiviert.',
    sections=[
        ('was', 'Was ist SET IPTV?', '''
<p>SET IPTV ist eine Abspiel-App, die sich besonders auf <a href="/iptv-samsung-tv/">Samsung</a>- und <a href="/iptv-lg-tv/">LG</a>-Fernsehern bewährt hat. Sie zeigt eine klassische Senderliste mit Programmführer und unterstützt Filme und Serien aus M3U-Listen. Die Verwaltung erfolgt über die Website des Entwicklers.</p>'''),
        ('einrichten', 'SET IPTV einrichten', steps(
            'SET IPTV im App-Store des Fernsehers suchen und installieren.',
            'App öffnen und die <b>MAC-Adresse</b> notieren.',
            'Auf der offiziellen SET-IPTV-Website die Seite zum Hochladen der Playlist öffnen.',
            'MAC-Adresse und <a href="/m3u-playlist/">M3U-Link</a> eingeben, optional eine EPG-Adresse.',
            'Speichern, App am Fernseher neu starten – fertig.')),
        ('aktivierung', 'Testphase und Aktivierung', '''
<p>Nach einer Testphase verlangt der Entwickler eine Aktivierungsgebühr, die über die Website mit der MAC-Adresse bezahlt wird. Den aktuellen Betrag und die Laufzeit der Aktivierung finden Sie dort. Die Aktivierung gilt für das jeweilige Gerät.</p>'''),
        ('vergleich', 'SET IPTV, Smart IPTV oder Flix IPTV?', table(['', 'SET IPTV', '<a href="/smart-iptv/">Smart IPTV</a>', '<a href="/flix-iptv/">Flix IPTV</a>'], [
            ['Playlist-Upload', 'Website + MAC', 'Website + MAC', 'Website + MAC'],
            ['Oberfläche', 'Klassisch', 'Schlicht', 'Modern'],
            ['Filme &amp; Serien', 'Ja', 'Eingeschränkt', 'Ja'],
            ['Geräte', 'Samsung, LG, Android', 'Samsung, LG, Android', 'Samsung, LG, Android, Fire TV'],
        ], 'SET IPTV im Vergleich') + LOGIN_TIP),
    ],
    faq=[
        ('Ist SET IPTV kostenlos?', 'SET IPTV bietet eine Testphase. Danach wird eine Aktivierungsgebühr an den Entwickler fällig. Ihr IPTV-Abo mit den Sendern ist davon unabhängig.'),
        ('Wo finde ich die MAC-Adresse in SET IPTV?', 'Die MAC-Adresse wird beim Start der App auf dem Bildschirm angezeigt, meist zusammen mit dem Aktivierungsstatus.'),
        ('Warum lädt SET IPTV meine Playlist nicht?', 'Prüfen Sie, ob die MAC-Adresse exakt stimmt und der M3U-Link im Browser funktioniert. Danach die App vollständig neu starten.'),
        ('Unterstützt SET IPTV EPG?', 'Ja. Der Programmführer wird aus der Playlist oder einer separat hinterlegten EPG-Adresse geladen.'),
    ],
    related=['smart-iptv', 'flix-iptv', 'smartone-iptv', 'iptv-samsung-tv', 'iptv-lg-tv', 'iptv-apps'],
    card=('SET IPTV', 'Playlist per MAC-Adresse hochladen und App aktivieren.'),
))

# ---------------------------------------------------------------- Flix IPTV
PAGES.append(dict(
    slug='flix-iptv', parent='apps', kind='guide',
    title='Flix IPTV: Einrichtung auf Samsung, LG & Fire TV',
    description='Flix IPTV einrichten: App auf Samsung, LG, Android oder Fire TV installieren, MAC-Adresse finden, Playlist hochladen, aktivieren und Einstellungen optimieren.',
    eyebrow='APP-ANLEITUNG', h1='Flix IPTV: Anleitung für Smart TV &amp; Fire TV',
    lead='Flix IPTV ist ein moderner IPTV Player mit übersichtlicher Oberfläche für Live-TV, Filme und Serien. Die Playlist laden Sie per MAC-Adresse über die Website.',
    answer='Flix IPTV ist ein IPTV Player für Samsung, LG, Android und Fire TV. Nach der Installation zeigt die App unter „Einstellungen → Benutzerkonto“ die MAC-Adresse. Auf der Upload-Seite der offiziellen Flix-IPTV-Website geben Sie MAC-Adresse und M3U-Link ein. Nach der Testphase wird eine einmalige Aktivierung pro Gerät fällig.',
    sections=[
        ('was', 'Was ist Flix IPTV?', '''
<p>Flix IPTV (auch „FlixIPTV“) ist ein reiner Player ohne eigene Inhalte. Viele Nutzer schätzen das an Streaming-Dienste angelehnte Design mit Postern für Filme und Serien, Untertitel-Unterstützung und Favoritenlisten.</p>
''' + proscons(['Modernes Design mit Postern', 'Auf vielen TV-Systemen verfügbar', 'Untertitel und Favoriten'],
               ['Aktivierung kostenpflichtig', 'Playlist nur über die Website änderbar'])),
        ('einrichten', 'Flix IPTV einrichten', steps(
            'Flix IPTV im App-Store von <a href="/iptv-samsung-tv/">Samsung</a> oder <a href="/iptv-lg-tv/">LG</a> installieren; auf Android aus dem Play Store, auf dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> per Downloader.',
            'App öffnen, links <b>„Einstellungen → Benutzerkonto“</b> wählen und die MAC-Adresse notieren.',
            'Auf der offiziellen Flix-IPTV-Website die Seite „Manage Playlist“ öffnen.',
            'MAC-Adresse eintragen, Playlist-Name und <a href="/m3u-playlist/">M3U-Link</a> eingeben, speichern.',
            'App neu starten, Playlist auswählen und loslegen.')),
        ('einstellungen', 'Empfohlene Einstellungen', checks(
            'Sprache unter Einstellungen auf Deutsch stellen.',
            'Zeitformat und Zeitzone für den Programmführer anpassen.',
            'Nicht benötigte Kategorien unter „Kategorien ausblenden“ entfernen.',
            'Bei Rucklern den alternativen Player in den Einstellungen testen.')),
        ('aktivierung', 'Flix IPTV aktivieren', '''
<p>Nach der kostenlosen Testphase aktivieren Sie Flix IPTV einmalig pro Gerät über die Website des Entwicklers. Preis und Bedingungen stehen dort. Die Aktivierung betrifft nur die App – Sender, Filme und Serien bringt Ihr <a href="/iptv-kaufen/">IPTV-Abo</a> mit.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Ist Flix IPTV kostenlos?', 'Flix IPTV ist in einer Testphase kostenlos. Danach wird eine einmalige Aktivierung pro Gerät beim Entwickler fällig.'),
        ('Gibt es Flix IPTV für den Fire TV Stick?', 'Ja, Flix IPTV läuft auf Fire-TV-Geräten mit Fire OS. Die Installation erfolgt in der Regel über die App Downloader.'),
        ('Wie ändere ich die Playlist in Flix IPTV?', 'Über die Manage-Playlist-Seite auf der Flix-IPTV-Website mit Ihrer MAC-Adresse. Danach die App neu starten.'),
        ('Unterstützt Flix IPTV Untertitel?', 'Ja, sofern der Film oder die Serie Untertitelspuren enthält, können Sie diese im Player auswählen.'),
    ],
    related=['set-iptv', 'smartone-iptv', 'smart-iptv', 'iptv-samsung-tv', 'iptv-lg-tv', 'iptv-apps'],
    card=('Flix IPTV', 'Moderner Player für Samsung, LG und Fire TV einrichten.'),
))

# ---------------------------------------------------------------- SmartOne
PAGES.append(dict(
    slug='smartone-iptv', parent='apps', kind='guide',
    title='SmartOne IPTV: Playlist hinzufügen & aktivieren',
    description='SmartOne IPTV auf Samsung, LG und Android einrichten: MAC-Adresse finden, M3U-Playlist hinzufügen, App aktivieren und Unterschiede zu Smart IPTV verstehen.',
    eyebrow='APP-ANLEITUNG', h1='SmartOne IPTV: Anleitung auf Deutsch',
    lead='SmartOne IPTV ist ein schlanker Player für Smart-TVs. Weil der Name Smart IPTV ähnelt, wird er oft verwechselt – wir zeigen die Unterschiede und die Einrichtung.',
    answer='SmartOne IPTV ist ein eigenständiger IPTV Player für Samsung, LG und Android, nicht zu verwechseln mit Smart IPTV (SIPTV). Die App zeigt beim Start eine MAC-Adresse; über die offizielle SmartOne-Website verknüpfen Sie diese mit Ihrem M3U-Link. Nach der Testphase ist eine kostenpflichtige Aktivierung nötig.',
    sections=[
        ('unterschied', 'SmartOne IPTV vs. Smart IPTV', table(['', 'SmartOne IPTV', '<a href="/smart-iptv/">Smart IPTV (SIPTV)</a>'], [
            ['Entwickler', 'Eigenständiges Projekt', 'Eigenständiges Projekt'],
            ['Playlist', 'Website + MAC', 'My-List-Seite + MAC'],
            ['Geräte', 'Samsung, LG, Android', 'Samsung, LG, Android'],
            ['Aktivierung', 'Kostenpflichtig nach Test', 'Einmalig nach Test'],
        ], 'SmartOne IPTV und Smart IPTV im Vergleich') + '''
<p>Beide Apps sind reine Player. Welche Sie wählen, ist Geschmackssache – entscheidend ist, dass sie auf Ihrem Modell im Store verfügbar ist.</p>'''),
        ('einrichten', 'SmartOne IPTV einrichten', steps(
            'SmartOne IPTV im App-Store Ihres Fernsehers installieren.',
            'App starten und die <b>MAC-Adresse</b> notieren.',
            'Auf der offiziellen SmartOne-IPTV-Website den Bereich zum Hinzufügen einer Playlist öffnen.',
            'MAC-Adresse und <a href="/m3u-playlist/">M3U-Link</a> eingeben und speichern.',
            'App am Fernseher neu starten.')),
        ('tipps', 'Tipps für SmartOne IPTV', checks(
            'Nach jeder Änderung der Playlist die App ganz schließen und neu öffnen.',
            'Bei Bildstörungen am <a href="/iptv-samsung-tv/">Samsung</a> oder <a href="/iptv-lg-tv/">LG</a> das Netzwerk per LAN-Kabel anschließen.',
            'Für mehr Komfort beim Programmführer <a href="/flix-iptv/">Flix IPTV</a> oder <a href="/set-iptv/">SET IPTV</a> testen.') + LOGIN_TIP),
    ],
    faq=[
        ('Ist SmartOne IPTV dasselbe wie Smart IPTV?', 'Nein. SmartOne IPTV und Smart IPTV (SIPTV) sind zwei verschiedene Apps unterschiedlicher Entwickler mit ähnlichem Prinzip.'),
        ('Ist SmartOne IPTV kostenlos?', 'Es gibt eine Testphase. Danach verlangt der Entwickler eine Aktivierungsgebühr, die Sie über die Website bezahlen.'),
        ('Welche Playlists unterstützt SmartOne IPTV?', 'SmartOne IPTV arbeitet mit M3U-Links. IPTV Kanal stellt Ihnen einen passenden Link bereit.'),
    ],
    related=['smart-iptv', 'set-iptv', 'flix-iptv', 'iptv-smart-tv', 'iptv-samsung-tv', 'iptv-apps'],
    card=('SmartOne IPTV', 'Einrichtung und Unterschied zu Smart IPTV.'),
))

# ---------------------------------------------------------------- Xtream / XCIPTV
PAGES.append(dict(
    slug='xtream-codes-iptv', parent='apps', kind='guide',
    title='Xtream Codes IPTV & XCIPTV: Login, M3U und Einrichtung',
    description='Was ist Xtream Codes? So nutzen Sie Xtream-IPTV-Logins in XCIPTV, Smarters & TiviMate, erzeugen einen M3U-Link und richten XCIPTV auf dem Fire TV Stick ein.',
    eyebrow='XTREAM CODES', h1='Xtream Codes IPTV und XCIPTV',
    lead='Server, Benutzername, Passwort: Der Xtream-Codes-Login ist der bequemste Weg, IPTV in eine App zu laden. Wir erklären das Format und die App XCIPTV.',
    answer='Xtream Codes ist ein Login-Standard für IPTV mit drei Angaben: Server-URL, Benutzername und Passwort. Apps wie XCIPTV, IPTV Smarters Pro und TiviMate laden damit Live-TV, Filme, Serien und EPG automatisch. Aus denselben Daten lässt sich bei Bedarf ein M3U-Link für Apps ohne Xtream-Unterstützung bilden.',
    sections=[
        ('was', 'Was ist Xtream Codes?', '''
<p>Ursprünglich war Xtream Codes eine Server-Software für IPTV-Anbieter. Ihr Login-Schema (die sogenannte Xtream Codes API) hat sich als Standard durchgesetzt und wird heute von vielen Panels und Apps unterstützt. Für Sie zählt nur: Mit drei Angaben ist alles eingerichtet.</p>
''' + table(['Feld', 'Beispiel'], [
            ['Server-URL', '<code>http://server.beispiel:8080</code>'],
            ['Benutzername', '<code>ihrname123</code>'],
            ['Passwort', '<code>abc456</code>'],
        ], 'Bestandteile eines Xtream-Codes-Logins')),
        ('m3u', 'Xtream IPTV als M3U nutzen', '''
<p>Manche Apps, etwa <a href="/smart-iptv/">Smart IPTV</a>, <a href="/ss-iptv/">SS IPTV</a> oder <a href="/iptv-pc-mac/">VLC</a>, kennen nur M3U. Aus einem Xtream-Login entsteht der Link in diesem Muster:</p>
<p><code>http://server:port/get.php?username=NAME&amp;password=PASSWORT&amp;type=m3u_plus&amp;output=ts</code></p>
<p>Bei IPTV Kanal müssen Sie das nicht selbst zusammensetzen – wir senden Ihnen beide Varianten. Mehr zu M3U-Listen im Ratgeber <a href="/m3u-playlist/">M3U Playlist</a>.</p>'''),
        ('xciptv', 'XCIPTV einrichten (Android &amp; Fire TV)', '''
<p><strong>XCIPTV</strong> (auch „XC IPTV“) ist ein Player, der speziell für Xtream-Codes-Logins entwickelt wurde. Er läuft auf Android-Smartphones, Android-TV-Boxen und dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> mit Fire OS. Für Samsung- und LG-Fernseher gibt es keine native Version; dort nutzen Sie einen Stick oder einen anderen Player.</p>
''' + steps(
            'XCIPTV aus dem Play Store installieren bzw. auf Fire TV per Downloader.',
            'Beim ersten Start „Xtream Codes“ auswählen.',
            'Server-URL, Benutzername und Passwort eintragen.',
            'Anmelden – Live-TV, Filme, Serien und EPG werden geladen.',
            'In den Einstellungen den Player (Exo/VLC) und die Puffergröße anpassen.')),
        ('apps', 'Welche Apps unterstützen Xtream Codes?', checks(
            '<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> – „Login mit Xtream Codes API“',
            '<a href="/tivimate/">TiviMate</a> – „Playlist hinzufügen → Xtream Codes“',
            'XCIPTV, OTT Navigator, iMPlayer und IBO Player',
            'Viele Apple-Apps wie IPTVX und Smarters Player Lite') + LOGIN_TIP),
    ],
    faq=[
        ('Was ist der Unterschied zwischen Xtream Codes und M3U?', 'M3U ist eine Liste von Streamadressen. Xtream Codes ist ein Login, mit dem die App Senderliste, Mediathek und EPG automatisch abruft. Xtream ist komfortabler, M3U ist universeller.'),
        ('Ist XCIPTV kostenlos?', 'XCIPTV ist als kostenloser Player erhältlich. Die Sender kommen aus Ihrem IPTV-Abo.'),
        ('Gibt es XCIPTV für Samsung oder LG?', 'Nein, XCIPTV gibt es für Android und Fire TV. Auf Samsung und LG nutzen Sie Player wie SET IPTV oder Flix IPTV oder einen Fire TV Stick.'),
        ('Warum funktioniert mein Xtream-Login nicht?', 'Meist fehlt in der Server-URL das http:// oder der Port, oder es hat sich ein Leerzeichen eingeschlichen. Prüfen Sie alle drei Angaben exakt.'),
    ],
    related=['m3u-playlist', 'iptv-smarters-pro', 'tivimate', 'iptv-fire-tv-stick', 'iptv-android', 'iptv-apps'],
    card=('Xtream Codes & XCIPTV', 'Login-Standard verstehen und XCIPTV einrichten.'),
))

# ---------------------------------------------------------------- Kodi / Plex / Jellyfin
PAGES.append(dict(
    slug='kodi-iptv', parent='apps', kind='guide',
    title='Kodi IPTV einrichten: PVR IPTV Simple Client (Anleitung)',
    description='IPTV in Kodi einrichten mit dem PVR IPTV Simple Client: M3U und EPG hinzufügen, Live-TV in Kodi nutzen – plus IPTV in Plex und Jellyfin.',
    eyebrow='MEDIACENTER', h1='Kodi IPTV: Live-TV mit dem PVR IPTV Simple Client',
    lead='Kodi verwandelt PC, Box oder Stick in ein Mediacenter. Mit dem offiziellen PVR IPTV Simple Client wird daraus ein vollwertiger IPTV-Empfänger mit Programmführer.',
    answer='Für IPTV in Kodi installieren Sie über „Add-ons → Aus Repository installieren → PVR-Clients“ den offiziellen PVR IPTV Simple Client. In dessen Einstellungen tragen Sie Ihren M3U-Link und die EPG-Adresse (XMLTV) ein. Nach einem Neustart erscheinen die Sender unter „TV“ mit Programmführer.',
    sections=[
        ('einrichten', 'Kodi IPTV einrichten: Schritt für Schritt', steps(
            'Kodi öffnen und <b>Add-ons → Aus Repository installieren → Kodi Add-on repository</b> wählen.',
            '<b>PVR-Clients → PVR IPTV Simple Client</b> installieren und aktivieren.',
            'Im Add-on <b>Konfigurieren → Allgemein</b>: Speicherort „Remote-Pfad (Internet)“ und Ihren <a href="/m3u-playlist/">M3U-Link</a> eintragen.',
            'Unter <b>EPG-Einstellungen</b> die XMLTV-Adresse einfügen.',
            'Kodi neu starten. Unter <b>TV</b> erscheinen Kanäle und Programmführer.')),
        ('tipps', 'Tipps für Live-TV in Kodi', checks(
            'Unter Einstellungen → PVR &amp; Live-TV „Kanäle beim Start synchronisieren“ aktivieren.',
            'Senderlogos über das Feld <code>tvg-logo</code> der Playlist laden lassen.',
            'Auf schwachen Geräten den Puffer in „advancedsettings.xml“ erhöhen.',
            'Die deutschsprachige Community von Kodinerds bietet Hilfe zu Skins und Einstellungen.')
         + tip('Meiden Sie inoffizielle Repositorys mit vorinstallierten Streams. Sie sind häufig unzuverlässig, rechtlich problematisch und ein Sicherheitsrisiko.', 'Achtung')),
        ('plex', 'IPTV in Plex', '''
<p>Plex bietet Live-TV &amp; DVR für Plex-Pass-Nutzer, erwartet aber einen Tuner. Für IPTV wird deshalb ein Vermittler wie <strong>Threadfin</strong> (Nachfolger von xTeVe) genutzt, der eine M3U-Liste als virtuellen Tuner bereitstellt. Für die meisten Zuschauer ist eine direkte IPTV-App einfacher.</p>'''),
        ('jellyfin', 'IPTV in Jellyfin', '''
<p>Jellyfin unterstützt IPTV direkt: Im Dashboard unter „Live-TV“ fügen Sie einen <strong>M3U-Tuner</strong> und einen <strong>XMLTV-Programmführer</strong> hinzu. Danach stehen Sender, EPG und Aufnahmen in allen Jellyfin-Apps bereit.</p>'''),
        ('geraete', 'Auf welchen Geräten läuft Kodi?', '''
<p>Kodi gibt es für <a href="/iptv-pc-mac/">Windows, Mac und Linux</a>, <a href="/iptv-android/">Android</a>, <a href="/iptv-box/">Android-TV-Boxen</a>, den <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> (Fire OS) und Apple TV. Auf Samsung- und LG-Fernsehern ist Kodi nicht verfügbar.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Wie bekomme ich IPTV in Kodi?', 'Über das offizielle Add-on PVR IPTV Simple Client. Dort tragen Sie Ihren M3U-Link und die EPG-Adresse ein und starten Kodi neu.'),
        ('Ist Kodi für IPTV kostenlos?', 'Ja, Kodi und der PVR IPTV Simple Client sind kostenlos und Open Source. Die Sender kommen aus Ihrem IPTV-Abo.'),
        ('Kann ich IPTV in Plex schauen?', 'Ja, über Plex Live-TV & DVR mit Plex Pass und einem Vermittler wie Threadfin, der die M3U-Liste als Tuner bereitstellt.'),
        ('Unterstützt Jellyfin IPTV?', 'Ja. Jellyfin kann M3U-Tuner und XMLTV-Programmführer direkt einbinden und bietet Live-TV mit Aufnahmefunktion.'),
    ],
    related=['m3u-playlist', 'iptv-pc-mac', 'iptv-box', 'iptv-android', 'tivimate', 'iptv-apps'],
    card=('Kodi IPTV', 'PVR IPTV Simple Client einrichten – plus Plex und Jellyfin.'),
))
