"""Third keyword pass (24.11.2026): Sky, football and sport, language/community pages, CloudStream,
payment and reseller. Rights facts were checked against kicker.de, sky.de help pages and sportschau.de
(as of November 2026). Pages describe who holds rights and how to watch on IPTV devices; they make no claim
about which channels a given IPTV Kanal access contains – that is shown in the free test."""
from .helpers import steps, checks, tip, table, proscons

PAGES = []

TEST_TIP = tip('Welche Sender und Sendergruppen Ihr Zugang enthält, sehen Sie vollständig im <a href="/kostenlos-testen/">kostenlosen Test</a> – auf Ihrem eigenen Gerät, bevor Sie etwas bezahlen.', 'Hinweis')

# ================================================================ SPORT
PAGES.append(dict(
    slug='sky-iptv', parent='ratgeber', kind='guide',
    title='Sky über IPTV: Sky Stream, Sky Q IPTV Box & Sky Sport',
    description='Sky über IPTV erklärt: Was aus der Sky Q IPTV Box wurde, wie Sky Stream funktioniert, Unterschiede zu Sky Q per Satellit und wie Sie Sky Sport auf IPTV-Geräten schauen.',
    eyebrow='PAY-TV &amp; IPTV', h1='Sky über IPTV: Sky Stream und Sky Q IPTV Box erklärt',
    lead='Sky Deutschland bietet sein Programm längst auch über das Internet an. Hier lesen Sie, was aus der Sky Q IPTV Box geworden ist, was Sky Stream kann und wie Sky mit anderen IPTV-Geräten zusammenpasst.',
    answer='Sky über IPTV heißt bei Sky Deutschland heute Sky Stream: Die frühere Sky Q IPTV Box wurde per Software-Update zu Sky Stream, neue Internetkunden erhalten nur noch Sky Stream. Die Box braucht ausschließlich Internet, kann Ultra HD und Dolby Atmos (als Option), nimmt aber nicht auf – statt Aufnahmen gibt es eine Playlist. Wer aufnehmen möchte, bleibt beim Sky Q Receiver über Satellit oder Kabel.',
    sections=[
        ('sky-q-iptv', 'Was wurde aus der Sky Q IPTV Box?', '''
<p>Die <strong>Sky Q IPTV Box</strong> war Skys erster Receiver, der das komplette Programm über die Internetleitung statt über Satellit oder Kabel empfing. Laut Sky-Hilfecenter wird sie per automatischem Software-Update zur <strong>Sky Stream</strong>-Box. Neue Hardware ist nicht nötig, Fernbedienung, Zugangsdaten und Vertrag bleiben, und der Monatspreis ändert sich nicht. Das Produkt „Sky Q IPTV“ gibt es danach nicht mehr.</p>
<p>Wer heute nach „Sky Q IPTV Box kaufen“ sucht, bekommt deshalb als Neukunde Sky Stream. Gebrauchte Sky-Q-IPTV-Boxen funktionieren nur mit einem eigenen Sky-Abo und werden ebenfalls auf Sky Stream umgestellt.</p>'''),
        ('vergleich', 'Sky Stream vs. Sky Q Receiver', table(['', 'Sky Stream (Internet)', 'Sky Q Receiver (Sat/Kabel)'], [
            ['Empfang', 'Nur Internet', 'Satellit oder Kabel, Internet für Abruf-Inhalte'],
            ['Ultra HD', 'Bis 3840 × 2160, UHD-Option buchbar', 'Bis 3840 × 2160 (50 fps)'],
            ['Aufnahme', 'Nein – stattdessen Playlist', 'Ja, auch Serienaufnahme'],
            ['Ohne Internet', 'Kein Empfang', 'Live-TV und Aufnahmen laufen weiter'],
            ['Weitere Fernseher', 'Bis zu zwei Zusatzboxen oder Sky-Q-App', 'Sky Q Mini oder Sky-Q-App'],
            ['Installation', 'Internet, Strom, HD-Fernseher', 'Sat- oder Kabelanschluss nötig'],
        ], 'Sky Stream und Sky Q im Vergleich') + '''
<p>Sky Q und Sky Stream laufen nicht parallel im selben Abo, Sie können aber zwischen beiden wechseln. Stand der Angaben: Sky-Hilfecenter, November 2026.</p>'''),
        ('internet', 'Welche Internetleitung braucht Sky über IPTV?', '''
<p>Für Sky Stream gelten dieselben Faustregeln wie für jedes IPTV: rund 16 Mbit/s für stabiles Full HD und mindestens 25 Mbit/s für Ultra HD – pro gleichzeitig laufender Box. Bei Sport am Samstagnachmittag ist die Leitung im ganzen Haushalt gefordert; ein LAN-Kabel zur Box verhindert Aussetzer. Fehlermeldungen wie „1002“ oder „1003“ bedeuten laut Sky, dass keine Internetverbindung besteht. Mehr zur Bandbreite im Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>.</p>'''),
        ('sky-sport', 'Sky Sport auf IPTV-Geräten', '''
<p>Sky zeigt in Deutschland unter anderem den Großteil der Bundesliga-Einzelspiele (Freitag 20:30 Uhr, Samstag 15:30 und 18:30 Uhr), die 2. Bundesliga und die Premier League. Diese Inhalte gibt es offiziell nur mit einem Sky- oder WOW-Abo. Auf Geräten wie dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, Google TV, <a href="/iptv-samsung-tv/">Samsung</a>- und <a href="/iptv-lg-tv/">LG</a>-Fernsehern oder <a href="/iptv-apple-tv-iphone/">Apple TV</a> installieren Sie dafür die WOW- bzw. Sky-App – sie läuft problemlos neben Ihrer IPTV-App. Welche Spiele wo laufen, zeigt unser Ratgeber <a href="/iptv-fussball/">Fußball per IPTV</a>.</p>'''),
        ('alternativen', 'Sky Stream, WOW oder unabhängiges IPTV?', proscons(
            ['Sky Stream: komplettes Sky-Programm mit eigener Box', 'WOW: Sky-Inhalte als App, monatlich kündbar', 'Unabhängiges IPTV: viele Sender, eigene App-Wahl, ohne Vertrag'],
            ['Sky Stream: keine Aufnahme, Vertragslaufzeit', 'WOW: kein klassisches Live-TV-Raster wie beim Receiver', 'Unabhängiges IPTV: Inhalte unterscheiden sich je Anbieter'],
            'Vorteile', 'Zu beachten') + TEST_TIP),
    ],
    faq=[
        ('Gibt es die Sky Q IPTV Box noch?', 'Nein. Laut Sky wird die Sky Q IPTV Box per Software-Update zu Sky Stream; das Produkt „Sky Q IPTV“ gibt es danach nicht mehr. Neue Internetkunden erhalten direkt Sky Stream.'),
        ('Kann Sky Stream aufnehmen?', 'Nein. Sky Stream hat keine Aufnahmefunktion, sondern eine persönliche Playlist mit Abruf-Inhalten. Wer aufnehmen möchte, nutzt den Sky Q Receiver über Satellit oder Kabel.'),
        ('Kann Sky Stream Ultra HD?', 'Ja, bis 3840 × 2160 Bildpunkte. Ultra HD und Dolby Atmos sind laut Sky optional buchbar und setzen einen UHD-Fernseher voraus.'),
        ('Wie schnell muss das Internet für Sky über IPTV sein?', 'Für Full HD sind etwa 16 Mbit/s, für Ultra HD mindestens 25 Mbit/s pro Box empfehlenswert. Ein LAN-Kabel ist stabiler als WLAN.'),
        ('Kann ich Sky auf dem Fire TV Stick schauen?', 'Ja, mit einem Sky- oder WOW-Abo über die offizielle App. Sie läuft auf dem Fire TV Stick neben anderen IPTV-Apps.'),
    ],
    related=['iptv-fussball', 'iptv-sport', 'iptv-telekom-vodafone', 'iptv-4k', 'iptv-fire-tv-stick', 'was-ist-iptv'],
    card=('Sky über IPTV', 'Sky Stream, Sky Q IPTV Box und Sky Sport erklärt.'),
))

