"""Gap-fill pages (second keyword pass, 24.11.2026): IPTV Stick, Formuler, TiviMate Premium,
IPTV Smarters Pro on Fire TV, IPTV Erfahrungen (forums/Reddit/Trustpilot) and the Senderliste guide.
Third-party prices are deliberately not quoted because they change; hardware facts were checked against
manufacturer and retailer listings."""
from .helpers import steps, checks, tip, table, proscons

PAGES = []

LOGIN_TIP = tip('Ihre Zugangsdaten von IPTV Kanal funktionieren auf diesem Gerät. Fragen Sie im <a href="/kostenlos-testen/">kostenlosen Test</a> direkt nach dem passenden Format (Xtream Codes, M3U oder Portal).', 'Hinweis')

# ---------------------------------------------------------------- IPTV Stick
PAGES.append(dict(
    slug='iptv-stick', parent='geraete', kind='guide',
    title='IPTV Stick 2026: Welcher Streaming-Stick passt zu IPTV?',
    description='IPTV Stick im Vergleich: Fire TV Stick 4K Max, Google TV Streamer, Xiaomi TV Stick 4K, Chromecast und Roku – welcher Stick IPTV-Apps kann und welcher nicht.',
    eyebrow='KAUFBERATUNG', h1='IPTV Stick: welcher Streaming-Stick für IPTV?',
    lead='Ein IPTV Stick macht aus jedem Fernseher mit HDMI-Anschluss einen IPTV-Empfänger. Entscheidend ist nicht die Marke, sondern ob der Stick die IPTV-App Ihrer Wahl installieren kann.',
    answer='Ein IPTV Stick ist ein Streaming-Stick, auf dem eine IPTV-App wie TiviMate oder IPTV Smarters Pro läuft. Am besten eignen sich Sticks mit Fire OS oder Google TV, etwa der Fire TV Stick 4K Max, der Xiaomi TV Stick 4K (2. Gen.) oder der Google TV Streamer. Sticks mit Vega OS und Roku sind für IPTV nur eingeschränkt geeignet. Sender enthält kein Stick – die kommen aus Ihrem IPTV-Abo.',
    sections=[
        ('was', 'Was ist ein IPTV Stick?', '''
<p>„IPTV Stick“ ist kein eigenes Produkt, sondern ein Sammelbegriff: gemeint ist ein kleiner Streaming-Stick, der in den HDMI-Anschluss des Fernsehers gesteckt wird und auf dem eine IPTV-App läuft. Der Stick bringt das Betriebssystem, die Fernbedienung und die WLAN-Verbindung mit; die App lädt mit Ihren Zugangsdaten Senderliste, Mediathek und Programmführer.</p>
<p>Gegenüber einer App direkt auf dem Smart-TV hat ein Stick drei Vorteile: Er bekommt länger Updates als viele Fernseher, er unterstützt mehr Apps (etwa <a href="/tivimate/">TiviMate</a>, das es auf Samsung und LG nicht gibt), und Sie können ihn beim Fernseherwechsel einfach mitnehmen. Vorsicht bei Angeboten, die als „IPTV Stick mit Sendern“ verkauft werden: Seriöse Sticks enthalten keine Sender.</p>'''),
        ('vergleich', 'IPTV Sticks im Vergleich', table(['Stick', 'System', 'IPTV-Apps', 'Für wen?'], [
            ['<a href="/iptv-fire-tv-stick/">Fire TV Stick 4K Max (2. Gen.)</a>', 'Fire OS', 'TiviMate, Smarters, XCIPTV u. a. (per Downloader)', 'Erste Wahl für die meisten Haushalte'],
            ['Fire TV Stick 4K (2. Gen.) / Fire TV Stick (3. Gen.)', 'Fire OS', 'Wie oben', 'Günstiger, etwas weniger Leistung'],
            ['Fire TV Stick 4K Select und andere Vega-OS-Modelle', 'Vega OS', 'Nur Apps aus dem Amazon Appstore, keine APKs', 'Für IPTV nicht zu empfehlen'],
            ['Xiaomi TV Stick 4K (2. Gen.)', 'Google TV', 'TiviMate, Smarters, OTT Navigator aus dem Play Store', 'Preiswerter Google-TV-Stick'],
            ['Google TV Streamer', 'Google TV', 'Volle Play-Store-Auswahl', 'Mehr Leistung, LAN-Anschluss am Gerät'],
            ['Chromecast mit Google TV', 'Google TV', 'Play Store', 'Wird nicht mehr verkauft, läuft aber weiter'],
            ['Roku Streaming Stick', 'Roku OS', 'Nur wenige IPTV-Player im Roku-Store', 'Eher ungeeignet'],
        ], 'IPTV Sticks im Vergleich') + '''
<p>Preise ändern sich ständig, besonders an Aktionstagen. Vergleichen Sie beim Kauf vor allem das <strong>Betriebssystem</strong>: Fire OS und Google TV sind für IPTV die sichere Wahl.</p>'''),
        ('kriterien', 'Worauf Sie beim Kauf eines IPTV Sticks achten sollten', checks(
            '<strong>Betriebssystem:</strong> Fire OS oder Google TV / Android TV. Bei Fire-TV-Geräten vor dem Kauf prüfen, dass es kein Vega-OS-Modell ist.',
            '<strong>4K und HEVC:</strong> für <a href="/iptv-4k/">IPTV in 4K</a> muss der Stick 4K, HEVC/H.265 und HDR unterstützen.',
            '<strong>WLAN 6 oder LAN-Adapter:</strong> Sticks hängen oft hinter dem Fernseher. Ein Ethernet-Adapter oder ein WLAN-6-Modell verhindert Ruckler.',
            '<strong>Speicher:</strong> mindestens 8 GB, damit App, Programmführer und Updates Platz haben.',
            '<strong>Fernbedienung:</strong> Programmtasten und eine Zifferneingabe sind bei vielen Sendern bequemer – Alternativen bietet eine <a href="/iptv-box/">IPTV Box</a>.')),
        ('einrichten', 'IPTV auf dem Stick einrichten', steps(
            'Stick in einen HDMI-Anschluss stecken, Netzteil anschließen (nicht den USB-Port des Fernsehers nutzen – zu wenig Strom).',
            'Mit WLAN verbinden und mit Amazon- bzw. Google-Konto anmelden, Systemupdates installieren.',
            '<b>Google TV:</b> TiviMate oder IPTV Smarters Pro aus dem Play Store installieren. <b>Fire OS:</b> der Anleitung <a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro auf dem Fire TV Stick</a> folgen.',
            'Zugangsdaten eintragen: Xtream-Codes-Login (Server, Benutzername, Passwort) oder <a href="/m3u-playlist/">M3U-Link</a>.',
            'In den Systemeinstellungen „Bildwiederholrate anpassen“ aktivieren, damit Sport flüssig läuft.') + LOGIN_TIP),
        ('chromecast', 'Chromecast und Google TV: Stick oder Casting?', '''
<p>Beim <strong>Chromecast mit Google TV</strong>, dem <strong>Google TV Streamer</strong> und Fernsehern mit Google TV läuft die IPTV-App direkt auf dem Gerät – das ist die stabilste Lösung. Ältere Chromecasts ohne Fernbedienung können dagegen nur empfangen, was Sie vom Handy „casten“. Viele mobile Player bieten dafür eine Cast-Taste; das Handy dient dann als Fernbedienung. Für Live-TV am Abend ist eine App direkt auf dem Stick aber deutlich angenehmer. Mehr zu Android-Geräten im Ratgeber <a href="/iptv-android/">IPTV auf Android und Google TV</a>.</p>'''),
        ('probleme', 'IPTV Stick ruckelt? Die häufigsten Ursachen', table(['Ursache', 'Lösung'], [
            ['WLAN-Empfang hinter dem Fernseher', 'HDMI-Verlängerung nutzen oder Ethernet-Adapter einstecken'],
            ['Stick wird heiß', 'Nicht direkt am Gehäuse einklemmen, Verlängerung nutzen'],
            ['Speicher voll', 'Cache leeren, ungenutzte Apps löschen'],
            ['Stromversorgung über USB des TV', 'Original-Netzteil verwenden'],
            ['4K ruckelt', 'Bandbreite prüfen (ab 25 Mbit/s), Hardware-Decoder in der App aktivieren'],
        ], 'Probleme mit IPTV Sticks')),
    ],
    faq=[
        ('Was ist der beste IPTV Stick?', 'Für die meisten Haushalte der Fire TV Stick 4K Max mit Fire OS oder ein Google-TV-Stick wie der Xiaomi TV Stick 4K (2. Gen.). Beide unterstützen TiviMate und IPTV Smarters Pro. Wer mehr Leistung und LAN möchte, nimmt den Google TV Streamer oder eine Android-TV-Box.'),
        ('Funktioniert jeder Fire TV Stick als IPTV Stick?', 'Nein. Modelle mit Fire OS funktionieren, neuere Modelle mit Vega OS wie der Fire TV Stick 4K Select erlauben keine Installation von IPTV-Apps außerhalb des Amazon Appstores.'),
        ('Brauche ich für einen IPTV Stick ein IPTV-Abo?', 'Ja. Der Stick und die App sind nur das Abspielgerät. Sender, Filme und Serien kommen aus Ihrem IPTV-Abo, dessen Zugangsdaten Sie in der App eintragen.'),
        ('Kann ich IPTV auf Chromecast schauen?', 'Ja. Auf Chromecast mit Google TV und dem Google TV Streamer installieren Sie TiviMate oder IPTV Smarters Pro direkt aus dem Play Store. Ältere Chromecasts ohne Fernbedienung empfangen nur gecastete Streams vom Handy.'),
        ('Lohnt sich ein IPTV Stick, wenn mein Fernseher schon Apps hat?', 'Oft ja: Ein Stick bekommt länger Updates, unterstützt mehr IPTV-Apps wie TiviMate und schaltet meist schneller um als die eingebaute Smart-TV-Plattform.'),
    ],
    related=['iptv-fire-tv-stick', 'iptv-smarters-pro-firestick', 'iptv-android', 'iptv-box', 'tivimate', 'iptv-geraete'],
    card=('IPTV Stick', 'Fire TV, Google TV, Xiaomi oder Roku: welcher Stick IPTV kann.'),
))

