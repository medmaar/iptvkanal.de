"""Deep SEO audit 25.11.2026: per-page fixes applied last by build-seo-pages.py.

DESCRIPTION: meta descriptions trimmed to 120–155 characters (no truncation in German SERPs).
TITLE / H1: titles in the 50–60 character window, H1s that carry the page's primary keyword.
LEAD: lead paragraphs that name the primary keyword in the first sentence.
SOURCES: outbound links to official manufacturer, app and authority websites where a page had none.
"""

DESCRIPTION = {
    'duplexplay': 'DuplexPlay IPTV einrichten: Geräte-ID und Code, Playlist über die Website hinzufügen, Aktivierung auf Samsung, LG und Android, Fehlerhilfe.',
    'flix-iptv': 'Flix IPTV einrichten: App auf Samsung, LG, Android oder Fire TV installieren, MAC-Adresse finden, Playlist hochladen und aktivieren.',
    'gse-smart-iptv': 'GSE Smart IPTV einrichten: Xtream Codes und M3U auf iPhone, Apple TV und Android hinzufügen, EPG, Einstellungen, Kosten und Hilfe bei Fehlern.',
    'hot-player': 'Hot Player und Bay IPTV einrichten: Playlist per MAC-Adresse hinzufügen, Aktivierung, unterstützte Geräte, typische Fehler und Alternativen.',
    'implayer': 'iMPlayer IPTV einrichten: Installation auf Android, Fire TV und Smart TV, Xtream Codes und M3U hinzufügen, Aktivierung und Fehlerhilfe.',
    'iplaytv': 'iPlayTV einrichten: M3U und Xtream auf Apple TV, iPhone und iPad hinzufügen, EPG-Raster, Kosten, beste Einstellungen und Hilfe bei Fehlern.',
    'iptv-4k': 'IPTV in 4K Ultra HD: wie viel Internet Sie brauchen, welche Geräte und Apps 4K können und warum 8K-IPTV meist nur Werbung ist. Mit Tabelle.',
    'iptv-aufnehmen': 'IPTV aufnehmen: welche Apps und Geräte Sendungen aufzeichnen, was Timeshift und Catch-up können, wie viel Speicher nötig ist und was erlaubt ist.',
    'iptv-chromecast': 'IPTV auf Chromecast: vom Handy casten mit IPTV Smarters, VLC oder GSE – oder TiviMate direkt auf Chromecast mit Google TV nutzen. Anleitung.',
    'iptv-einrichten': 'IPTV einrichten in 4 Schritten: Gerät prüfen, App wählen, Xtream-Login, M3U-Link oder MAC eintragen und EPG laden – für alle Geräte erklärt.',
    'iptv-extreme': 'IPTV Extreme und IPTV Extreme Pro einrichten: M3U und Xtream hinzufügen, Unterschiede zur Pro-Version, Aufnahme, EPG und Hilfe bei Fehlern.',
    'iptv-geraete': 'Auf welchen Geräten läuft IPTV? Smart TV, Fire TV Stick, Android-Box, MAG, Receiver, Apple TV, iPhone und PC – mit passender App und Anleitung.',
    'iptv-google-tv': 'IPTV auf Google TV Streamer und Chromecast mit Google TV: Unterschiede der Modelle, beste Apps wie TiviMate, Einstellungen und Fehlerhilfe.',
    'iptv-hisense-tv': 'IPTV auf dem Hisense Smart TV mit VIDAA: welche Apps der VIDAA Store bietet, warum ein Stick oft besser ist und wie Sie alles einrichten.',
    'iptv-kaufen': 'IPTV kaufen ohne Vertrag: 20.000+ Sender, Filme und Serien bis 4K, 1 bis 5 Geräte, 1 bis 12 Monate, keine Verlängerung. Jetzt kostenlos testen.',
    'iptv-metz-tv': 'IPTV auf dem Metz Smart TV: Metz Blue mit Android TV oder Google TV, Metz Classic mit eigenem System, passende Apps und Einrichtung.',
    'iptv-pc-mac': 'IPTV am PC, Laptop und Mac: M3U-Playlist in VLC öffnen, IPTV Smarters für Windows, Kodi am Computer und IPTV im Browser – Schritt für Schritt.',
    'iptv-reseller': 'IPTV Reseller erklärt: wie Reseller-Panels, Credits und Unterkonten funktionieren, welche Risiken es gibt und wie Kunden Reseller erkennen.',
    'iptv-senderliste': 'IPTV Senderliste verstehen: deutsche Sender in der Playlist finden, Länder ausblenden, Favoriten anlegen und den Programmführer (EPG) verknüpfen.',
    'iptv-sharp-tv': 'IPTV auf dem Sharp Smart TV: Sharp Aquos mit Android TV oder Google TV, andere Systeme, beste IPTV App und Lösungen, wenn nichts funktioniert.',
    'iptv-smarters-pro-firestick': 'IPTV Smarters Pro auf dem Fire TV Stick installieren: Downloader einrichten, App sicher laden, Xtream-Login eintragen, Hilfe bei Vega OS.',
    'iptv-stick': 'IPTV Stick im Vergleich: Fire TV Stick 4K Max, Google TV Streamer, Xiaomi TV Stick 4K und Roku – welcher Stick IPTV-Apps kann und welcher nicht.',
    'iptv-stream-player': 'IPTV Stream Player und Smart IPTV Xtream Player: was hinter den Apps steckt, wie Sie Xtream Codes und M3U einrichten und seriöse Apps erkennen.',
    'iptv-telefunken-tv': 'IPTV auf dem Telefunken Smart TV: Modelle mit Fire TV Edition, Android TV oder anderen Systemen, beste App und Anleitung mit Downloader.',
    'iptv-vu-plus': 'IPTV auf Vu+ einrichten: Zero 4K, Uno 4K SE und Duo 4K SE mit OpenATV oder VTi, Plugins wie XStreamity und e2m3u2bouquet, EPG und Fehlerhilfe.',
    'iptv-xiaomi-tv': 'IPTV auf dem Xiaomi Smart TV: Xiaomi TV A, A Pro und Q-Serie mit Google TV oder Android TV, beste IPTV App und Tipps für große Senderlisten.',
    'm3u-playlist': 'Was ist eine M3U Playlist? So laden Sie eine IPTV M3U Liste in VLC, Smarters, TiviMate und Smart IPTV und vermeiden unsichere Gratis-Listen.',
    'mac-player': 'MAC Player, Virginia, Family und King 4K Player: wie MAC-basierte IPTV Apps funktionieren, Playlist hinzufügen, Aktivierung und Alternativen.',
    'max-player': 'MaxPlayer IPTV einrichten: unterstützte Geräte von Samsung bis iPhone, Playlist hinzufügen, Aktivierung, Kosten, Einstellungen und Fehlerhilfe.',
    'mx-player-iptv': 'MX Player für IPTV: M3U-Streams und Sender-Links abspielen, als externen Player in IPTV-Apps nutzen, Grenzen ohne EPG und bessere Alternativen.',
    'net-iptv': 'Net IPTV einrichten: Playlist über die Website hochladen, Aktivierung und Kosten, Samsung- und LG-Fernseher, Net ipTV Pro für iPhone, Fehlerhilfe.',
    'perfect-player': 'Perfect Player IPTV einrichten: M3U-Playlist und XMLTV-EPG eintragen, Receiver-Oberfläche, Einstellungen für Android und Windows, Alternativen.',
    'pvr-iptv-simple-client': 'PVR IPTV Simple Client in Kodi einrichten: Add-on aktivieren, M3U-Playlist und XMLTV-EPG eintragen, Catch-up nutzen und Fehler beheben.',
    'room-iptv': 'Room IPTV einrichten: unterstützte Geräte (Samsung, LG, Android), Playlist per MAC-Adresse hinzufügen, Aktivierung, Einstellungen und Fehlerhilfe.',
    'smart-iptv': 'Smart IPTV (SIPTV) auf Samsung und LG: App installieren, MAC-Adresse finden, Playlist über „My List“ hochladen, aktivieren und Fehler beheben.',
    'smart-stb': 'Smart STB einrichten: MAG-Portal auf Samsung- und LG-Smart-TVs nutzen, Portal-URL und MAC-Adresse, Aktivierung und Hilfe bei „STB blocked“.',
    'smarters-player-lite': 'Smarters Player Lite einrichten: Xtream Codes und M3U auf iPhone, iPad und Apple TV, Unterschiede zu Smarters Pro, Einstellungen und Fehlerhilfe.',
    'stbemu': 'STBEmu und STBEmu Pro einrichten: MAG-Portal auf Android und Fire TV, Profil anlegen, Portal-URL und MAC-Adresse eintragen, Fehlerhilfe.',
    'tivimate': 'TiviMate IPTV Player auf Fire TV Stick und Android TV einrichten: Playlist hinzufügen, Premium freischalten, EPG, Aufnahme und Fehlerhilfe.',
    'tvip-box': 'TVIP S-Box v.605 für IPTV einrichten: Dual-Boot mit Linux und Android, Stalker-Portal und M3U, 4K HEVC, WLAN und die besten Einstellungen.',
    'vlc-iptv': 'IPTV mit VLC Media Player: M3U-Playlist auf Windows, Mac, Linux, Android und iPhone öffnen, Netzwerkstream einrichten und Puffer anpassen.',
    'vu-iptv-player': 'VU IPTV Player und Vu Player Pro einrichten: unterstützte Geräte, Playlist per MAC oder Login hinzufügen, Aktivierung und Hilfe bei Problemen.',
    'was-ist-iptv': 'Was ist IPTV? Internet Protocol Television einfach erklärt: wie Fernsehen über das Internet funktioniert, was Sie brauchen und was es kostet.',
    'xtream-codes-iptv': 'Was ist Xtream Codes? So nutzen Sie Xtream-Logins in XCIPTV, Smarters und TiviMate, erzeugen einen M3U-Link und richten XCIPTV auf Fire TV ein.',
}

