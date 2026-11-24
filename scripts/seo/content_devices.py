"""Device pages (protected device keywords)."""
from .helpers import steps, checks, tip, table, proscons

PAGES = []

LOGIN_TIP = tip('Testen Sie IPTV Kanal zuerst auf genau diesem Gerät: Den <a href="/kostenlos-testen/">kostenlosen Testzugang</a> erhalten Sie ohne Zahlungsdaten, auf Wunsch mit Einrichtungshilfe per WhatsApp.', 'Hinweis')

# ---------------------------------------------------------------- Hub
PAGES.append(dict(
    slug='iptv-geraete', parent='ratgeber', kind='hub', hub='geraete',
    title='IPTV Geräte: Smart TV, Fire TV, Box & Handy im Überblick',
    description='Auf welchen Geräten läuft IPTV? Smart TV (Samsung, LG), Fire TV Stick, Android-Box, MAG, Receiver, Apple TV, iPhone und PC – mit passender App und Anleitung.',
    eyebrow='GERÄTE & EINRICHTUNG', h1='IPTV Geräte: Was Sie brauchen',
    lead='IPTV läuft auf fast jedem Bildschirm, den Sie schon besitzen. Finden Sie Ihr Gerät, die passende App und eine Schritt-für-Schritt-Anleitung.',
    answer='IPTV funktioniert auf Smart-TVs von Samsung und LG, dem Fire TV Stick, Android-TV-Boxen, MAG-Boxen, Enigma2-Receivern, Apple TV, iPhone, iPad, Android-Smartphones sowie Windows-PC und Mac. Für den Fernseher ist ein Fire TV Stick mit Fire OS oder eine Android-TV-Box die flexibelste Lösung, weil dort die meisten IPTV Apps laufen.',
    sections=[
        ('uebersicht', 'Welches Gerät für IPTV?', table(['Gerät', 'Empfohlene App', 'Für wen?'], [
            ['<a href="/iptv-fire-tv-stick/">Fire TV Stick</a>', 'TiviMate, IPTV Smarters Pro', 'Günstig, alle Apps, jeder Fernseher'],
            ['<a href="/iptv-samsung-tv/">Samsung Smart TV</a>', 'SET IPTV, Flix IPTV, Smart IPTV', 'Ohne Zusatzgerät'],
            ['<a href="/iptv-lg-tv/">LG Smart TV</a>', 'SS IPTV, Smart IPTV, Flix IPTV', 'Ohne Zusatzgerät'],
            ['<a href="/iptv-smart-tv/">Hisense, Sony, Philips, Panasonic</a>', 'je nach System', 'Andere TV-Marken'],
            ['<a href="/iptv-stick/">IPTV Stick (Google TV, Xiaomi)</a>', 'TiviMate, Smarters', 'Klein, günstig, jeder HDMI-Fernseher'],
            ['<a href="/iptv-box/">Android-TV-Box</a>', 'TiviMate, Smarters', 'Maximale Leistung, 4K'],
            ['<a href="/formuler-iptv/">Formuler Box</a>', 'MyTVOnline 3', 'Receiver-Bedienung mit Android'],
            ['<a href="/mag-box-iptv/">MAG-Box</a>', 'Integriertes Portal', 'Bedienung wie Receiver'],
            ['<a href="/iptv-receiver/">Enigma2-Receiver</a>', 'Plugins', 'Sat + IPTV kombiniert'],
            ['<a href="/iptv-apple-tv-iphone/">Apple TV, iPhone, iPad</a>', 'IPTVX, Smarters Player Lite', 'Apple-Nutzer'],
            ['<a href="/iptv-android/">Android-Handy, Google TV</a>', 'Smarters, TiviMate (TV)', 'Unterwegs und Google TV'],
            ['<a href="/iptv-pc-mac/">PC &amp; Mac</a>', 'VLC, Smarters Desktop', 'Am Schreibtisch'],
        ], 'IPTV Geräte im Überblick')),
        ('empfehlung', 'Unsere Empfehlung für den Fernseher', '''
<p>Wenn Ihr Fernseher keine passende App bietet oder Sie den größten Komfort möchten, ist ein <a href="/iptv-fire-tv-stick/">Fire TV Stick 4K</a> mit Fire OS oder eine <a href="/iptv-box/">Android-TV-Box</a> die beste Wahl: TiviMate, IPTV Smarters und fast alle anderen <a href="/iptv-apps/">IPTV Apps</a> laufen dort. Achten Sie beim Kauf neuer Fire-TV-Modelle darauf, dass sie noch Fire OS nutzen – Geräte mit Vega OS erlauben keine IPTV-Apps außerhalb des Amazon Appstores.</p>'''),
        ('mehrere', 'IPTV auf mehreren Geräten gleichzeitig', '''
<p>Mit einem IPTV-Kanal-Paket für 2 bis 5 Geräte schauen mehrere Personen gleichzeitig – etwa Wohnzimmer-TV, Kinderzimmer-Stick und Tablet. Die Preise stehen unter <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>'''),
    ],
    faq=[
        ('Welches Gerät ist am besten für IPTV?', 'Für den Fernseher ein Fire TV Stick 4K mit Fire OS oder eine Android-TV-Box, weil dort die meisten IPTV Apps laufen. Samsung- und LG-Fernseher funktionieren auch ohne Zusatzgerät mit Apps wie SET IPTV oder Flix IPTV.'),
        ('Brauche ich eine IPTV Box?', 'Nicht unbedingt. Smart-TVs, Smartphones und Computer reichen. Eine Box oder ein Stick lohnt sich, wenn Ihr Fernseher keine passende App hat oder Sie bessere Leistung möchten.'),
        ('Kann ich IPTV auf einem alten Fernseher schauen?', 'Ja. Jeder Fernseher mit HDMI-Anschluss wird mit einem Fire TV Stick oder einer Android-Box IPTV-fähig.'),
        ('Wie viele Geräte kann ich mit einem Abo nutzen?', 'Bei IPTV Kanal wählen Sie 1 bis 5 gleichzeitig nutzbare Geräte. Die Geräteanzahl bestimmt, wie viele Streams parallel laufen.'),
    ],
    related=['iptv-apps', 'iptv-fire-tv-stick', 'iptv-smart-tv', 'iptv-box', 'iptv-4k', 'iptv-kaufen'],
    card=('IPTV Geräte', 'Smart TV, Stick, Box, Handy und PC – mit passender App.'),
))