# ---------------------------------------------------------------- Formuler
PAGES.append(dict(
    slug='formuler-iptv', parent='geraete', kind='guide',
    title='Formuler IPTV Box: Z11 Pro Max, Z10 & MyTVOnline 3',
    description='Formuler IPTV Box einrichten: Z11 Pro Max, Z11 Pro, Z10 Pro Max und ältere Modelle wie Z8, Z7+ und Z Nano im Überblick – mit MyTVOnline-3-Anleitung.',
    eyebrow='GERÄTE-ANLEITUNG', h1='Formuler IPTV Box: Modelle und MyTVOnline-Anleitung',
    lead='Formuler baut Android-Boxen, die speziell für IPTV gedacht sind: mit eigener IPTV-App MyTVOnline, Programmführer im Receiver-Stil und Fernbedienung mit Sendertasten.',
    answer='Eine Formuler IPTV Box ist eine Android-Box mit der vorinstallierten IPTV-App MyTVOnline. Aktuelle Modelle sind die Z11 Pro und Z11 Pro Max mit Android 11 und MyTVOnline 3; die Z11 Pro Max hat 4 GB RAM, 32 GB Speicher, Gigabit-LAN und WLAN 6. Sie tragen Ihr Portal, Ihren Xtream-Codes-Login oder eine M3U-Liste in MyTVOnline ein und schauen wie mit einem Receiver.',
    sections=[
        ('modelle', 'Formuler-Modelle im Überblick', table(['Modell', 'System', 'Hinweis'], [
            ['Z11 Pro Max (auch als BT1-Edition)', 'Android 11, MyTVOnline 3', '4 GB RAM, 32 GB Speicher, Gigabit-LAN, WLAN 6 – das aktuelle Topmodell'],
            ['Z11 Pro', 'Android 11, MyTVOnline 3', '16 GB Speicher, gute Wahl für eine einzelne Playlist'],
            ['Z10 Pro Max / Z10 Pro 4K', 'Android 10', 'Vorgängergeneration, für 4K-IPTV weiterhin brauchbar'],
            ['Z8 Pro / Z8', 'älteres Android', 'Läuft, bekommt aber kaum noch Updates'],
            ['Z7+, Z+, Z Nano, Z Neo', 'älteres Android', 'Ältere Generationen – beim Neukauf eher zur Z11-Serie greifen'],
        ], 'Formuler Modelle für IPTV') + '''
<p>Die Bezeichnung „BT“ bzw. „BT1“ steht für eine Fernbedienung mit Bluetooth und Sprachsteuerung. Technisch identisch ist die Box selbst. Formuler-Boxen sind über Fachhändler und große Elektronikportale in Deutschland, Österreich und der Schweiz erhältlich; Preise schwanken je nach Händler.</p>'''),
        ('mytvonline', 'Was ist MyTVOnline 3?', '''
<p><strong>MyTVOnline</strong> ist die IPTV-Oberfläche von Formuler. Sie bündelt Live-TV, Programmführer, Mediathek, Catch-Up und Aufnahme auf einen USB-Speicher in einer App, die sich wie ein klassischer Receiver bedienen lässt. Version 3 kam mit der Z11-Serie und ist schneller, übersichtlicher und unterstützt mehrere Portale gleichzeitig.</p>
''' + proscons(['Receiver-ähnliche Bedienung mit Sendertasten', 'Portal (MAC), Xtream Codes und M3U in einer App', 'Aufnahme und Timeshift', 'Daneben laufen TiviMate und Smarters aus dem Play Store'],
               ['Teurer als ein Streaming-Stick', 'Ältere Modelle ohne aktuelle Updates', 'Viele Menüs – kurze Eingewöhnung nötig'])),
        ('einrichten', 'Formuler mit MyTVOnline einrichten', steps(
            'Box per HDMI an den Fernseher und per LAN-Kabel an den Router anschließen, Systemupdates installieren.',
            'MyTVOnline öffnen. Für ein MAC-Portal notieren Sie die angezeigte <b>MAC-Adresse</b> und schicken sie Ihrem Anbieter.',
            '<b>Portal hinzufügen:</b> Namen vergeben und die Portal-Adresse eintragen – oder den Typ Xtream Codes bzw. M3U wählen und die Zugangsdaten eingeben.',
            'Portal speichern und verbinden. MyTVOnline lädt Sender, Mediathek und Programmführer.',
            'Unter den Einstellungen Zeitzone (Europa/Berlin) und Sprache des Programmführers prüfen.',
            'Optional einen USB-Speicher anschließen, um Sendungen aufzunehmen.') + LOGIN_TIP),
        ('alternativen', 'Formuler, MAG oder Android-Box?', '''
<p>Eine Formuler ist der Mittelweg zwischen einer <a href="/mag-box-iptv/">MAG-Box</a> (reines Portal-Gerät, sehr einfach) und einer offenen <a href="/iptv-box/">Android-TV-Box</a> wie Nvidia Shield (maximale App-Auswahl). Wer IPTV wie mit einem Sat-Receiver bedienen möchte und trotzdem den Play Store nutzen will, ist mit Formuler gut bedient. Wer zusätzlich Satellit oder Kabel braucht, schaut sich einen <a href="/iptv-receiver/">Enigma2-Receiver</a> an.</p>'''),
        ('probleme', 'Typische Probleme mit Formuler-Boxen', table(['Problem', 'Lösung'], [
            ['Portal verbindet nicht', 'MAC-Adresse beim Anbieter prüfen lassen, Portal-URL inklusive /c/ korrekt eintragen'],
            ['Programmführer leer', 'In MyTVOnline EPG neu laden, Zeitzone prüfen'],
            ['Ruckeln bei 4K', 'LAN statt WLAN, Auflösung und Bildwiederholrate in den Systemeinstellungen anpassen'],
            ['Box sehr langsam', 'Cache von MyTVOnline leeren, nicht genutzte Portale entfernen'],
        ], 'Formuler Problemlösungen')),
    ],
    faq=[
        ('Welche Formuler Box ist die beste für IPTV?', 'Aktuell die Formuler Z11 Pro Max: Android 11, MyTVOnline 3, 4 GB RAM, 32 GB Speicher, Gigabit-LAN und WLAN 6. Die Z11 Pro reicht, wenn Sie nur eine Playlist nutzen.'),
        ('Enthält eine Formuler Box Sender?', 'Nein. Formuler liefert nur Hardware und die App MyTVOnline. Die Sender kommen aus Ihrem IPTV-Abo, das Sie als Portal, Xtream-Codes-Login oder M3U-Liste eintragen.'),
        ('Kann ich auf einer Formuler auch TiviMate nutzen?', 'Ja. Formuler-Boxen haben Android und den Play Store, daher laufen auch TiviMate und IPTV Smarters Pro neben MyTVOnline.'),
        ('Lohnt sich eine ältere Formuler wie Z8 oder Z7+ noch?', 'Für einfache HD-Nutzung ja, als Neukauf aber kaum: ältere Modelle bekommen kaum noch Updates. Für 4K und aktuelle Apps ist die Z11-Serie die bessere Wahl.'),
    ],
    related=['iptv-box', 'mag-box-iptv', 'iptv-receiver', 'tivimate', 'iptv-4k', 'iptv-geraete'],
    card=('Formuler IPTV Box', 'Z11 Pro Max, Z10 und ältere Modelle mit MyTVOnline 3.'),
))

