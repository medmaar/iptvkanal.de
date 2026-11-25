"""Keyword-cluster pass (25.11.2026), part 2: recording, SAT>IP, VOD/streaming services, lifetime offers,
servers and buffering, English-language TV, German playlists. LINK_FROM adds the new pages to the related
links of existing guides so every new URL is reachable from at least three pages."""
from .helpers import steps, checks, tip, table, proscons

PAGES = []

TEST_TIP = tip('Welche Sender, Sendergruppen und Mediathek-Inhalte Ihr Zugang enthält, sehen Sie vollständig im '
               '<a href="/kostenlos-testen/">kostenlosen Test</a> – auf Ihrem eigenen Gerät, bevor Sie etwas bezahlen.', 'Hinweis')

# ================================================================ AUFNEHMEN (iptv dvr)
PAGES.append(dict(
    slug='iptv-aufnehmen', parent='ratgeber', kind='guide',
    title='IPTV aufnehmen: Aufnahme, Timeshift & Catch-up',
    description='IPTV aufnehmen: welche Apps und Geräte Sendungen aufzeichnen, was Timeshift und Catch-up können, wie viel Speicher Sie brauchen und was rechtlich erlaubt ist.',
    eyebrow='AUFNAHME &amp; DVR', h1='IPTV aufnehmen: so zeichnen Sie Sendungen auf',
    lead='Den Tatort am Sonntag verpasst oder das Spiel läuft parallel zur Arbeit? Mit IPTV gibt es drei Wege, Sendungen später zu sehen: Aufnahme, Timeshift und Catch-up. Hier lesen Sie, was Ihr Gerät davon kann.',
    answer='IPTV aufnehmen können Sie mit Apps wie TiviMate Premium, IPTV Smarters Pro (Android) und Kodi mit TVHeadend sowie mit Enigma2-Receivern, Jellyfin oder Plex. Die Aufnahme landet auf dem internen Speicher, einem USB-Stick oder einer Festplatte. Smart-TV-Apps für Samsung und LG nehmen meist nicht auf. Alternativ bieten viele Anbieter Catch-up: Sendungen der letzten Tage direkt im Programmführer abrufen.',
    sections=[
        ('drei-wege', 'Aufnahme, Timeshift, Catch-up: der Unterschied', table(['Funktion', 'Was passiert', 'Wo gespeichert', 'Abhängig von'], [
            ['Aufnahme (DVR)', 'Sendung wird als Datei gespeichert', 'Gerät, USB, NAS oder Server', 'App bzw. Gerät'],
            ['Timeshift', 'Live-Sendung pausieren und zurückspulen', 'Zwischenspeicher des Geräts', 'App bzw. Gerät'],
            ['Catch-up / Archiv', 'Vergangene Sendungen im EPG abrufen', 'Beim Anbieter', 'Anbieter und Sender'],
        ], 'Aufnahme, Timeshift und Catch-up') + '''
<p>Catch-up ist am bequemsten, weil Sie nichts planen müssen: Im Programmführer zurückblättern, Sendung wählen, abspielen. Es steht aber nur für Sender zur Verfügung, für die der Anbieter ein Archiv vorhält – oft erkennbar an einem Uhr-Symbol neben dem Sendernamen. Für alles andere brauchen Sie eine echte Aufnahme.</p>'''),
        ('apps', 'Welche Apps und Geräte können aufnehmen?', table(['App / Gerät', 'Aufnahme', 'Speicherort', 'Ratgeber'], [
            ['TiviMate (Premium)', 'Ja, auch geplant und als Serie', 'Intern, USB, Netzwerkordner', '<a href="/tivimate-premium/">TiviMate Premium</a>'],
            ['IPTV Smarters Pro (Android)', 'Ja, je nach Version', 'Interner Speicher', '<a href="/iptv-smarters-pro/">Smarters Pro</a>'],
            ['Kodi', 'Nur mit Backend wie TVHeadend', 'Server', '<a href="/kodi-iptv/">Kodi</a>'],
            ['Jellyfin, Plex', 'Ja (Plex mit Plex Pass)', 'Server-Festplatte', '<a href="/plex-jellyfin-iptv/">Plex &amp; Jellyfin</a>'],
            ['Enigma2-Receiver (Dreambox, Vu+)', 'Ja', 'Festplatte, USB, NAS', '<a href="/iptv-receiver/">IPTV Receiver</a>'],
            ['MAG-Box, Formuler', 'Je nach Modell und Portal', 'USB', '<a href="/formuler-iptv/">Formuler</a>'],
            ['Samsung- und LG-Apps (SET IPTV, IBO u. a.)', 'Meist nein', '–', '<a href="/iptv-samsung-tv/">Samsung TV</a>'],
        ], 'IPTV-Apps mit Aufnahmefunktion') + '''
<p>Auf dem Fire TV Stick ist der Speicher knapp. Für regelmäßige Aufnahmen schließen Sie über einen OTG-Adapter einen USB-Stick an oder speichern in einen Netzwerkordner auf dem NAS.</p>'''),
        ('tivimate', 'Beispiel: Aufnahme in TiviMate einrichten', steps(
            'TiviMate Premium aktivieren (Aufnahmen gibt es nur mit Premium).',
            '<b>Einstellungen → Aufnahme</b> öffnen und den Speicherort wählen: intern, USB-Speicher oder SMB-Netzwerkordner.',
            'Im Programmführer eine Sendung markieren und lange auf OK drücken.',
            '<b>„Aufnehmen“</b> oder <b>„Serie aufnehmen“</b> wählen. Vor- und Nachlauf (z. B. 2 und 10 Minuten) einstellen – bei Fußball lieber 30 Minuten Nachlauf.',
            'Fertige Aufnahmen finden Sie im Menü unter „Aufnahmen“.')
         + tip('Eine Aufnahme belegt eine Verbindung Ihres Zugangs. Schauen Sie gleichzeitig einen anderen Sender, brauchen Sie ein Paket mit mindestens zwei Geräten.')),
        ('speicher', 'Wie viel Speicher brauchen Aufnahmen?', table(['Qualität', 'Speicher pro Stunde (ca.)', '90-Minuten-Film'], [
            ['SD', '1–1,5 GB', 'ca. 2 GB'],
            ['Full HD (H.264)', '2,5–4 GB', 'ca. 5 GB'],
            ['4K (HEVC)', '7–12 GB', 'ca. 15 GB'],
        ], 'Speicherbedarf von IPTV-Aufnahmen') + '''
<p>Die Werte hängen von der Bitrate des Senders ab. Ein 64-GB-USB-Stick fasst also rund 15 Stunden Full HD. Für Serienaufnahmen ist eine externe Festplatte oder ein NAS sinnvoller. Wie Bitraten und Codecs zusammenhängen, erklärt der Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>.</p>'''),
        ('recht', 'Darf ich IPTV aufnehmen?', '''
<p>In Deutschland erlaubt § 53 Urheberrechtsgesetz Privatkopien für den eigenen, nicht kommerziellen Gebrauch – sofern die Quelle nicht offensichtlich rechtswidrig ist. Aufnahmen aus einem regulären Abo dürfen Sie also für sich und Ihren Haushalt speichern. Nicht erlaubt ist das Weitergeben, Hochladen oder Verkaufen. Manche Pay-TV-Inhalte sind zusätzlich technisch gegen Aufnahmen geschützt.</p>
<p>Bei Telekom, Vodafone und Co. gibt es Aufnahmen meist als Cloud-Funktion mit begrenztem Kontingent – mehr dazu unter <a href="/iptv-telekom-vodafone/">IPTV bei Telekom und Vodafone</a>. Sky Stream nimmt gar nicht auf, wie der Ratgeber <a href="/sky-iptv/">Sky über IPTV</a> zeigt.</p>''' + TEST_TIP),
    ],
    faq=[
        ('Kann ich mit IPTV Sendungen aufnehmen?', 'Ja, wenn Ihre App oder Ihr Gerät eine Aufnahmefunktion hat – etwa TiviMate Premium, IPTV Smarters Pro auf Android, Enigma2-Receiver, Jellyfin oder Plex. Die meisten Smart-TV-Apps für Samsung und LG nehmen nicht auf.'),
        ('Was ist der Unterschied zwischen Catch-up und Aufnahme?', 'Bei Catch-up speichert der Anbieter vergangene Sendungen, die Sie im Programmführer abrufen. Bei einer Aufnahme speichert Ihr Gerät die Sendung selbst als Datei.'),
        ('Wo speichert TiviMate Aufnahmen?', 'Wahlweise im internen Speicher, auf einem USB-Speicher oder in einem Netzwerkordner (SMB) auf NAS oder PC. Den Ort legen Sie unter Einstellungen → Aufnahme fest.'),
        ('Belegt eine Aufnahme eine Verbindung?', 'Ja. Während der Aufnahme läuft ein Stream. Wenn Sie gleichzeitig etwas anderes schauen, brauchen Sie ein Paket mit mindestens zwei gleichzeitigen Verbindungen.'),
        ('Ist das Aufnehmen von IPTV legal?', 'Privatkopien für den eigenen Gebrauch sind nach § 53 UrhG erlaubt, wenn die Quelle legal ist. Weitergeben, Hochladen oder Verkaufen ist nicht erlaubt.'),
    ],
    related=['tivimate-premium', 'plex-jellyfin-iptv', 'iptv-receiver', 'kodi-iptv', 'iptv-einrichten', 'iptv-4k'],
    card=('IPTV aufnehmen', 'Aufnahme, Timeshift und Catch-up auf allen Geräten.'),
    sources=[('§ 53 UrhG – Vervielfältigungen zum privaten Gebrauch', 'https://www.gesetze-im-internet.de/urhg/__53.html')],
))