PAGES.append(dict(
    slug='iptv-fussball', parent='ratgeber', kind='guide',
    title='Fußball per IPTV 2026/27: Bundesliga & Champions League',
    description='Fußball per IPTV: Wer zeigt Bundesliga, Champions League, Premier League und DFB-Pokal 2026/27 – und wie Sie Fußball auf Fire TV, Smart TV und Box ruckelfrei schauen.',
    eyebrow='FUSSBALL &amp; IPTV', h1='Fußball per IPTV: Bundesliga, Champions League &amp; Co.',
    lead='Live-Fußball ist der härteste Test für jede Internetleitung und jedes IPTV-Gerät. Hier sehen Sie, wer in der Saison 2026/27 welche Spiele zeigt und wie Sie sie ohne Ruckler schauen.',
    answer='In Deutschland zeigt Sky in der Saison 2026/27 den Großteil der Bundesliga (Freitag, Samstag 15:30 und 18:30 Uhr), DAZN die Sonntagsspiele und die Samstagskonferenz. Die Champions League läuft bei DAZN und Amazon Prime Video, ab 2027/28 hauptsächlich bei Paramount+. Für flüssigen Fußball per IPTV brauchen Sie mindestens 16 Mbit/s pro Gerät, ein LAN-Kabel und die richtige Bildwiederholrate.',
    sections=[
        ('bundesliga', 'Bundesliga per IPTV: wer zeigt was?', table(['Spiel', 'Anbieter (2025/26–2028/29)'], [
            ['Freitag 20:30 Uhr', 'Sky'],
            ['Samstag 15:30 Uhr (Einzelspiele)', 'Sky'],
            ['Samstag 15:30 Uhr (Konferenz)', 'DAZN'],
            ['Samstag 18:30 Uhr (Topspiel)', 'Sky'],
            ['Sonntag 15:30, 17:30, 19:30 Uhr', 'DAZN'],
            ['Saisoneröffnung, Relegation, Supercup', 'Sat.1 (frei empfangbar)'],
            ['Zusammenfassungen', 'ARD Sportschau, ZDF Sportstudio'],
        ], 'Bundesliga TV-Rechte') + '''
<p>Quelle: kicker.de, Stand der Medienrechte bis 2028/29. Die 2. Bundesliga läuft vollständig bei Sky; ein Topspiel pro Spieltag zeigt zusätzlich das Free-TV.</p>'''),
        ('champions-league', 'Champions League per IPTV', table(['Saison', 'Hauptanbieter', 'Weitere'], [
            ['2026/27', 'DAZN (fast alle Spiele)', 'Amazon Prime Video (Dienstag-Topspiel), ZDF (Finale, Highlights)'],
            ['ab 2027/28', 'Paramount+', 'Amazon Prime Video, ZDF-Zusammenfassungen'],
        ], 'Champions League TV-Rechte') + '''
<p>Für die Europa League und Conference League gilt bis 2026/27 RTL bzw. RTL+, ab 2027/28 DAZN. Rechte werden regelmäßig neu vergeben – prüfen Sie vor Saisonbeginn die Angaben der Anbieter.</p>'''),
        ('weitere-ligen', 'Premier League, DFB-Pokal und WM', checks(
            '<strong>Premier League (England):</strong> Sky bzw. WOW.',
            '<strong>DFB-Pokal:</strong> Sky mit dem Großteil der Spiele, ausgewählte Partien im Free-TV.',
            '<strong>LaLiga, Serie A, Ligue 1:</strong> DAZN.',
            '<strong>3. Liga:</strong> MagentaSport, ausgewählte Spiele in den Dritten Programmen.',
            '<strong>FIFA WM 2026:</strong> MagentaTV zeigte alle 104 Spiele, ARD und ZDF 60 davon frei.')),
        ('technik', 'Fußball ruckelfrei: die richtigen Einstellungen', steps(
            '<b>LAN statt WLAN:</b> Am Samstagnachmittag ist das WLAN in vielen Häusern überlastet.',
            '<b>Bildwiederholrate anpassen (AFR):</b> In TiviMate, Kodi und auf Google TV aktivieren, damit 50-Hz-Übertragungen ohne Mikroruckler laufen.',
            '<b>Hardware-Decoder</b> in der App wählen und den Puffer auf „mittel“ stellen.',
            '<b>Bewegungsglättung des Fernsehers</b> testweise ausschalten – sie verursacht bei schnellen Bällen Artefakte.',
            '<b>Verzögerung beachten:</b> Streams laufen 20–60 Sekunden hinter dem Kabelsignal. Push-Nachrichten von Ergebnis-Apps besser stummschalten.')
         + '''<p>Weitere Tipps gegen Ruckler finden Sie in den Ratgebern <a href="/iptv-4k/">IPTV in 4K</a> und <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>.</p>'''),
        ('geraete', 'Fußball-Apps auf IPTV-Geräten', '''
<p>Die Apps von Sky/WOW, DAZN, Amazon Prime Video, Paramount+, MagentaTV und den Mediatheken laufen auf denselben Geräten wie Ihre IPTV-App: <a href="/iptv-stick/">Fire TV und Google-TV-Sticks</a>, <a href="/iptv-smart-tv/">Smart-TVs</a>, <a href="/iptv-box/">Android-TV-Boxen</a> und <a href="/iptv-apple-tv-iphone/">Apple TV</a>. So haben Sie alles auf einer Fernbedienung. Hintergründe zu Sky über das Internet lesen Sie unter <a href="/sky-iptv/">Sky über IPTV</a>.</p>''' + TEST_TIP),
    ],
    faq=[
        ('Wer zeigt die Bundesliga 2026/27?', 'Sky zeigt die Freitagsspiele, die Samstagsspiele um 15:30 Uhr als Einzelspiele und das Topspiel um 18:30 Uhr. DAZN zeigt die Sonntagsspiele und die Samstagskonferenz. Sat.1 überträgt ausgewählte Spiele wie die Saisoneröffnung frei.'),
        ('Wo läuft die Champions League 2026/27?', 'Bei DAZN mit fast allen Spielen und bei Amazon Prime Video mit einem Topspiel am Dienstag. Ab der Saison 2027/28 übernimmt Paramount+ den Großteil der Spiele.'),
        ('Warum ist Fußball per IPTV verzögert?', 'Streams werden codiert, verteilt und auf Ihrem Gerät gepuffert. Dadurch laufen sie meist 20 bis 60 Sekunden hinter Kabel oder Satellit.'),
        ('Wie viel Internet brauche ich für Fußball per IPTV?', 'Für Full HD rund 16 Mbit/s, für 4K mindestens 25 Mbit/s pro Gerät. Ein LAN-Kabel ist bei Live-Sport deutlich stabiler als WLAN.'),
        ('Warum ruckelt Fußball, obwohl mein Internet schnell ist?', 'Häufig liegt es an einer falschen Bildwiederholrate, an überlastetem WLAN oder an der Bewegungsglättung des Fernsehers. Aktivieren Sie AFR in der App und nutzen Sie ein LAN-Kabel.'),
    ],
    related=['iptv-sport', 'sky-iptv', 'iptv-4k', 'iptv-fire-tv-stick', 'tivimate', 'iptv-stick'],
    card=('Fußball per IPTV', 'Bundesliga, Champions League und Premier League 2026/27.'),
))

PAGES.append(dict(
    slug='iptv-sport', parent='ratgeber', kind='guide',
    title='IPTV Sport: Formel 1, NBA, UFC & internationaler Sport',
    description='IPTV Sport erklärt: Wo Formel 1, NBA, UFC, Eurosport, beIN Sports, ESPN und Fox Sports laufen und wie Sie Sport per IPTV in bester Qualität und ohne Ruckler schauen.',
    eyebrow='SPORT &amp; IPTV', h1='IPTV Sport: Formel 1, NBA, UFC und mehr',
    lead='Sport ist der Hauptgrund, warum viele zu IPTV wechseln. Hier finden Sie, welche Dienste in Deutschland Motorsport, US-Sport und Kampfsport zeigen – und wie Sie auf Ihrem IPTV-Gerät das Beste herausholen.',
    answer='Sport per IPTV bedeutet: Live-Übertragungen kommen über das Internet auf Ihr Gerät. Formel 1 gibt es in Deutschland bei Sky und über den offiziellen Dienst F1 TV, die NBA über den NBA League Pass, die UFC über UFC Fight Pass. Sender wie beIN Sports, ESPN oder Fox Sports richten sich an andere Länder. Für ruckelfreien Sport brauchen Sie ein LAN-Kabel, AFR und einen guten Player.',
    sections=[
        ('uebersicht', 'Wo läuft welcher Sport?', table(['Sportart', 'Offizielle Wege in Deutschland'], [
            ['Formel 1', 'Sky; F1 TV (offizieller Streamingdienst der Formel 1)'],
            ['NBA (Basketball)', 'NBA League Pass'],
            ['UFC (Kampfsport)', 'UFC Fight Pass; ausgewählte Events bei Partnern'],
            ['Tennis, Radsport, Wintersport', 'Eurosport 1 (frei empfangbar) und die Streaming-Angebote von Warner Bros. Discovery'],
            ['Fußball international', 'Sky, DAZN, Amazon Prime Video – siehe <a href="/iptv-fussball/">Fußball per IPTV</a>'],
        ], 'Sport-Übertragungen in Deutschland') + '''
<p>Übertragungsrechte ändern sich häufig, oft von Saison zu Saison. Die Angaben entsprechen dem Stand November 2026.</p>'''),
        ('international', 'beIN Sports, ESPN, Fox Sports: internationale Sportsender', '''
<p><strong>beIN Sports</strong> sendet vor allem für Frankreich, die Türkei und den Nahen Osten, <strong>ESPN</strong> und <strong>Fox Sports</strong> sind US-amerikanische Sender, <strong>Sky Sports</strong> und <strong>TNT Sports</strong> richten sich an Großbritannien. Diese Sender haben in Deutschland in der Regel keine eigenen Angebote, weil die Rechte für jedes Land einzeln vergeben werden. Wer in Deutschland nach „IPTV beIN Sport“ oder „IPTV ESPN“ sucht, schaut am sichersten über die Dienste, die die jeweiligen Wettbewerbe hierzulande zeigen.</p>'''),
        ('technik', 'Sport per IPTV: so läuft es flüssig', table(['Problem', 'Ursache', 'Lösung'], [
            ['Mikroruckler bei Kameraschwenks', '50-Hz-Signal auf 60-Hz-Ausgabe', 'Bildwiederholrate anpassen (AFR) aktivieren'],
            ['Puffern zur Hauptsendezeit', 'WLAN überlastet', 'LAN-Kabel oder 5-GHz-WLAN'],
            ['Unscharfes Bild', 'Schwacher Decoder', 'Hardware-Decoder wählen, 4K-fähiges Gerät nutzen'],
            ['Ergebnis kommt vor dem Tor', 'Streaming-Verzögerung', 'Benachrichtigungen von Ergebnis-Apps stummschalten'],
        ], 'Sport per IPTV optimieren') + '''
<p>Die besten Player für Sport sind auf Android-TV <a href="/tivimate/">TiviMate</a> (mit Mehrfachansicht in Premium) und <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>. Mehr Geräte-Tipps im Ratgeber <a href="/iptv-stick/">IPTV Stick</a>.</p>'''),
        ('motorsport', 'Formel 1 per IPTV: Tipps für Rennwochenenden', checks(
            'Onboard-Kameras und Timing laufen am besten in der offiziellen F1-TV-App auf einem zweiten Gerät.',
            'Für 4K-Übertragungen 25 Mbit/s pro Gerät einplanen (siehe <a href="/iptv-4k/">IPTV in 4K</a>).',
            'Rennstart und Qualifying sind Lastspitzen: andere Downloads im Haushalt pausieren.',
            'Programmführer (EPG) nutzen, um Trainings, Qualifying und Rennen nicht zu verpassen.') + TEST_TIP),
    ],
    faq=[
        ('Wo kann ich Formel 1 in Deutschland per IPTV schauen?', 'Bei Sky und über den offiziellen Streamingdienst F1 TV. Beide Apps laufen auf Fire TV, Google TV, Smart-TVs und Apple TV.'),
        ('Gibt es beIN Sports in Deutschland?', 'In der Regel nicht. beIN Sports sendet vor allem für Frankreich, die Türkei und den Nahen Osten. Die Rechte an Wettbewerben werden für jedes Land einzeln vergeben.'),
        ('Wie schaue ich NBA und UFC in Deutschland?', 'Die NBA über den NBA League Pass, die UFC über UFC Fight Pass. Beide sind als App für gängige Streaming-Geräte erhältlich.'),
        ('Warum ruckelt Sport per IPTV mehr als Filme?', 'Sport hat schnelle Bewegungen und wird mit 50 Bildern pro Sekunde gesendet. Ohne passende Bildwiederholrate (AFR) und mit überlastetem WLAN fallen Ruckler deutlich stärker auf.'),
    ],
    related=['iptv-fussball', 'sky-iptv', 'iptv-4k', 'tivimate', 'iptv-stick', 'iptv-apps'],
    card=('IPTV Sport', 'Formel 1, NBA, UFC und internationale Sportsender.'),
))