TITLE = {
    'sat-ip': 'SAT>IP vs. IPTV: Unterschiede, Geräte, Apps & was besser ist',
}

H1 = {
    'bob-player': 'Bob Player und Bob Pro IPTV: Anleitung',
    'iplaytv': 'iPlayTV Player: IPTV auf Apple TV und iPhone',
    'iptv-bergisches-land': 'IPTV im Bergischen Land (Bergisches Land): Anbieter, Abo und Test',
    'iptv-box': 'IPTV Box kaufen: die beste Android-TV-Box für IPTV 2026',
    'iptv-im-browser': 'IPTV im Browser schauen: Fernsehen ohne App am PC und Laptop',
    'iptv-lg-tv': 'IPTV auf dem LG Smart TV (webOS)',
    'iptv-regionen': 'IPTV nach Region: Bundesländer und Regionen',
    'iptv-staedte': 'IPTV nach Stadt: die 50 größten Städte',
    'iptv-stick': 'IPTV Stick 2026: welcher Streaming-Stick für IPTV?',
    'iptv-server': 'IPTV Server erklärt: wie Streams zu Ihnen kommen – und warum sie puffern',
    'iptv-vu-plus': 'IPTV auf Vu+ einrichten: Zero 4K, Uno 4K SE und Duo 4K SE',
    'kodi-iptv': 'Kodi IPTV einrichten: Live-TV mit dem PVR IPTV Simple Client',
    'net-iptv': 'Net IPTV einrichten: Anleitung für Samsung, LG und iPhone',
    'was-ist-iptv': 'Was ist IPTV? Internet Protocol Television einfach erklärt',
    'xciptv': 'XCIPTV Player einrichten: Anleitung und Einstellungen',
}