# ---------------------------------------------------------------- Fire TV
PAGES.append(dict(
    slug='iptv-fire-tv-stick', parent='geraete', kind='guide',
    title='IPTV auf dem Fire TV Stick: Anleitung 2026 (Fire OS & Vega)',
    description='IPTV auf dem Fire TV Stick einrichten: Downloader, TiviMate oder IPTV Smarters installieren, Login eintragen – und welche Modelle mit Vega OS nicht gehen.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf dem Fire TV Stick: Anleitung 2026',
    lead='Der Amazon Fire TV Stick ist der beliebteste Weg zu IPTV am Fernseher. Seit Amazon neue Modelle mit Vega OS ausliefert, kommt es aber auf das richtige Gerät an.',
    answer='Auf einem Fire TV Stick mit Fire OS installieren Sie IPTV in vier Schritten: Entwickleroptionen aktivieren, die App Downloader installieren, damit eine IPTV App wie TiviMate oder IPTV Smarters Pro laden und Ihre Zugangsdaten eintragen. Neuere Modelle mit Vega OS, etwa der Fire TV Stick 4K Select, erlauben keine Installation von Apps außerhalb des Amazon Appstores.',
    sections=[
        ('modelle', 'Welcher Fire TV Stick eignet sich für IPTV?', table(['Modell', 'System', 'IPTV-Apps installierbar?'], [
            ['Fire TV Stick 4K Max (2. Gen.)', 'Fire OS', 'Ja – erste Wahl'],
            ['Fire TV Stick 4K (2. Gen.)', 'Fire OS', 'Ja'],
            ['Fire TV Stick (3. Gen.) / Lite', 'Fire OS', 'Ja, nur Full HD'],
            ['Fire TV Cube (3. Gen.)', 'Fire OS', 'Ja, viel Leistung'],
            ['Fire TV Stick 4K Select', 'Vega OS', 'Nein'],
            ['Neuere Modelle mit Vega OS (z. B. Fire TV Stick HD neue Generation)', 'Vega OS', 'Nein'],
        ], 'Fire TV Modelle und IPTV') + '''
<p>Das System prüfen Sie unter <b>Einstellungen → Mein Fire TV → Info</b>. Steht dort Fire OS, funktioniert die Anleitung unten. Für 4K-Sender brauchen Sie ein 4K-Modell und rund 25 Mbit/s (siehe <a href="/iptv-4k/">IPTV in 4K</a>).</p>'''),
        ('anleitung', 'IPTV auf dem Fire TV Stick installieren', steps(
            '<b>Downloader installieren:</b> Auf der Startseite nach „Downloader“ suchen und die App aus dem Amazon Appstore laden.',
            '<b>Entwickleroptionen freischalten:</b> Einstellungen → Mein Fire TV → Info → siebenmal auf den Gerätenamen klicken.',
            '<b>Unbekannte Apps erlauben:</b> Einstellungen → Mein Fire TV → Entwickleroptionen → Apps unbekannter Herkunft → Downloader aktivieren.',
            '<b>IPTV App laden:</b> In Downloader die offizielle Download-Adresse von <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a> eingeben und installieren. TiviMate ist teils direkt im Appstore gelistet. Ausführlich: <a href="/iptv-smarters-pro-firestick/">IPTV Smarters Pro auf dem Fire TV Stick installieren</a>.',
            '<b>Zugangsdaten eintragen:</b> App öffnen, Xtream-Codes-Login (Server, Benutzername, Passwort) eingeben.',
            '<b>Losschauen:</b> Sender öffnen, Favoriten anlegen, fertig.')
         + tip('Geben Sie in Downloader nur Adressen ein, deren Herkunft Sie kennen. Kurzcodes aus Foren können auf manipulierte Apps verweisen.', 'Sicherheit')),
        ('apps', 'Bester IPTV Player für den Fire TV Stick', table(['App', 'Kosten', 'Stärke'], [
            ['<a href="/tivimate/">TiviMate</a>', 'Kostenlos, Premium optional', 'Bester Programmführer, Aufnahme'],
            ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'Kostenlos', 'Einfacher Einstieg auf Deutsch'],
            ['<a href="/xtream-codes-iptv/">XCIPTV</a>', 'Kostenlos', 'Schnell mit Xtream-Login'],
            ['<a href="/flix-iptv/">Flix IPTV</a>', 'Aktivierung nach Test', 'Modernes Design'],
            ['<a href="/kodi-iptv/">Kodi</a>', 'Kostenlos', 'Mediacenter mit Add-ons'],
        ], 'IPTV Apps für Fire TV')),
        ('vega', 'Vega OS: was tun mit einem neuen Fire TV Stick?', '''
<p>Amazon stellt neue Fire-TV-Geräte schrittweise auf das eigene Betriebssystem Vega OS um. Darauf laufen nur Apps aus dem Amazon Appstore; Downloader und Android-APKs funktionieren nicht. Wenn Sie einen solchen Stick schon besitzen, gibt es drei Wege:</p>
''' + checks(
            'Prüfen, ob eine passende IPTV App im Amazon Appstore für Ihr Gerät verfügbar ist.',
            'Den Stick zurückgeben und ein Fire-OS-Modell wie den Fire TV Stick 4K Max wählen.',
            'Auf eine <a href="/iptv-box/">Android-TV-Box</a> oder einen Google-TV-Stick ausweichen – Vergleich im Ratgeber <a href="/iptv-stick/">IPTV Stick</a>.')),
        ('probleme', 'IPTV ruckelt auf dem Fire TV Stick?', table(['Ursache', 'Lösung'], [
            ['Schwaches WLAN', 'Stick mit HDMI-Verlängerung freier platzieren oder Ethernet-Adapter nutzen'],
            ['Voller Speicher', 'Cache unbenutzter Apps leeren, nicht genutzte Apps löschen'],
            ['Falscher Decoder', 'In TiviMate/Smarters Hardware-Decoder aktivieren'],
            ['Überhitzung', 'Stick nicht hinter dem Fernseher einklemmen, Verlängerung nutzen'],
        ], 'Fire TV IPTV Problemlösungen') + LOGIN_TIP),
    ],
    faq=[
        ('Kann man IPTV auf dem Fire TV Stick schauen?', 'Ja, auf allen Fire-TV-Modellen mit Fire OS. Sie installieren eine IPTV App wie TiviMate oder IPTV Smarters Pro und tragen Ihre Zugangsdaten ein. Modelle mit Vega OS unterstützen keine APK-Installation.'),
        ('Welcher ist der beste IPTV Player für den Fire TV Stick?', 'TiviMate bietet den besten Programmführer, IPTV Smarters Pro den einfachsten kostenlosen Einstieg. Beide laufen auf Fire-OS-Geräten stabil.'),
        ('Welcher Fire TV Stick ist für IPTV am besten?', 'Der Fire TV Stick 4K Max mit Fire OS: genug Leistung, WLAN 6E und 4K. Achten Sie darauf, kein Modell mit Vega OS wie den Fire TV Stick 4K Select zu kaufen.'),
        ('Woran erkenne ich, ob mein Fire TV Vega OS hat?', 'Unter Einstellungen → Mein Fire TV → Info wird das Betriebssystem angezeigt. Bei Vega OS fehlen außerdem die Entwickleroptionen für Apps unbekannter Herkunft.'),
        ('Ist IPTV auf dem Fire TV Stick legal?', 'Die Apps und die Installation sind legal. Entscheidend ist, dass Ihr IPTV-Anbieter die Inhalte rechtmäßig bereitstellt.'),
    ],
    related=['iptv-smarters-pro-firestick', 'tivimate', 'iptv-stick', 'iptv-4k', 'iptv-box', 'iptv-geraete'],
    card=('Fire TV Stick', 'IPTV mit Downloader, TiviMate oder Smarters – inklusive Vega-OS-Check.'),
))