# ================================================================ SAT>IP
PAGES.append(dict(
    slug='sat-ip', parent='ratgeber', kind='guide',
    title='SAT>IP vs. IPTV: Unterschiede, Geräte & Apps',
    description='SAT>IP erklärt: wie Satellitenfernsehen ins Heimnetz kommt, welche Server und Apps es gibt und worin sich SAT>IP von IPTV unterscheidet.',
    eyebrow='SAT-TV IM NETZWERK', h1='SAT>IP und IPTV: was ist der Unterschied?',
    lead='SAT>IP klingt nach IPTV, ist aber etwas ganz anderes: Das Signal kommt weiterhin von Ihrer Satellitenschüssel und wird nur im Heimnetz verteilt. Wann sich das lohnt und wann IPTV die bessere Lösung ist, lesen Sie hier.',
    answer='SAT>IP ist ein Standard, mit dem ein Server das Signal Ihrer Satellitenschüssel ins Heimnetz einspeist. Tablets, Smartphones, PCs und Fernseher empfangen es dann per WLAN oder LAN – ganz ohne Koaxialkabel zu jedem Raum. Anders als IPTV braucht SAT>IP eine Schüssel und funktioniert nur zu Hause. IPTV kommt dagegen über das Internet und läuft überall, wo es eine Internetverbindung gibt.',
    sections=[
        ('funktion', 'So funktioniert SAT>IP', steps(
            'Die Satellitenschüssel empfängt wie gewohnt das Signal, zum Beispiel von Astra 19,2° Ost.',
            'Ein <b>SAT>IP-Server</b> (auch Multiswitch mit SAT>IP oder Netzwerk-Tuner) wandelt das Signal in IP-Datenpakete um.',
            'Der Server hängt per LAN am Router und verteilt die Sender im Heimnetz.',
            'Endgeräte spielen die Sender mit einer SAT>IP-fähigen App oder einem SAT>IP-Client im Fernseher ab.')
         + '<p>Der Standard wurde vom Satellitenbetreiber SES entwickelt und später als europäische Norm (EN 50585) festgeschrieben. Er sorgt dafür, dass Server und Apps unterschiedlicher Hersteller zusammenarbeiten.</p>'),
        ('vergleich', 'SAT>IP, IPTV und klassisches Sat-TV im Vergleich', table(['', 'Klassisches Sat-TV', 'SAT>IP', 'IPTV'], [
            ['Signalquelle', 'Schüssel', 'Schüssel', 'Internet'],
            ['Verteilung im Haus', 'Koaxialkabel', 'Heimnetz (LAN/WLAN)', 'Heimnetz (LAN/WLAN)'],
            ['Außer Haus nutzbar', 'Nein', 'Nein (nur mit Umwegen)', 'Ja'],
            ['Gleichzeitige Sender', 'Je Tuner im Receiver', 'Je Tuner im Server (meist 2–8)', 'Je Verbindung im Paket'],
            ['Senderauswahl', 'Frei empfangbare Sat-Sender, HD+ gegen Gebühr', 'Wie Sat-TV', 'Je nach Anbieter, oft auch international'],
            ['Internet nötig', 'Nein', 'Nein', 'Ja, ca. 16 Mbit/s je HD-Stream'],
        ], 'SAT>IP, Sat-TV und IPTV') + '''
<p>Mehr zu den Grundlagen von IPTV lesen Sie unter <a href="/was-ist-iptv/">Was ist IPTV?</a>. IPTV der Netzbetreiber wie MagentaTV ordnet der Ratgeber <a href="/iptv-telekom-vodafone/">IPTV bei Telekom und Vodafone</a> ein.</p>'''),
        ('geraete', 'Welche Geräte und Apps unterstützen SAT>IP?', checks(
            '<strong>SAT>IP-Server:</strong> Netzwerk-Tuner verschiedener Hersteller (u. a. Telestar, Kathrein, Triax, Inverto, Digital Devices), oft mit 4 oder 8 Tunern.',
            '<strong>Enigma2-Receiver:</strong> Viele Dreambox- und Vu+-Modelle können als SAT>IP-Server oder -Client arbeiten – siehe <a href="/iptv-receiver/">IPTV Receiver</a>.',
            '<strong>Fernseher:</strong> Einige Smart-TVs, etwa viele Panasonic-Modelle, haben einen SAT>IP-Client eingebaut.',
            '<strong>Apps:</strong> Hersteller-Apps der Server sowie VLC und Kodi (über TVHeadend) auf PC, Android und iOS.',
            '<strong>Kabel-Variante:</strong> Für Kabelfernsehen gibt es vergleichbare Lösungen, etwa die DVB-C-Funktion mancher FRITZ!Box-Kabelrouter.')),
        ('wann', 'Wann lohnt sich SAT>IP, wann IPTV?', proscons(
            ['Sie haben bereits eine Schüssel und möchten keine Kabel verlegen', 'Sie schauen vor allem frei empfangbare deutsche Sender', 'Fernsehen soll ohne Internetverbindung laufen'],
            ['Sie möchten auch unterwegs oder im Urlaub schauen', 'Sie haben keine Schüssel oder dürfen keine montieren', 'Sie möchten internationale Sender, Mediathek und Programmführer in einer App'],
            'SAT>IP passt, wenn …', 'IPTV passt besser, wenn …')
         + '<p>Beides lässt sich kombinieren: Ein Enigma2-Receiver kann Satellitensender und IPTV-Bouquets in einer Senderliste zeigen. Wie Sie IPTV auf dem Receiver einbinden, zeigen die Ratgeber <a href="/iptv-dreambox/">Dreambox</a> und <a href="/iptv-vu-plus/">Vu+</a>.</p>'),
        ('probleme', 'Typische Stolpersteine bei SAT>IP', table(['Problem', 'Ursache', 'Lösung'], [
            ['Bild bricht im WLAN ab', 'Hohe Bitrate unverschlüsselter Sat-Streams', 'Endgerät per LAN oder 5-GHz-WLAN anbinden'],
            ['Nicht alle Räume gleichzeitig', 'Zu wenige Tuner im Server', 'Server mit mehr Tunern wählen'],
            ['HD+ und Sky fehlen', 'Verschlüsselte Sender', 'Nur mit kompatibler Entschlüsselung bzw. Herstellerlösung'],
            ['Kein Empfang unterwegs', 'SAT>IP ist fürs Heimnetz gedacht', 'Für unterwegs IPTV nutzen'],
        ], 'SAT>IP-Probleme')),
    ],
    faq=[
        ('Ist SAT>IP das Gleiche wie IPTV?', 'Nein. Bei SAT>IP kommt das Signal von Ihrer eigenen Satellitenschüssel und wird nur im Heimnetz verteilt. IPTV kommt komplett über das Internet und braucht keine Schüssel.'),
        ('Brauche ich für SAT>IP Internet?', 'Nein. SAT>IP nutzt nur Ihr Heimnetz. Internet ist nicht nötig, solange Sie zu Hause schauen.'),
        ('Kann ich SAT>IP unterwegs nutzen?', 'Nur mit technischem Aufwand, etwa per VPN ins Heimnetz und ausreichendem Upload. Für Fernsehen unterwegs ist IPTV die einfachere Lösung.'),
        ('Wie viele Fernseher können SAT>IP gleichzeitig nutzen?', 'So viele, wie der Server Tuner hat – typischerweise 2 bis 8. Mehrere Geräte auf demselben Sender teilen sich meist einen Tuner.'),
        ('Kann ich SAT>IP und IPTV kombinieren?', 'Ja, zum Beispiel auf einem Enigma2-Receiver oder in Kodi. Dort erscheinen Satellitensender und IPTV-Sender in einer gemeinsamen Liste.'),
    ],
    related=['was-ist-iptv', 'iptv-receiver', 'iptv-telekom-vodafone', 'iptv-dreambox', 'kodi-iptv', 'iptv-einrichten'],
    card=('SAT>IP vs. IPTV', 'Sat-TV im Heimnetz oder Fernsehen übers Internet?'),
))