LEAD = {
    'bester-iptv-player': 'Der beste IPTV Player hängt von Ihrem Gerät ab – für jedes gibt es einen klaren Favoriten. Wir haben die gängigen Apps nach Bedienung, Programmführer, Mediathek, Aufnahme und Kostenmodell eingeordnet.',
    'duplexplay': 'DuplexPlay IPTV gehört zu den bekannten Smart-TV-Playern, bei denen die Playlist über eine Website verknüpft wird. So richten Sie die App Schritt für Schritt ein.',
    'fire-tv-modelle': 'Fire TV Stick Modelle unterscheiden sich stark: Lite, HD, 4K, 4K Max und Cube haben verschiedene Leistung, Speicher und vor allem Betriebssysteme. Hier sehen Sie, welches Modell für IPTV taugt.',
    'iplaytv': 'iPlayTV ist ein Klassiker unter den IPTV- und M3U-Playern für Apple TV. Sein Programmführer im Raster erinnert an einen Receiver – ideal für alle, die viel linear fernsehen.',
    'iptv-anbieter': 'IPTV Anbieter in Deutschland gibt es in drei Formen: Internetanbieter, TV-Streaming-Apps und unabhängige IPTV-Dienste. Wir erklären die Unterschiede und woran Sie einen guten Anbieter erkennen.',
    'iptv-apple-tv-iphone': 'IPTV auf Apple TV, iPhone und iPad kommt immer aus dem App Store. Das macht die Einrichtung sicher und einfach – TiviMate gibt es hier allerdings nicht, dafür starke Alternativen.',
    'iptv-apps': 'Die besten IPTV Apps sind Ihre Fernbedienung für Senderliste, Programmführer und Mediathek. Hier finden Sie den passenden IPTV Player für jedes Gerät – mit Anleitungen.',
    'iptv-aufnehmen': 'IPTV aufnehmen geht auf drei Wegen: Aufnahme, Timeshift und Catch-up. Ob Tatort am Sonntag oder das Spiel während der Arbeit – hier lesen Sie, was Ihr Gerät davon kann.',
    'iptv-balkan': 'IPTV Balkan: Dobro došli! Programme aus Bosnien und Herzegowina, Kroatien, Serbien und Montenegro sind in Deutschland gefragt. Per IPTV kommen sie über Ihre Internetleitung auf jeden Fernseher.',
    'iptv-bezahlen': 'IPTV bezahlen Sie am besten so, dass Sie Ihr Geld zurückbekommen, wenn etwas schiefläuft. Hier vergleichen wir Paysafecard, PayPal, Überweisung und Kryptowährungen beim IPTV-Kauf.',
    'iptv-box': 'Wer eine IPTV Box kaufen möchte, sollte auf schnelles Umschalten, flüssiges 4K und freie App-Wahl achten. Wir zeigen, worauf es 2026 ankommt – und welche Modelle sich bewährt haben.',
    'iptv-dreambox': 'IPTV auf der Dreambox DM920 und Dreambox One: Der Klassiker unter den Linux-Receivern zeigt mit dem richtigen Plugin IPTV-Sender direkt neben Ihren Satellitenprogrammen.',
    'iptv-englisch': 'Englisches Fernsehen in Deutschland suchen Hunderttausende – Briten, Iren, Amerikaner und alle, die lieber im Original schauen. Hier lesen Sie, welche Wege es gibt und wo die Grenzen liegen.',
    'iptv-erfahrungen': 'IPTV Erfahrungen sind vor dem Kauf wertvoll – doch in kaum einer Branche sind Bewertungen so gemischt und so oft gekauft. So filtern Sie die brauchbaren Berichte heraus.',
    'iptv-georgisch': 'IPTV Georgisch: Sie suchen Imedi oder Rustavi 2 in Deutschland? Per IPTV kommen georgische Programme über Ihre Internetleitung auf Fernseher, Handy und Tablet – mit Programmführer in deutscher Zeit.',
    'iptv-grundig-tv': 'IPTV auf dem Grundig Smart TV: Die Geräte gibt es mit Android TV, Google TV oder als Fire TV Edition. Auf allen drei Varianten lässt sich IPTV direkt einrichten – nur der Weg zur App ist verschieden.',
    'iptv-hisense-tv': 'IPTV auf dem Hisense Smart TV ist möglich, hat aber eine Hürde: Das hauseigene System VIDAA bietet nur wenige IPTV-Player. Wir zeigen die besten Apps und die einfachste Lösung.',
    'iptv-im-browser': 'IPTV im Browser schauen ist ideal, wenn Sie am Arbeitsplatz, auf dem Firmenlaptop oder Chromebook nichts installieren dürfen. Wir zeigen, was Web Player können, wo die Grenzen liegen und wie Sie Ihre Zugangsdaten schützen.',
    'iptv-international': 'IPTV International: Millionen Menschen in Deutschland schauen gern Programme aus ihrer Heimat. Mit IPTV brauchen Sie dafür keine zweite Satellitenschüssel – nur die richtige Senderliste in Ihrer App.',
    'iptv-medion-tv': 'IPTV auf dem Medion Smart TV klappt bei den meisten aktuellen Modellen direkt, denn viele laufen mit Android TV oder Google TV. So richten Sie die passende App ein.',
    'iptv-metz-tv': 'IPTV auf dem Metz Smart TV hängt von der Modelllinie ab: Metz steht für Fernseher mit langer Tradition aus Franken, heute gibt es zwei Linien – und für IPTV ist wichtig, welche Sie haben.',
    'iptv-philips-tv': 'IPTV auf dem Philips Smart TV: Die Geräte gibt es mit vier verschiedenen Systemen. Ob IPTV direkt auf dem Fernseher läuft, hängt davon ab, welches Ihr Modell hat – so finden Sie es heraus.',
    'iptv-regionen': 'IPTV nach Region: alle Bundesländer und die wichtigsten Regionen – vom Ruhrgebiet über die Eifel bis ins Allgäu. Mit Tipps für langsame Leitungen auf dem Land und für die Ferienwohnung.',
    'iptv-roku': 'IPTV auf dem Roku Streaming Stick ist nur eingeschränkt möglich. Roku-Geräte sind einfach zu bedienen und in Deutschland erhältlich – hier lesen Sie, warum sie für eigene IPTV-Zugänge kaum taugen und welche Wege es gibt.',
    'iptv-samsung-tv': 'IPTV auf dem Samsung Smart TV läuft unter Tizen. TiviMate gibt es dort nicht – dafür eine Reihe guter IPTV Player, die Sie in wenigen Minuten einrichten.',
    'iptv-server': 'IPTV Server erklärt: Wenn IPTV puffert, liegt es selten nur an einer Stelle. Zwischen Fernsehsender und Fernseher liegen Server, Rechenzentren, Netzbetreiber und Ihr Heimnetz – wer die Kette kennt, findet den Fehler schneller.',
    'iptv-sharp-tv': 'IPTV auf dem Sharp Smart TV: Sharp Aquos läuft in Europa häufig mit Android TV oder Google TV, einige Modelle mit anderen Systemen. So richten Sie IPTV ein.',
    'iptv-smarters-pro-smart-tv': 'IPTV Smarters Pro auf Samsung, LG und anderen Smart TVs: Ob die App im Store steht, hängt von Marke, Betriebssystem und Baujahr ab. Hier sehen Sie für jede Plattform, was geht und was Sie tun, wenn die App fehlt.',
    'iptv-staedte': 'IPTV nach Stadt: Von Berlin bis Osnabrück zeigen wir für die 50 größten Städte Deutschlands, was Sie für IPTV vor Ort wissen sollten – Leitung, Regionalprogramm, Sport und Test.',
    'iptv-stick': 'Ein IPTV Stick macht 2026 aus jedem Fernseher mit HDMI-Anschluss einen IPTV-Empfänger. Entscheidend ist nicht die Marke, sondern ob der Stick die IPTV-App Ihrer Wahl installieren kann.',
    'iptv-strong-thomson-box': 'IPTV auf Strong LEAP-S3 und Thomson Streaming Box 240G: Beide Hersteller bauen günstige, von Google zertifizierte Streaming-Boxen. Hier lesen Sie, wie Sie IPTV einrichten und was die Geräte unterscheidet.',
    'iptv-tcl-tv': 'IPTV auf dem TCL Smart TV ist besonders einfach: TCL setzt in Europa fast durchgehend auf Google TV, damit sind alle wichtigen IPTV-Apps verfügbar.',
    'iptv-telekom-vodafone': 'Fernsehen über Telekom, Vodafone, 1&amp;1 und o2 kommt per IPTV als Zusatz zum Internetanschluss. Wir erklären, wie das funktioniert – und wann eine unabhängige Lösung besser passt.',
    'iptv-toshiba-tv': 'IPTV auf dem Toshiba Smart TV: Die Geräte werden in Europa in Lizenz gebaut und laufen je nach Modell mit Fire TV, VIDAA oder Android TV. Für IPTV müssen Sie deshalb zuerst Ihr System kennen.',
    'iptv-xiaomi-tv-box': 'IPTV auf Xiaomi Mi Box S, TV Box S und TV Stick 4K: Xiaomis Zuspieler sind günstige Android-TV-Geräte und bei IPTV-Nutzern sehr beliebt. Hier sehen Sie, welches Modell was kann.',
    'iptv-xiaomi-tv': 'IPTV auf dem Xiaomi Smart TV ist unkompliziert: Die Fernseher laufen in Europa mit Google TV bzw. Android TV, damit stehen alle wichtigen IPTV-Apps aus dem Play Store bereit.',
    'kodi-iptv': 'Kodi IPTV einrichten dauert nur wenige Minuten: Kodi verwandelt PC, Box oder Stick in ein Mediacenter, und mit dem offiziellen PVR IPTV Simple Client wird daraus ein IPTV-Empfänger mit Programmführer.',
    'm3u-playlist': 'Die M3U Playlist ist das Rückgrat vieler IPTV-Apps. Wir zeigen, was in einer IPTV M3U Liste steckt, wie Sie sie laden und warum „beste M3U Liste deutsch gratis“ selten hält, was sie verspricht.',
    'mac-player': 'MAC Player, Virginia Player, Family Player und King 4K Player folgen demselben Prinzip: MAC-Adresse anzeigen, Playlist über die Website verknüpfen, nach dem Test aktivieren. Hier erfahren Sie, worauf Sie achten sollten.',
    'mag-box-modelle': 'MAG Box Modelle gibt es viele: Infomir hat in 15 Jahren zahlreiche Boxen gebaut, die teils noch im Einsatz sind – aber nicht jede taugt für heutige IPTV-Streams. Hier sehen Sie, welche Box was kann.',
    'nanomid-player': 'Nanomid Player IPTV ist ein Aktivierungs-Player für Smart TVs und Mobilgeräte. Die Playlist wird über die Website verknüpft, die App am Fernseher bleibt einfach.',
    'net-iptv': 'Net IPTV einrichten ist einfach: Der schlanke Player für Smart TVs lädt die Playlist, die Sie bequem am Handy oder PC hochladen. Hier lesen Sie, wie das funktioniert.',
    'plex-jellyfin-iptv': 'IPTV in Plex und Jellyfin: Haben Sie bereits einen Mediaserver für Filme und Serien, können Sie dort auch Live-TV einbinden – mit Programmführer, Aufnahmen und Zugriff von jedem Gerät im Haushalt.',
    'progtv': 'ProgTV IPTV stammt von den Machern von ProgDVB und bringt eine Fernseh-Oberfläche auf Computer und Android – inklusive Programmführer und Aufnahme.',
    'purple-iptv': 'Purple IPTV Player ist eine ganze App-Familie: Purple Easy, Purple Lite, Purple Mobile und weitere. Hier sehen Sie, welche Variante zu Ihrem Gerät passt.',
    'tvip-box': 'TVIP S-Box v.605 IPTV einrichten: Die kompakte 4K-Box hat zwei Systeme – Linux für Portal-IPTV wie bei einer MAG-Box und Android für Apps. So nutzen Sie beide.',
}