# ---------------------------------------------------------------- Smart TV (generic + other brands)
PAGES.append(dict(
    slug='iptv-smart-tv', parent='geraete', kind='guide',
    title='IPTV auf dem Smart TV: Samsung, LG, Hisense, Sony & Co.',
    description='IPTV auf dem Smart TV: die passende App für Samsung, LG, Hisense VIDAA, Sony, Philips, Panasonic, Toshiba und Roku – und wann ein Stick besser ist.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf dem Smart TV',
    lead='Ob Samsung, LG, Hisense, Sony oder Philips: Fast jeder Smart TV kann IPTV. Welche App funktioniert, hängt vom Betriebssystem Ihres Fernsehers ab.',
    answer='Für IPTV auf dem Smart TV entscheidet das Betriebssystem: Samsung (Tizen) und LG (webOS) nutzen Player wie SET IPTV, Flix IPTV oder Smart IPTV. Sony, Philips, TCL und viele andere mit Google TV oder Android TV können TiviMate und IPTV Smarters installieren. Hisense (VIDAA), Roku und ältere Modelle haben wenig Auswahl – dort ist ein Fire TV Stick die einfachste Lösung.',
    sections=[
        ('system', 'Welches System hat Ihr Fernseher?', table(['Marke', 'System', 'Passende IPTV Apps'], [
            ['<a href="/iptv-samsung-tv/">Samsung</a>', 'Tizen', 'SET IPTV, Flix IPTV, Smart IPTV, IBO Player'],
            ['<a href="/iptv-lg-tv/">LG</a>', 'webOS', 'SS IPTV, Smart IPTV, Flix IPTV, SET IPTV'],
            ['Sony Bravia', 'Google TV / Android TV', '<a href="/tivimate/">TiviMate</a>, <a href="/iptv-smarters-pro/">Smarters</a>'],
            ['Philips', 'Google TV, Android TV oder Titan OS', 'Android-Modelle: TiviMate, Smarters'],
            ['TCL', 'Google TV', 'TiviMate, Smarters'],
            ['Hisense', 'VIDAA', 'Kleine Auswahl, Stick empfohlen'],
            ['Panasonic', 'Fire TV OS oder my Home Screen', 'Fire-TV-Modelle: wie <a href="/iptv-fire-tv-stick/">Fire TV</a>'],
            ['Toshiba', 'Fire TV, VIDAA oder Android', 'Je nach Modell'],
            ['Roku', 'Roku OS', 'Kaum IPTV-Player, Stick empfohlen'],
        ], 'Smart-TV-Systeme und IPTV Apps') + '''
<p>Das System finden Sie in den Einstellungen unter „Info“ oder „Über dieses Gerät“, oder am Startbildschirm: Google TV zeigt eine Leiste „Für dich“, Fire TV die Amazon-Oberfläche.</p>'''),
        ('android', 'Sony, Philips &amp; TCL: Google TV und Android TV', '''
<p>Fernseher mit Google TV oder Android TV sind für IPTV ideal: Im Google Play Store finden Sie IPTV Smarters, TiviMate, Kodi und weitere Player. Die Einrichtung entspricht der auf einer <a href="/iptv-box/">Android-TV-Box</a> oder auf <a href="/iptv-android/">Android und Google TV</a>.</p>'''),
        ('hisense', 'Hisense VIDAA, Roku und Titan OS', '''
<p>Auf Hisense-Fernsehern mit VIDAA, auf Roku-Geräten und auf Philips-Modellen mit Titan OS ist die Auswahl an IPTV-Playern klein und wechselt häufig. Die zuverlässigste Lösung ist ein <a href="/iptv-fire-tv-stick/">Fire TV Stick mit Fire OS</a> oder ein Google TV Streamer am HDMI-Anschluss – kostet wenig und bietet alle Apps.</p>'''),
        ('anleitung', 'Allgemeine Anleitung für jeden Smart TV', steps(
            'System des Fernsehers prüfen (Tabelle oben).',
            'Passende App aus dem App-Store des Fernsehers installieren.',
            'Bei MAC-basierten Apps die MAC-Adresse notieren und die Playlist auf der Website des Entwicklers hochladen.',
            'Bei Xtream-fähigen Apps Server, Benutzername und Passwort direkt eingeben.',
            'Fernseher per LAN-Kabel verbinden, damit auch <a href="/iptv-4k/">4K</a> stabil läuft.')),
        ('vergleich', 'Smart-TV-App oder Stick?', proscons(
            ['Kein Zusatzgerät, eine Fernbedienung', 'Integrierter Tuner für 4K-HDR', 'LAN-Anschluss meist vorhanden'],
            ['Weniger App-Auswahl', 'Viele Player kostenpflichtig nach Test', 'Ältere TVs werden langsam'],
            'Vorteile Smart-TV-App', 'Nachteile Smart-TV-App') + LOGIN_TIP),
    ],
    faq=[
        ('Kann jeder Smart TV IPTV?', 'Fast jeder, aber nicht mit jeder App. Samsung und LG nutzen eigene Player, Google-TV-Modelle die bekannten Android-Apps. Für Fernseher mit wenig Auswahl ist ein Fire TV Stick die einfachste Lösung.'),
        ('Welche IPTV App für Hisense VIDAA?', 'Die Auswahl im VIDAA-Store ist klein und ändert sich. Am zuverlässigsten ist ein Fire TV Stick oder ein Google TV Streamer am HDMI-Anschluss.'),
        ('Funktioniert IPTV auf Roku?', 'Auf Roku-Geräten gibt es kaum IPTV-Player. Wer einen Roku-Fernseher nutzt, schließt für IPTV am besten einen Fire TV Stick an.'),
        ('Wie bekomme ich IPTV auf einen Sony- oder Philips-Fernseher?', 'Bei Google TV oder Android TV installieren Sie IPTV Smarters oder TiviMate aus dem Play Store und tragen Ihre Zugangsdaten ein.'),
    ],
    related=['iptv-samsung-tv', 'iptv-lg-tv', 'iptv-fire-tv-stick', 'iptv-android', 'smart-iptv', 'iptv-geraete'],
    card=('Smart TV', 'Die passende App für jede Fernsehermarke.'),
))

# ---------------------------------------------------------------- Samsung
PAGES.append(dict(
    slug='iptv-samsung-tv', parent='geraete', kind='guide',
    title='IPTV auf Samsung Smart TV (Tizen): beste Apps & Anleitung',
    description='IPTV auf dem Samsung Smart TV (Tizen): die besten Apps wie SET IPTV, Flix IPTV und Smart IPTV, Anleitung Schritt für Schritt und Lösungen bei Problemen.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf dem Samsung Smart TV',
    lead='Samsung-Fernseher laufen mit Tizen. TiviMate gibt es dort nicht – dafür eine Reihe guter IPTV Player, die Sie in wenigen Minuten einrichten.',
    answer='Für IPTV auf dem Samsung Smart TV installieren Sie einen Tizen-kompatiblen Player wie SET IPTV, Flix IPTV oder IBO Player aus dem Samsung App-Store, notieren die angezeigte MAC-Adresse und laden Ihre M3U-Playlist auf der Website des Entwicklers hoch. Alternativ schließen Sie einen Fire TV Stick an und nutzen TiviMate oder IPTV Smarters.',
    sections=[
        ('apps', 'Die besten IPTV Apps für Samsung (Tizen)', table(['App', 'Login', 'Kosten', 'Anleitung'], [
            ['SET IPTV', 'M3U per MAC', 'Aktivierung nach Test', '<a href="/set-iptv/">SET IPTV</a>'],
            ['Flix IPTV', 'M3U per MAC', 'Aktivierung nach Test', '<a href="/flix-iptv/">Flix IPTV</a>'],
            ['Smart IPTV', 'M3U per MAC', 'Aktivierung nach Test', '<a href="/smart-iptv/">Smart IPTV</a>'],
            ['SmartOne IPTV', 'M3U per MAC', 'Aktivierung nach Test', '<a href="/smartone-iptv/">SmartOne</a>'],
            ['IPTV Smarters', 'Xtream / M3U', 'Je nach Region', '<a href="/iptv-smarters-pro/">Smarters</a>'],
        ], 'IPTV Apps für Samsung Smart TV') + '''
<p>Die Verfügbarkeit hängt vom Modelljahr und der Region ab. Suchen Sie im Samsung-App-Store (Smart Hub → Apps → Lupe) nach dem Namen.</p>'''),
        ('anleitung', 'IPTV auf Samsung TV einrichten', steps(
            'Fernbedienung: <b>Home → Apps → Suche</b> und „SET IPTV“ oder „Flix IPTV“ eingeben.',
            'App installieren und öffnen; die angezeigte <b>MAC-Adresse</b> notieren.',
            'Am Handy die Upload-Seite des App-Entwicklers öffnen.',
            'MAC-Adresse und <a href="/m3u-playlist/">M3U-Link</a> eintragen und speichern.',
            'App am Fernseher neu starten. Sender und Programmführer erscheinen.')),
        ('stick', 'Alternative: Fire TV Stick am Samsung TV', '''
<p>Wer <a href="/tivimate/">TiviMate</a> oder die volle Auswahl an Apps möchte, steckt einen <a href="/iptv-fire-tv-stick/">Fire TV Stick mit Fire OS</a> in einen HDMI-Anschluss. Per HDMI-CEC steuern Sie ihn sogar mit der Samsung-Fernbedienung.</p>'''),
        ('probleme', 'Häufige Probleme auf Samsung-Fernsehern', table(['Problem', 'Lösung'], [
            ['App nicht im Store', 'Anderen Player wählen oder Fire TV Stick nutzen'],
            ['Bild ruckelt', 'LAN statt WLAN, im Player den Puffer erhöhen'],
            ['Kein Ton bei manchen Sendern', 'Audioausgabe auf PCM stellen (Einstellungen → Ton → Experteneinstellungen)'],
            ['Senderliste veraltet', 'Playlist auf der Website neu speichern, App neu starten'],
        ], 'Samsung TV IPTV Problemlösungen') + LOGIN_TIP),
    ],
    faq=[
        ('Welche IPTV App ist die beste für Samsung Smart TV?', 'Beliebt sind SET IPTV, Flix IPTV und Smart IPTV. Welche verfügbar ist, hängt vom Modelljahr ab. Für TiviMate brauchen Sie einen Fire TV Stick.'),
        ('Gibt es TiviMate für Samsung TV?', 'Nein. TiviMate läuft nur auf Android-TV-Systemen. Am Samsung-Fernseher nutzen Sie dafür einen Fire TV Stick oder eine Android-Box.'),
        ('Kann ich IPTV Smarters Pro auf Samsung TV installieren?', 'Je nach Modell und Region gibt es eine Smarters-App im Samsung-Store. Ist sie nicht verfügbar, funktionieren SET IPTV oder Flix IPTV mit Ihrem M3U-Link.'),
        ('Funktioniert IPTV auf älteren Samsung-Fernsehern?', 'Modelle ab etwa 2017 mit Tizen unterstützen die meisten Player. Bei älteren Geräten ist ein Fire TV Stick die bessere Wahl.'),
    ],
    related=['iptv-lg-tv', 'set-iptv', 'flix-iptv', 'smart-iptv', 'iptv-fire-tv-stick', 'iptv-smart-tv'],
    card=('Samsung Smart TV', 'Die besten Tizen-Apps und Anleitung für Samsung.'),
))