# ================================================================ INTERNATIONAL / COMMUNITY
COMMUNITY_SETUP = steps(
    'Kostenlosen Test anfragen und die Senderliste auf Ihrem Gerät öffnen.',
    'In der App die Gruppen der gewünschten Sprache bzw. des Landes einblenden, alle anderen ausblenden.',
    'Lieblingssender als Favoriten anlegen – so stehen sie direkt neben den deutschen Sendern.',
    'Im Programmführer die Zeitzone auf Europa/Berlin lassen; die Sendezeiten werden automatisch umgerechnet.',
    'Bei Bedarf die Sprache der App-Oberfläche umstellen (Smarters und TiviMate unterstützen viele Sprachen).')

PAGES.append(dict(
    slug='iptv-international', parent='ratgeber', kind='hub', hub='international',
    title='IPTV International: Sender in Ihrer Sprache in Deutschland',
    description='IPTV International: Fernsehen auf Albanisch, Bosnisch, Kroatisch, Serbisch, Rumänisch, Russisch, Türkisch und Englisch in Deutschland – Sendergruppen, Apps und Einrichtung.',
    eyebrow='IPTV INTERNATIONAL', h1='IPTV International: Fernsehen in Ihrer Sprache',
    lead='Millionen Menschen in Deutschland schauen gern Programme aus ihrer Heimat. Mit IPTV brauchen Sie dafür keine zweite Satellitenschüssel – nur die richtige Senderliste in Ihrer App.',
    answer='Mit IPTV schauen Sie internationale Sender über Ihre Internetleitung, ohne zusätzliche Schüssel oder Receiver. In der App blenden Sie die Sendergruppen Ihrer Sprache ein, legen Favoriten an und erhalten den Programmführer in deutscher Zeit. Unsere Ratgeber zeigen beliebte Sender und Einrichtungstipps für Albanisch, Balkan-Sprachen, Rumänisch, Russisch und Türkisch.',
    sections=[
        ('warum', 'Warum IPTV für internationale Sender?', checks(
            '<strong>Keine zweite Schüssel:</strong> Viele Heimatsender sind per Satellit nur mit anderer Ausrichtung oder gar nicht zu empfangen.',
            '<strong>Alles in einer App:</strong> Deutsche und internationale Sender stehen in einer Senderliste nebeneinander.',
            '<strong>Programmführer in deutscher Zeit:</strong> Sendezeiten werden automatisch umgerechnet.',
            '<strong>Auf jedem Gerät:</strong> Fernseher, Handy, Tablet und PC – auch unterwegs.')),
        ('englisch', 'Englischsprachiges Fernsehen: BBC und England', '''
<p>Für Zuschauer aus Großbritannien und alle, die Programme auf Englisch mögen: Die BBC bietet ihren Streamingdienst BBC iPlayer offiziell nur in Großbritannien an. In Deutschland sind englischsprachige Nachrichtensender wie BBC News über viele Kabel- und IPTV-Angebote empfangbar. Englische Originalton-Versionen von Filmen und Serien finden Sie in vielen Mediatheken und auf Streamingdiensten. Englischer Fußball läuft hierzulande bei Sky bzw. WOW – siehe <a href="/iptv-fussball/">Fußball per IPTV</a>.</p>'''),
        ('einrichten', 'Internationale Sender einrichten', COMMUNITY_SETUP + TEST_TIP),
    ],
    faq=[
        ('Kann ich mit IPTV Sender aus meiner Heimat schauen?', 'Ja, IPTV überträgt Sender aus vielen Ländern über das Internet. Welche Sender Ihr Zugang genau enthält, sehen Sie im kostenlosen Test in der vollständigen Senderliste.'),
        ('Brauche ich für internationale Sender eine zweite Satellitenschüssel?', 'Nein. Mit IPTV kommen alle Sender über Ihre Internetleitung. Sie brauchen nur ein Gerät mit IPTV-App.'),
        ('Gibt es BBC iPlayer in Deutschland?', 'Offiziell nein. BBC iPlayer ist auf Großbritannien beschränkt. Englischsprachige Nachrichten wie BBC News sind in Deutschland über Kabel- und IPTV-Angebote verbreitet.'),
    ],
    related=['iptv-senderliste', 'iptv-apps', 'iptv-geraete', 'was-ist-iptv', 'iptv-kaufen', 'm3u-playlist'],
    card=('IPTV International', 'Sender auf Albanisch, Balkan, Rumänisch, Russisch und Türkisch.'),
))


def community(slug, title, description, h1, lead, answer, welcome, channels, extra_h2, extra, faq, card, related):
    return dict(
        slug=slug, parent='international', kind='guide', title=title, description=description,
        eyebrow='IPTV INTERNATIONAL', h1=h1, lead=lead, answer=answer,
        sections=[
            ('willkommen', 'Fernsehen aus der Heimat – in Deutschland', welcome),
            ('sender', 'Beliebte Sender, nach denen Zuschauer suchen', table(['Sender', 'Programm'], channels, 'Beliebte Sender') + '''
<p>Die Liste zeigt bekannte Sender des Landes, keine Zusage für einen bestimmten Zugang. Welche davon Ihre Senderliste enthält, prüfen Sie im kostenlosen Test.</p>'''),
            (extra_h2[0], extra_h2[1], extra),
            ('einrichten', 'So richten Sie die Sender ein', COMMUNITY_SETUP + '''
<p>Anleitungen für Ihr Gerät: <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, <a href="/iptv-samsung-tv/">Samsung TV</a>, <a href="/iptv-lg-tv/">LG TV</a>, <a href="/iptv-android/">Android</a> und <a href="/iptv-apple-tv-iphone/">Apple</a>. Wie Sie Gruppen sortieren, zeigt der Ratgeber <a href="/iptv-senderliste/">IPTV Senderliste</a>.</p>''' + TEST_TIP),
        ],
        faq=faq, related=related, card=card)