# ================================================================ VOD / NETFLIX / STREAMING
PAGES.append(dict(
    slug='iptv-vod', parent='ratgeber', kind='guide',
    title='IPTV & Streaming: Netflix, HBO Max, Pluto TV & VOD',
    description='IPTV und Streaming kombinieren: Netflix, HBO Max, Disney+, Pluto TV und Mediatheken neben der IPTV-App – und was VOD im IPTV-Paket bedeutet.',
    eyebrow='FILME &amp; SERIEN', h1='IPTV und Streaming: Netflix, HBO Max, Pluto TV und VOD',
    lead='Live-TV über IPTV und Filme bei Netflix – das schließt sich nicht aus. Hier lesen Sie, wie beides auf einem Gerät zusammenpasst, was „VOD“ in IPTV-Paketen bedeutet und welche kostenlosen Streaming-Sender es legal gibt.',
    answer='IPTV und Streaming-Dienste wie Netflix, HBO Max, Disney+ oder Amazon Prime Video sind getrennte Angebote: Netflix läuft nur in der Netflix-App, nicht in einem IPTV-Player. Beide Apps lassen sich aber auf demselben Fire TV Stick, Smart-TV oder Apple TV nutzen. „VOD“ in einem IPTV-Paket meint eine Mediathek mit Filmen und Serien zum Abruf. Kostenlose, legale Live-Kanäle gibt es zusätzlich bei Pluto TV, Samsung TV Plus, Joyn und in den Mediatheken von ARD und ZDF.',
    sections=[
        ('unterschied', 'IPTV, Streaming-Dienst, VOD: die Begriffe', table(['Begriff', 'Bedeutung', 'Beispiele'], [
            ['IPTV (Live-TV)', 'Fernsehsender mit festem Programm über das Internet', 'IPTV-Anbieter, MagentaTV, waipu.tv'],
            ['VOD (Video on Demand)', 'Filme und Serien jederzeit abrufen', 'Mediathek im IPTV-Paket, Netflix, Prime Video'],
            ['SVOD', 'VOD im Abo', 'Netflix, Disney+, HBO Max, Paramount+, RTL+'],
            ['FAST-Kanäle', 'Kostenlose, werbefinanzierte Live-Kanäle', 'Pluto TV, Samsung TV Plus, LG Channels, Rakuten TV'],
            ['Mediathek', 'Abruf und Livestream der Sender', 'ARD Mediathek, ZDF, Joyn, RTL+'],
        ], 'Begriffe rund um IPTV und Streaming') + '''
<p>Wer „IPTV Netflix“ sucht, möchte meist wissen, ob er Netflix über seine IPTV-App schauen kann. Die Antwort ist nein – Netflix und alle anderen Streaming-Dienste sind nur in ihren eigenen Apps verfügbar. Angebote, die „Netflix-Inhalte“ in einer IPTV-Liste versprechen, sind nicht lizenziert.</p>'''),
        ('kombinieren', 'Streaming-Apps und IPTV auf einem Gerät', table(['Gerät', 'Netflix, Prime, Disney+, HBO Max', 'IPTV-App'], [
            ['<a href="/iptv-fire-tv-stick/">Fire TV Stick</a>', 'Ja, aus dem Appstore', 'TiviMate, IPTV Smarters Pro'],
            ['<a href="/iptv-google-tv/">Google TV</a> / Android TV', 'Ja, aus dem Play Store', 'TiviMate, OTT Navigator'],
            ['<a href="/iptv-samsung-tv/">Samsung</a> / <a href="/iptv-lg-tv/">LG</a>', 'Ja, vorinstalliert oder im Store', 'SET IPTV, IBO Player'],
            ['<a href="/iptv-apple-tv-iphone/">Apple TV</a>', 'Ja, aus dem App Store', 'IPTVX, iPlayTV'],
        ], 'Streaming und IPTV je Gerät') + '''
<p>Ein Tipp für Fire TV und Google TV: Legen Sie Ihre IPTV-App und die Streaming-Apps in die erste Reihe der Startseite. TiviMate kann zusätzlich so eingestellt werden, dass es nach dem Einschalten direkt mit dem letzten Sender startet. So fühlt sich das Gerät an wie ein Fernseher mit eingebauten Streaming-Diensten.</p>'''),
        ('vod-im-paket', 'VOD im IPTV-Paket: Filme und Serien', '''
<p>Viele IPTV-Zugänge enthalten neben Live-TV eine Mediathek mit Filmen und Serien. Mit einem <a href="/xtream-codes-iptv/">Xtream-Codes-Login</a> zeigen Apps wie IPTV Smarters Pro oder IPTVX sie mit Cover, Beschreibung, Staffeln und „Weiterschauen“-Funktion an. Bei M3U-Listen erscheinen Filme oft nur als lange Liste. Achten Sie bei der Wahl der App deshalb auf eine gute Mediathek-Ansicht – unser Vergleich <a href="/bester-iptv-player/">Bester IPTV Player</a> hilft dabei.</p>'''
         + checks(
            '<strong>Tonspuren:</strong> Viele Filme haben mehrere Sprachen. Die Tonspur wechseln Sie im Player über das Audio-Symbol.',
            '<strong>Untertitel:</strong> Werden angezeigt, wenn sie im Stream enthalten sind. Externe Untertitel unterstützen nur manche Apps.',
            '<strong>4K und HDR:</strong> Setzen ein kompatibles Gerät, HEVC-Unterstützung und ausreichend Bandbreite voraus – siehe <a href="/iptv-4k/">IPTV in 4K</a>.')
         + TEST_TIP),
        ('kostenlos', 'Kostenlose und legale Streaming-Sender', table(['Angebot', 'Was es bietet', 'Wo'], [
            ['Pluto TV', 'Über 100 kostenlose Themenkanäle mit Werbung, dazu Filme auf Abruf', 'App und Browser, ohne Anmeldung'],
            ['Samsung TV Plus', 'Kostenlose Kanäle auf Samsung-Fernsehern und -Handys', 'Vorinstalliert'],
            ['LG Channels', 'Kostenlose Kanäle auf LG-Fernsehern', 'Vorinstalliert'],
            ['Joyn', 'Livestreams von ProSieben, Sat.1, Kabel Eins u. a.', 'App und Browser'],
            ['ARD Mediathek, ZDF', 'Livestreams aller öffentlich-rechtlichen Sender', 'App und Browser'],
        ], 'Kostenlose Streaming-Angebote in Deutschland') + '''
<p>Diese Angebote ergänzen ein IPTV-Paket gut, ersetzen es aber nicht: Sport, Pay-TV-Sender und internationale Programme fehlen weitgehend. Wie legale Gratis-Listen für IPTV-Apps aussehen, beschreibt der Ratgeber <a href="/iptv-playlist-deutsch/">IPTV Playlist Deutsch</a>.</p>'''),
        ('dienste', 'Die wichtigsten Streaming-Dienste in Deutschland 2026', checks(
            '<strong>Netflix:</strong> Serien, Filme, eigene Produktionen; einzelne Live-Events.',
            '<strong>Amazon Prime Video:</strong> Filme, Serien, dazu ein Champions-League-Topspiel pro Spieltag.',
            '<strong>Disney+:</strong> Disney, Pixar, Marvel, Star Wars, National Geographic.',
            '<strong>HBO Max:</strong> Seit 2026 als eigener Dienst in Deutschland verfügbar; zuvor liefen HBO-Serien bei Sky und WOW.',
            '<strong>WOW (Sky):</strong> Sky-Serien, Filme und Sport – mehr unter <a href="/sky-iptv/">Sky über IPTV</a>.',
            '<strong>DAZN:</strong> Bundesliga-Sonntagsspiele, Champions League und weitere Sportarten – siehe <a href="/iptv-fussball/">Fußball per IPTV</a>.',
            '<strong>Paramount+ und RTL+:</strong> Serien und Filme, RTL+ zusätzlich mit RTL-Livestreams.')
         + '<p>Stand der Angaben: November 2026. Inhalte und Preise ändern sich regelmäßig – prüfen Sie die Angaben der Dienste.</p>'),
    ],
    faq=[
        ('Kann ich Netflix über IPTV schauen?', 'Nein. Netflix läuft nur in der offiziellen Netflix-App. Sie können die Netflix-App aber auf demselben Gerät nutzen wie Ihre IPTV-App, etwa auf dem Fire TV Stick oder Smart-TV.'),
        ('Was bedeutet VOD bei IPTV?', 'VOD steht für Video on Demand. Gemeint ist eine Mediathek mit Filmen und Serien, die Sie jederzeit abrufen können – zusätzlich zum Live-TV.'),
        ('Ist Pluto TV kostenlos?', 'Ja. Pluto TV ist kostenlos und werbefinanziert. Sie brauchen keine Anmeldung und können es per App oder Browser nutzen.'),
        ('Gibt es HBO Max in Deutschland?', 'Ja. HBO Max ist seit 2026 als eigener Dienst in Deutschland verfügbar. Vorher liefen HBO-Serien hierzulande bei Sky und WOW.'),
        ('Welche App zeigt Filme und Serien aus dem IPTV-Paket am schönsten?', 'IPTV Smarters Pro und IPTVX zeigen die Mediathek mit Covern, Staffeln und Fortsetzen-Funktion. TiviMate ist stärker beim Live-TV als bei Filmen.'),
    ],
    related=['iptv-senderliste', 'was-ist-iptv', 'iptv-smarters-pro', 'iptvx', 'iptv-telekom-vodafone', 'iptv-playlist-deutsch'],
    card=('IPTV & Streaming', 'Netflix, HBO Max, Pluto TV und VOD im Überblick.'),
))