# ---------------------------------------------------------------- TiviMate Premium
PAGES.append(dict(
    slug='tivimate-premium', parent='apps', kind='guide',
    title='TiviMate Premium: Kosten, Kauf & Freischaltung 2026',
    description='TiviMate Premium erklärt: was es kostet, welche Funktionen es freischaltet, wie Sie es über TiviMate Companion kaufen und auf bis zu 5 Geräten aktivieren.',
    eyebrow='APP-ANLEITUNG', h1='TiviMate Premium: Kosten, Kauf und Freischaltung',
    lead='Die Grundversion von TiviMate ist kostenlos. Mit Premium kommen Aufnahmen, mehrere Playlists und Favoriten dazu. Hier steht, was Premium kostet, wie der Kauf funktioniert und wovor Sie sich hüten sollten.',
    answer='TiviMate Premium ist die kostenpflichtige Lizenz des IPTV-Players TiviMate. Sie kaufen sie als Jahreslizenz oder als einmalige Lifetime-Lizenz über die App TiviMate Companion auf einem Android-Gerät und melden sich danach in TiviMate mit demselben Konto an. Ein Premium-Konto gilt für bis zu fünf eigene Geräte. Premium enthält keine Sender – die kommen aus Ihrem IPTV-Abo.',
    sections=[
        ('funktionen', 'Was bringt TiviMate Premium?', table(['Funktion', 'Kostenlos', 'Premium'], [
            ['Playlist mit Xtream Codes oder M3U', '1 Playlist', 'Mehrere Playlists'],
            ['Programmführer (EPG)', 'Ja', 'Ja, mit mehr Anpassungen'],
            ['Favoriten und eigene Senderreihenfolge', 'Eingeschränkt', 'Ja'],
            ['Aufnahme (lokal oder Netzwerkspeicher)', 'Nein', 'Ja'],
            ['Catch-Up / Timeshift', 'Eingeschränkt', 'Ja'],
        ], 'TiviMate kostenlos vs. Premium') + '''
<p>Für die meisten Zuschauer ist Premium vor allem wegen <strong>Favoriten, Aufnahme und mehrerer Playlists</strong> interessant. Wer nur gelegentlich schaut, kommt mit der kostenlosen Version aus. Die Grundlagen zur App stehen im Ratgeber <a href="/tivimate/">TiviMate einrichten</a>.</p>'''),
        ('kosten', 'Was kostet TiviMate Premium?', '''
<p>TiviMate Premium gibt es in zwei Varianten: als <strong>Jahreslizenz</strong> und als einmalige <strong>Lifetime-Lizenz</strong>. Beide gelten für bis zu fünf Geräte desselben Kontos. Die Preise legt der Entwickler fest; sie liegen bei wenigen Euro pro Jahr bzw. einem niedrigen zweistelligen Betrag für die Lifetime-Lizenz und werden in der Companion-App in Euro angezeigt. Weil sie sich ändern können, nennen wir hier bewusst keinen festen Betrag.</p>
''' + tip('Die Premium-Gebühr geht an den App-Entwickler, nicht an Ihren IPTV-Anbieter. Ein IPTV-Abo bei IPTV Kanal funktioniert auch mit der kostenlosen TiviMate-Version.', 'Gut zu wissen')),
        ('kaufen', 'TiviMate Premium kaufen: Schritt für Schritt', steps(
            '<b>TiviMate Companion</b> aus dem Google Play Store auf einem Android-Smartphone, Tablet oder Google-TV-Gerät installieren.',
            'In der Companion-App ein Konto anlegen (E-Mail und Passwort).',
            'Jahres- oder Lifetime-Lizenz wählen und über Google Play bezahlen.',
            'Auf dem Fernseher TiviMate öffnen: Einstellungen → Premium → Anmelden.',
            'Mit den Companion-Zugangsdaten anmelden. Premium ist sofort aktiv.',
            'Für weitere Geräte (bis zu fünf) dieselben Zugangsdaten verwenden.')
         + tip('Auf dem Fire TV Stick gibt es keinen Google Play Store. Kaufen Sie Premium deshalb mit der Companion-App auf dem Handy und melden Sie sich dann auf dem Fire TV an.')),
        ('warnung', 'Vorsicht bei „TiviMate Premium Accounts“ und APKs', '''
<p>Im Netz werden „TiviMate Premium Accounts“ oder „TiviMate Premium APK“ billig oder gratis angeboten. Dahinter stecken geteilte Konten, die jederzeit gesperrt werden, oder manipulierte Versionen der App. Solche APKs bekommen keine Updates und können Schadsoftware enthalten; zudem verstoßen sie gegen die Lizenz. Die offizielle Lizenz ist günstig genug, dass sich das Risiko nicht lohnt.</p>
''' + checks(
            'Premium nur über die offizielle Companion-App kaufen.',
            'TiviMate nur aus dem Play Store oder von der offiziellen Quelle installieren.',
            'Keine Zugangsdaten für Premium-Konten von Dritten verwenden.')),
        ('probleme', 'Premium wird nicht erkannt? Lösungen', table(['Problem', 'Lösung'], [
            ['Premium nach dem Kauf nicht aktiv', 'In TiviMate abmelden und mit den Companion-Daten neu anmelden'],
            ['„Geräteanzahl überschritten“', 'In der Companion-App alte Geräte entfernen'],
            ['Companion-App lässt sich nicht installieren', 'Ein Android-Gerät mit Google Play nutzen, z. B. ein Smartphone oder Google-TV-Gerät'],
            ['Lizenz abgelaufen', 'Jahreslizenz in der Companion-App verlängern oder auf Lifetime wechseln'],
        ], 'TiviMate Premium Problemlösungen') + '''
<p>TiviMate läuft nur auf Android-TV-Geräten wie <a href="/iptv-fire-tv-stick/">Fire TV mit Fire OS</a>, <a href="/iptv-box/">Android-TV-Boxen</a> und <a href="/iptv-stick/">Google-TV-Sticks</a>. Für Samsung, LG und Apple TV gibt es andere <a href="/iptv-apps/">IPTV Apps</a>.</p>'''),
    ],
    faq=[
        ('Was kostet TiviMate Premium?', 'TiviMate Premium gibt es als Jahreslizenz für wenige Euro und als einmalige Lifetime-Lizenz. Die aktuellen Preise zeigt die TiviMate-Companion-App; sie werden vom Entwickler festgelegt.'),
        ('Auf wie vielen Geräten gilt TiviMate Premium?', 'Ein Premium-Konto gilt für bis zu fünf eigene Geräte. Sie melden sich auf jedem Gerät mit denselben Companion-Zugangsdaten an.'),
        ('Gibt es TiviMate Companion für das iPhone?', 'Die Companion-App wird über Google Play für Android angeboten. Wer nur ein iPhone besitzt, nutzt für den Kauf ein Android-Tablet, ein Google-TV-Gerät oder das Android-Handy eines Familienmitglieds.'),
        ('Brauche ich TiviMate Premium für IPTV Kanal?', 'Nein. Ihr IPTV-Abo funktioniert auch mit der kostenlosen TiviMate-Version. Premium lohnt sich, wenn Sie Favoriten, Aufnahmen oder mehrere Playlists nutzen möchten.'),
        ('Ist ein TiviMate Premium Account von Drittanbietern sicher?', 'Nein. Geteilte Premium-Konten werden häufig gesperrt, und gecrackte APKs können Schadsoftware enthalten. Kaufen Sie Premium nur über die offizielle Companion-App.'),
    ],
    related=['tivimate', 'iptv-fire-tv-stick', 'iptv-stick', 'iptv-smarters-pro', 'iptv-box', 'iptv-apps'],
    card=('TiviMate Premium', 'Kosten, Kauf über Companion und Freischaltung auf bis zu 5 Geräten.'),
))