PAGES.append(community(
    'iptv-albanisch', 'IPTV Albanisch: Albanische Sender (Shqip) in Deutschland',
    'IPTV auf Albanisch in Deutschland: albanische Kanäle aus Albanien und Kosovo per IPTV schauen – beliebte Sender, Apps, Programmführer und Einrichtung Schritt für Schritt.',
    'IPTV Albanisch: albanische Kanäle in Deutschland',
    'Mirë se vini! Sie suchen albanische Kanäle („Alb Kanale“) in Deutschland? Mit IPTV schauen Sie Programme aus Albanien und dem Kosovo über Ihre Internetleitung – live und mit Programmführer.',
    'Mit IPTV schauen Sie albanische Sender aus Albanien, dem Kosovo und Nordmazedonien in Deutschland, ohne Satellitenschüssel. Sie öffnen in Ihrer IPTV-App die albanischen Sendergruppen, legen Favoriten an und nutzen den Programmführer in deutscher Zeit. Welche albanischen Kanäle Ihr Zugang enthält, sehen Sie im kostenlosen Test.',
    '''<p><strong>Mirë se vini!</strong> In Deutschland leben viele Menschen mit albanischen Wurzeln aus Albanien, dem Kosovo und Nordmazedonien. Suchanfragen wie „Alb Kanal IPTV“, „Albkanale IPTV“ oder „IPTV Shqip live“ zeigen: Gefragt sind Nachrichten, Unterhaltung und Musik in der Muttersprache. Per IPTV kommen diese Programme ohne zusätzliche Hardware auf Fernseher, Handy und Tablet.</p>''',
    [['RTSH', 'Öffentlich-rechtlicher Rundfunk Albaniens'], ['Top Channel', 'Privatsender aus Tirana: Shows, Nachrichten'],
     ['Klan', 'Privatsender aus Tirana'], ['Vizion Plus', 'Unterhaltung und Serien'], ['RTK', 'Öffentlich-rechtlicher Rundfunk des Kosovo'],
     ['Klan Kosova', 'Privatsender aus Pristina'], ['KTV / RTV21', 'Kosovarische Privatsender'], ['News 24 / ABC News Albania', 'Nachrichtensender']],
    ('tipps', 'Tipps für albanische Sender'), checks(
        'Sendergruppen heißen oft „AL“, „ALB“, „Shqip“ oder „Kosova“ – suchen Sie in der App nach diesen Kürzeln.',
        'Albanische Sonderzeichen (ë, ç) werden korrekt angezeigt, wenn die Playlist als M3U8 (UTF-8) geladen wird.',
        'Für Hochzeitsmusik- und Musiksender lohnt sich eine eigene Favoritenliste.'),
    [('Kann ich albanische Sender in Deutschland per IPTV schauen?', 'Ja. Per IPTV kommen albanische Programme aus Albanien und dem Kosovo über Ihre Internetleitung. Welche Kanäle Ihr Zugang enthält, zeigt der kostenlose Test.'),
     ('Was bedeutet „Alb Kanale“?', '„Alb Kanale“ oder „Albkanale“ ist eine gängige Suche nach albanischen Fernsehkanälen. Gemeint sind Sender aus Albanien, dem Kosovo und Nordmazedonien.'),
     ('Welche App eignet sich für albanische Sender?', 'Jede gängige IPTV-App, etwa IPTV Smarters Pro, TiviMate oder Smart IPTV. Wichtig ist, dass Sonderzeichen korrekt angezeigt werden – laden Sie die Playlist dafür als M3U8.')],
    ('IPTV Albanisch', 'Albanische Kanäle aus Albanien und Kosovo per IPTV.'),
    ['iptv-international', 'iptv-balkan', 'iptv-russisch', 'iptv-senderliste', 'iptv-smarters-pro', 'm3u-playlist']))

PAGES.append(community(
    'iptv-balkan', 'IPTV Balkan: Ex-YU Sender (IP televizija) in Deutschland',
    'IP televizija u Njemačkoj: Balkan-Sender aus Bosnien, Kroatien, Serbien, Montenegro und Nordmazedonien per IPTV – Programme, Pakete, Apps und Einrichtung.',
    'IPTV Balkan: IP televizija in Deutschland',
    'Dobro došli! Programme aus Bosnien und Herzegowina, Kroatien, Serbien und Montenegro sind in Deutschland gefragt. Per IPTV kommen sie über Ihre Internetleitung auf jeden Fernseher.',
    'IP televizija – also IPTV – bringt Sender aus Bosnien und Herzegowina, Kroatien, Serbien, Montenegro und Nordmazedonien nach Deutschland, ohne Satellitenschüssel. In Ihrer IPTV-App öffnen Sie die Ex-YU-Sendergruppen, legen Favoriten an und nutzen den Programmführer. Welche Programme Ihr Zugang enthält, sehen Sie im kostenlosen Test.',
    '''<p><strong>Dobro došli!</strong> Suchanfragen wie „IP televizija“, „IPTV kanali“, „IPTV programi“ oder „IPTV paketi“ zeigen, wie viele Menschen in Deutschland Fernsehen aus dem ehemaligen Jugoslawien schauen möchten. IPTV ist dafür ideal: Kein zweiter Receiver, keine Ausrichtung auf einen anderen Satelliten – nur die passende Senderliste in Ihrer App. Fragen zu „IPTV cena“ und „IPTV ponuda“ (Preis und Angebot) beantwortet unsere <a href="/preise/">Preisseite</a>: Alle Pakete enthalten dieselben Inhalte, Sie wählen nur Laufzeit und Geräteanzahl.</p>''',
    [['RTS', 'Öffentlich-rechtlicher Rundfunk Serbiens'], ['HRT', 'Öffentlich-rechtlicher Rundfunk Kroatiens'],
     ['BHRT / FTV / RTRS', 'Öffentlich-rechtliche Programme in Bosnien und Herzegowina'], ['RTCG', 'Öffentlich-rechtlicher Rundfunk Montenegros'],
     ['Pink', 'Privatsender aus Serbien'], ['Nova', 'Privatsender in Kroatien und Serbien'], ['RTL Hrvatska', 'Privatsender aus Kroatien'],
     ['N1', 'Nachrichtensender für die Region']],
    ('pakete', 'IPTV paketi i cena: Pakete und Preise'), '''
<p>Bei IPTV Kanal gibt es keine getrennten Länderpakete: Jedes Paket enthält dieselbe Senderliste, Sie wählen nur Laufzeit (1, 3, 6 oder 12 Monate) und Anzahl der Geräte. Das Jahrespaket für ein Gerät kostet 49 €, ohne automatische Verlängerung. Alle Preise unter <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>''' + checks(
        'Sendergruppen heißen oft „EX-YU“, „BA“, „HR“, „RS“ oder „MNE“.',
        'Kyrillische und lateinische Sendernamen werden mit einer M3U8-Playlist (UTF-8) korrekt angezeigt.',
        'Für Sport aus der Region (z. B. Arena Sport) zuerst im Test prüfen, ob die Sender enthalten sind.'),
    [('Was ist IP televizija?', 'IP televizija ist der Begriff für IPTV in den Sprachen des ehemaligen Jugoslawiens: Fernsehen über das Internet statt über Kabel oder Satellit.'),
     ('Kann ich Ex-YU Sender in Deutschland per IPTV schauen?', 'Ja. Per IPTV kommen Programme aus Bosnien und Herzegowina, Kroatien, Serbien und Montenegro über Ihre Internetleitung. Welche Sender Ihr Zugang enthält, zeigt der kostenlose Test.'),
     ('Was kostet IPTV für Balkan-Sender?', 'Bei IPTV Kanal enthalten alle Pakete dieselben Inhalte. Ein Monat kostet 9 €, ein Jahr 49 € für ein Gerät, ohne automatische Verlängerung.'),
     ('Werden kyrillische Sendernamen richtig angezeigt?', 'Ja, wenn die Playlist als M3U8 mit UTF-8-Kodierung geladen wird oder Sie einen Xtream-Codes-Login nutzen.')],
    ('IPTV Balkan', 'IP televizija: Sender aus Bosnien, Kroatien und Serbien.'),
    ['iptv-international', 'iptv-albanisch', 'iptv-rumaenisch', 'iptv-tuerkisch', 'iptv-senderliste', 'iptv-kaufen']))