# ================================================================ LIFETIME
PAGES.append(dict(
    slug='iptv-lifetime', parent='ratgeber', kind='guide',
    title='IPTV Lifetime: Warum Lebenszeit-Abos ein Warnsignal sind',
    description='IPTV Lifetime für einmalig 50 oder 100 Euro? Warum Lebenszeit-Angebote fast immer enden, woran Sie unseriöse Anbieter erkennen und was sich lohnt.',
    eyebrow='KAUFBERATUNG', h1='IPTV Lifetime: was hinter Lebenszeit-Angeboten steckt',
    lead='„Einmal zahlen, für immer fernsehen“ – IPTV-Lifetime-Angebote klingen nach dem besten Deal. In der Praxis sind sie eines der deutlichsten Warnsignale beim IPTV-Kauf. Wir erklären, warum.',
    answer='IPTV Lifetime bedeutet, dass Sie einmal zahlen und den Zugang angeblich unbegrenzt nutzen. Weil ein IPTV-Dienst laufende Kosten für Server, Bandbreite und Support hat, rechnet sich das für keinen Anbieter dauerhaft. „Lifetime“ meint deshalb in der Regel die Lebenszeit des Anbieters – und die ist oft kurz. Sicherer ist eine feste Laufzeit von 1 bis 12 Monaten ohne automatische Verlängerung, idealerweise nach einem kostenlosen Test.',
    sections=[
        ('rechnung', 'Warum sich Lifetime nicht rechnen kann', '''
<p>Ein IPTV-Dienst zahlt jeden Monat für Server, Datenverkehr, Programmdaten und Support. Ein Full-HD-Stream verbraucht rund 2 bis 3 Gigabyte pro Stunde. Wer jeden Abend drei Stunden schaut, erzeugt im Jahr über zwei Terabyte Datenverkehr – Jahr für Jahr. Diese Kosten wachsen mit jeder Nutzungsstunde, die Einnahme aus einem Lifetime-Verkauf nicht.</p>
<p>Ein Lifetime-Modell funktioniert deshalb nur, solange ständig neue Käufer nachkommen. Bleiben sie aus, wird der Dienst langsamer, verliert Sender oder verschwindet ganz. Rückerstattungen gibt es dann meist nicht, weil der Verkäufer nicht mehr erreichbar ist.</p>'''),
        ('warnsignale', 'Woran Sie unseriöse Lifetime-Angebote erkennen', checks(
            '<strong>Kein Impressum</strong> oder nur eine Kontaktadresse über Messenger.',
            '<strong>Zahlung nur per Krypto, Gutscheinkarte oder PayPal „Freunde und Familie“</strong> – ohne Käuferschutz. Mehr dazu unter <a href="/iptv-bezahlen/">IPTV bezahlen</a>.',
            '<strong>Unrealistische Senderzahlen</strong> wie „50.000 Sender und 100.000 Filme“.',
            '<strong>Kein Test</strong> vor dem Kauf – oder ein Test erst nach Zahlung.',
            '<strong>Zeitdruck</strong> („nur heute“, „letzte 10 Plätze“).',
            '<strong>„Lifetime“ und gleichzeitig Reseller-Credits</strong>: Oft verkaufen Wiederverkäufer Zugänge, deren Laufzeit sie selbst nicht garantieren können – siehe <a href="/iptv-reseller/">IPTV Reseller</a>.')),
        ('laufzeit', 'Welche Laufzeit lohnt sich wirklich?', table(['Laufzeit', 'Für wen', 'Risiko'], [
            ['Kostenloser Test', 'Jeden – vor dem ersten Kauf', 'Keins'],
            ['1 Monat', 'Einsteiger, Sport-Saison, Urlaubszeit', 'Sehr gering'],
            ['3 bis 6 Monate', 'Wer den Dienst kennt und sparen möchte', 'Gering'],
            ['12 Monate', 'Zufriedene Bestandskunden mit dem günstigsten Monatspreis', 'Überschaubar bei seriösem Anbieter'],
            ['Lifetime', 'Niemanden', 'Hoch – Totalverlust möglich'],
        ], 'IPTV-Laufzeiten im Vergleich') + '''
<p>Ein Jahresabo bei einem Anbieter mit Impressum, Test und Käuferschutz ist praktisch immer günstiger als ein Lifetime-Angebot, das nach wenigen Monaten endet. Wie Sie Anbieter systematisch prüfen, zeigt der <a href="/iptv-anbieter-vergleich/">IPTV-Anbieter-Vergleich</a>.</p>'''),
        ('app-lizenz', 'Nicht verwechseln: Lifetime-Lizenzen für Apps', '''
<p>Ganz anders sieht es bei <strong>IPTV-Apps</strong> aus. Player wie <a href="/tivimate-premium/">TiviMate Premium</a>, <a href="/set-iptv/">SET IPTV</a> oder <a href="/ibo-player/">IBO Player</a> verkaufen oft eine einmalige Lizenz für die App selbst. Das ist seriös, weil die App keine laufenden Streaming-Kosten hat – sie spielt nur ab. Eine solche Lizenz enthält aber keine Sender. Für das Fernsehprogramm brauchen Sie immer einen IPTV-Zugang mit eigener Laufzeit.</p>'''),
        ('iptv-kanal', 'So handhabt es IPTV Kanal', '''
<p>Bei IPTV Kanal zahlen Sie einmal für eine feste Laufzeit von 1, 3, 6 oder 12 Monaten – ohne automatische Verlängerung und ohne Lifetime-Versprechen. Vorher testen Sie kostenlos und ohne Zahlungsdaten auf Ihrem eigenen Gerät. Alle Pakete und Preise finden Sie unter <a href="/preise/">Preise</a>, Hintergründe zum Kauf im Ratgeber <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>'''),
    ],
    faq=[
        ('Gibt es seriöses IPTV Lifetime?', 'Für IPTV-Zugänge praktisch nicht, weil Server und Bandbreite laufend Geld kosten. „Lifetime“ endet meist, wenn der Anbieter aufhört. Seriös sind dagegen Lifetime-Lizenzen für Apps wie TiviMate, die keine Sender enthalten.'),
        ('Was passiert, wenn ein Lifetime-Anbieter verschwindet?', 'Der Zugang funktioniert nicht mehr, und das Geld ist in der Regel verloren. Ohne Impressum und Käuferschutz gibt es kaum eine Möglichkeit, es zurückzufordern.'),
        ('Welche IPTV-Laufzeit ist am günstigsten?', 'Pro Monat gerechnet meist das Jahresabo. Starten Sie trotzdem mit einem kostenlosen Test und einem Monat, bevor Sie sich länger festlegen.'),
        ('Woran erkenne ich einen seriösen IPTV-Anbieter?', 'An Impressum, kostenlosem Test vor dem Kauf, Zahlung mit Käuferschutz, erreichbarem Support und realistischen Angaben zu Sendern und Geräten.'),
        ('Ist eine TiviMate-Lifetime-Lizenz dasselbe wie IPTV Lifetime?', 'Nein. Die TiviMate-Lizenz schaltet nur Funktionen der App frei. Sender sind darin nicht enthalten – dafür brauchen Sie einen IPTV-Zugang.'),
    ],
    related=['iptv-kaufen', 'iptv-anbieter-vergleich', 'iptv-bezahlen', 'iptv-erfahrungen', 'iptv-reseller', 'tivimate-premium'],
    card=('IPTV Lifetime', 'Warum Lebenszeit-Abos ein Warnsignal sind.'),
    sources=[('Verbraucherzentrale', 'https://www.verbraucherzentrale.de/')],
))