# ---------------------------------------------------------------- LG
PAGES.append(dict(
    slug='iptv-lg-tv', parent='geraete', kind='guide',
    title='IPTV auf LG Smart TV (webOS): Apps & Anleitung',
    description='IPTV auf dem LG Smart TV mit webOS: SS IPTV, Smart IPTV, Flix IPTV und SET IPTV im LG Content Store installieren und einrichten – Schritt für Schritt.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf dem LG Smart TV',
    lead='LG-Fernseher mit webOS gehören zu den IPTV-freundlichsten Smart-TVs. Im LG Content Store finden Sie mehrere bewährte Player.',
    answer='Auf LG Smart TVs mit webOS installieren Sie IPTV-Player wie SS IPTV, Smart IPTV, Flix IPTV oder SET IPTV aus dem LG Content Store. Bei SS IPTV verbinden Sie Ihre M3U-Playlist per Code, bei den anderen über die MAC-Adresse auf der Entwickler-Website. Für TiviMate brauchen Sie einen Fire TV Stick.',
    sections=[
        ('apps', 'IPTV Apps für LG webOS', table(['App', 'Verknüpfung', 'Kosten', 'Anleitung'], [
            ['SS IPTV', 'Code', 'Kostenlos mit Werbung', '<a href="/ss-iptv/">SS IPTV</a>'],
            ['Smart IPTV', 'MAC-Adresse', 'Aktivierung nach Test', '<a href="/smart-iptv/">Smart IPTV</a>'],
            ['Flix IPTV', 'MAC-Adresse', 'Aktivierung nach Test', '<a href="/flix-iptv/">Flix IPTV</a>'],
            ['SET IPTV', 'MAC-Adresse', 'Aktivierung nach Test', '<a href="/set-iptv/">SET IPTV</a>'],
            ['IPTV Smarters', 'Xtream / M3U', 'Je nach Region', '<a href="/iptv-smarters-pro/">Smarters</a>'],
        ], 'IPTV Apps für LG Smart TV')),
        ('anleitung', 'IPTV auf LG TV einrichten', steps(
            '<b>Home-Taste</b> drücken und den <b>LG Content Store</b> (Apps) öffnen.',
            'Nach „SS IPTV“, „Smart IPTV“ oder „Flix IPTV“ suchen und installieren.',
            'App öffnen: Bei SS IPTV in den Einstellungen einen Code erzeugen, bei den anderen die MAC-Adresse notieren.',
            'Auf der Website des Entwicklers Code bzw. MAC-Adresse und Ihren <a href="/m3u-playlist/">M3U-Link</a> eingeben.',
            'App neu starten und Sender aufrufen.')),
        ('tipps', 'Tipps für LG-Fernseher', checks(
            'Unter <b>Allgemein → Netzwerk</b> per LAN verbinden – webOS-Fernseher haben oft nur 2,4-GHz-WLAN-Leistung im Randbereich.',
            '„Quick Start+“ deaktivieren, wenn Apps nach dem Einschalten hängen.',
            'Bei Tonproblemen die Audioausgabe auf PCM stellen.',
            'Für <a href="/iptv-4k/">4K-Sender</a> mindestens 25 Mbit/s einplanen.') + LOGIN_TIP),
    ],
    faq=[
        ('Welche IPTV App ist die beste für LG TV?', 'Kostenlos ist SS IPTV, komfortabler sind Flix IPTV und SET IPTV. Smart IPTV ist ebenfalls weit verbreitet. Alle finden Sie im LG Content Store.'),
        ('Gibt es TiviMate für LG webOS?', 'Nein. Für TiviMate schließen Sie einen Fire TV Stick mit Fire OS oder eine Android-TV-Box an den LG-Fernseher an.'),
        ('Wie lade ich eine M3U-Liste auf meinen LG TV?', 'Über die IPTV-App: Bei SS IPTV per Verbindungscode im Playlist-Editor, bei Smart IPTV, Flix IPTV oder SET IPTV über die MAC-Adresse auf der jeweiligen Website.'),
    ],
    related=['iptv-samsung-tv', 'ss-iptv', 'smart-iptv', 'flix-iptv', 'iptv-fire-tv-stick', 'iptv-smart-tv'],
    card=('LG Smart TV', 'webOS-Apps wie SS IPTV und Flix IPTV einrichten.'),
))