PAGES.append(community(
    'iptv-rumaenisch', 'IPTV Rumänisch: Canale românești in Deutschland',
    'Canale românești per IPTV in Deutschland: rumänische Sender wie TVR, Pro TV und Antena 1 – beliebte Programme, Apps, Programmführer und Einrichtung.',
    'IPTV Rumänisch: rumänische Sender in Deutschland',
    'Bine ați venit! Sie möchten rumänisches Fernsehen in Deutschland schauen? Per IPTV kommen Programme aus Rumänien und der Republik Moldau über Ihre Internetleitung.',
    'Mit IPTV schauen Sie rumänische Sender (canale românești) in Deutschland, ohne Satellitenschüssel. In der IPTV-App öffnen Sie die rumänischen Sendergruppen, legen Favoriten an und nutzen den Programmführer in deutscher Zeit. Welche rumänischen Kanäle Ihr Zugang enthält, sehen Sie im kostenlosen Test.',
    '''<p><strong>Bine ați venit!</strong> Rumänen bilden eine der größten Zuwanderergruppen in Deutschland. Die Suche nach „canale românești IPTV“ zeigt, dass Nachrichten, Unterhaltung und Serien aus der Heimat gefragt sind. Per IPTV landen sie in derselben App wie Ihre deutschen Sender.</p>''',
    [['TVR 1 / TVR 2 / TVR Internațional', 'Öffentlich-rechtlicher Rundfunk Rumäniens'], ['Pro TV', 'Größter Privatsender: Shows und Nachrichten'],
     ['Antena 1', 'Privatsender: Unterhaltung'], ['Kanal D', 'Privatsender: Serien und Shows'], ['Digi24', 'Nachrichtensender'],
     ['Prima TV', 'Privatsender'], ['TVR Moldova', 'Programm für die Republik Moldau']],
    ('tipps', 'Tipps für rumänische Sender'), checks(
        'Sendergruppen heißen meist „RO“ oder „Romania“.',
        'Rumänische Sonderzeichen (ă, â, î, ș, ț) erscheinen korrekt mit M3U8 (UTF-8) oder Xtream-Codes-Login.',
        'Rumänien liegt eine Stunde vor Deutschland – der Programmführer rechnet das bei richtiger Zeitzone automatisch um.'),
    [('Kann ich rumänische Sender in Deutschland per IPTV schauen?', 'Ja. Per IPTV kommen rumänische Programme über Ihre Internetleitung. Welche Kanäle Ihr Zugang enthält, zeigt der kostenlose Test.'),
     ('Warum stimmen die Sendezeiten im Programmführer nicht?', 'Rumänien liegt eine Stunde vor Deutschland. Stellen Sie die Zeitzone in der App auf Europa/Berlin, dann werden die Zeiten automatisch umgerechnet.'),
     ('Welche App eignet sich für rumänische Sender?', 'Jede gängige IPTV-App wie IPTV Smarters Pro, TiviMate oder Smart IPTV. Die Oberfläche von Smarters lässt sich auch auf Rumänisch einstellen.')],
    ('IPTV Rumänisch', 'Canale românești: TVR, Pro TV und Antena per IPTV.'),
    ['iptv-international', 'iptv-balkan', 'iptv-senderliste', 'iptv-smarters-pro', 'tivimate', 'iptv-apps']))

PAGES.append(community(
    'iptv-russisch', 'IPTV Russisch: russischsprachiges TV in Deutschland',
    'Russischsprachiges Fernsehen per IPTV in Deutschland: was erlaubt ist, welche Sendergruppen es gibt, kyrillischer Programmführer, Zeitzonen und Einrichtung in der App.',
    'IPTV Russisch: russischsprachiges Fernsehen in Deutschland',
    'Добро пожаловать! Viele Menschen in Deutschland schauen gern Fernsehen auf Russisch. Hier lesen Sie, was dabei zu beachten ist und wie Sie russischsprachige Sender in Ihrer IPTV-App einrichten.',
    'Mit IPTV schauen Sie russischsprachiges Fernsehen in Deutschland über Ihre Internetleitung. Wichtig: Mehrere russische Staatssender sind wegen EU-Sanktionen in der EU nicht zur Verbreitung zugelassen. Russischsprachige Programme aus anderen Ländern sowie Film-, Kinder- und Musikkanäle richten Sie in der App wie jede Sendergruppe ein. Welche Sender Ihr Zugang enthält, sehen Sie im kostenlosen Test.',
    '''<p><strong>Добро пожаловать!</strong> Russischsprachige Zuschauer in Deutschland – Spätaussiedler, Menschen aus der Ukraine, dem Baltikum, Kasachstan und vielen weiteren Ländern – suchen nach „RU IPTV“, „russische IPTV Anbieter“ oder „IPTV russische TV“. Per IPTV kommen russischsprachige Programme ohne zusätzliche Schüssel auf den Fernseher.</p>''',
    [['Russischsprachige Nachrichtenkanäle aus der EU', 'z. B. Programme baltischer und europäischer Sender'], ['Russischsprachige Programme aus der Ukraine', 'Nachrichten und Unterhaltung'],
     ['Film- und Serienkanäle', 'Kino und Serien auf Russisch'], ['Kinderkanäle', 'Zeichentrick auf Russisch'], ['Musikkanäle', 'Pop und Klassik']],
    ('sanktionen', 'Was Sie über EU-Sanktionen wissen sollten'), '''
<p>Seit 2022 hat die Europäische Union die Verbreitung mehrerer russischer Staatsmedien untersagt, darunter RT und Sputnik sowie weitere staatliche Fernsehsender. Diese Sender dürfen in der EU weder per Kabel, Satellit noch per IPTV verbreitet werden. Achten Sie bei Angeboten, die damit werben, auf dieses Verbot. Russischsprachige Programme anderer Herkunft sind davon nicht betroffen.</p>''' + checks(
        'Sendergruppen heißen oft „RU“, „Russian“ oder „СНГ“.',
        'Kyrillische Sendernamen und EPG werden mit M3U8 (UTF-8) oder Xtream-Codes-Login korrekt angezeigt.',
        'IPTV Smarters Pro und TiviMate lassen sich auf Russisch umstellen.'),
    [('Kann ich russisches Fernsehen in Deutschland per IPTV schauen?', 'Russischsprachige Programme ja. Mehrere russische Staatssender sind aufgrund von EU-Sanktionen in der EU jedoch nicht zur Verbreitung zugelassen. Welche Sender Ihr Zugang enthält, zeigt der kostenlose Test.'),
     ('Wird der Programmführer auf Kyrillisch angezeigt?', 'Ja, wenn die Playlist als M3U8 mit UTF-8 geladen wird oder Sie einen Xtream-Codes-Login nutzen.'),
     ('Gibt es IPTV-Apps auf Russisch?', 'Ja. IPTV Smarters Pro, TiviMate und viele andere Player bieten eine russische Oberfläche.')],
    ('IPTV Russisch', 'Russischsprachiges TV in Deutschland: Sender, EPG und Regeln.'),
    ['iptv-international', 'iptv-senderliste', 'iptv-smarters-pro', 'tivimate', 'm3u-playlist', 'iptv-apps']))

PAGES.append(community(
    'iptv-tuerkisch', 'IPTV Türkisch: Türkische Sender in Deutschland',
    'Türkisches Fernsehen per IPTV in Deutschland: TRT, Show TV, Star TV, Kanal D, ATV, Beyaz TV und Now – beliebte Sender, Apps, EPG und Einrichtung.',
    'IPTV Türkisch: türkische Sender in Deutschland',
    'Hoş geldiniz! Türkisches Fernsehen gehört für Millionen Haushalte in Deutschland dazu. Per IPTV kommen Serien, Shows und Nachrichten aus der Türkei ohne zweite Schüssel auf Ihren Fernseher.',
    'Mit IPTV schauen Sie türkische Sender in Deutschland über Ihre Internetleitung, ohne auf Türksat ausgerichtete Schüssel. In der IPTV-App öffnen Sie die türkischen Sendergruppen, legen Favoriten an und nutzen den Programmführer in deutscher Zeit. Welche türkischen Kanäle Ihr Zugang enthält, sehen Sie im kostenlosen Test.',
    '''<p><strong>Hoş geldiniz!</strong> Türkische Serien (dizi), Shows und Nachrichten sind in Deutschland seit Jahrzehnten beliebt. Früher brauchte man dafür eine zweite Schüssel auf Türksat; per IPTV reicht die Internetleitung. Auch nach einzelnen Sendern wird gezielt gesucht, etwa „Beyaz IPTV“ für Beyaz TV.</p>''',
    [['TRT 1 / TRT Türk', 'Öffentlich-rechtlicher Rundfunk der Türkei'], ['Show TV', 'Serien und Shows'], ['Star TV', 'Serien und Unterhaltung'],
     ['Kanal D', 'Serien, Nachrichten'], ['ATV', 'Serien und Shows'], ['Beyaz TV', 'Unterhaltung und Familienprogramm'],
     ['Now (ehemals FOX Türkiye)', 'Serien und Nachrichten'], ['TV8', 'Shows und Wettbewerbe']],
    ('tipps', 'Tipps für türkische Sender'), checks(
        'Sendergruppen heißen meist „TR“ oder „Türkiye“.',
        'Türkische Zeichen (ç, ğ, ı, ö, ş, ü) werden mit M3U8 (UTF-8) oder Xtream-Codes-Login korrekt angezeigt.',
        'Die Türkei liegt im Winter zwei Stunden, im Sommer eine Stunde vor Deutschland – mit Zeitzone Europa/Berlin rechnet der Programmführer automatisch um.',
        'Für Serien lohnt sich Catch-Up: verpasste Folgen der letzten Tage nachholen, sofern der Sender Catch-Up unterstützt.'),
    [('Kann ich türkische Sender in Deutschland per IPTV schauen?', 'Ja. Per IPTV kommen türkische Programme über Ihre Internetleitung, ohne Türksat-Schüssel. Welche Kanäle Ihr Zugang enthält, zeigt der kostenlose Test.'),
     ('Was ist Beyaz IPTV?', 'Mit „Beyaz IPTV“ suchen viele nach dem türkischen Sender Beyaz TV per IPTV. Ob er in Ihrer Senderliste enthalten ist, sehen Sie im kostenlosen Test.'),
     ('Wie heißt FOX TV in der Türkei heute?', 'Der frühere Sender FOX Türkiye heißt seit 2024 Now. Bei der Suche nach „Fox TV IPTV“ ist häufig dieser Sender gemeint.'),
     ('Warum sind die Sendezeiten verschoben?', 'Die Türkei hat keine Sommerzeit und liegt im Winter zwei Stunden vor Deutschland. Stellen Sie die Zeitzone in der App auf Europa/Berlin.')],
    ('IPTV Türkisch', 'Türkische Sender wie TRT, Show TV und Beyaz TV per IPTV.'),
    ['iptv-international', 'iptv-balkan', 'iptv-russisch', 'iptv-senderliste', 'iptv-smarters-pro', 'tivimate']))