# ---------------------------------------------------------------- IPTV Smarters Pro on Fire TV
PAGES.append(dict(
    slug='iptv-smarters-pro-firestick', parent='apps', kind='guide',
    title='IPTV Smarters Pro auf Fire TV Stick installieren (2026)',
    description='IPTV Smarters Pro auf dem Fire TV Stick installieren: Downloader einrichten, App sicher laden, Xtream-Login eintragen – plus Lösungen für Vega OS und Fehler.',
    eyebrow='SCHRITT-FÜR-SCHRITT', h1='IPTV Smarters Pro auf dem Fire TV Stick installieren',
    lead='IPTV Smarters Pro ist auf dem Fire TV Stick meist nicht im Amazon Appstore zu finden. Mit der App Downloader ist die Installation trotzdem in zehn Minuten erledigt – sofern Ihr Stick Fire OS nutzt.',
    answer='So installieren Sie IPTV Smarters Pro auf dem Fire TV Stick: Downloader aus dem Amazon Appstore laden, in den Entwickleroptionen „Apps unbekannter Herkunft“ für Downloader erlauben, die APK-Adresse von der offiziellen Smarters-Website in Downloader eingeben, installieren und anschließend mit Ihrem Xtream-Codes-Login anmelden. Auf Fire-TV-Geräten mit Vega OS funktioniert das nicht.',
    sections=[
        ('vorher', 'Vorher prüfen: Fire OS oder Vega OS?', '''
<p>Öffnen Sie <b>Einstellungen → Mein Fire TV → Info</b>. Steht dort Fire OS, funktioniert diese Anleitung. Neuere Geräte wie der Fire TV Stick 4K Select laufen mit <strong>Vega OS</strong>; darauf lassen sich keine Android-Apps außerhalb des Amazon Appstores installieren. Welche Modelle betroffen sind, zeigt unsere Übersicht <a href="/iptv-fire-tv-stick/">IPTV auf dem Fire TV Stick</a>. Wer noch keinen Stick hat, findet Kaufhilfe im Ratgeber <a href="/iptv-stick/">IPTV Stick</a>.</p>'''),
        ('downloader', 'Schritt 1: Downloader installieren und freischalten', steps(
            'Auf der Startseite die Suche (Lupe) öffnen und „Downloader“ eingeben.',
            'Die App <b>Downloader</b> (orangefarbenes Symbol) aus dem Amazon Appstore installieren.',
            '<b>Einstellungen → Mein Fire TV → Info</b> öffnen und siebenmal auf den Gerätenamen klicken, bis „Sie sind jetzt Entwickler“ erscheint.',
            'Zurück zu <b>Mein Fire TV → Entwickleroptionen → Apps unbekannter Herkunft installieren</b> und Downloader auf „Ein“ stellen.')),
        ('installieren', 'Schritt 2: IPTV Smarters Pro herunterladen', steps(
            'Downloader öffnen und Zugriff auf Dateien erlauben.',
            'In das Adressfeld die Download-Adresse der Android-Version von der <b>offiziellen IPTV-Smarters-Website</b> eingeben und „Go“ drücken.',
            'Nach dem Download „Installieren“ wählen, danach „Fertig“.',
            'Die heruntergeladene APK-Datei in Downloader löschen, um Speicher zu sparen.',
            'Optional: In den Fire-TV-Einstellungen unter Anwendungen die App auf die Startseite legen.')
         + tip('Geben Sie keine Kurzcodes aus Foren, Videos oder Kommentaren in Downloader ein (mehr dazu im Ratgeber <a href="/cloudstream/">CloudStream</a>). Sie können auf veränderte Versionen der App verweisen, die Zugangsdaten abgreifen oder Schadsoftware enthalten.', 'Sicherheit')),
        ('anmelden', 'Schritt 3: Mit Xtream Codes anmelden', steps(
            'IPTV Smarters Pro öffnen, Nutzungsbedingungen akzeptieren und „TV“ als Gerätetyp wählen.',
            '<b>„Login mit Xtream Codes API“</b> auswählen.',
            'Einen Namen eingeben (z. B. „IPTV Kanal“), dann Benutzername, Passwort und Server-URL exakt aus Ihrer Zugangs-E-Mail übernehmen.',
            '„Nutzer hinzufügen“ drücken – Live-TV, Filme, Serien und Programmführer werden geladen.',
            'Unter Einstellungen → EPG die Zeitzone prüfen und den Programmführer einmal aktualisieren.') + LOGIN_TIP),
        ('fehler', 'Häufige Fehler auf dem Fire TV Stick', table(['Meldung / Problem', 'Lösung'], [
            ['„App nicht installiert“', 'Speicher freigeben (mindestens 500 MB) und erneut installieren'],
            ['„Fehler beim Parsen des Pakets“', 'Download abgebrochen oder falsche Datei – APK neu laden'],
            ['Entwickleroptionen fehlen', 'Siebenmal auf den Gerätenamen klicken; fehlen sie weiterhin, hat das Gerät wahrscheinlich Vega OS'],
            ['Downloader findet die Adresse nicht', 'Schreibweise prüfen, offizielle Website auf dem Handy aufrufen und Adresse abgleichen'],
            ['Ruckeln oder Einfrieren', 'Hardware-Decoder wählen, Puffer erhöhen, LAN-Adapter nutzen'],
        ], 'Fehlerbehebung Smarters auf Fire TV')),
        ('update', 'IPTV Smarters Pro aktualisieren oder ersetzen', '''
<p>Außerhalb des Appstores installierte Apps aktualisieren sich nicht automatisch. Laden Sie für ein Update die neue Version wie oben über Downloader – Ihre Anmeldedaten bleiben erhalten. Wer einen ausführlicheren Programmführer möchte, kann parallel <a href="/tivimate/">TiviMate</a> installieren; mit <a href="/tivimate-premium/">TiviMate Premium</a> kommen Aufnahme und Favoriten dazu. Alle Funktionen von Smarters auf anderen Geräten erklärt der Hauptratgeber <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</p>'''),
    ],
    faq=[
        ('Gibt es IPTV Smarters Pro im Amazon Appstore?', 'In Deutschland ist IPTV Smarters Pro meist nicht im Amazon Appstore gelistet. Auf Fire-TV-Geräten mit Fire OS installieren Sie die App deshalb mit der App Downloader von der offiziellen Smarters-Website.'),
        ('Ist die Installation mit Downloader sicher?', 'Ja, wenn Sie nur die offizielle Download-Adresse des Entwicklers verwenden. Kurzcodes aus Foren oder Videos können auf manipulierte Versionen verweisen.'),
        ('Warum fehlen auf meinem Fire TV die Entwickleroptionen?', 'Sie erscheinen erst, nachdem Sie unter Einstellungen → Mein Fire TV → Info siebenmal auf den Gerätenamen geklickt haben. Bei Geräten mit Vega OS gibt es diese Option nicht.'),
        ('Wie aktualisiere ich IPTV Smarters Pro auf dem Fire TV Stick?', 'Laden Sie die neue Version wie bei der Erstinstallation über Downloader von der offiziellen Website und installieren Sie sie über die alte Version. Ihre Zugangsdaten bleiben erhalten.'),
        ('Funktioniert IPTV Smarters Pro auf dem Fire TV Stick 4K Select?', 'Nein. Der Fire TV Stick 4K Select nutzt Vega OS und erlaubt keine Installation von Android-Apps außerhalb des Amazon Appstores.'),
    ],
    related=['iptv-smarters-pro', 'iptv-fire-tv-stick', 'tivimate', 'iptv-stick', 'xtream-codes-iptv', 'iptv-apps'],
    card=('Smarters auf Fire TV', 'IPTV Smarters Pro mit Downloader auf dem Fire TV Stick installieren.'),
))