# ---------------------------------------------------------------- Android / Google TV / Chromecast
PAGES.append(dict(
    slug='iptv-android', parent='geraete', kind='guide',
    title='IPTV auf Android, Google TV & Chromecast: Apps & Anleitung',
    description='IPTV auf Android-Smartphone, Tablet, Google TV und Chromecast: die besten IPTV Player für Android, Einrichtung und Streaming auf den Fernseher.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf Android, Google TV und Chromecast',
    lead='Android ist die flexibelste Plattform für IPTV: Fast jede App ist verfügbar, auf dem Handy für unterwegs und auf Google TV für das Wohnzimmer.',
    answer='Auf Android-Smartphones und Tablets installieren Sie IPTV Smarters Pro, XCIPTV oder OTT Navigator aus dem Play Store und tragen Ihren Xtream-Codes-Login ein. Auf Google TV, Android TV und Chromecast mit Google TV ist zusätzlich TiviMate verfügbar. Vom Handy übertragen Sie Streams per Chromecast-Symbol auf den Fernseher.',
    sections=[
        ('apps', 'Beste IPTV Player für Android', table(['App', 'Handy/Tablet', 'Google TV / Android TV'], [
            ['<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>', 'Ja', 'Ja'],
            ['<a href="/tivimate/">TiviMate</a>', 'Nein', 'Ja'],
            ['<a href="/xtream-codes-iptv/">XCIPTV</a>', 'Ja', 'Ja'],
            ['OTT Navigator', 'Ja', 'Ja'],
            ['<a href="/kodi-iptv/">Kodi</a>', 'Ja', 'Ja'],
            ['<a href="/mag-box-iptv/">STBEmu</a>', 'Ja', 'Ja'],
            ['VLC', 'Ja', 'Ja'],
        ], 'IPTV Apps für Android')),
        ('handy', 'IPTV auf dem Android-Handy einrichten', steps(
            'Play Store öffnen und „IPTV Smarters Pro“ oder „XCIPTV“ installieren.',
            'App öffnen und „Xtream Codes“ als Login wählen.',
            'Server-URL, Benutzername und Passwort eintragen.',
            'Senderliste laden und Favoriten setzen.',
            'Unterwegs: In der App die Streamqualität reduzieren, um mobile Daten zu sparen.')),
        ('google-tv', 'Google TV, Android TV und Chromecast', '''
<p>Der Chromecast mit Google TV und sein Nachfolger Google TV Streamer sind vollwertige Android-TV-Geräte: Sie installieren TiviMate oder Smarters direkt aus dem Play Store. Auch Fernseher von Sony, TCL und viele Philips-Modelle laufen mit Google TV – siehe <a href="/iptv-smart-tv/">IPTV auf dem Smart TV</a>.</p>
<p>Ein älterer Chromecast ohne Fernbedienung kann keine Apps installieren. Dort öffnen Sie den Stream auf dem Handy und tippen auf das <strong>Cast-Symbol</strong> – unterstützt von IPTV Smarters und vielen anderen Playern. Welche Sticks sich am besten eignen, zeigt der Ratgeber <a href="/iptv-stick/">IPTV Stick</a>.</p>'''),
        ('box', 'Android-TV-Box für mehr Leistung', '''
<p>Für 4K, viele Sender und schnelle Umschaltzeiten lohnt sich eine leistungsstarke Box wie Nvidia Shield oder Homatics. Mehr dazu im Ratgeber <a href="/iptv-box/">IPTV Box kaufen</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Welche ist die beste IPTV App für Android?', 'Auf dem Handy IPTV Smarters Pro oder XCIPTV, auf Android-TV-Geräten TiviMate. Alle unterstützen Xtream-Codes-Logins und laden Mediathek und EPG automatisch.'),
        ('Kann ich IPTV vom Handy auf den Fernseher streamen?', 'Ja, per Chromecast-Symbol in Apps wie IPTV Smarters. Der Fernseher braucht dafür Chromecast-Unterstützung oder einen Chromecast-Stick.'),
        ('Funktioniert TiviMate auf dem Android-Handy?', 'Nein. TiviMate ist für TV-Geräte gemacht. Auf dem Handy nutzen Sie IPTV Smarters Pro, XCIPTV oder OTT Navigator.'),
        ('Wie viele Daten verbraucht IPTV auf dem Handy?', 'Etwa 1 bis 3 GB pro Stunde in SD bis HD. Für mobile Nutzung empfiehlt sich eine niedrigere Qualitätsstufe oder WLAN.'),
    ],
    related=['iptv-smarters-pro', 'tivimate', 'iptv-box', 'xtream-codes-iptv', 'iptv-smart-tv', 'iptv-geraete'],
    card=('Android & Google TV', 'IPTV auf Handy, Tablet, Google TV und Chromecast.'),
))

# ---------------------------------------------------------------- Box
PAGES.append(dict(
    slug='iptv-box', parent='geraete', kind='guide',
    title='IPTV Box kaufen 2026: Beste Android-TV-Box für IPTV',
    description='Beste IPTV Box 2026: Android-TV-Boxen wie Nvidia Shield, Formuler, Homatics, Ugoos und TVIP im Vergleich – worauf Sie beim IPTV Box Kauf achten sollten.',
    eyebrow='KAUFBERATUNG', h1='IPTV Box: die beste Android-TV-Box für IPTV',
    lead='Eine gute IPTV Box schaltet schnell um, spielt 4K flüssig und lässt Ihnen die freie Wahl der App. Wir zeigen, worauf es ankommt – und welche Modelle sich bewährt haben.',
    answer='Die beste IPTV Box ist eine zertifizierte Android-TV- oder Google-TV-Box mit mindestens 2 GB RAM, LAN-Anschluss und 4K-HEVC-Unterstützung. Bewährt haben sich Nvidia Shield TV, Homatics Box, Formuler-Boxen mit MyTVOnline, Ugoos und TVIP. Wer es klassisch mag, wählt eine MAG-Box. Eine Box enthält keine Sender – diese kommen aus Ihrem IPTV-Abo.',
    sections=[
        ('kriterien', 'Worauf Sie beim IPTV Box Kauf achten sollten', checks(
            '<strong>Zertifiziertes Android TV / Google TV:</strong> nur so sind Play Store und Netflix &amp; Co. offiziell dabei.',
            '<strong>LAN-Anschluss:</strong> stabiler als WLAN, besonders für <a href="/iptv-4k/">4K</a>.',
            '<strong>Mindestens 2 GB RAM und 16 GB Speicher</strong> für flüssige Apps und EPG.',
            '<strong>HEVC/H.265 und HDR</strong> für 4K-Sender.',
            '<strong>Updates:</strong> Hersteller mit regelmäßigen Sicherheitsupdates wählen.')
         + tip('Meiden Sie „vorinstallierte“ IPTV-Boxen mit Gratis-Sendern. Sie sind oft rechtlich problematisch, bekommen keine Updates und enthalten nicht selten Schadsoftware.', 'Achtung')),
        ('modelle', 'Bewährte IPTV Boxen im Überblick', table(['Box', 'System', 'Stärken'], [
            ['Nvidia Shield TV / Pro', 'Android TV', 'Sehr schnell, KI-Upscaling, lange Updates'],
            ['Homatics Box Q / R', 'Google TV / Android TV', 'Zertifiziert, gutes Preis-Leistungs-Verhältnis'],
            ['Formuler Z-Serie (Z8, Z10 Pro, Z11)', 'Android mit MyTVOnline', 'Eigene IPTV-Oberfläche, Fernbedienung mit IPTV-Tasten'],
            ['Ugoos AM-Serie', 'Android', 'Viel Leistung, viele Einstellungen für Bastler'],
            ['TVIP S-Box v.605 / 705', 'Linux / Android', 'Schnelles Umschalten, in Deutschland verbreitet'],
            ['<a href="/mag-box-iptv/">MAG-Boxen</a>', 'Linux / Android', 'Portal-Bedienung wie ein Receiver'],
            ['<a href="/iptv-fire-tv-stick/">Fire TV Cube / 4K Max</a>', 'Fire OS', 'Günstig, kompakt'],
        ], 'IPTV Boxen im Vergleich') + '''
<p>Preise schwanken stark nach Händler und Modelljahr; vergleichen Sie aktuelle Angebote direkt beim Kauf.</p>'''),
        ('formuler', 'Formuler: IPTV Box mit eigener App', '''
<p>Formuler-Boxen (Z Nano, Z Neo, Z+, Z7+, Z8, Z8 Pro, Z10 Pro, Z10 Pro Max, Z11) kommen mit der App <strong>MyTVOnline</strong>, die speziell für IPTV gebaut ist: Sie tragen Ihr Portal oder Ihren Xtream-Login ein und erhalten ein Programmführer-Raster wie beim Receiver. Zusätzlich laufen <a href="/tivimate/">TiviMate</a> und <a href="/iptv-smarters-pro/">Smarters</a>. Modelle, MyTVOnline 3 und Einrichtung erklärt der Ratgeber <a href="/formuler-iptv/">Formuler IPTV Box</a>.</p>'''),
        ('aliexpress', 'IPTV Box von Amazon, AliExpress oder Alibaba?', '''
<p>Günstige IPTV Boxen werden massenhaft bei AliExpress und Alibaba sowie über Marktplatz-Händler bei Amazon angeboten. Viele davon sind technisch brauchbar, aber es gibt typische Fallstricke:</p>
''' + checks(
            '<strong>Kein zertifiziertes Android TV:</strong> Ohne Zertifizierung fehlen oft Play Store, Netflix in HD und Sicherheitsupdates.',
            '<strong>Geschönte Angaben:</strong> „8K“, „Android 14“ oder „32 GB RAM“ stimmen bei Billigboxen häufig nicht.',
            '<strong>Vorinstallierte Apps:</strong> Boxen „mit Sendern“ enthalten meist fragwürdige Apps und teils Schadsoftware.',
            '<strong>CE-Kennzeichen, Garantie und Zoll:</strong> Bei Direktimport aus China fehlen Ansprechpartner in der EU; Einfuhrabgaben kommen hinzu.') + '''
<p>Für einen fairen Preis und Ruhe im Betrieb greifen Sie lieber zu Markengeräten wie einer Google-TV-Box, einem <a href="/iptv-stick/">IPTV Stick</a> mit Fire OS oder Google TV oder einer Formuler. Testberichte großer Technikportale sind beim Vergleich hilfreicher als Sterne auf Marktplätzen.</p>'''),
        ('einrichten', 'IPTV Box einrichten', steps(
            'Box per HDMI mit dem Fernseher und per LAN mit dem Router verbinden.',
            'Mit Google-Konto anmelden und Systemupdates installieren.',
            'IPTV App aus dem Play Store installieren, etwa TiviMate.',
            'Zugangsdaten eintragen (Xtream Codes, M3U oder Portal).',
            'Unter Anzeige die Auflösung auf 4K und „Bildwiederholrate anpassen“ stellen.') + LOGIN_TIP),
        ('receiver', 'IPTV Box oder Receiver?', '''
<p>Wer zusätzlich Satellit oder Kabel empfangen möchte, ist mit einem <a href="/iptv-receiver/">Enigma2-Receiver</a> besser bedient. Wer nur IPTV schaut, fährt mit einer Android-TV-Box günstiger und hat mehr Apps.</p>'''),
    ],
    faq=[
        ('Welche ist die beste IPTV Box 2026?', 'Für maximale Leistung Nvidia Shield TV, für das beste Preis-Leistungs-Verhältnis eine Google-TV-Box wie Homatics, für IPTV-Spezialisten eine Formuler-Box mit MyTVOnline.'),
        ('Brauche ich eine IPTV Box?', 'Nein, aber sie lohnt sich, wenn Ihr Fernseher keine passende App hat oder Sie 4K, schnelles Umschalten und volle App-Auswahl wollen.'),
        ('Enthält eine IPTV Box Sender?', 'Seriöse Boxen enthalten keine Sender. Die Inhalte kommen aus Ihrem IPTV-Abo, dessen Zugangsdaten Sie in eine App eintragen.'),
        ('Kann ich eine IPTV Box bei AliExpress kaufen?', 'Möglich, aber riskant: Billigboxen aus Direktimport sind oft nicht als Android TV zertifiziert, haben geschönte Leistungsangaben, keine Updates und mitunter Schadsoftware. Markengeräte aus dem Handel sind die sicherere Wahl.'),
        ('Was ist besser: Fire TV Stick oder Android-Box?', 'Ein Fire TV Stick 4K Max ist günstig und reicht für die meisten Haushalte. Eine Android-TV-Box bietet mehr Leistung, LAN-Anschluss und den vollen Play Store.'),
    ],
    related=['formuler-iptv', 'iptv-stick', 'mag-box-iptv', 'iptv-receiver', 'tivimate', 'iptv-geraete'],
    card=('IPTV Box', 'Die besten Android-TV-Boxen für IPTV im Vergleich.'),
))

# ---------------------------------------------------------------- Receiver / Enigma2
PAGES.append(dict(
    slug='iptv-receiver', parent='geraete', kind='guide',
    title='IPTV Receiver: Enigma2, Dreamlink, Edision & GigaBlue',
    description='IPTV auf dem Receiver: Enigma2-Boxen wie GigaBlue, Edision Ping und Dreamlink für IPTV einrichten, passende Plugins und Unterschiede zur Android-Box.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV Receiver: Enigma2 und Co.',
    lead='Viele deutsche Haushalte nutzen einen Linux-Receiver für Satellit oder Kabel. Mit dem richtigen Plugin empfängt er zusätzlich IPTV – mit vertrauter Bedienung.',
    answer='Ein IPTV Receiver ist eine Set-Top-Box, die IPTV-Streams wie Fernsehsender abspielt. Enigma2-Receiver (z. B. GigaBlue, Edision, VU+, Dreambox) binden IPTV über Plugins ein, die Ihren Xtream-Login oder M3U-Link in Senderlisten (Bouquets) umwandeln. Reine IPTV-Receiver wie Dreamlink oder MAG-Boxen bringen eine eigene IPTV-Oberfläche mit.',
    sections=[
        ('arten', 'Arten von IPTV Receivern', table(['Typ', 'Beispiele', 'IPTV-Einbindung'], [
            ['Enigma2-Receiver (Sat/Kabel + IPTV)', 'GigaBlue, Edision, VU+, Dreambox', 'Plugins, Bouquets'],
            ['Reine IPTV-Receiver (Linux)', 'Dreamlink T2/T3, TVIP', 'Eigene Portal- oder Xtream-Oberfläche'],
            ['<a href="/mag-box-iptv/">MAG-Boxen</a>', 'MAG 324, 424, 524', 'Portal-URL + MAC-Adresse'],
            ['<a href="/iptv-box/">Android-TV-Boxen</a>', 'Formuler, Nvidia Shield', 'Apps aus dem Play Store'],
        ], 'Arten von IPTV Receivern')),
        ('enigma2', 'IPTV auf Enigma2 einrichten', steps(
            'Receiver per LAN verbinden und das aktuelle Image (z. B. OpenATV) installieren.',
            'Über den Plugin-Browser ein IPTV-Plugin installieren, etwa XStreamity oder Jedi Maker Xtream.',
            'Im Plugin einen neuen Zugang mit Server-URL, Benutzername und Passwort anlegen.',
            'Bouquets erzeugen lassen – die IPTV-Sender erscheinen in der Kanalliste.',
            'EPG über das Plugin oder EPGImport zuordnen.')
         + tip('Enigma2-Boxen haben teils schwächere Prozessoren. Für 4K-Streams ist ein aktuelles Modell mit HEVC-Decoder nötig.')),
        ('modelle', 'Edision Ping, GigaBlue &amp; Dreamlink', '''
<p><strong>Edision Ping</strong> ist ein kompakter Linux-Receiver ohne Tuner, der sich auf IPTV konzentriert. <strong>GigaBlue</strong> bietet Enigma2-Receiver mit Sat- oder Kabeltuner und IPTV-Unterstützung. <strong>Dreamlink T2 und T3</strong> sind IPTV-Boxen mit eigener Oberfläche für Portal- und Xtream-Zugänge. Welche Variante passt, hängt davon ab, ob Sie weiterhin Satellit empfangen möchten.</p>'''),
        ('vergleich', 'Receiver oder Android-Box?', proscons(
            ['Bedienung wie gewohnt', 'Sat/Kabel und IPTV in einer Senderliste', 'Aufnahme auf Festplatte'],
            ['Einrichtung technischer', 'Weniger Apps', 'Teurer als ein Stick'],
            'Vorteile Receiver', 'Nachteile Receiver') + LOGIN_TIP),
    ],
    faq=[
        ('Was ist ein IPTV Receiver?', 'Eine Set-Top-Box, die IPTV-Streams wie Fernsehsender abspielt. Dazu zählen Enigma2-Receiver mit Plugins, reine IPTV-Boxen wie Dreamlink und MAG-Boxen.'),
        ('Kann mein Sat-Receiver IPTV?', 'Wenn es ein Linux-Receiver mit Enigma2 ist, meist ja – über ein IPTV-Plugin. Einfache Sat-Receiver ohne Netzwerkfunktion können kein IPTV.'),
        ('Welches Plugin für IPTV auf Enigma2?', 'Verbreitet sind XStreamity und Jedi Maker Xtream. Sie lesen Ihren Xtream-Login ein und erzeugen daraus Senderlisten mit EPG.'),
        ('Ist ein 4K IPTV Receiver nötig?', 'Nur wenn Sie 4K-Sender schauen und einen 4K-Fernseher haben. Achten Sie dann auf HEVC-Unterstützung und LAN-Anschluss.'),
    ],
    related=['mag-box-iptv', 'iptv-box', 'xtream-codes-iptv', 'iptv-4k', 'iptv-fire-tv-stick', 'iptv-geraete'],
    card=('IPTV Receiver', 'Enigma2, Dreamlink, Edision und GigaBlue einrichten.'),
))

# ---------------------------------------------------------------- MAG
PAGES.append(dict(
    slug='mag-box-iptv', parent='geraete', kind='guide',
    title='MAG Box IPTV: Portal einrichten (MAG 322, 424, 524) & STBEmu',
    description='MAG Box IPTV einrichten: Portal-URL eintragen, MAC-Adresse freischalten, Modelle MAG 254 bis 524 im Überblick – plus STBEmu als MAG-Emulator für Android.',
    eyebrow='GERÄTE-ANLEITUNG', h1='MAG Box IPTV: Einrichtung und Modelle',
    lead='MAG-Boxen von Infomir sind IPTV-Receiver mit Portal-Oberfläche: einschalten, Portal eintragen, fertig. Wir zeigen Einrichtung, Modelle und die App-Alternative STBEmu.',
    answer='Für IPTV auf einer MAG Box geben Sie dem Anbieter die MAC-Adresse vom Aufkleber der Box, damit er sie freischaltet. Dann tragen Sie unter Einstellungen → Server → Portale die Portal-URL ein und starten neu. Auf Android-Geräten emuliert die App STBEmu eine MAG Box mit demselben Portal.',
    sections=[
        ('einrichten', 'MAG Box einrichten: Schritt für Schritt', steps(
            'MAC-Adresse von der Unterseite der Box (beginnt mit 00:1A:79) notieren und an den Anbieter senden.',
            'Box per LAN verbinden und einschalten.',
            'Im Menü <b>Einstellungen → Systemeinstellungen → Server → Portale</b> öffnen.',
            'Bei „Portal 1 Name“ einen Namen, bei „Portal 1 URL“ die Portal-Adresse eintragen.',
            'Speichern und die Box neu starten – das Portal lädt Senderliste, Mediathek und EPG.')),
        ('modelle', 'MAG-Modelle für IPTV', table(['Modell', 'Auflösung', 'Hinweis'], [
            ['MAG 250 / 254 / 256', 'Full HD', 'Ältere Modelle, teils ohne Updates'],
            ['MAG 322 / 324', 'Full HD, HEVC', 'Solide Einstiegsmodelle'],
            ['MAG 410', '4K', 'Android-basiert'],
            ['MAG 420 / 424', '4K, HEVC', 'Linux, schnelles Portal'],
            ['MAG 520 / 524', '4K HDR', 'Aktuelle Generation, WLAN integriert'],
        ], 'MAG Box Modelle') + '''
<p>Für <a href="/iptv-4k/">4K-Sender</a> wählen Sie eine Box der 4xx- oder 5xx-Serie. Ältere MAG 250 erhalten keine Updates mehr und sind nur noch eingeschränkt empfehlenswert.</p>'''),
        ('stbemu', 'STBEmu: MAG Box als App', '''
<p><strong>STBEmu</strong> (auch „STB Emu Pro“) ist eine Android-App, die eine MAG Box nachbildet. Sie funktioniert auf Smartphones, <a href="/iptv-box/">Android-TV-Boxen</a> und dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> mit Fire OS.</p>
''' + steps(
            'STBEmu installieren und öffnen.',
            '<b>Einstellungen → Profile → Profil hinzufügen</b> wählen.',
            'Unter „Portal-Einstellungen“ die Portal-URL eintragen.',
            'Unter „STB-Konfiguration“ die MAC-Adresse anzeigen lassen und an den Anbieter senden.',
            'Profil aktivieren und neu starten.')),
        ('vergleich', 'MAG Box oder Android-Box?', proscons(
            ['Bedienung wie ein klassischer Receiver', 'Schnelles Portal, wenig Einrichtung', 'Stabil im Dauerbetrieb'],
            ['Kaum zusätzliche Apps', 'Bindung an Portal-Zugang', 'Ältere Modelle ohne Updates'],
            'Vorteile MAG', 'Nachteile MAG') + '''
<p>Mehr Optionen zeigt der Ratgeber <a href="/iptv-box/">IPTV Box kaufen</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Wie richte ich IPTV auf einer MAG Box ein?', 'MAC-Adresse an den Anbieter senden, unter Einstellungen → Server → Portale die Portal-URL eintragen und die Box neu starten.'),
        ('Welche MAG Box ist die beste für IPTV?', 'Aktuell die MAG 524 oder MAG 424 für 4K. Für Full HD reicht eine MAG 322 oder 324.'),
        ('Was ist STBEmu?', 'STBEmu ist eine Android-App, die eine MAG Box emuliert. Sie tragen dieselbe Portal-URL ein und lassen die angezeigte MAC-Adresse vom Anbieter freischalten.'),
        ('Funktioniert die MAG 250 noch?', 'Grundsätzlich ja, sie erhält aber keine Updates mehr und unterstützt kein HEVC. Für neue Anschaffungen ist eine aktuelle Box empfehlenswerter.'),
    ],
    related=['iptv-box', 'iptv-receiver', 'iptv-android', 'iptv-4k', 'iptv-fire-tv-stick', 'iptv-geraete'],
    card=('MAG Box & STBEmu', 'Portal einrichten auf MAG 322, 424, 524 und per App.'),
))

# ---------------------------------------------------------------- Apple
PAGES.append(dict(
    slug='iptv-apple-tv-iphone', parent='geraete', kind='guide',
    title='IPTV auf Apple TV, iPhone & iPad: beste Apps & Anleitung',
    description='IPTV auf Apple TV, iPhone und iPad: die besten IPTV Apps aus dem App Store (IPTVX, Smarters Player Lite u. a.), Einrichtung und AirPlay auf den Fernseher.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV auf Apple TV, iPhone und iPad',
    lead='Auf Apple-Geräten kommt jede IPTV App aus dem App Store. Das macht die Einrichtung sicher und einfach – TiviMate gibt es hier allerdings nicht.',
    answer='Für IPTV auf Apple TV, iPhone und iPad laden Sie einen Player wie IPTVX oder Smarters Player Lite aus dem App Store, wählen „Xtream Codes“ oder „M3U“ und tragen Ihre Zugangsdaten ein. Vom iPhone übertragen Sie Streams per AirPlay auf Apple TV oder AirPlay-fähige Fernseher. TiviMate ist für Apple-Geräte nicht verfügbar.',
    sections=[
        ('apps', 'Die besten IPTV Apps für Apple-Geräte', table(['App', 'iPhone/iPad', 'Apple TV', 'Login'], [
            ['IPTVX', 'Ja', 'Ja', 'Xtream, M3U'],
            ['Smarters Player Lite', 'Ja', 'Ja', 'Xtream, M3U'],
            ['GSE Smart IPTV', 'Ja', 'Ja', 'Xtream, M3U'],
            ['VLC', 'Ja', 'Ja', 'M3U'],
        ], 'IPTV Apps für Apple') + '''
<p>Einige Apps bieten Zusatzfunktionen per In-App-Kauf. Das Angebot im App Store ändert sich gelegentlich; prüfen Sie Bewertungen und Aktualität vor dem Download. Hintergrund zu Smarters lesen Sie unter <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>.</p>'''),
        ('apple-tv', 'IPTV auf Apple TV einrichten', steps(
            'Auf dem Apple TV den App Store öffnen und „IPTVX“ oder „Smarters Player Lite“ installieren.',
            'App öffnen und eine neue Playlist bzw. einen neuen Nutzer anlegen.',
            '„Xtream Codes“ wählen und Server, Benutzername und Passwort eingeben – am bequemsten über die iPhone-Tastatur-Einblendung.',
            'Senderliste laden und in den Einstellungen den Programmführer aktivieren.')),
        ('iphone', 'IPTV auf iPhone und iPad', '''
<p>Auf dem iPhone funktioniert die Einrichtung genauso. Praktisch: Mit <strong>AirPlay</strong> schicken Sie das Bild auf Apple TV oder auf Smart-TVs mit AirPlay-Unterstützung (viele Samsung- und LG-Modelle). Unterwegs reduzieren Sie in der App die Qualität, um mobile Daten zu sparen.</p>'''),
        ('mac', 'IPTV auf dem Mac', '''
<p>Am MacBook oder iMac nutzen Sie VLC, die Smarters-Desktop-Version oder IPTVX für macOS. Die Anleitung finden Sie unter <a href="/iptv-pc-mac/">IPTV am PC und Mac</a>.</p>'''),
        ('tivimate', 'Und TiviMate auf Apple TV?', '''
<p><a href="/tivimate/">TiviMate</a> gibt es nur für Android-TV-Systeme. Wer das TiviMate-Erlebnis am Fernseher möchte, nutzt einen <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder eine <a href="/iptv-box/">Android-TV-Box</a>.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Welche IPTV App ist die beste für Apple TV?', 'IPTVX gilt als besonders komfortabel, Smarters Player Lite als einfacher Einstieg. Beide unterstützen Xtream-Codes-Logins und M3U.'),
        ('Gibt es TiviMate für Apple TV oder iPhone?', 'Nein. TiviMate ist nur für Android-TV-Systeme verfügbar. Auf Apple-Geräten nutzen Sie IPTVX, Smarters Player Lite oder GSE Smart IPTV.'),
        ('Kann ich IPTV vom iPhone auf den Fernseher übertragen?', 'Ja, per AirPlay auf Apple TV oder auf Smart-TVs mit AirPlay-Unterstützung.'),
        ('Funktioniert IPTV auf dem iPad?', 'Ja. Alle genannten Apps laufen auch auf dem iPad, inklusive Bild-in-Bild in vielen Apps.'),
    ],
    related=['iptv-smarters-pro', 'iptv-pc-mac', 'iptv-android', 'm3u-playlist', 'iptv-4k', 'iptv-geraete'],
    card=('Apple TV & iPhone', 'IPTVX, Smarters Lite und AirPlay einrichten.'),
))

# ---------------------------------------------------------------- PC / Mac / VLC
PAGES.append(dict(
    slug='iptv-pc-mac', parent='geraete', kind='guide',
    title='IPTV am PC & Mac: VLC, Smarters für Windows & Browser',
    description='IPTV am PC, Laptop und Mac schauen: M3U-Playlist in VLC öffnen, IPTV Smarters für Windows nutzen, Kodi am Computer und IPTV im Webbrowser – Schritt für Schritt.',
    eyebrow='GERÄTE-ANLEITUNG', h1='IPTV am PC und Mac',
    lead='Am Computer schauen Sie IPTV ohne Zusatzgeräte – im Arbeitszimmer, am Laptop oder per HDMI auf dem Fernseher. VLC ist dafür der einfachste Weg.',
    answer='Für IPTV am PC oder Mac öffnen Sie VLC, wählen „Medien → Netzwerkstream öffnen“ und fügen Ihren M3U-Link ein. Für Programmführer und Mediathek nutzen Sie die Desktop-Version von IPTV Smarters für Windows und Mac oder Kodi mit dem PVR IPTV Simple Client. Webplayer im Browser funktionieren ebenfalls, sehen aber Ihre Zugangsdaten.',
    sections=[
        ('vlc', 'IPTV mit VLC öffnen', steps(
            'VLC Media Player von videolan.org installieren (Windows, Mac, Linux).',
            'Windows: <b>Medien → Netzwerkstream öffnen</b>; Mac: <b>Ablage → Netzwerk öffnen</b>.',
            'Ihren <a href="/m3u-playlist/">M3U-Link</a> einfügen und „Wiedergabe“ klicken.',
            'Über <b>Ansicht → Wiedergabeliste</b> (Strg+L) zwischen Sendern wechseln.',
            'Optional: Playlist als Datei speichern, um sie später per Doppelklick zu öffnen.')
         + tip('VLC zeigt keinen Programmführer im Raster. Wer EPG und Mediathek möchte, nimmt Smarters oder Kodi.')),
        ('smarters', 'IPTV Smarters für Windows und Mac', '''
<p>Die Desktop-Version von <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> gibt es auf der offiziellen Website für Windows und macOS. Nach dem Download melden Sie sich mit Ihrem Xtream-Codes-Login an und erhalten Live-TV, EPG, Filme und Serien wie auf dem Fernseher.</p>'''),
        ('weitere', 'Weitere Programme für Windows und Mac', table(['Programm', 'System', 'Besonderheit'], [
            ['VLC', 'Windows, Mac, Linux', 'Kostenlos, universell'],
            ['IPTV Smarters Desktop', 'Windows, Mac', 'Xtream-Login mit EPG'],
            ['<a href="/kodi-iptv/">Kodi</a>', 'Windows, Mac, Linux', 'Mediacenter mit TV-Raster'],
            ['IPTVX', 'Mac', 'Apple-typisches Design'],
            ['MyIPTV Player', 'Windows (Microsoft Store)', 'Einfache M3U-Wiedergabe'],
        ], 'IPTV Programme für PC und Mac') + '''
<p><a href="/tivimate/">TiviMate</a> gibt es nicht für Windows oder Mac; nur über einen Android-Emulator, was selten sinnvoll ist.</p>'''),
        ('browser', 'IPTV im Webbrowser', '''
<p>Online-Player im Browser spielen M3U8-Streams ohne Installation ab. Bedenken Sie: Der Webdienst sieht Ihren Link samt Zugangsdaten. Für persönliche Zugänge sind lokale Programme wie VLC sicherer.</p>'''),
        ('fernseher', 'Vom Laptop auf den Fernseher', '''
<p>Ein HDMI-Kabel vom Laptop zum Fernseher genügt, um IPTV groß zu schauen. Dauerhaft komfortabler ist ein <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder eine <a href="/iptv-box/">IPTV Box</a> mit Fernbedienung.</p>''' + LOGIN_TIP),
    ],
    faq=[
        ('Wie schaue ich IPTV am PC?', 'Am einfachsten mit VLC: Medien → Netzwerkstream öffnen → M3U-Link einfügen. Mit Programmführer geht es mit IPTV Smarters Desktop oder Kodi.'),
        ('Gibt es IPTV Smarters Pro für Windows?', 'Ja, auf der offiziellen Smarters-Website gibt es eine Desktop-Version für Windows und macOS.'),
        ('Kann ich IPTV am MacBook schauen?', 'Ja, mit VLC, IPTVX oder der Smarters-Desktop-Version für macOS.'),
        ('Funktioniert TiviMate auf dem PC?', 'Nicht direkt. TiviMate ist eine Android-TV-App. Am PC sind VLC, Smarters oder Kodi die bessere Wahl.'),
    ],
    related=['m3u-playlist', 'iptv-smarters-pro', 'kodi-iptv', 'iptv-apple-tv-iphone', 'xtream-codes-iptv', 'iptv-geraete'],
    card=('PC & Mac', 'IPTV mit VLC, Smarters Desktop und Kodi am Computer.'),
))