# ================================================================ CloudStream
PAGES.append(dict(
    slug='cloudstream', parent='apps', kind='guide',
    title='CloudStream App: Was ist das, wie sicher – und Alternativen',
    description='CloudStream erklärt: Was die Open-Source-App ist, wie Erweiterungen funktionieren, welche Risiken bestehen und welche IPTV-Apps die bessere Wahl sind.',
    eyebrow='APP-RATGEBER', h1='CloudStream: was die App kann und worauf Sie achten müssen',
    lead='CloudStream (oft „Cloud Stream“ geschrieben) taucht in vielen Fire-TV-Foren auf. Hier steht neutral, was die App ist, warum sie keine eigenen Inhalte hat und wann eine klassische IPTV-App besser passt.',
    answer='CloudStream ist eine quelloffene Android-App, die selbst keine Inhalte enthält. Filme, Serien und Livestreams kommen über Erweiterungen (Extensions) aus Repositories von Drittanbietern, die oft fremde Webseiten auslesen. Die App ist nicht im Play Store, Erweiterungen sind nicht geprüft, und viele Quellen verbreiten Inhalte ohne Rechte. Für Live-TV mit Programmführer sind IPTV-Apps wie TiviMate oder IPTV Smarters Pro die stabilere Wahl.',
    sections=[
        ('was', 'Was ist CloudStream?', '''
<p><strong>CloudStream</strong> ist ein Open-Source-Projekt für Android, Android TV und Fire TV mit Fire OS. Die App bringt eine Oberfläche für Filme, Serien und Livestreams mit, aber keine eigenen Quellen. Nutzer fügen Erweiterungen hinzu, die Inhalte aus dem Netz sammeln. Die App selbst ist nicht im Google Play Store oder Amazon Appstore gelistet und wird als APK installiert.</p>'''),
        ('risiken', 'Risiken: Recht, Sicherheit und Stabilität', checks(
            '<strong>Ungeprüfte Erweiterungen:</strong> Jeder kann Repositories veröffentlichen; Code und Herkunft sind für Laien nicht nachvollziehbar.',
            '<strong>Rechtliche Lage:</strong> Viele Erweiterungen greifen auf Seiten zu, die Filme und Sender ohne Lizenz verbreiten. Das Streamen offensichtlich illegaler Quellen kann auch für Nutzer rechtliche Folgen haben.',
            '<strong>Werbung und Weiterleitungen:</strong> Quellseiten finanzieren sich oft über aggressive Werbung und Pop-ups.',
            '<strong>Stabilität:</strong> Quellen fallen häufig aus; Live-TV ist unzuverlässig und ohne echten Programmführer.')),
        ('vergleich', 'CloudStream oder IPTV-App?', table(['', 'CloudStream', 'IPTV-App (z. B. TiviMate)'], [
            ['Inhalte', 'Aus Erweiterungen Dritter', 'Aus Ihrem IPTV-Abo'],
            ['Live-TV mit EPG', 'Kaum', 'Ja, vollständiger Programmführer'],
            ['Installation', 'Nur als APK', 'Play Store / Appstore oder offizielle APK'],
            ['Stabilität', 'Schwankend', 'Abhängig vom Anbieter, mit Support'],
            ['Support', 'Community', 'Anbieter-Support, z. B. per WhatsApp'],
        ], 'CloudStream im Vergleich')),
        ('alternativen', 'Die bessere Wahl für Live-TV', '''
<p>Wer Live-Fernsehen mit Programmführer, Catch-Up und Mediathek möchte, ist mit einer klassischen IPTV-App und einem Zugang mit Support besser bedient: <a href="/tivimate/">TiviMate</a> und <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> auf Fire TV und Android TV, <a href="/smart-iptv/">Smart IPTV</a> oder <a href="/set-iptv/">SET IPTV</a> auf Samsung und LG. Für Filme und Serien gibt es zudem legale Streamingdienste und die Mediatheken von ARD und ZDF. Alle Player im Überblick: <a href="/iptv-apps/">IPTV Apps</a>.</p>''' + TEST_TIP),
    ],
    faq=[
        ('Ist CloudStream legal?', 'Die App selbst ist Open Source und enthält keine Inhalte. Viele Erweiterungen greifen aber auf Quellen ohne Lizenz zu. Wer offensichtlich illegale Streams nutzt, kann sich in Deutschland rechtlich angreifbar machen.'),
        ('Ist CloudStream sicher?', 'Die App ist quelloffen, Erweiterungen von Drittanbietern sind jedoch nicht geprüft. Zudem leiten viele Quellseiten auf Werbung und fragwürdige Seiten weiter. Installieren Sie nur, was Sie nachvollziehen können.'),
        ('Gibt es CloudStream im Play Store?', 'Nein. CloudStream ist weder im Google Play Store noch im Amazon Appstore gelistet und wird als APK installiert.'),
        ('Was ist eine gute Alternative zu CloudStream?', 'Für Live-TV mit Programmführer eine IPTV-App wie TiviMate oder IPTV Smarters Pro mit einem Zugang inklusive Support. Für Filme und Serien legale Streamingdienste und die Mediatheken.'),
    ],
    related=['iptv-apps', 'tivimate', 'iptv-smarters-pro', 'kodi-iptv', 'iptv-fire-tv-stick', 'iptv-smarters-pro-firestick'],
    card=('CloudStream', 'Was die App ist, welche Risiken bestehen und bessere Alternativen.'),
))

# ================================================================ Payment
PAGES.append(dict(
    slug='iptv-bezahlen', parent='ratgeber', kind='guide',
    title='IPTV bezahlen: Paysafecard, PayPal & sichere Zahlungsarten',
    description='IPTV bezahlen: Paysafecard, PayPal, Überweisung oder Krypto – welche Zahlungsart wie sicher ist, was Käuferschutz bedeutet und worauf Sie beim IPTV-Kauf achten sollten.',
    eyebrow='KAUFBERATUNG', h1='IPTV bezahlen: Paysafecard, PayPal und Co.',
    lead='Die Wahl der Zahlungsart entscheidet, ob Sie Ihr Geld zurückbekommen, wenn etwas schiefläuft. Hier vergleichen wir Paysafecard, PayPal, Überweisung und Kryptowährungen beim IPTV-Kauf.',
    answer='Beim IPTV-Kauf ist eine Zahlungsart mit Rückbuchungsmöglichkeit am sichersten. Paysafecard ist anonym und bequem, bietet aber keinen Käuferschutz – das Guthaben ist nach Weitergabe des PINs weg. Überweisung und Kryptowährungen lassen sich ebenfalls kaum zurückholen. Bei IPTV Kanal testen Sie zuerst kostenlos und erhalten die verfügbaren Zahlungsarten mit Ihrem Angebot.',
    sections=[
        ('vergleich', 'Zahlungsarten im Vergleich', table(['Zahlungsart', 'Anonym?', 'Geld zurückholbar?', 'Hinweis'], [
            ['Paysafecard', 'Weitgehend', 'Nein', 'PIN nie an Unbekannte weitergeben'],
            ['PayPal (Waren &amp; Dienstleistungen)', 'Nein', 'Käuferschutz möglich', '„Freunde &amp; Familie“ hat keinen Käuferschutz'],
            ['Kreditkarte', 'Nein', 'Rückbuchung (Chargeback) möglich', 'Frist der Bank beachten'],
            ['SEPA-Überweisung', 'Nein', 'Kaum', 'Nur bei bekannten Empfängern'],
            ['Kryptowährung', 'Teilweise', 'Nein', 'Transaktionen sind endgültig'],
        ], 'IPTV Zahlungsarten im Vergleich')),
        ('paysafecard', 'IPTV mit Paysafecard bezahlen: was Sie wissen müssen', '''
<p>Die <strong>Paysafecard</strong> ist eine Prepaid-Karte, die Sie im Supermarkt, an der Tankstelle oder im Kiosk kaufen. Bezahlt wird mit einem 16-stelligen PIN. Vorteil: Sie geben keine Bank- oder Kartendaten preis. Nachteil: Wer den PIN kennt, kann das Guthaben sofort ausgeben, und eine Rückbuchung ist praktisch unmöglich. Die Polizei warnt regelmäßig vor Betrugsmaschen, bei denen Paysafecard-PINs per Chat oder Telefon erfragt werden.</p>
''' + tip('Geben Sie einen Paysafecard-PIN nur auf der offiziellen Bezahlseite eines Shops ein – niemals per WhatsApp, E-Mail oder Telefon an Personen, die Sie nicht kennen.', 'Sicherheit')),
        ('worauf-achten', 'Worauf Sie beim Bezahlen eines IPTV-Abos achten sollten', checks(
            '<strong>Erst testen, dann zahlen:</strong> Ein seriöser Anbieter lässt Sie vorher kostenlos testen.',
            '<strong>Klare Laufzeit:</strong> Einmalzahlung ohne automatische Verlängerung, wie bei allen <a href="/iptv-kaufen/">Paketen von IPTV Kanal</a>.',
            '<strong>Keine Vorkasse für „Lifetime“:</strong> Lifetime-Angebote verschwinden oft nach Wochen.',
            '<strong>Beleg aufheben:</strong> Bestellbestätigung und Zahlungsnachweis speichern.',
            '<strong>Support vor dem Kauf testen:</strong> Eine Frage stellen und die Antwortzeit prüfen.')),
        ('ablauf', 'So läuft die Bezahlung bei IPTV Kanal', steps(
            '<a href="/kostenlos-testen/">Kostenlos testen</a> – ohne Zahlungsdaten.',
            'Paket auf der <a href="/preise/">Preisseite</a> wählen und die Bestellanfrage senden.',
            'Sie erhalten per E-Mail oder WhatsApp Ihre Zugangsdaten und die verfügbaren Zahlungsarten.',
            'Einmal zahlen – es gibt keine automatische Verlängerung.')),
    ],
    faq=[
        ('Kann ich IPTV mit Paysafecard bezahlen?', 'Manche Anbieter akzeptieren Paysafecard. Bedenken Sie, dass es dabei keinen Käuferschutz gibt. Welche Zahlungsarten IPTV Kanal anbietet, nennen wir Ihnen mit Ihrem Angebot nach der Bestellanfrage.'),
        ('Welche Zahlungsart ist beim IPTV-Kauf am sichersten?', 'Zahlungsarten mit Rückbuchungsmöglichkeit, etwa Kreditkarte oder PayPal mit Käuferschutz. Paysafecard, Überweisung und Kryptowährungen lassen sich kaum zurückholen.'),
        ('Muss ich vor dem Test Zahlungsdaten angeben?', 'Bei IPTV Kanal nicht. Der Test ist kostenlos und ohne Zahlungsdaten; Sie zahlen erst, wenn Sie ein Paket bestellen.'),
        ('Verlängert sich mein IPTV-Abo nach der Zahlung automatisch?', 'Nein. Alle Pakete von IPTV Kanal sind Einmalzahlungen für die gewählte Laufzeit ohne automatische Verlängerung.'),
    ],
    related=['iptv-kaufen', 'iptv-anbieter-vergleich', 'iptv-erfahrungen', 'iptv-anbieter', 'iptv-reseller', 'was-ist-iptv'],
    card=('IPTV bezahlen', 'Paysafecard, PayPal und Co.: welche Zahlungsart sicher ist.'),
))