# Outbound links to official sources (manufacturer, app developer, authority, reference).
_BNETZA = ('Bundesnetzagentur: Breitbandmessung', 'https://breitbandmessung.de/')
_ATLAS = ('Gigabit-Grundbuch / Breitbandatlas des Bundes', 'https://gigabitgrundbuch.bund.de/')

SOURCES = {
    'tivimate': [('TiviMate – offizielle Website', 'https://tivimate.com/'), ('TiviMate IPTV Player bei Google Play', 'https://play.google.com/store/apps/details?id=ar.tvplayer.tv')],
    'tivimate-fire-tv-stick': [('TiviMate – offizielle Website', 'https://tivimate.com/'), ('Wikipedia: Amazon Fire TV', 'https://de.wikipedia.org/wiki/Amazon_Fire_TV')],
    'tivimate-premium': [('TiviMate – offizielle Website', 'https://tivimate.com/')],
    'tivimate-andere-geraete': [('TiviMate – offizielle Website', 'https://tivimate.com/'), ('Android TV – offizielle Website', 'https://www.android.com/tv/')],
    'kodi-iptv': [('Kodi – offizielle Website', 'https://kodi.tv/'), ('Kodi Wiki: PVR IPTV Simple Client', 'https://kodi.wiki/view/Add-on:PVR_IPTV_Simple_Client')],
    'pvr-iptv-simple-client': [('Kodi Wiki: PVR IPTV Simple Client', 'https://kodi.wiki/view/Add-on:PVR_IPTV_Simple_Client'), ('Kodi – offizielle Website', 'https://kodi.tv/')],
    'vlc-iptv': [('VLC Media Player – VideoLAN', 'https://www.videolan.org/vlc/'), ('VideoLAN Wiki', 'https://wiki.videolan.org/')],
    'plex-jellyfin-iptv': [('Plex Support: Live TV & DVR', 'https://support.plex.tv/'), ('Jellyfin Dokumentation', 'https://jellyfin.org/docs/')],
    'iptv-smarters-pro': [('IPTV Smarters – offizielle Website', 'https://www.iptvsmarters.com/')],
    'iptv-smarters-pro-firestick': [('IPTV Smarters – offizielle Website', 'https://www.iptvsmarters.com/')],
    'iptv-smarters-pro-smart-tv': [('IPTV Smarters – offizielle Website', 'https://www.iptvsmarters.com/')],
    'smarters-player-lite': [('IPTV Smarters – offizielle Website', 'https://www.iptvsmarters.com/')],
    'xciptv': [('XCIPTV Player bei Google Play', 'https://play.google.com/store/search?q=xciptv&c=apps')],
    'smart-iptv': [('Smart IPTV – offizielle Website', 'https://siptv.app/')],
    'set-iptv': [('SET IPTV – offizielle Website', 'https://setsysteme.com/')],
    'flix-iptv': [('Flix IPTV – offizielle Website', 'https://flixiptv.eu/')],
    'ibo-player': [('IBO Player – offizielle Website', 'https://iboplayer.com/')],
    'gse-smart-iptv': [('GSE Smart IPTV bei Google Play', 'https://play.google.com/store/search?q=gse%20smart%20iptv&c=apps')],
    'iplaytv': [('Apple App Store', 'https://www.apple.com/de/app-store/')],
    'iptvx': [('Apple App Store', 'https://www.apple.com/de/app-store/'), ('Apple TV Support', 'https://support.apple.com/de-de/apple-tv')],
    'perfect-player': [('Perfect Player bei Google Play', 'https://play.google.com/store/search?q=perfect%20player%20iptv&c=apps')],
    'ott-navigator': [('OTT Navigator bei Google Play', 'https://play.google.com/store/search?q=ott%20navigator&c=apps')],
    'televizo': [('Televizo bei Google Play', 'https://play.google.com/store/search?q=televizo&c=apps')],
    'sparkle-tv': [('Sparkle TV bei Google Play', 'https://play.google.com/store/search?q=sparkle%20tv%20iptv&c=apps')],
    'iptvnator': [('IPTVnator auf GitHub', 'https://github.com/4gray/iptvnator')],
    'stbemu': [('STBEmu bei Google Play', 'https://play.google.com/store/search?q=stbemu&c=apps')],
    'mx-player-iptv': [('MX Player bei Google Play', 'https://play.google.com/store/search?q=mx%20player&c=apps')],
    'iptv-extreme': [('IPTV Extreme bei Google Play', 'https://play.google.com/store/search?q=iptv%20extreme&c=apps')],
    'mag-box-iptv': [('Infomir – Hersteller der MAG-Boxen', 'https://www.infomir.eu/')],
    'mag-box-modelle': [('Infomir – Hersteller der MAG-Boxen', 'https://www.infomir.eu/')],
    'iptv-receiver': [('OpenATV – Enigma2-Image', 'https://www.opena.tv/')],
    'iptv-vu-plus': [('Vu+ – Hersteller', 'https://www.vuplus.com/'), ('OpenATV – Enigma2-Image', 'https://www.opena.tv/')],
    'iptv-dreambox': [('Dream Property – Hersteller der Dreambox', 'https://www.dream-multimedia-tv.de/')],
    'iptv-nvidia-shield': [('NVIDIA Shield TV – Hersteller', 'https://www.nvidia.com/de-de/shield/')],
    'iptv-google-tv': [('Google TV Hilfe', 'https://support.google.com/googletv/')],
    'iptv-chromecast': [('Chromecast Hilfe – Google', 'https://support.google.com/chromecast/')],
    'iptv-android': [('Android TV – offizielle Website', 'https://www.android.com/tv/')],
    'iptv-apple-tv': [('Apple TV Support', 'https://support.apple.com/de-de/apple-tv')],
    'iptv-apple-tv-iphone': [('Apple TV Support', 'https://support.apple.com/de-de/apple-tv'), ('Apple App Store', 'https://www.apple.com/de/app-store/')],
    'iptv-samsung-tv': [('Samsung Support Deutschland', 'https://www.samsung.com/de/support/')],
    'iptv-lg-tv': [('LG Support: Fernseher', 'https://www.lg.com/de/support/')],
    'iptv-sony-bravia': [('Sony Deutschland: BRAVIA', 'https://www.sony.de/')],
    'iptv-philips-tv': [('Philips Deutschland', 'https://www.philips.de/')],
    'iptv-hisense-tv': [('Hisense Deutschland', 'https://www.hisense.de/')],
    'iptv-tcl-tv': [('TCL Deutschland', 'https://www.tcl.com/de/de')],
    'iptv-xiaomi-tv': [('Xiaomi Deutschland', 'https://www.mi.com/de/')],
    'iptv-xiaomi-tv-box': [('Xiaomi Deutschland', 'https://www.mi.com/de/')],
    'iptv-panasonic-tv': [('Panasonic Deutschland', 'https://www.panasonic.com/de/')],
    'iptv-grundig-tv': [('Grundig Deutschland', 'https://www.grundig.com/')],
    'iptv-metz-tv': [('Metz Blue – Hersteller', 'https://www.metz-ce.de/')],
    'iptv-loewe-tv': [('Loewe – Hersteller', 'https://www.loewe.tv/')],
    'iptv-medion-tv': [('Medion Deutschland', 'https://www.medion.com/de/')],
    'iptv-telefunken-tv': [('Wikipedia: Amazon Fire TV', 'https://de.wikipedia.org/wiki/Amazon_Fire_TV')],
    'iptv-toshiba-tv': [('Toshiba TV Europa', 'https://www.toshiba-tv.com/')],
    'iptv-sharp-tv': [('Sharp Europa', 'https://www.sharpconsumer.eu/')],
    'iptv-roku': [('Roku Deutschland', 'https://www.roku.com/de-de/')],
    'iptv-stick': [('Wikipedia: Amazon Fire TV', 'https://de.wikipedia.org/wiki/Amazon_Fire_TV'), ('Google TV Hilfe', 'https://support.google.com/googletv/')],
    'fire-tv-modelle': [('Wikipedia: Amazon Fire TV', 'https://de.wikipedia.org/wiki/Amazon_Fire_TV')],
    'iptv-fire-tv-stick': [('Wikipedia: Amazon Fire TV', 'https://de.wikipedia.org/wiki/Amazon_Fire_TV')],
    'iptv-pc-mac': [('VLC Media Player – VideoLAN', 'https://www.videolan.org/vlc/')],
    'iptv-4k': [_BNETZA, ('Wikipedia: Ultra High Definition Television', 'https://de.wikipedia.org/wiki/Ultra_High_Definition_Television')],
    'iptv-server': [_BNETZA],
    'm3u-playlist': [('Wikipedia: M3U', 'https://de.wikipedia.org/wiki/M3U')],
    'sat-ip': [('SES – Satellitenbetreiber und SAT>IP-Initiator', 'https://www.ses.com/'), ('Wikipedia: IPTV', 'https://de.wikipedia.org/wiki/IPTV')],
    'iptv-telekom-vodafone': [('Telekom MagentaTV', 'https://www.telekom.de/magenta-tv'), ('Vodafone Deutschland', 'https://www.vodafone.de/')],
    'iptv-bezahlen': [('Verbraucherzentrale: Rat zu Zahlung und Verträgen', 'https://www.verbraucherzentrale.de/')],
    'iptv-erfahrungen': [('Verbraucherzentrale: Verbraucherrat', 'https://www.verbraucherzentrale.de/')],
    'iptv-fussball': [('DFL Deutsche Fußball Liga', 'https://www.dfl.de/de/')],
    'iptv-sport': [('Sportschau (ARD)', 'https://www.sportschau.de/')],
    'sky-iptv': [('Sky Deutschland', 'https://www.sky.de/')],
    'iptv-senderliste': [('ARD Mediathek', 'https://www.ardmediathek.de/'), ('ZDF Mediathek', 'https://www.zdf.de/')],
}