# ================================================================ SERVER / BUFFERING
PAGES.append(dict(
    slug='iptv-server', parent='ratgeber', kind='guide',
    title='IPTV Server erklärt: Warum Streams puffern & was hilft',
    description='IPTV Server einfach erklärt: wie Streams zu Ihnen kommen, warum IPTV abends puffert, was „max connections“ bedeutet und welche Lösungen helfen.',
    eyebrow='TECHNIK VERSTÄNDLICH', h1='IPTV Server: wie Streams zu Ihnen kommen – und warum sie puffern',
    lead='Wenn IPTV puffert, liegt es selten nur an einer Stelle. Zwischen Fernsehsender und Fernseher liegen Server, Rechenzentren, Netzbetreiber und Ihr Heimnetz. Wer die Kette kennt, findet den Fehler schneller.',
    answer='Ein IPTV Server empfängt Fernsehsender, wandelt sie in Datenströme um und verteilt sie über das Internet an die Geräte der Kunden. Puffern entsteht, wenn an einer Stelle der Kette zu wenig Kapazität ist: beim Server des Anbieters, an der Verbindung zwischen Rechenzentrum und Ihrem Netzbetreiber oder in Ihrem WLAN. Gegen Probleme im Heimnetz helfen LAN-Kabel, größerer Puffer und das TS-Format; Serverprobleme muss der Anbieter lösen.',
    sections=[
        ('kette', 'Der Weg eines IPTV-Streams', steps(
            '<b>Quelle:</b> Das Fernsehsignal wird empfangen, etwa über Satellit oder Glasfaser.',
            '<b>Encoder/Transcoder:</b> Das Signal wird in ein Streaming-Format umgewandelt (H.264 oder HEVC, meist als MPEG-TS oder HLS).',
            '<b>Hauptserver und Panel:</b> Verwalten Sender, Zugänge, Programmführer und erlaubte Verbindungen.',
            '<b>Lastverteiler und Edge-Server:</b> Verteilen die Zuschauer auf mehrere Server, möglichst nah an Ihrem Wohnort.',
            '<b>Internet und Netzbetreiber:</b> Der Stream läuft über Austauschpunkte (Peering) in das Netz von Telekom, Vodafone, 1&amp;1 oder O2.',
            '<b>Heimnetz und Gerät:</b> Router, WLAN oder LAN, schließlich der Player auf Ihrem Gerät.')
         + '<p>Ein Ausfall oder Engpass an jeder dieser Stationen führt zum selben Ergebnis: Das Bild bleibt stehen, der Ladekreis dreht sich.</p>'),
        ('ursachen', 'Woher kommt das Puffern? Eine Eingrenzung', table(['Anzeichen', 'Wahrscheinliche Ursache', 'Wer kann es lösen?'], [
            ['Nur ein Sender puffert, andere laufen', 'Problem mit der Quelle dieses Senders', 'Anbieter'],
            ['Alle Sender puffern, nur abends', 'Überlastetes WLAN oder Engpass beim Peering', 'Sie (Heimnetz) oder Anbieter (Peering)'],
            ['Alle Sender puffern immer', 'Leitung zu langsam oder Gerät überfordert', 'Sie'],
            ['Puffert nur bei Fußball', 'Viele Zuschauer gleichzeitig, Server ausgelastet', 'Anbieter'],
            ['Läuft am Handy im Mobilfunk, aber nicht zu Hause', 'Heimnetz oder Route über Ihren Netzbetreiber', 'Sie, ggf. Anbieter'],
        ], 'Ursachen für Puffern eingrenzen') + '''
<p>Der Mobilfunk-Test ist der schnellste Hinweis: Starten Sie denselben Sender auf dem Handy ohne WLAN. Läuft er dort flüssig, liegt das Problem sehr wahrscheinlich in Ihrem Heimnetz oder auf dem Weg zu Ihrem Festnetzanbieter.</p>'''),
        ('selbst', 'Was Sie selbst tun können', checks(
            '<strong>LAN statt WLAN:</strong> Der wirksamste Einzelschritt. Für Fire TV Sticks gibt es günstige USB-LAN-Adapter.',
            '<strong>5-GHz-WLAN nutzen</strong>, wenn kein Kabel möglich ist, und den Router nicht hinter den Fernseher stellen.',
            '<strong>Stream-Format TS statt HLS</strong> in der App wählen – schnelleres Umschalten, weniger Aussetzer.',
            '<strong>Puffer auf „groß“</strong> stellen und den Hardware-Decoder aktivieren.',
            '<strong>Router und Gerät neu starten</strong>, besonders nach Firmware-Updates.',
            '<strong>Geschwindigkeit abends messen</strong>, nicht morgens – etwa 16 Mbit/s für Full HD, 25 Mbit/s für 4K pro Gerät.')
         + '<p>Gerätespezifische Tipps finden Sie in den Anleitungen für <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, <a href="/tivimate/">TiviMate</a> und <a href="/iptv-4k/">4K-Streams</a>.</p>'),
        ('verbindungen', '„Max connections“: Verbindungen und Geräte', '''
<p>Jeder Zugang erlaubt eine bestimmte Zahl <strong>gleichzeitiger Verbindungen</strong>. Startet ein weiteres Gerät einen Stream, meldet der Server „max connections reached“ oder beendet den ältesten Stream. Häufige Auslöser: eine App, die im Hintergrund weiterläuft, eine laufende Aufnahme oder der Programmführer-Abruf mancher Apps. Schließen Sie Apps auf anderen Geräten vollständig und warten Sie eine Minute, bis der Server die Verbindung freigibt. Wie viele Geräte Sie brauchen, hängt von Ihrem Haushalt ab – bei IPTV Kanal wählen Sie zwischen 1 und 5 Geräten, siehe <a href="/preise/">Preise</a>.</p>'''),
        ('anbieter', 'Woran Sie gute IPTV Server beim Anbieter erkennen', '''
<p>Als Kunde sehen Sie die Server nicht, aber ihre Qualität: Wie schnell schaltet ein Sender um? Läuft Fußball am Samstagabend ohne Aussetzer? Antwortet der Support, wenn ein Sender ausfällt? Ein <strong>kostenloser Test</strong> am Abend oder während eines Spiels sagt mehr als jede Werbeaussage. Vorsicht bei Angeboten wie „Anti-Freeze-Server“ oder „Lifetime“ – mehr dazu unter <a href="/iptv-lifetime/">IPTV Lifetime</a> und im <a href="/iptv-anbieter-vergleich/">Anbieter-Vergleich</a>.</p>'''
         + tip('Testen Sie IPTV Kanal kostenlos genau dann, wenn Sie sonst fernsehen – zum Beispiel zum Bundesliga-Topspiel. So sehen Sie unter echten Bedingungen, wie stabil es auf Ihrem Gerät und Ihrer Leitung läuft.', 'Unser Rat')),
    ],
    faq=[
        ('Was ist ein IPTV Server?', 'Ein IPTV Server empfängt Fernsehsender, wandelt sie in Datenströme um und verteilt sie über das Internet an die Geräte der Kunden. Große Anbieter nutzen viele Server, auf die die Zuschauer verteilt werden.'),
        ('Warum puffert IPTV abends?', 'Abends sind WLAN, Netzbetreiber und Server am stärksten ausgelastet. Häufigste Ursache ist überlastetes WLAN im eigenen Haus; ein LAN-Kabel hilft meist sofort.'),
        ('Was bedeutet „max connections reached“?', 'Ihr Zugang ist bereits auf der erlaubten Zahl von Geräten aktiv. Schließen Sie die App auf anderen Geräten vollständig und warten Sie kurz, bevor Sie erneut starten.'),
        ('Wie finde ich heraus, ob das Problem bei mir oder beim Anbieter liegt?', 'Starten Sie denselben Sender auf dem Handy im Mobilfunknetz. Läuft er dort flüssig, liegt das Problem wahrscheinlich im Heimnetz oder bei Ihrem Festnetzanbieter.'),
        ('Hilft ein VPN gegen Puffern?', 'Manchmal, wenn die direkte Route zwischen Ihrem Netzbetreiber und dem Server schlecht ist. Ein VPN kann aber auch zusätzliche Verzögerung bringen. Prüfen Sie zuerst Heimnetz und Gerät.'),
    ],
    related=['iptv-4k', 'iptv-fire-tv-stick', 'iptv-anbieter', 'iptv-fussball', 'iptv-einrichten', 'iptv-lifetime'],
    card=('IPTV Server & Puffern', 'Wie Streams zu Ihnen kommen und was gegen Puffern hilft.'),
))