# ================================================================ Reseller
PAGES.append(dict(
    slug='iptv-reseller', parent='ratgeber', kind='guide',
    title='IPTV Reseller: Wie Reseller-Panels und Credits funktionieren',
    description='IPTV Reseller erklärt: Wie Reseller-Panels, Credits und Unterkonten funktionieren, welche Risiken Wiederverkäufer tragen und wie Kunden einen Reseller erkennen.',
    eyebrow='HINTERGRUND', h1='IPTV Reseller: so funktioniert der Wiederverkauf',
    lead='Viele IPTV-Angebote stammen nicht vom Betreiber der Server, sondern von Wiederverkäufern. Hier lesen Sie, wie das Reseller-Modell funktioniert – aus Sicht von Interessenten und von Kunden.',
    answer='Ein IPTV Reseller kauft beim Betreiber eines IPTV-Dienstes Guthaben (Credits) und erstellt damit über ein Reseller-Panel Zugänge für eigene Kunden. Er kümmert sich um Verkauf und Support, betreibt aber selbst keine Server. Für Kunden ist das unproblematisch, solange Preis, Laufzeit und Erreichbarkeit stimmen; Reseller tragen dagegen das Risiko, wenn der Dienst dahinter ausfällt.',
    sections=[
        ('modell', 'Wie das Reseller-Modell funktioniert', steps(
            '<b>Panel:</b> Der Reseller erhält Zugang zu einer Weboberfläche, in der er Kundenzugänge anlegt, verlängert und sperrt.',
            '<b>Credits:</b> Er kauft Guthaben im Voraus; ein Credit entspricht meist einem Monat für ein Gerät.',
            '<b>Unterkonten:</b> Große Reseller vergeben eigene Sub-Reseller-Zugänge.',
            '<b>Verkauf und Support:</b> Kundenkontakt, Einrichtung und Zahlungsabwicklung liegen beim Reseller.')),
        ('risiken', 'Risiken für Reseller', checks(
            '<strong>Abhängigkeit:</strong> Fällt der Dienst dahinter aus, sind Guthaben und Kundenbeziehungen gefährdet.',
            '<strong>Rechtliche Verantwortung:</strong> Wer Zugänge verkauft, haftet als Verkäufer gegenüber seinen Kunden und muss in Deutschland ein Impressum führen, Steuern abführen und Verbraucherrecht beachten.',
            '<strong>Lizenzfrage:</strong> Ein Reseller ist mitverantwortlich, wenn der Dienst Inhalte ohne Rechte verbreitet.',
            '<strong>Support-Last:</strong> Kunden wenden sich bei jedem Problem an den Reseller, nicht an den Betreiber.')),
        ('kunden', 'Für Kunden: einen Reseller erkennen', '''
<p>Für Zuschauer ist ein Reseller nicht automatisch schlechter. Achten Sie auf dieselben Kriterien wie bei jedem <a href="/iptv-anbieter/">IPTV Anbieter</a>: Testzugang, klare Laufzeit ohne Verlängerung, erreichbarer Support auf Deutsch und vollständiges Impressum. Warnzeichen sind sehr niedrige „Lifetime“-Preise, wechselnde Markennamen und Support nur über anonyme Chat-Konten. Unsere Bewertungsmatrix im <a href="/iptv-anbieter-vergleich/">IPTV-Anbieter-Vergleich</a> hilft beim Prüfen.</p>'''),
        ('kontakt', 'Partnerschaft mit IPTV Kanal?', '''
<p>Sie interessieren sich für eine Zusammenarbeit? Schreiben Sie uns an <a href="mailto:kontakt@iptvkanal.de">kontakt@iptvkanal.de</a> oder per <a href="/go/wa">WhatsApp</a>. Wir melden uns mit allen Informationen. Für Ihren eigenen Gebrauch starten Sie am besten mit dem <a href="/kostenlos-testen/">kostenlosen Test</a>.</p>'''),
    ],
    faq=[
        ('Was ist ein IPTV Reseller?', 'Ein Wiederverkäufer, der beim Betreiber eines IPTV-Dienstes Guthaben kauft und über ein Reseller-Panel Zugänge für eigene Kunden erstellt. Er übernimmt Verkauf und Support, betreibt aber keine Server.'),
        ('Was ist ein IPTV Reseller-Panel?', 'Eine Weboberfläche, in der Reseller Kundenzugänge anlegen, verlängern und sperren. Abgerechnet wird meist über vorab gekaufte Credits.'),
        ('Ist es schlecht, bei einem Reseller zu kaufen?', 'Nicht zwingend. Entscheidend sind Testzugang, faire Laufzeit, erreichbarer Support und ein vollständiges Impressum – wie bei jedem Anbieter.'),
        ('Welche Pflichten hat ein IPTV Reseller in Deutschland?', 'Wer gewerblich verkauft, braucht unter anderem ein Impressum, muss Steuern abführen und das Verbraucherrecht beachten. Zudem ist er mitverantwortlich, wenn der Dienst Inhalte ohne Rechte verbreitet.'),
    ],
    related=['iptv-anbieter', 'iptv-anbieter-vergleich', 'iptv-bezahlen', 'iptv-erfahrungen', 'iptv-kaufen', 'was-ist-iptv'],
    card=('IPTV Reseller', 'Reseller-Panels, Credits und Risiken verständlich erklärt.'),
))

# ================================================================ depth additions (audit: >= 450 words per guide)
_BY = {p['slug']: p for p in PAGES}
_DESC = {
    'iptv-international': 'IPTV International: Sender auf Albanisch, Bosnisch, Kroatisch, Serbisch, Rumänisch, Russisch, Türkisch und Englisch in Deutschland – Apps und Einrichtung.',
    'sky-iptv': 'Sky über IPTV: Was aus der Sky Q IPTV Box wurde, wie Sky Stream funktioniert, was es von Sky Q per Satellit unterscheidet und wie Sky Sport auf IPTV läuft.',
    'iptv-sport': 'IPTV Sport: Wo Formel 1, NBA, UFC, Eurosport, beIN Sports, ESPN und Fox Sports laufen – und wie Sie Sport per IPTV ohne Ruckler in bester Qualität schauen.',
    'iptv-russisch': 'Russischsprachiges Fernsehen per IPTV in Deutschland: was erlaubt ist, Sendergruppen, kyrillischer Programmführer, Zeitzonen und Einrichtung in der App.',
    'iptv-fussball': 'Fußball per IPTV: Wer Bundesliga, Champions League, Premier League und DFB-Pokal 2026/27 zeigt – und wie Sie Fußball auf jedem Gerät ruckelfrei schauen.',
    'iptv-bezahlen': 'IPTV bezahlen: Paysafecard, PayPal, Überweisung oder Krypto – welche Zahlungsart wie sicher ist, was Käuferschutz bedeutet und worauf Sie achten sollten.',
    'iptv-albanisch': 'IPTV auf Albanisch in Deutschland: albanische Kanäle aus Albanien und Kosovo per IPTV – beliebte Sender, Apps, Programmführer und Einrichtung.',
}
for _s, _d in _DESC.items():
    _BY[_s]['description'] = _d