# ---------------------------------------------------------------- IPTV Erfahrungen
PAGES.append(dict(
    slug='iptv-erfahrungen', parent='ratgeber', kind='guide',
    title='IPTV Erfahrungen: Forum, Reddit & Trustpilot richtig lesen',
    description='IPTV Erfahrungen richtig einordnen: Was Forum, Reddit und Trustpilot über IPTV Anbieter verraten, wie Sie gekaufte Bewertungen erkennen und selbst testen.',
    eyebrow='ERFAHRUNGEN &amp; BEWERTUNGEN', h1='IPTV Erfahrungen: Foren, Reddit und Trustpilot richtig lesen',
    lead='Bevor Sie ein IPTV-Abo kaufen, lesen Sie Erfahrungsberichte – zu Recht. Doch in kaum einer Branche sind Bewertungen so gemischt und so oft gekauft. So filtern Sie die brauchbaren heraus.',
    answer='IPTV-Erfahrungen aus Foren, Reddit und Trustpilot sind nützlich, um Warnsignale zu erkennen: Ausfälle am Abend, Support, der nach der Zahlung schweigt, oder Abos, die sich automatisch verlängern. Für Empfehlungen taugen sie weniger, weil Bewertungen in dieser Branche oft gekauft sind. Am verlässlichsten ist Ihr eigener kostenloser Test zur Hauptsendezeit.',
    sections=[
        ('quellen', 'Wo Nutzer über IPTV berichten', table(['Quelle', 'Stärke', 'Schwäche'], [
            ['Reddit (z. B. r/IPTV)', 'Viele technische Fragen zu Apps und Geräten', 'Englischsprachig; Anbieternamen sind in vielen Subreddits verboten'],
            ['Deutschsprachige Foren (z. B. Kodinerds für Kodi)', 'Fundierte Hilfe zu Apps, Receivern und Einstellungen', 'Kaum Anbieterempfehlungen'],
            ['Trustpilot und Google-Bewertungen', 'Schneller Eindruck, Antworten des Anbieters sichtbar', 'Anfällig für gekaufte und gefilterte Bewertungen'],
            ['YouTube-Tests', 'Oberfläche und Einrichtung live zu sehen', 'Oft mit Affiliate-Links, selten unabhängig'],
            ['Telegram- und WhatsApp-Gruppen', 'Aktuelle Störungsmeldungen', 'Werbung und Weiterverkauf weit verbreitet'],
        ], 'Quellen für IPTV Erfahrungen') + '''
<p>Für Fragen zu Apps wie <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a> sind Foren hervorragend. Für die Frage, welcher Anbieter gut ist, sollten Sie die Aussagen mit eigenen Tests abgleichen.</p>'''),
        ('reddit', 'Reddit: „best IPTV“ und was dahinter steckt', '''
<p>Suchen Sie auf Reddit nach „best IPTV“ oder „best IPTV provider“, finden Sie viele Threads, aber selten konkrete Namen. Der Grund: In großen IPTV-Communities ist das Nennen und Anfragen von Anbietern meist untersagt, um Werbung und Spam zu verhindern. Wer trotzdem per Direktnachricht Empfehlungen anbietet, ist häufig ein Verkäufer. Wertvoll sind Reddit-Threads vor allem für Gerätefragen, App-Vergleiche und typische Fehlerbilder.</p>'''),
        ('trustpilot', 'Trustpilot und Co.: gekaufte Bewertungen erkennen', checks(
            '<strong>Zeitliche Häufung:</strong> Viele Fünf-Sterne-Bewertungen an wenigen Tagen deuten auf eine Kampagne hin.',
            '<strong>Einmal-Profile:</strong> Rezensenten mit nur einer einzigen Bewertung sind weniger aussagekräftig.',
            '<strong>Austauschbare Texte:</strong> Allgemeines Lob ohne Gerät, App oder Situation ist wenig wert.',
            '<strong>Umgang mit Kritik:</strong> Antwortet der Anbieter sachlich auf negative Bewertungen – oder gar nicht?',
            '<strong>Hinweise der Plattform:</strong> Trustpilot kennzeichnet Profile, bei denen gefälschte Bewertungen festgestellt wurden. Lesen Sie diese Hinweise.')),
        ('warnsignale', 'Die häufigsten Warnsignale in IPTV-Erfahrungsberichten', table(['Erfahrungsbericht nennt…', 'Was das bedeutet'], [
            ['„Seit dem Wochenende geht nichts mehr“', 'Serverausfälle unter Last – testen Sie zur Hauptsendezeit'],
            ['„Support antwortet nach der Zahlung nicht mehr“', 'Das wichtigste Warnsignal überhaupt'],
            ['„Lifetime-Zugang nach drei Monaten weg“', 'Lifetime-Angebote sind selten nachhaltig – siehe <a href="/iptv-kaufen/">IPTV kaufen</a>'],
            ['„Abo hat sich verlängert“', 'Automatische Verlängerung, die vorher nicht klar war'],
            ['„Nur mit bestimmter App“', 'Eingeschränkte Gerätewahl – vorher Ihr Gerät prüfen'],
        ], 'Warnsignale in IPTV Erfahrungen')),
        ('selbst-testen', 'Eigene Erfahrungen sammeln: der faire Test', steps(
            'Kostenlosen Testzugang auf dem Gerät einrichten, das Sie wirklich nutzen.',
            'Mindestens einen Abend zur Hauptsendezeit schauen, idealerweise mit Live-Sport.',
            'Umschaltzeiten, Programmführer und Bildqualität notieren.',
            'Dem Support eine echte Frage stellen und die Antwortzeit messen.',
            'Die Ergebnisse mit der Bewertungsmatrix im <a href="/iptv-anbieter-vergleich/">IPTV-Anbieter-Vergleich</a> auswerten.') + '''
<p>Genau dafür bieten wir den <a href="/kostenlos-testen/">kostenlosen IPTV-Test</a> an – ohne Zahlungsdaten. Sammeln Sie Ihre eigene Erfahrung, bevor Sie sich auf fremde verlassen.</p>'''),
    ],
    faq=[
        ('Wo finde ich ehrliche IPTV Erfahrungen?', 'In Foren und auf Reddit finden Sie ehrliche Berichte zu Apps, Geräten und typischen Problemen. Zu einzelnen Anbietern sind Bewertungsportale aussagekräftiger, wenn Sie auf zeitliche Häufungen und die Reaktionen auf Kritik achten. Am verlässlichsten ist ein eigener Test.'),
        ('Warum nennt auf Reddit niemand IPTV-Anbieter?', 'In vielen IPTV-Communities auf Reddit ist das Nennen und Anfragen von Anbietern verboten, um Werbung und Spam zu unterbinden. Wer per Direktnachricht Anbieter empfiehlt, verkauft häufig selbst.'),
        ('Sind Trustpilot-Bewertungen von IPTV-Anbietern echt?', 'Nicht immer. Achten Sie auf viele Bewertungen an wenigen Tagen, Profile mit nur einer Bewertung und Hinweise von Trustpilot auf gefälschte Bewertungen. Konkrete Berichte mit Gerät und Situation sind glaubwürdiger.'),
        ('Gibt es ein deutsches IPTV Forum?', 'Für Kodi ist Kodinerds das bekannteste deutschsprachige Forum. Daneben gibt es Technikforen zu Receivern und Android-Boxen. Anbieterempfehlungen finden Sie dort selten, dafür gute Hilfe bei der Einrichtung.'),
    ],
    related=['iptv-anbieter-vergleich', 'iptv-anbieter', 'kodi-iptv', 'iptv-kaufen', 'iptv-smarters-pro', 'was-ist-iptv'],
    card=('IPTV Erfahrungen', 'Foren, Reddit und Trustpilot richtig lesen – und selbst testen.'),
))