def _play(name, query):
    return (f'{name} bei Google Play', 'https://play.google.com/store/search?q=' + query.replace(' ', '%20') + '&c=apps')


_ANDROID_TV = ('Android TV – offizielle Website', 'https://www.android.com/tv/')
_WIKI_IPTV = ('Wikipedia: IPTV', 'https://de.wikipedia.org/wiki/IPTV')
_VZ = ('Verbraucherzentrale', 'https://www.verbraucherzentrale.de/')
SOURCES.update({
    'bester-iptv-player': [('TiviMate – offizielle Website', 'https://tivimate.com/'), ('IPTV Smarters – offizielle Website', 'https://www.iptvsmarters.com/'), ('Kodi – offizielle Website', 'https://kodi.tv/')],
    'bob-player': [_play('Bob Player', 'bob player iptv')],
    'cloudstream': [('CloudStream auf GitHub', 'https://github.com/recloudstream/cloudstream')],
    'duplexplay': [_play('DuplexPlay', 'duplexplay')],
    'flex-iptv': [_play('Flex IPTV', 'flex iptv')],
    'hot-player': [_play('Hot Player', 'hot player iptv')],
    'ibo-player-alternativen': [('IBO Player – offizielle Website', 'https://iboplayer.com/'), ('TiviMate – offizielle Website', 'https://tivimate.com/')],
    'implayer': [_play('iMPlayer', 'implayer')],
    'iptv-pro-app': [_play('IPTV Pro', 'iptv pro')],
    'lillyplayer': [_play('Lilly Player', 'lilly player')],
    'mac-player': [_play('MAC Player', 'mac player iptv')],
    'max-player': [_play('MaxPlayer', 'max player iptv')],
    'myiptv-player': [('Microsoft Store', 'https://apps.microsoft.com/')],
    'nanomid-player': [_play('Nanomid Player', 'nanomid player')],
    'net-iptv': [_play('Net IPTV', 'net iptv')],
    'progtv': [('ProgDVB / ProgTV – offizielle Website', 'https://www.progdvb.com/')],
    'purple-iptv': [_play('Purple IPTV', 'purple iptv')],
    'room-iptv': [_play('Room IPTV', 'room iptv')],
    'smart-stb': [('Samsung Support Deutschland', 'https://www.samsung.com/de/support/'), ('LG Support: Fernseher', 'https://www.lg.com/de/support/')],
    'snappier-iptv': [_play('Snappier IPTV', 'snappier iptv')],
    'uhf-iptv': [_play('UHF', 'uhf iptv')],
    'vu-iptv-player': [_play('VU IPTV Player', 'vu iptv player')],
    'iptv-stream-player': [_play('IPTV Stream Player', 'iptv stream player')],
    'iptv-nokia-streaming-box': [_ANDROID_TV, ('Google TV Hilfe', 'https://support.google.com/googletv/')],
    'iptv-strong-thomson-box': [_ANDROID_TV, ('Google TV Hilfe', 'https://support.google.com/googletv/')],
    'tvip-box': [('Wikipedia: Set-Top-Box', 'https://de.wikipedia.org/wiki/Set-Top-Box'), _ANDROID_TV],
    'iptv-tuerkisch': [('TRT – türkischer öffentlicher Rundfunk', 'https://www.trt.net.tr/'), _WIKI_IPTV],
    'iptv-albanisch': [('RTSH – albanischer öffentlicher Rundfunk', 'https://www.rtsh.al/'), _WIKI_IPTV],
    'iptv-balkan': [('HRT – kroatischer öffentlicher Rundfunk', 'https://www.hrt.hr/'), ('RTS – serbischer öffentlicher Rundfunk', 'https://www.rts.rs/'), ('BHRT – Rundfunk Bosnien und Herzegowina', 'https://www.bhrt.ba/')],
    'iptv-rumaenisch': [('TVR – rumänischer öffentlicher Rundfunk', 'https://www.tvr.ro/'), _WIKI_IPTV],
    'iptv-russisch': [('DW auf Russisch (Deutsche Welle)', 'https://www.dw.com/ru/'), _WIKI_IPTV],
    'iptv-georgisch': [('GPB – georgischer öffentlicher Rundfunk', 'https://1tv.ge/'), _WIKI_IPTV],
    'iptv-international': [('Deutsche Welle', 'https://www.dw.com/de/'), _WIKI_IPTV],
    'iptv-vod': [('Wikipedia: Video-on-Demand', 'https://de.wikipedia.org/wiki/Video-on-Demand'), ('ARD Mediathek', 'https://www.ardmediathek.de/')],
    'iptv-im-browser': [('BSI: Sicherheit im Internet', 'https://www.bsi.bund.de/'), ('Wikipedia: HTTP Live Streaming', 'https://de.wikipedia.org/wiki/HTTP_Live_Streaming')],
    'iptv-reseller': [_VZ, _WIKI_IPTV],
    'iptv-anbieter-liste': [_VZ, _WIKI_IPTV],
    'iptv-regionen': [_BNETZA, _ATLAS],
    'iptv-staedte': [_BNETZA, _ATLAS],
})