_MORE = {
    'iptv-sport': ('mehrfach', 'Mehrere Spiele gleichzeitig: Multiview und zweite Bildschirme', '''
<p>An großen Sporttagen laufen Wettbewerbe parallel. TiviMate Premium bietet eine Mehrfachansicht, in der Sie bis zu vier Streams auf einem Fernseher anordnen. Jeder dieser Streams zählt als eigene Verbindung – planen Sie Bandbreite und Geräteanzahl entsprechend: Vier Full-HD-Streams brauchen rund 64 Mbit/s. Alternativ läuft ein zweites Spiel auf Tablet oder Handy; die Zahl gleichzeitiger Geräte wählen Sie bei IPTV Kanal im Paket (1 bis 5 Geräte).</p>'''),
    'iptv-russisch': ('zeit', 'Zeitzonen und Programmführer auf Russisch', '''
<p>Russischsprachige Programme senden aus verschiedenen Zeitzonen – von Mitteleuropa bis weit nach Osten. Der Programmführer rechnet alle Zeiten korrekt um, wenn in der App die Zeitzone Europa/Berlin eingestellt ist. Weicht eine Sendung trotzdem um Stunden ab, hilft in TiviMate die Option „EPG-Zeitverschiebung“ pro Playlist, in IPTV Smarters Pro die Einstellung „Zeitformat und Zeitzone“. Bei Catch-Up-Sendungen gilt dieselbe Zeitzone; Sendungen der letzten Tage lassen sich so zuverlässig finden.</p>'''),
    'iptv-rumaenisch': ('catchup', 'Serien und Shows nachholen: Catch-Up für rumänische Sender', '''
<p>Viele rumänische Zuschauer in Deutschland arbeiten im Schichtdienst und verpassen die Hauptsendezeit in Bukarest, die wegen der Zeitverschiebung ohnehin eine Stunde früher liegt. Unterstützt ein Sender Catch-Up, erkennen Sie das in TiviMate und IPTV Smarters Pro an einem kleinen Uhr-Symbol im Programmführer. Wählen Sie eine vergangene Sendung aus und starten Sie sie von Anfang an. Für Nachrichtensender lohnt sich außerdem eine eigene Favoritengruppe, damit Sie morgens schnell zwischen Digi24, TVR und deutschen Nachrichten wechseln.</p>
<p>Auf Smart-TVs von Samsung und LG eignen sich Player wie <a href="/smart-iptv/">Smart IPTV</a> oder <a href="/set-iptv/">SET IPTV</a>; auf einem <a href="/iptv-stick/">IPTV Stick</a> mit Fire OS oder Google TV ist <a href="/tivimate/">TiviMate</a> die komfortabelste Wahl.</p>'''),
    'iptv-tuerkisch': ('dizi', 'Türkische Serien (Dizi) komfortabel schauen', '''
<p>Türkische Serien laufen oft wöchentlich mit Folgen von zwei Stunden und mehr. Drei Funktionen machen das Schauen per IPTV angenehmer: <strong>Catch-Up</strong> für verpasste Folgen (sofern der Sender es unterstützt), <strong>Timeshift</strong> zum Pausieren während der Sendung und <strong>Favoritenlisten</strong> mit Ihren Lieblingssendern ganz oben. In TiviMate Premium können Sie Folgen zusätzlich auf einen USB-Speicher aufnehmen. Viele Zuschauer nutzen außerdem die Mediathek-Apps der Sender, die neben der IPTV-App auf Fire TV und Google TV laufen.</p>
<p>Für Haushalte mit mehreren Fernsehern: Wenn Eltern türkische und Kinder deutsche Sender schauen, brauchen Sie ein Paket mit zwei gleichzeitigen Geräten – Preise unter <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>'''),
    'cloudstream': ('installation', 'Warum wir keine Installationsanleitung für CloudStream geben', '''
<p>Für CloudStream kursieren zahlreiche Anleitungen mit Downloader-Codes und Listen von Repositories. Wir verzichten bewusst darauf: Welche Erweiterungen auf welche Quellen zugreifen, lässt sich von außen kaum prüfen, und Repositories ändern sich häufig. Wer die App trotzdem ausprobieren möchte, sollte sie nur aus dem offiziellen Projekt-Repository beziehen, keine Zugangsdaten anderer Dienste darin eingeben und die Berechtigungen der App prüfen.</p>
<p>Für den Fernseher im Wohnzimmer empfehlen wir eine stabile Kombination aus Gerät und App: einen <a href="/iptv-stick/">IPTV Stick</a> mit Fire OS oder Google TV, darauf <a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>, und einen Zugang mit Programmführer und Support. Wie die Installation auf dem Fire TV sicher gelingt, zeigt der Ratgeber <a href="/iptv-smarters-pro-firestick/">Smarters auf dem Fire TV Stick</a>.</p>'''),
    'iptv-reseller': ('begriffe', 'Die wichtigsten Begriffe im Reseller-Geschäft', table(['Begriff', 'Bedeutung'], [
        ['Panel', 'Weboberfläche zum Anlegen und Verwalten von Kundenzugängen'],
        ['Credit', 'Vorab gekauftes Guthaben, meist ein Monat für ein Gerät'],
        ['Line', 'Ein einzelner Kundenzugang mit Benutzername und Passwort'],
        ['Connections', 'Anzahl gleichzeitiger Streams pro Line'],
        ['Sub-Reseller', 'Wiederverkäufer, der Credits von einem anderen Reseller bezieht'],
        ['Trial', 'Kurzer Testzugang, der meist kein oder wenig Guthaben kostet'],
    ], 'Reseller-Begriffe') + '''
<p>Für Kunden heißt das: Ein Reseller kann Ihren Zugang verlängern, die Anzahl der Geräte ändern oder ihn bei Missbrauch sperren – nicht aber die Qualität der Server verbessern. Bei Problemen mit Sendern oder Stabilität hängt er vom Betreiber ab. Fragen Sie deshalb vor dem Kauf, wer Ihnen bei Störungen hilft und wie schnell. Mehr Kriterien im Ratgeber <a href="/iptv-erfahrungen/">IPTV Erfahrungen</a>.</p>'''),
    'iptv-bezahlen': ('betrug', 'Typische Betrugsmaschen beim IPTV-Kauf', checks(
        '<strong>Gutschein-Betrug:</strong> Der „Anbieter“ verlangt Paysafecard-, Amazon- oder iTunes-Codes per Chat und meldet sich danach nicht mehr.',
        '<strong>Lifetime-Lockangebot:</strong> Ein sehr niedriger Einmalpreis für „lebenslang“ – der Dienst verschwindet nach wenigen Wochen.',
        '<strong>Gefälschte Bewertungen:</strong> Viele Fünf-Sterne-Bewertungen an wenigen Tagen, ohne Details zu Gerät oder App.',
        '<strong>Druck:</strong> „Nur heute“-Rabatte, die zur sofortigen Zahlung ohne Test drängen.',
        '<strong>Weitergeleitete Zahlungen:</strong> Zahlungsempfänger, dessen Name nicht zum Anbieter passt.') + '''
<p>Wer betroffen ist, sollte die Zahlung dokumentieren und – bei Paysafecard – sofort den Kundenservice von Paysafecard sowie die Polizei informieren. Bei PayPal oder Kreditkarte lohnt sich ein schneller Antrag auf Käuferschutz bzw. Rückbuchung. Wie Sie seriöse Anbieter erkennen, zeigt unser <a href="/iptv-anbieter-vergleich/">IPTV-Anbieter-Vergleich</a>.</p>'''),
    'iptv-albanisch': ('geraete', 'Albanische Sender auf Fernseher, Handy und unterwegs', '''
<p>Am Fernseher laufen albanische Kanäle am komfortabelsten über einen <a href="/iptv-stick/">IPTV Stick</a> mit <a href="/tivimate/">TiviMate</a> oder <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>. Auf Samsung- und LG-Fernsehern ohne Stick nutzen Sie Player wie <a href="/smart-iptv/">Smart IPTV</a> oder <a href="/set-iptv/">SET IPTV</a>. Unterwegs oder im Urlaub in der Heimat schauen Sie auf dem Handy mit derselben App – innerhalb der gebuchten Anzahl gleichzeitiger Geräte. Für Hochzeiten und Familienfeiern, die von Musiksendern live übertragen werden, lohnt sich ein Paket mit zwei Geräten.</p>'''),
}
for _s, (_id, _h2, _html) in _MORE.items():
    _BY[_s]['sections'].append((_id, _h2, _html))
_BY['iptv-reseller']['sections'].append(('vertrag', 'Was Kunden bei einem Reseller klären sollten', checks(
    'Wer ist mein Ansprechpartner bei Störungen – und über welchen Kanal?',
    'Wie lange läuft mein Zugang genau, und verlängert er sich automatisch?',
    'Kann ich die Anzahl der Geräte später ändern, und was kostet das?',
    'Bekomme ich eine Rechnung oder Bestellbestätigung mit vollständigem Impressum?',
    'Gibt es vor dem Kauf einen kostenlosen Test auf meinem eigenen Gerät?')))