# ================================================================ ENGLISCH / UK
PAGES.append(dict(
    slug='iptv-englisch', parent='international', kind='guide',
    title='Englisches Fernsehen in Deutschland: BBC, ITV & UK-TV',
    description='Englisches Fernsehen in Deutschland: BBC, ITV und UK-Sender per Satellit, Streaming und IPTV – was legal geht und was Geoblocking bedeutet.',
    eyebrow='INTERNATIONAL', h1='Englisches Fernsehen in Deutschland: BBC, ITV und UK-Sender',
    lead='Briten, Iren, Amerikaner und alle, die lieber im Original schauen: In Deutschland leben Hunderttausende, die englischsprachiges Fernsehen suchen. Hier lesen Sie, welche Wege es gibt – und wo die Grenzen liegen.',
    answer='Britische Sender wie BBC One, ITV oder Channel 4 sind in Deutschland nur eingeschränkt verfügbar: BBC iPlayer, ITVX und Channel 4 streamen nur innerhalb Großbritanniens. Per Satellit (Astra 28,2° Ost) lassen sich viele UK-Sender empfangen, allerdings nur mit einer deutlich größeren Schüssel. Englischsprachige Nachrichtensender wie CNN International und BBC News sind dagegen weit verbreitet, und Streaming-Dienste bieten fast alles im Originalton.',
    sections=[
        ('wege', 'Vier Wege zu englischsprachigem Fernsehen', table(['Weg', 'Was Sie bekommen', 'Einschränkungen'], [
            ['Satellit Astra 28,2° Ost (Freesat)', 'BBC, ITV, Channel 4, Channel 5 u. a. frei empfangbar', 'Große Schüssel nötig, je nach Wohnort weit über 1 Meter'],
            ['Streaming-Dienste im Originalton', 'Netflix, Prime Video, Disney+, HBO Max mit englischer Tonspur', 'Kein lineares UK-Fernsehen, keine britischen Nachrichten'],
            ['Internationale Nachrichtensender', 'CNN International, BBC News, Sky News, Euronews (EN)', 'Nachrichten, keine Unterhaltung'],
            ['IPTV mit internationalen Paketen', 'Live-Sender inkl. Programmführer auf jedem Gerät', 'Senderumfang je nach Anbieter – vorher testen'],
        ], 'Englisches Fernsehen in Deutschland') + '''
<p>Für Sport im Originalkommentar lohnt außerdem ein Blick in die Audio-Optionen deutscher Anbieter: Manche Übertragungen bieten eine zweite Tonspur. Welche Rechte wo liegen, zeigen die Ratgeber <a href="/iptv-fussball/">Fußball per IPTV</a> und <a href="/iptv-sport/">IPTV Sport</a>.</p>'''),
        ('geoblocking', 'Warum BBC iPlayer in Deutschland nicht funktioniert', '''
<p>Die BBC finanziert sich über die britische Rundfunkgebühr (TV Licence) und besitzt Senderechte meist nur für Großbritannien. BBC iPlayer prüft deshalb Ihren Standort und blockiert Zugriffe aus dem Ausland. Dasselbe gilt für ITVX, Channel 4 und My5. Innerhalb der EU gibt es zwar die Portabilitätsverordnung, die Abo-Dienste auf Reisen nutzbar macht – sie gilt aber nur für Abos aus EU-Ländern und damit nicht für britische Dienste.</p>
<p>Ein VPN umgeht die Standortprüfung technisch, verstößt aber gegen die Nutzungsbedingungen der Sender. Rechtlich ist das eine Grauzone, praktisch blockieren die Dienste bekannte VPN-Adressen regelmäßig.</p>'''),
        ('satellit', 'UK-Sender per Satellit empfangen', steps(
            'Eine Schüssel auf Astra 28,2° Ost ausrichten – nicht auf das in Deutschland übliche Astra 19,2° Ost.',
            'Die Größe vom Wohnort abhängig machen: Die britischen Sender werden mit einem engen Ausleuchtungsbereich (Spotbeam) auf Großbritannien gesendet. In Deutschland sind deshalb deutlich größere Schüsseln nötig als für deutsche Sender.',
            'Einen Receiver mit Freesat-kompatiblem Programmführer oder einen <a href="/iptv-receiver/">Enigma2-Receiver</a> anschließen.',
            'Wer zusätzlich deutsche Sender möchte, braucht einen Multifeed-Aufbau oder eine zweite Schüssel.')
         + tip('Vermieter und Eigentümergemeinschaften müssen große Schüsseln oft genehmigen. IPTV braucht dagegen keine Montage – ein Streaming-Stick genügt.', 'Gut zu wissen')),
        ('iptv', 'Englischsprachiges Fernsehen per IPTV', '''
<p>Mit IPTV erhalten Sie Live-Sender aus vielen Ländern auf jedem Gerät – vom <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> bis zum <a href="/iptv-apple-tv-iphone/">Apple TV</a>. In einer guten App sortieren Sie internationale Sender in eigene Gruppen, etwa „UK“, „USA“ oder „News EN“, und blenden alles Übrige aus. So entsteht eine englischsprachige Senderliste mit Programmführer.</p>
<p>Wie internationale Senderpakete aufgebaut sind, beschreibt der Ratgeber <a href="/iptv-international/">IPTV International</a>. Tipps zum Sortieren von Gruppen und Favoriten finden Sie unter <a href="/iptv-senderliste/">IPTV Senderliste</a>.</p>''' + TEST_TIP),
        ('originalton', 'Tipp: Originalton bei Filmen und Serien', '''
<p>Für Filme und Serien ist die einfachste Lösung oft die Tonspur. Netflix, Prime Video, Disney+, HBO Max und Sky bieten fast alle Titel im englischen Original mit Untertiteln an. Auch Mediathek-Inhalte in IPTV-Paketen haben häufig mehrere Tonspuren – Sie wechseln sie im Player über das Audio-Symbol. Mehr zur Kombination von Streaming und Live-TV lesen Sie unter <a href="/iptv-vod/">IPTV und Streaming</a>.</p>'''),
    ],
    faq=[
        ('Kann ich BBC iPlayer in Deutschland nutzen?', 'Offiziell nein. BBC iPlayer ist auf Großbritannien beschränkt und prüft den Standort. Die EU-Portabilitätsverordnung gilt nicht für britische Dienste.'),
        ('Wie empfange ich britische Sender in Deutschland?', 'Per Satellit über Astra 28,2° Ost mit einer deutlich größeren Schüssel als üblich, über internationale IPTV-Pakete oder – für Nachrichten – über Sender wie BBC News und CNN International.'),
        ('Welche englischsprachigen Nachrichtensender gibt es in Deutschland?', 'Unter anderem CNN International, BBC News, Sky News und Euronews auf Englisch – je nach Empfangsweg über Satellit, Kabel, Streaming oder IPTV.'),
        ('Gibt es englische Filme und Serien im Originalton?', 'Ja. Netflix, Prime Video, Disney+, HBO Max und Sky bieten fast alle Titel mit englischer Tonspur. Auch viele IPTV-Mediatheken haben mehrere Tonspuren.'),
        ('Welche UK-Sender enthält IPTV Kanal?', 'Die vollständige Senderliste Ihres Zugangs sehen Sie im kostenlosen Test auf Ihrem eigenen Gerät, bevor Sie etwas bezahlen.'),
    ],
    related=['iptv-international', 'iptv-senderliste', 'iptv-sport', 'iptv-vod', 'iptv-receiver', 'iptv-fire-tv-stick'],
    card=('Englisches TV', 'BBC, ITV und UK-Sender in Deutschland schauen.'),
    sources=[('BBC iPlayer Hilfe', 'https://www.bbc.co.uk/iplayer/help')],
))