# Regional public broadcasters, linked from every city and region page together with the Bundesnetzagentur tools.
BROADCASTER_URL = {
    'WDR': 'https://www1.wdr.de/', 'BR': 'https://www.br.de/', 'SWR': 'https://www.swr.de/', 'NDR': 'https://www.ndr.de/',
    'hr': 'https://www.hessenschau.de/', 'MDR': 'https://www.mdr.de/', 'rbb': 'https://www.rbb24.de/', 'SR': 'https://www.sr.de/',
    'Radio Bremen': 'https://www.butenunbinnen.de/',
}
LOCAL_SOURCES = [_BNETZA, _ATLAS]

# Brand-specific sections for the TV pages that shared most of their setup text (same OS family).
EXTRA_SECTIONS = {
    'iptv-sony-bravia': [('bravia-tipps', 'Bildeinstellungen für IPTV auf dem BRAVIA', '''
<p>Sony-Fernseher sind für ihre Bildverarbeitung bekannt – und die lässt sich für IPTV gezielt einstellen. Für Fußball und anderen Sport empfiehlt sich eine moderate Stufe von <b>Motionflow</b>; „Hoch“ kann bei 50-Hz-Sendern zu sichtbaren Artefakten führen. Für Filme aus der Mediathek wählen Sie den Bildmodus „Kino“ oder „Benutzerdefiniert“.</p>
<p>Viele BRAVIA-Modelle haben nur wenige Gigabyte freien Speicher. Installieren Sie nur eine IPTV-App und leeren Sie bei Rucklern deren Cache unter Einstellungen → Apps. Wer eine Soundbar per eARC nutzt, stellt den Digitalton in der App auf „Auto“, damit Dolby-Ton korrekt durchgereicht wird. Passende Apps vergleicht der Ratgeber <a href="/bester-iptv-player/">Bester IPTV Player</a>.</p>''')],
    'iptv-philips-tv': [('ambilight', 'Ambilight und IPTV: was funktioniert', '''
<p>Das Markenzeichen von Philips ist Ambilight – die Hintergrundbeleuchtung, die Farben des Bildes an die Wand projiziert. Auf Modellen mit Google TV oder Android TV folgt Ambilight auch den Bildern einer IPTV-App, weil die App direkt auf dem Fernseher läuft. Bei einem externen Stick am HDMI-Anschluss funktioniert Ambilight ebenfalls, solange der Eingang nicht im Spielemodus betrieben wird.</p>
<p>Für Sport empfiehlt sich, „Perfect Natural Motion“ auf eine mittlere Stufe zu setzen. Ältere Philips-Geräte mit Saphi-System haben keinen Zugriff auf IPTV-Apps; hier ist ein <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder ein <a href="/iptv-google-tv/">Google-TV-Gerät</a> die bessere Lösung.</p>''')],
    'iptv-sharp-tv': [('sharp-tipps', 'Sharp Aquos: Speicher, Fernbedienung und Updates', '''
<p>Viele Sharp-Fernseher sind preiswerte Einstiegsmodelle mit wenig internem Speicher. Installieren Sie deshalb nur die IPTV-App, die Sie wirklich nutzen, und deaktivieren Sie vorinstallierte Apps, die Sie nicht brauchen. Bei großen Senderlisten mit mehreren Tausend Kanälen hilft es, in der App nur die deutschen Gruppen zu laden – das beschleunigt den Start deutlich.</p>
<p>Prüfen Sie vor der Einrichtung, ob ein Software-Update verfügbar ist: Neuere Versionen bringen oft eine aktuellere Google-TV- oder Android-TV-Basis mit. Wenn Ihr Modell ein anderes System hat, ist ein Stick am HDMI-Anschluss der einfachste Weg; welche Sticks sich eignen, zeigt der Ratgeber <a href="/iptv-stick/">IPTV Stick</a>.</p>''')],
    'iptv-metz-tv': [('metz-tipps', 'Metz-Fernseher im Alltag mit IPTV', '''
<p>Metz-Kunden legen oft Wert auf einfache Bedienung und guten Ton. Für IPTV bedeutet das: Richten Sie in der App Favoritenlisten mit den gewohnten deutschen Sendern ein und blenden Sie Ländergruppen aus, die Sie nicht brauchen. So bleibt die Senderliste so übersichtlich wie beim klassischen Kabelempfang. Wie das geht, erklärt die <a href="/iptv-senderliste/">IPTV Senderliste</a>.</p>
<p>Bei Modellen ohne Google TV oder Android TV ist ein Stick die beste Lösung. Stecken Sie ihn in einen HDMI-Anschluss mit CEC-Unterstützung, dann steuern Sie ihn mit der Metz-Fernbedienung. Für Fragen bei der Einrichtung hilft unser Support per E-Mail oder WhatsApp.</p>''')],
    'iptv-medion-tv': [('medion-tipps', 'Medion-Fernseher aus dem Discounter: worauf achten?', '''
<p>Medion-Fernseher werden oft in Aktionen bei Discountern verkauft. Vor dem Kauf lohnt ein Blick auf das System: Steht „Android TV“ oder „Google TV“ auf dem Karton, können Sie IPTV-Apps direkt installieren. Bei anderen Systemen planen Sie einen Stick ein – das ist mit rund 30 bis 70 Euro oft günstiger als ein teureres Fernsehermodell.</p>
<p>Die günstigeren Modelle haben meist wenig Arbeitsspeicher. Wählen Sie eine schlanke App wie <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a>, laden Sie nur die benötigten Sendergruppen und starten Sie den Fernseher gelegentlich komplett neu, indem Sie ihn kurz vom Strom trennen.</p>''')],
    'iptv-grundig-tv': [('grundig-tipps', 'Grundig: Fire TV Edition oder Google TV?', '''
<p>Grundig bietet Fernseher mit Fire TV Edition und mit Google TV an. Für IPTV haben beide Varianten Vorteile: Auf der Fire TV Edition installieren Sie Apps über den Amazon Appstore oder den <a href="/iptv-downloader/">Downloader</a>, auf Google TV direkt aus dem Play Store. Wer TiviMate nutzen möchte, hat mit Google TV den einfacheren Weg.</p>
<p>Bei der Fire TV Edition empfiehlt es sich, unter Einstellungen → Display die Bildwiederholrate an den Inhalt anzupassen, damit 50-Hz-Sender flüssig laufen. Die Alexa-Sprachsteuerung öffnet auf Wunsch direkt die IPTV-App – praktisch für alle, die nicht lange durch Menüs scrollen möchten.</p>''')],
    'iptv-xiaomi-tv': [('xiaomi-tipps', 'PatchWall, Google TV und Speicher bei Xiaomi', '''
<p>Ältere Xiaomi-Fernseher starten mit der hauseigenen Oberfläche PatchWall, neuere mit Google TV. Für IPTV ist das zweitrangig: In beiden Fällen gibt es den Play Store, aus dem Sie TiviMate oder IPTV Smarters Pro laden. Wer PatchWall nicht mag, kann in den Einstellungen den Android-TV-Startbildschirm als Standard wählen.</p>
<p>Viele Xiaomi-Modelle haben 8 bis 16 GB Speicher, von denen nach Updates nicht viel übrig bleibt. Löschen Sie vorinstallierte Apps, die Sie nicht nutzen, und laden Sie in der IPTV-App nur die deutschen Sendergruppen. Für mehr Leistung gibt es die <a href="/iptv-xiaomi-tv-box/">Xiaomi TV Box</a> als Zuspieler.</p>''')],
    'iptv-tcl-tv': [('tcl-tipps', 'TCL: Bewegungsglättung und Energiesparen anpassen', '''
<p>TCL-Fernseher werden ab Werk oft mit aktivem Energiesparmodus ausgeliefert, der die Helligkeit reduziert. Für IPTV am Abend ist das meist kein Problem, bei Tageslicht kann das Bild aber flau wirken – stellen Sie den Bildmodus dann auf „Standard“ oder „Film“. Für Fußball lohnt es sich, die Bewegungsglättung (MEMC) auf eine niedrige oder mittlere Stufe zu setzen.</p>
<p>Weil TCL in Europa fast durchgehend Google TV nutzt, stehen TiviMate, IPTV Smarters Pro und OTT Navigator im Play Store bereit. Größere QLED- und Mini-LED-Modelle haben genug Leistung für 4K-Streams; bei Einstiegsmodellen empfiehlt sich Full HD. Welche Bandbreite Sie brauchen, steht in <a href="/iptv-4k/">IPTV in 4K</a>.</p>''')],
}