# ---------------------------------------------------------------- Senderliste
PAGES.append(dict(
    slug='iptv-senderliste', parent='ratgeber', kind='guide',
    title='IPTV Senderliste: alle Sender finden, sortieren & EPG nutzen',
    description='IPTV Senderliste verstehen: So finden Sie deutsche Sender in Ihrer Playlist, blenden Länder aus, legen Favoriten an und verknüpfen den Programmführer (EPG).',
    eyebrow='IPTV-GRUNDLAGEN', h1='IPTV Senderliste: alle Sender finden und sortieren',
    lead='Eine IPTV-Senderliste mit tausenden Kanälen ist schnell unübersichtlich. Mit ein paar Handgriffen in Ihrer App haben Sie die deutschen Sender, die Sie wirklich schauen, auf den ersten Plätzen.',
    answer='Die IPTV-Senderliste ist die Liste aller Kanäle in Ihrem Zugang, sortiert nach Gruppen wie Ländern oder Themen. In Apps wie TiviMate, IPTV Smarters Pro oder Smart IPTV blenden Sie nicht benötigte Gruppen aus, legen deutsche Sender als Favoriten an und verknüpfen den Programmführer (EPG). Welche Sender Ihr Zugang enthält, sehen Sie schon im kostenlosen Test.',
    sections=[
        ('aufbau', 'Wie eine IPTV-Senderliste aufgebaut ist', '''
<p>Jeder Sender in Ihrer Playlist gehört zu einer <strong>Gruppe</strong> (auch Kategorie). Die Gruppen sind meist nach Ländern und Themen geordnet, etwa „Deutschland | Vollprogramme“, „Deutschland | Nachrichten“, „Deutschland | Kinder“, „Österreich“, „Schweiz“ oder internationale Länder. In einer <a href="/m3u-playlist/">M3U-Playlist</a> steht diese Zuordnung im Feld <code>group-title</code>; bei Xtream-Codes-Logins liefert der Server sie automatisch.</p>
<p>Zu jedem Sender gehören außerdem ein Name, ein Logo und eine <strong>EPG-ID</strong>, über die die App den passenden Programmführer zuordnet. Stimmen diese Angaben, sehen Sie zu jedem Kanal, was gerade läuft und was als Nächstes kommt.</p>'''),
        ('deutsche-sender', 'Deutsche Sender in der Senderliste', table(['Gruppe', 'Typische Inhalte'], [
            ['Öffentlich-rechtliche Vollprogramme', 'Das Erste, ZDF und weitere bundesweite Programme'],
            ['Dritte Programme', 'Regionale Programme der ARD-Anstalten'],
            ['Private Vollprogramme', 'Unterhaltung, Serien, Shows'],
            ['Nachrichten &amp; Dokumentation', 'Nachrichtenkanäle, Wissen, Natur, Geschichte'],
            ['Kinder &amp; Familie', 'Zeichentrick und Familienprogramm'],
            ['Sport', 'Sportnachrichten und Übertragungen'],
            ['Österreich &amp; Schweiz', 'Programme aus dem deutschsprachigen Ausland'],
        ], 'Typische deutsche Sendergruppen') + '''
<p>Sender in anderen Sprachen finden Sie in eigenen Gruppen; Tipps dazu in unseren Ratgebern zu <a href="/iptv-tuerkisch/">türkischen</a>, <a href="/iptv-russisch/">russischsprachigen</a>, <a href="/iptv-rumaenisch/">rumänischen</a>, <a href="/iptv-albanisch/">albanischen</a> und <a href="/iptv-balkan/">Balkan-Sendern</a>.</p>
<p>Die genaue Zusammensetzung hängt vom Zugang ab. Die beste Möglichkeit, Ihre Wunschsender zu prüfen, ist der <a href="/kostenlos-testen/">kostenlose IPTV-Test</a>: Sie sehen die vollständige Senderliste mit allen Gruppen auf Ihrem eigenen Gerät.</p>'''),
        ('sortieren', 'Senderliste sortieren: so geht es in Ihrer App', table(['App', 'Gruppen ausblenden', 'Favoriten anlegen'], [
            ['<a href="/tivimate/">TiviMate</a>', 'Einstellungen → Playlists → Gruppen verwalten', 'Sender lange gedrückt halten → Zu Favoriten (Premium)'],
            ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'Einstellungen → Kategorien bearbeiten / Kindersicherung', 'Sender lange gedrückt halten → Favoriten'],
            ['<a href="/smart-iptv/">Smart IPTV</a>', 'Beim Hochladen nur benötigte Gruppen behalten', 'Sender auswählen → Favoriten'],
            ['<a href="/iptv-pc-mac/">VLC</a>', 'Wiedergabeliste filtern', 'Eigene Wiedergabeliste speichern'],
            ['<a href="/mag-box-iptv/">MAG / Formuler</a>', 'Portal-Einstellungen → Kategorien', 'Favoriten-Taste der Fernbedienung'],
        ], 'Senderliste sortieren nach App') + tip('Blenden Sie zuerst alle Ländergruppen aus, die Sie nie nutzen. Das macht die Senderliste nicht nur übersichtlicher, die App lädt auch schneller.')),
        ('epg', 'Programmführer (EPG) mit der Senderliste verbinden', steps(
            '<b>Xtream-Codes-Login:</b> Der Programmführer kommt automatisch mit. Nach dem ersten Start einmal „EPG aktualisieren“ wählen.',
            '<b>M3U-Link:</b> Falls kein Programm angezeigt wird, in der App zusätzlich die XMLTV-/EPG-Adresse Ihres Anbieters eintragen.',
            '<b>Zeitzone prüfen:</b> Auf Europa/Berlin stellen; sonst sind alle Sendungen um Stunden verschoben.',
            '<b>Fehlende Zuordnung:</b> In TiviMate lässt sich einem Sender manuell ein EPG-Kanal zuweisen.')
         + '''<p>Die Unterschiede zwischen M3U und Xtream Codes erklärt der Ratgeber <a href="/xtream-codes-iptv/">Xtream Codes &amp; XCIPTV</a>.</p>'''),
        ('playlist-deutsch', 'IPTV Playlist auf Deutsch: was Sie beachten sollten', '''
<p>Viele suchen nach einer „IPTV Playlist deutsch“ oder einer Liste mit „allen Sendern“. Kostenlose Listen aus dem Netz enthalten meist Streams ohne Erlaubnis der Rechteinhaber, fallen nach Tagen aus und haben keinen Programmführer. Eine stabile deutsche Senderliste bekommen Sie nur über einen Anbieter, der die Server betreibt und pflegt. Hintergründe dazu finden Sie unter <a href="/m3u-playlist/">M3U Playlist</a> und <a href="/was-ist-iptv/">Was ist IPTV?</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Wie finde ich die deutschen Sender in meiner IPTV-Senderliste?', 'Öffnen Sie in der App die Gruppen- oder Kategorieansicht und wählen Sie die Gruppen mit „Deutschland“ oder „DE“. Blenden Sie andere Länder aus und legen Sie Ihre Lieblingssender als Favoriten an.'),
        ('Enthält ein IPTV-Zugang alle Sender?', 'Kein Zugang enthält „alle“ Sender der Welt. Welche Sender und Gruppen in Ihrem Zugang enthalten sind, sehen Sie im kostenlosen Test vollständig auf Ihrem eigenen Gerät.'),
        ('Warum zeigt meine Senderliste kein Programm an?', 'Meist fehlt die EPG-Adresse (bei M3U-Listen) oder die Zeitzone stimmt nicht. Aktualisieren Sie den Programmführer, prüfen Sie die Zeitzone und tragen Sie bei M3U die XMLTV-Adresse Ihres Anbieters ein.'),
        ('Kann ich die Reihenfolge der Sender ändern?', 'Ja. In den meisten Apps legen Sie Favoritenlisten in eigener Reihenfolge an. TiviMate erlaubt mit Premium zusätzlich das freie Sortieren aller Sender.'),
    ],
    related=['m3u-playlist', 'xtream-codes-iptv', 'tivimate', 'iptv-smarters-pro', 'was-ist-iptv', 'iptv-kaufen'],
    card=('IPTV Senderliste', 'Deutsche Sender finden, Gruppen ausblenden, Favoriten und EPG.'),
))