# ================================================================ PLAYLIST DEUTSCH
PAGES.append(dict(
    slug='iptv-playlist-deutsch', parent='ratgeber', kind='guide',
    title='IPTV Playlist Deutsch: legale M3U-Listen & Risiken',
    description='IPTV Playlist Deutsch: welche kostenlosen M3U-Listen legal sind, was in iptv-org und Kodinerds steckt und warum Gratis-Listen mit Pay-TV riskant sind.',
    eyebrow='M3U-LISTEN', h1='IPTV Playlist Deutsch: legale M3U-Listen und ihre Grenzen',
    lead='Wer „IPTV Playlist Deutsch“ oder „beste M3U Liste“ sucht, findet unzählige Links. Einige sind legal und nützlich, viele sind veraltet – und manche bringen echte Risiken mit. Hier ist der Überblick.',
    answer='Legale deutsche IPTV-Playlists gibt es: Sammlungen wie iptv-org auf GitHub oder die Kodinerds-Liste enthalten Livestreams, die Sender wie ARD, ZDF und Regionalsender selbst frei im Internet anbieten. Pay-TV, Sky, DAZN oder Bundesliga sind darin nicht enthalten. Gratis-Listen, die solche Inhalte versprechen, sind nicht lizenziert – nach einem Urteil des EuGH kann schon das Ansehen offensichtlich rechtswidriger Streams unzulässig sein. Für ein vollständiges Programm brauchen Sie einen IPTV-Zugang.',
    sections=[
        ('legal', 'Welche deutschen Playlists sind legal?', table(['Quelle', 'Inhalt', 'Zuverlässigkeit'], [
            ['iptv-org (GitHub)', 'Öffentlich verfügbare Streams, sortiert nach Ländern, Sprachen und Kategorien', 'Wird laufend gepflegt, einzelne Links fallen aus'],
            ['Kodinerds-IPTV-Liste', 'Livestreams öffentlich-rechtlicher und frei verfügbarer deutscher Sender', 'Auf deutsche Sender spezialisiert'],
            ['Mediatheken der Sender', 'Offizielle Livestreams von ARD, ZDF, Dritten, Arte, 3sat u. a.', 'Sehr zuverlässig, aber nur in den eigenen Apps'],
            ['FAST-Dienste (Pluto TV, Samsung TV Plus)', 'Kostenlose Themenkanäle mit Werbung', 'Zuverlässig, nur in den eigenen Apps'],
        ], 'Legale Quellen für deutsche Sender') + '''
<p>Diese Listen enthalten Streams, die die Sender selbst öffentlich bereitstellen. Sie lassen sich in fast jeden Player laden, etwa in <a href="/vlc-iptv/">VLC</a> oder <a href="/kodi-iptv/">Kodi</a>. Erwarten Sie aber kein Komplettprogramm: Private Sender in HD, Pay-TV und Sport fehlen, und manche Streams sind nur in Deutschland abrufbar.</p>'''),
        ('laden', 'So laden Sie eine Playlist in Ihre App', steps(
            'Die Adresse der Liste (endet meist auf <code>.m3u</code> oder <code>.m3u8</code>) kopieren.',
            'In der App „Playlist hinzufügen“ und den Typ <b>M3U-URL</b> wählen.',
            'Adresse einfügen, Namen vergeben und speichern.',
            'Optional eine EPG-Adresse (XMLTV) ergänzen, damit der Programmführer erscheint.',
            'Nicht funktionierende Sender in der App ausblenden.')
         + '<p>Wie M3U-Listen aufgebaut sind und wie Sie sie bearbeiten, erklärt der Ratgeber <a href="/m3u-playlist/">M3U-Playlist</a>. Auf Samsung- und LG-Fernsehern laden Sie die Liste meist über die Website der App hoch, etwa bei <a href="/set-iptv/">SET IPTV</a> oder <a href="/smart-iptv/">Smart IPTV</a>.</p>'),
        ('risiken', 'Gratis-Listen mit Sky, DAZN und Bundesliga: die Risiken', checks(
            '<strong>Rechtlich:</strong> Der Europäische Gerichtshof hat 2017 (Rechtssache C-527/15, „Filmspeler“) entschieden, dass auch das Streamen offensichtlich rechtswidriger Quellen eine unzulässige Vervielfältigung sein kann.',
            '<strong>Technisch:</strong> Solche Listen werden schnell gesperrt; Sender fallen mitten im Spiel aus.',
            '<strong>Sicherheit:</strong> Listen werden oft über Telegram, Foren oder Downloader-Codes verteilt und mit manipulierten Apps kombiniert – siehe <a href="/iptv-downloader/">Downloader sicher nutzen</a>.',
            '<strong>Datenschutz:</strong> Der Betreiber der Liste sieht Ihre IP-Adresse und Sehgewohnheiten.')
         + tip('Eine Liste mit „10.000 Sendern gratis“ ist kein Schnäppchen, sondern ein Warnsignal. Seriöse Anbieter zeigen vorab, was enthalten ist, und lassen Sie kostenlos testen.', 'Hinweis')),
        ('beste-liste', 'Was ist die „beste M3U-Liste“?', '''
<p>Die beste Liste ist die, die zuverlässig funktioniert, einen gepflegten Programmführer hat und deren Sender Sie tatsächlich schauen. Bei frei verfügbaren Listen bedeutet das: lieber eine kleine, gepflegte Liste mit deutschen öffentlich-rechtlichen Sendern als eine riesige Sammlung mit vielen toten Links. Wer ein vollständiges deutsches Programm mit privaten Sendern in HD, Sport und internationalen Paketen möchte, braucht einen IPTV-Zugang. Dort kommt die Playlist mit Programmführer und Kategorien vom Anbieter – als <a href="/xtream-codes-iptv/">Xtream-Codes-Login</a> oder M3U-Link.</p>
<p>Welche Sendergruppen typischerweise enthalten sind, zeigt die <a href="/iptv-senderliste/">IPTV Senderliste</a>. Kostenlose Streaming-Alternativen fasst der Ratgeber <a href="/iptv-vod/">IPTV und Streaming</a> zusammen.</p>'''),
        ('pflege', 'Playlist pflegen: tote Links und Sortierung', table(['Aufgabe', 'Werkzeug'], [
            ['Tote Links finden', 'Sender in VLC testen oder in der App „nicht verfügbare Sender ausblenden“'],
            ['Sender sortieren und umbenennen', 'Texteditor oder Playlist-Editoren am PC'],
            ['Sendergruppen anlegen', 'Feld <code>group-title</code> in der M3U-Datei'],
            ['Programmführer zuordnen', 'Feld <code>tvg-id</code> passend zur XMLTV-Datei'],
        ], 'M3U-Playlist pflegen')),
    ],
    faq=[
        ('Gibt es eine legale kostenlose IPTV Playlist für Deutschland?', 'Ja. Sammlungen wie iptv-org auf GitHub oder die Kodinerds-Liste enthalten Livestreams, die Sender wie ARD und ZDF selbst frei anbieten. Pay-TV und Sport sind darin nicht enthalten.'),
        ('Was ist die Kodinerds IPTV-Liste?', 'Eine von der Kodi-Community gepflegte M3U-Liste mit frei verfügbaren Livestreams deutscher Sender, vor allem der öffentlich-rechtlichen Programme. Sie lässt sich in Kodi, VLC und andere Player laden.'),
        ('Sind Gratis-Listen mit Sky und Bundesliga legal?', 'Nein. Solche Listen sind nicht lizenziert. Nach dem Filmspeler-Urteil des EuGH von 2017 kann bereits das Ansehen offensichtlich rechtswidriger Streams unzulässig sein.'),
        ('Warum funktionieren viele Sender aus kostenlosen Listen nicht?', 'Streams werden geändert, abgeschaltet oder sind nur in bestimmten Ländern abrufbar. Freie Sammlungen werden zwar gepflegt, einzelne Links fallen aber regelmäßig aus.'),
        ('Wie lade ich eine M3U-Playlist auf meinen Fernseher?', 'In Apps wie TiviMate oder IPTV Smarters Pro über „Playlist hinzufügen“ und den Typ M3U-URL. Auf Samsung und LG laden Sie die Liste meist über die Website der App, etwa bei SET IPTV.'),
    ],
    related=['m3u-playlist', 'iptv-senderliste', 'kodi-iptv', 'vlc-iptv', 'iptv-vod', 'xtream-codes-iptv'],
    card=('IPTV Playlist Deutsch', 'Legale M3U-Listen für deutsche Sender und ihre Grenzen.'),
    sources=[('iptv-org auf GitHub', 'https://github.com/iptv-org/iptv'),
             ('EuGH, Rechtssache C-527/15 (Filmspeler)', 'https://curia.europa.eu/juris/liste.jsf?num=C-527/15')],
))