def _chips(items):
    return '<ul class="chip-list">' + ''.join(f'<li><a href="/{slug}/">{label}</a></li>' for slug, label in items) + '</ul>'


# Contextual hub links added in the deep audit: brand, player and box pages were only reachable via hubs and siblings.
EXTRA_SECTIONS.update({
    'iptv-smart-tv': [('marken', 'IPTV-Anleitungen nach Fernsehermarke', '<p>Jede Marke nutzt ein eigenes Betriebssystem – und davon hängt ab, welche IPTV-App Sie installieren können. Wählen Sie Ihren Hersteller für die passende Schritt-für-Schritt-Anleitung:</p>' + _chips([
        ('iptv-samsung-tv', 'Samsung'), ('iptv-lg-tv', 'LG'), ('iptv-sony-bravia', 'Sony BRAVIA'), ('iptv-philips-tv', 'Philips'),
        ('iptv-panasonic-tv', 'Panasonic'), ('iptv-tcl-tv', 'TCL'), ('iptv-hisense-tv', 'Hisense'), ('iptv-xiaomi-tv', 'Xiaomi'),
        ('iptv-grundig-tv', 'Grundig'), ('iptv-telefunken-tv', 'Telefunken'), ('iptv-toshiba-tv', 'Toshiba'), ('iptv-sharp-tv', 'Sharp'),
        ('iptv-medion-tv', 'Medion'), ('iptv-metz-tv', 'Metz'), ('iptv-loewe-tv', 'Loewe')]) + '<p>Findet sich für Ihr Modell keine passende App, ist ein <a href="/iptv-stick/">IPTV Stick</a> am HDMI-Anschluss die einfachste Lösung.</p>')],
    'bester-iptv-player': [('weitere-player', 'Weitere IPTV Player im Überblick', '<p>Neben den großen Namen gibt es viele Player, die nach dem gleichen Prinzip arbeiten: App installieren, MAC-Adresse oder Geräte-ID notieren, Playlist auf der Website des Herstellers verknüpfen und nach der Testphase aktivieren. Zu jedem finden Sie eine eigene Anleitung:</p>' + _chips([
        ('ibo-player', 'IBO Player'), ('duplexplay', 'DuplexPlay'), ('flex-iptv', 'Flex IPTV'), ('implayer', 'iMPlayer'), ('net-iptv', 'Net IPTV'),
        ('room-iptv', 'Room IPTV'), ('vu-iptv-player', 'VU IPTV Player'), ('bob-player', 'Bob Player'), ('hot-player', 'Hot Player'),
        ('max-player', 'MaxPlayer'), ('nanomid-player', 'Nanomid Player'), ('mac-player', 'MAC Player'), ('lillyplayer', 'Lilly Player'),
        ('purple-iptv', 'Purple IPTV'), ('mx-player-iptv', 'MX Player'), ('cloudstream', 'CloudStream')]) + '<p>Welche Alternativen es zu kostenpflichtigen Aktivierungs-Playern gibt, zeigt <a href="/ibo-player-alternativen/">IBO Player Alternativen</a>.</p>')],
    'iptv-box': [('weitere-boxen', 'Weitere Boxen und Receiver mit Anleitung', '<p>Für diese Zuspieler gibt es eigene Einrichtungsanleitungen mit Modellübersicht, passenden Apps und Lösungen für typische Probleme:</p>' + _chips([
        ('iptv-nvidia-shield', 'Nvidia Shield'), ('iptv-xiaomi-tv-box', 'Xiaomi TV Box'), ('iptv-nokia-streaming-box', 'Nokia Streaming Box'),
        ('iptv-strong-thomson-box', 'Strong &amp; Thomson'), ('formuler-iptv', 'Formuler'), ('tvip-box', 'TVIP S-Box'), ('mag-box-iptv', 'MAG-Box'),
        ('iptv-dreambox', 'Dreambox'), ('iptv-vu-plus', 'Vu+')]) + '<p>Wer lieber einen klassischen Receiver nutzt, findet Hinweise unter <a href="/iptv-receiver/">IPTV Receiver</a>.</p>')],
})