# New pages appended to the related links of existing guides (aggressive internal linking).
LINK_FROM = {
    'iptv-einrichten': ['was-ist-iptv', 'iptv-kaufen', 'xtream-codes-iptv', 'm3u-playlist', 'iptv-geraete', 'iptv-apps', 'iptv-smart-tv'],
    'bester-iptv-player': ['iptv-apps', 'tivimate', 'iptv-smarters-pro', 'iptv-fire-tv-stick', 'iptv-android', 'set-iptv'],
    'tivimate-fire-tv-stick': ['tivimate', 'tivimate-premium', 'iptv-fire-tv-stick', 'fire-tv-modelle', 'iptv-smarters-pro-firestick'],
    'iptv-chromecast': ['iptv-google-tv', 'iptv-stick', 'iptv-geraete', 'gse-smart-iptv'],
    'iptv-im-browser': ['iptv-pc-mac', 'vlc-iptv', 'iptv-apps'],
    'iptv-downloader': ['iptv-fire-tv-stick', 'iptv-smarters-pro-firestick', 'cloudstream', 'xciptv', 'ott-navigator'],
    'plex-jellyfin-iptv': ['kodi-iptv', 'pvr-iptv-simple-client', 'iptv-apps'],
    'iptv-aufnehmen': ['tivimate-premium', 'iptv-receiver', 'sky-iptv', 'iptv-dreambox'],
    'sat-ip': ['iptv-telekom-vodafone', 'iptv-receiver', 'was-ist-iptv', 'iptv-vu-plus'],
    'iptv-vod': ['iptv-senderliste', 'was-ist-iptv', 'iptv-telekom-vodafone', 'iptvx'],
    'iptv-lifetime': ['iptv-kaufen', 'iptv-anbieter-vergleich', 'iptv-bezahlen', 'iptv-erfahrungen', 'iptv-reseller'],
    'iptv-server': ['iptv-4k', 'iptv-fussball', 'iptv-anbieter', 'iptv-sport'],
    'iptv-englisch': ['iptv-international', 'iptv-sport', 'iptv-russisch', 'iptv-balkan'],
    'iptv-playlist-deutsch': ['m3u-playlist', 'iptv-senderliste', 'kodi-iptv', 'vlc-iptv'],
}
