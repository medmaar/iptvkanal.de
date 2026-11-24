"""Core guide and money pages (German). Facts about the offer come from the live pricing in assets/main.js."""
from .helpers import steps, checks, tip, table, proscons, chips

PRICE_ROWS = [
    ['1 Gerät', '9 €', '29 €', '39 €', '<strong>49 €</strong>'],
    ['2 Geräte', '18 €', '50 €', '69 €', '<strong>89 €</strong>'],
    ['3 Geräte', '27 €', '75 €', '105 €', '<strong>135 €</strong>'],
    ['4 Geräte', '36 €', '99 €', '140 €', '<strong>180 €</strong>'],
    ['5 Geräte', '45 €', '120 €', '175 €', '<strong>225 €</strong>'],
]
PRICE_TABLE = table(['Geräte gleichzeitig', '1 Monat', '3 Monate', '6 Monate', '1 Jahr'], PRICE_ROWS,
                    'IPTV-Kanal-Preise nach Laufzeit und Geräteanzahl')

PAGES = []

# ---------------------------------------------------------------- Was ist IPTV
PAGES.append(dict(
    slug='was-ist-iptv', parent='ratgeber', kind='guide',
    title='Was ist IPTV? Internet Protocol Television einfach erklärt',
    description='Was ist IPTV und wie funktioniert Internet Protocol Television? Technik, Vorteile, Voraussetzungen und Unterschiede zu Kabel, Satellit und Streaming – verständlich erklärt.',
    eyebrow='IPTV-GRUNDLAGEN', h1='Was ist IPTV?',
    lead='IPTV steht für Internet Protocol Television: Fernsehen, das über Ihre Internetleitung statt über Kabel, Satellit oder Antenne kommt. Hier erfahren Sie, wie das funktioniert und was Sie dafür brauchen.',
    answer='IPTV (Internet Protocol Television) überträgt Fernsehsender, Filme und Serien als Datenstrom über das Internet. Sie brauchen nur einen Internetanschluss ab etwa 10 Mbit/s, ein Abspielgerät wie Smart-TV, Fire TV Stick oder Smartphone und eine IPTV-App. Live-TV, Mediathek und Programmführer laufen dann in einer Oberfläche.',
    sections=[
        ('definition', 'IPTV: die Definition in einem Satz', '''
<p><strong>IPTV</strong> ist jede Form von Fernsehen, bei der Bild und Ton mit dem Internet-Protokoll (IP) übertragen werden. Statt eines Funksignals vom Satelliten oder eines Kabelsignals aus der Wand empfängt Ihr Gerät kleine Datenpakete über den Router – genau wie bei einer Webseite, nur als fortlaufender Videostream.</p>
<p>Der Begriff wird in Deutschland für zwei Dinge benutzt: für das Fernsehen der Internetanbieter (zum Beispiel MagentaTV der Telekom, mehr dazu in unserem Ratgeber <a href="/iptv-telekom-vodafone/">IPTV bei Telekom, Vodafone, 1&amp;1 und o2</a>) und für unabhängige IPTV-Dienste, die über jede beliebige Internetleitung funktionieren – so wie <a href="/">IPTV Kanal</a>.</p>'''),
        ('funktionsweise', 'So funktioniert Internet Protocol Television', '''
<p>Ein IPTV-Dienst nimmt Fernsehsignale auf, codiert sie (meist in H.264 oder HEVC/H.265) und verteilt sie über Server. Ihre App fragt den gewünschten Sender an und erhält einen Stream. Weil das über das normale Internet passiert, ist es egal, ob Sie DSL, Glasfaser, Kabelinternet oder 5G nutzen.</p>
''' + steps(
            '<b>Zugang:</b> Sie erhalten Zugangsdaten – als Xtream-Codes-Login (Server, Benutzername, Passwort), als <a href="/m3u-playlist/">M3U-Playlist</a> oder als Portal-Adresse für MAG-Boxen.',
            '<b>App:</b> Eine IPTV-App wie <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a> lädt damit Senderliste, Mediathek und Programmführer (EPG).',
            '<b>Stream:</b> Beim Umschalten öffnet die App den Datenstrom des Senders; ein Puffer von wenigen Sekunden gleicht Schwankungen der Leitung aus.',
            '<b>Extras:</b> Catch-Up (zeitversetzt schauen), Video-on-Demand und Favoritenlisten kommen ohne Zusatzhardware dazu.') + '''
<p>Die Formate dahinter (M3U, M3U8, Xtream Codes, Stalker-Portal) erklären wir ausführlich im Ratgeber <a href="/xtream-codes-iptv/">Xtream Codes &amp; XCIPTV</a>.</p>'''),
        ('vergleich', 'IPTV vs. Kabel, Satellit und Streaming', '''
<p>Die wichtigsten Unterschiede auf einen Blick:</p>
''' + table(['', 'IPTV', 'Kabel-TV', 'Satellit', 'Streaming-Dienst'], [
            ['Empfang', 'Internetleitung', 'Kabelanschluss', 'Schüssel + Receiver', 'Internetleitung'],
            ['Live-TV', 'Ja', 'Ja', 'Ja', 'Meist nein'],
            ['Filme &amp; Serien auf Abruf', 'Ja (VOD)', 'Eingeschränkt', 'Nein', 'Ja'],
            ['Programmführer &amp; Catch-Up', 'Ja', 'Teilweise', 'Teilweise', 'Nein'],
            ['Mehrere Geräte / unterwegs', 'Ja', 'Nein', 'Nein', 'Ja'],
            ['Installation', 'App öffnen', 'Techniker / Dose', 'Montage', 'App öffnen'],
        ], 'Vergleich von IPTV mit Kabel, Satellit und Streaming') + '''
<p>Seit dem Ende des Nebenkostenprivilegs im Juli 2024 dürfen Vermieter Kabelfernsehen nicht mehr über die Nebenkosten abrechnen. Viele Haushalte haben deshalb erstmals verglichen – und festgestellt, dass ihre ohnehin bezahlte Internetleitung für Fernsehen reicht.</p>'''),
        ('voraussetzungen', 'Was Sie für IPTV brauchen', checks(
            '<strong>Internet:</strong> ab 10 Mbit/s für HD, ab 16 Mbit/s für Full HD und ab 25 Mbit/s für 4K – pro gleichzeitig genutztem Gerät. Details im Ratgeber <a href="/iptv-4k/">IPTV in 4K</a>.',
            '<strong>Gerät:</strong> Smart-TV, <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>, <a href="/iptv-box/">Android-Box</a>, <a href="/iptv-apple-tv-iphone/">Apple TV, iPhone</a>, <a href="/iptv-pc-mac/">PC oder Mac</a>. Alle Optionen in der <a href="/iptv-geraete/">Geräteübersicht</a>.',
            '<strong>App:</strong> einen IPTV-Player. Welche App zu welchem Gerät passt, zeigt unsere <a href="/iptv-apps/">IPTV-App-Übersicht</a>.',
            '<strong>Zugang:</strong> ein IPTV-Abo mit Zugangsdaten – bei IPTV Kanal ab 9 € für einen Monat, ohne automatische Verlängerung.')),
        ('vorteile', 'Vorteile und Grenzen von IPTV', proscons(
            ['Kein Kabelanschluss, keine Schüssel, kein Techniker', 'Live-TV, Mediathek und EPG in einer App', 'Auf mehreren Geräten und unterwegs nutzbar', 'Flexible Laufzeiten statt langer Verträge', 'Bild bis 4K bei ausreichender Bandbreite'],
            ['Abhängig von einer stabilen Internetleitung', 'WLAN-Störungen können Ruckler verursachen', 'Qualität unterscheidet sich stark zwischen Anbietern', 'Etwas Einrichtung beim ersten Start nötig'])
         + tip('Testen Sie IPTV vor dem Kauf auf genau dem Gerät, das Sie später nutzen möchten. Den <a href="/kostenlos-testen/">kostenlosen IPTV-Test</a> können Sie ohne Zahlungsdaten anfragen.')),
        ('rechtliches', 'Ist IPTV legal?', '''
<p>Die Technik IPTV ist in Deutschland selbstverständlich legal – auch die Fernsehangebote der großen Internetanbieter laufen per IPTV. Entscheidend ist bei jedem Dienst, ob er die Rechte an den angebotenen Programmen besitzt. Apps wie IPTV Smarters, TiviMate oder VLC sind reine Abspielprogramme und enthalten selbst keine Sender. Achten Sie bei jedem Anbieter auf ein vollständiges Impressum, nachvollziehbare Zahlungswege und erreichbaren Support. Worauf es bei der Auswahl sonst ankommt, lesen Sie im Ratgeber <a href="/iptv-anbieter/">IPTV-Anbieter finden</a>.</p>'''),
    ],
    faq=[
        ('Was bedeutet IPTV?', 'IPTV ist die Abkürzung für Internet Protocol Television, also Fernsehen über das Internet-Protokoll. Sender, Filme und Serien kommen als Datenstrom über Ihre Internetleitung statt über Kabel, Satellit oder Antenne.'),
        ('Brauche ich für IPTV einen speziellen Fernseher?', 'Nein. Jeder Smart-TV mit App-Store, ein Fire TV Stick, eine Android-Box, ein Smartphone, Tablet oder Computer reicht. Ältere Fernseher ohne Apps rüsten Sie mit einem günstigen Streaming-Stick nach.'),
        ('Wie schnell muss mein Internet für IPTV sein?', 'Für HD-Sender genügen etwa 10 Mbit/s, für Full HD rund 16 Mbit/s und für 4K mindestens 25 Mbit/s pro Gerät, das gleichzeitig schaut. Ein LAN-Kabel ist stabiler als WLAN.'),
        ('Was ist der Unterschied zwischen IPTV und Streaming?', 'Streaming-Dienste bieten meist nur Filme und Serien auf Abruf. IPTV liefert zusätzlich lineares Live-Fernsehen mit Programmführer, Catch-Up und Senderliste – also klassisches Fernsehen über das Internet.'),
        ('Funktioniert IPTV ohne Kabelanschluss?', 'Ja. IPTV braucht nur einen Internetzugang, egal ob DSL, Glasfaser, Kabelinternet oder Mobilfunk. Ein TV-Kabelanschluss oder eine Satellitenschüssel ist nicht nötig.'),
    ],
    related=['iptv-anbieter', 'iptv-geraete', 'iptv-apps', 'm3u-playlist', 'iptv-4k', 'iptv-telekom-vodafone'],
    card=('Was ist IPTV?', 'Internet Protocol Television einfach erklärt: Technik, Vorteile und Voraussetzungen.'),
))

# ---------------------------------------------------------------- IPTV kaufen
PAGES.append(dict(
    slug='iptv-kaufen', parent=None, kind='money',
    title='IPTV kaufen – Abo ab 9 €, ohne Vertrag | IPTV Kanal',
    description='IPTV kaufen ohne Vertrag: 20.000+ Sender, Filme & Serien in bis zu 4K. 1 bis 5 Geräte, 1 bis 12 Monate, keine automatische Verlängerung. Jetzt kostenlos testen.',
    eyebrow='IPTV ABO OHNE VERTRAG', h1='IPTV kaufen: Ihr Abo ohne Vertrag',
    lead='Einmal zahlen, sofort schauen: Bei IPTV Kanal kaufen Sie Ihr IPTV-Abo für 1, 3, 6 oder 12 Monate und 1 bis 5 Geräte – ohne automatische Verlängerung und ohne Kündigungsfrist.',
    answer='Bei IPTV Kanal kostet ein IPTV-Abo ab 9 € für einen Monat; das Jahrespaket für ein Gerät liegt bei 49 € (rund 4,08 € pro Monat). Sie zahlen einmalig, es gibt keine automatische Verlängerung. Enthalten sind 20.000+ Sender, Filme und Serien, 4K-Qualität, EPG mit Catch-Up und deutscher Support.',
    sections=[
        ('preise', 'Was kostet IPTV? Alle Preise im Überblick', '''
<p>Der Preis hängt von zwei Dingen ab: der Laufzeit und der Anzahl der Geräte, die <strong>gleichzeitig</strong> schauen. Je länger die Laufzeit, desto günstiger wird jeder Monat.</p>
''' + PRICE_TABLE + '''
<p>Alle Pakete enthalten dieselben Inhalte. Der Unterschied liegt allein in Laufzeit und gleichzeitigen Streams. Zum Bestellen wählen Sie Ihr Paket auf der <a href="/preise/">Preisseite</a> oder direkt: <a href="/bestellen/1-monat/">1 Monat</a>, <a href="/bestellen/3-monate/">3 Monate</a>, <a href="/bestellen/6-monate/">6 Monate</a> oder <a href="/bestellen/1-jahr/">IPTV 12 Monate</a>.</p>'''),
        ('enthalten', 'Das ist in jedem IPTV-Abo enthalten', checks(
            '20.000+ Live-Sender aus Deutschland, Europa und der Welt',
            'Filme und Serien auf Abruf (VOD)',
            'HD, Full HD und <a href="/iptv-4k/">4K Ultra HD</a> – je nach Sender',
            'Elektronischer Programmführer (EPG) und Catch-Up TV',
            'Zugangsdaten für alle gängigen <a href="/iptv-apps/">IPTV-Apps</a> und <a href="/iptv-geraete/">Geräte</a>',
            '24/7 deutschsprachiger Support, auch bei der Einrichtung')),
        ('ablauf', 'IPTV kaufen in drei Schritten', steps(
            '<b>Paket wählen:</b> Laufzeit und Geräteanzahl auf der <a href="/preise/">Preisseite</a> auswählen.',
            '<b>Anfrage senden:</b> Auf der Bestellseite Name, E-Mail oder WhatsApp angeben. Wir melden uns mit Zugangsdaten und Zahlungsinformationen.',
            '<b>Losschauen:</b> Zugangsdaten in Ihre App eintragen – zum Beispiel <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> oder <a href="/tivimate/">TiviMate</a>. Auf Wunsch helfen wir per WhatsApp.')),
        ('laufzeit', 'Welche Laufzeit lohnt sich?', '''
<p><strong>1 Monat</strong> eignet sich, wenn Sie nach dem <a href="/kostenlos-testen/">kostenlosen Test</a> noch etwas länger ausprobieren möchten oder nur für ein Turnier oder einen Urlaub schauen. <strong>3 und 6 Monate</strong> sind der Mittelweg. Das <strong>IPTV-Jahresabo (12 Monate)</strong> ist pro Monat am günstigsten: 49 € statt 108 € bei zwölf Einzelmonaten – Sie sparen 55 %.</p>
<p>Weil sich kein Paket automatisch verlängert, gehen Sie mit keiner Laufzeit ein Risiko ein. Sie entscheiden am Ende neu.</p>'''),
        ('worauf-achten', 'Worauf Sie beim IPTV-Kauf achten sollten', checks(
            '<strong>Testmöglichkeit:</strong> Seriöse Anbieter lassen Sie vorher testen.',
            '<strong>Keine Abofalle:</strong> klare Laufzeit ohne stillschweigende Verlängerung.',
            '<strong>Erreichbarer Support</strong> auf Deutsch – per E-Mail und WhatsApp.',
            '<strong>Ehrliche Angebote:</strong> „Lifetime IPTV“ für einmalig 30 € gibt es nicht dauerhaft; solche Dienste verschwinden oft nach wenigen Wochen.',
            '<strong>Transparente Geräteregeln:</strong> wie viele Streams gleichzeitig laufen dürfen.') + '''
<p>Eine ausführliche Checkliste finden Sie im <a href="/iptv-anbieter-vergleich/">IPTV-Anbieter-Vergleich</a>.</p>'''),
    ],
    faq=[
        ('Was kostet ein IPTV-Abo bei IPTV Kanal?', 'Ab 9 € für einen Monat und ein Gerät. 3 Monate kosten 29 €, 6 Monate 39 € und 12 Monate 49 €. Für bis zu 5 Geräte gleichzeitig gibt es eigene Pakete, zum Beispiel 89 € für ein Jahr mit 2 Geräten.'),
        ('Verlängert sich das IPTV-Abo automatisch?', 'Nein. Sie zahlen einmalig für die gewählte Laufzeit. Es gibt keine automatische Verlängerung und keine Kündigungsfrist.'),
        ('Kann ich IPTV vor dem Kauf testen?', 'Ja. Über die Seite Kostenlos testen fragen Sie einen kostenlosen Testzugang an – ohne Zahlungsdaten.'),
        ('Wie schnell bekomme ich nach dem Kauf meinen Zugang?', 'In der Regel erhalten Sie Ihre Zugangsdaten kurz nach der Bestellung per E-Mail oder WhatsApp und können sofort starten.'),
        ('Gibt es IPTV mit Lifetime-Zugang?', 'Wir bieten bewusst kein Lifetime-Paket an. Dauerhafter Betrieb von Servern kostet laufend Geld; einmalige Lifetime-Angebote sind deshalb meist nicht nachhaltig. Das Jahrespaket ist unsere günstigste Option.'),
        ('Auf welchen Geräten funktioniert das IPTV-Abo?', 'Auf Smart-TVs von Samsung und LG, Fire TV Stick, Android-TV-Boxen, MAG-Boxen, Apple TV, iPhone, iPad, Android-Smartphones sowie PC und Mac.'),
    ],
    related=['iptv-anbieter-vergleich', 'iptv-4k', 'iptv-fire-tv-stick', 'iptv-smarters-pro', 'was-ist-iptv', 'iptv-geraete'],
    card=('IPTV kaufen', 'Alle Pakete, Preise und Laufzeiten – ohne Vertrag und ohne Verlängerung.'),
    pricing=True,
))

# ---------------------------------------------------------------- IPTV Anbieter
PAGES.append(dict(
    slug='iptv-anbieter', parent='ratgeber', kind='guide',
    title='IPTV Anbieter in Deutschland: So finden Sie einen guten',
    description='IPTV Anbieter in Deutschland: Welche Arten es gibt, woran Sie einen seriösen IPTV Provider erkennen und welche Fragen Sie vor dem Kauf stellen sollten.',
    eyebrow='IPTV PROVIDER', h1='IPTV Anbieter in Deutschland',
    lead='Internetanbieter, TV-Streaming-Apps oder unabhängige IPTV-Dienste: Wir erklären, welche Arten von IPTV Anbietern es gibt und woran Sie einen guten erkennen.',
    answer='In Deutschland gibt es drei Arten von IPTV Anbietern: Internetprovider mit eigenem TV (z. B. MagentaTV), TV-Streaming-Apps für frei empfangbare Sender und unabhängige IPTV-Dienste mit Zugangsdaten für beliebige Apps. Einen guten Anbieter erkennen Sie an Testzugang, stabilen Servern, klaren Laufzeiten ohne Abofalle und erreichbarem deutschem Support.',
    sections=[
        ('arten', 'Drei Arten von IPTV Anbietern', '''
<h3>1. Internetanbieter mit TV-Paket</h3>
<p>Telekom, Vodafone, 1&amp;1 und o2 bieten Fernsehen zum Internetanschluss an. Vorteil: alles aus einer Hand. Nachteil: meist an Vertrag, Laufzeit und eigenen Receiver gebunden. Mehr dazu im Ratgeber <a href="/iptv-telekom-vodafone/">IPTV bei Telekom, Vodafone, 1&amp;1 und o2</a>.</p>
<h3>2. TV-Streaming-Apps</h3>
<p>Apps mit deutschen Free-TV-Sendern, oft mit monatlichem Abo und eigener App. Sie funktionieren unabhängig vom Internetanbieter, sind aber auf die eigene App beschränkt.</p>
<h3>3. Unabhängige IPTV-Dienste</h3>
<p>Dienste wie <a href="/">IPTV Kanal</a> liefern Zugangsdaten (Xtream Codes, M3U oder MAG-Portal), die Sie in eine App Ihrer Wahl eintragen. Vorteil: große Senderauswahl, VOD, flexible Laufzeiten und freie Wahl von <a href="/iptv-geraete/">Gerät</a> und <a href="/iptv-apps/">App</a>.</p>'''),
        ('kriterien', 'Woran Sie einen guten IPTV Provider erkennen', table(['Kriterium', 'Darauf achten', 'Warnsignal'], [
            ['Test', 'Kostenloser Testzugang vor dem Kauf', 'Nur Vorkasse, kein Test'],
            ['Laufzeit', 'Feste Laufzeit, keine Verlängerung', 'Abo verlängert sich stillschweigend'],
            ['Support', 'Deutsch, per E-Mail/WhatsApp erreichbar', 'Nur Telegram-Bot oder gar kein Kontakt'],
            ['Stabilität', 'Wenig Puffern auch zu Spitzenzeiten', 'Ausfälle bei großen Live-Events'],
            ['Geräte', 'Klare Regel für gleichzeitige Streams', 'Unklare oder wechselnde Regeln'],
            ['Preis', 'Realistisch und transparent', '„Lifetime“ für einmalig wenige Euro'],
        ], 'Kriterien für die Auswahl eines IPTV Anbieters')),
        ('fragen', 'Fünf Fragen an jeden IPTV Anbieter', steps(
            'Kann ich vorher kostenlos testen – auf meinem eigenen Gerät?',
            'Wie viele Geräte dürfen gleichzeitig schauen, und was kostet ein zweites Gerät?',
            'Verlängert sich das Abo automatisch?',
            'Welche Apps und Geräte werden unterstützt (Fire TV, Samsung, LG, MAG, Apple)?',
            'Wie erreiche ich den Support, wenn am Samstagabend etwas nicht läuft?') + '''
<p>Bei IPTV Kanal lauten die Antworten: ja, <a href="/kostenlos-testen/">kostenloser Test</a>; 1 bis 5 Geräte mit festen <a href="/iptv-kaufen/">Paketpreisen</a>; keine Verlängerung; alle gängigen Geräte; Support per E-Mail und WhatsApp.</p>'''),
        ('reseller', 'IPTV Reseller und Wiederverkäufer', '''
<p>Viele Angebote im Netz stammen von Wiederverkäufern (Resellern), die Zugänge eines größeren Dienstes weiterverkaufen. Das ist nicht automatisch schlecht – problematisch wird es, wenn der Reseller keinen eigenen Support leistet oder plötzlich verschwindet. Fragen Sie deshalb immer nach Kontaktwegen und testen Sie zuerst.</p>'''),
    ],
    faq=[
        ('Welcher IPTV Anbieter ist der beste in Deutschland?', 'Den einen besten Anbieter für alle gibt es nicht. Wichtig sind ein Testzugang, stabile Streams zu Spitzenzeiten, deutscher Support, klare Preise und eine Laufzeit ohne automatische Verlängerung. Unser IPTV-Anbieter-Vergleich zeigt die Kriterien im Detail.'),
        ('Was kostet ein IPTV Anbieter im Monat?', 'Bei IPTV Kanal ab 9 € für einen Monat oder umgerechnet rund 4,08 € pro Monat im Jahrespaket. TV-Pakete von Internetanbietern kosten zusätzlich zum Internetvertrag.'),
        ('Brauche ich für einen IPTV Anbieter einen bestimmten Internetanschluss?', 'Unabhängige IPTV-Dienste funktionieren mit jedem Internetanschluss. Nur das TV-Angebot eines Internetanbieters setzt meist dessen eigenen Anschluss voraus.'),
        ('Wie erkenne ich unseriöse IPTV Anbieter?', 'Typische Warnsignale sind fehlender Testzugang, kein erreichbarer Kontakt, ungewöhnliche Zahlungswege ohne Beleg, unrealistische Lifetime-Angebote und Abos, die sich stillschweigend verlängern.'),
    ],
    related=['iptv-anbieter-vergleich', 'iptv-kaufen', 'was-ist-iptv', 'iptv-telekom-vodafone', 'iptv-apps', 'iptv-geraete'],
    card=('IPTV Anbieter finden', 'Arten von Anbietern, Kriterien und Fragen vor dem Kauf.'),
))

# ---------------------------------------------------------------- Vergleich / beste
PAGES.append(dict(
    slug='iptv-anbieter-vergleich', parent='ratgeber', kind='guide',
    title='IPTV Anbieter Vergleich 2026: Bester IPTV Anbieter finden',
    description='IPTV Anbieter Vergleich 2026: 8 Kriterien, Bewertungsmatrix und Tipps aus Foren und Reddit, mit denen Sie den besten IPTV Anbieter für sich finden.',
    eyebrow='VERGLEICH 2026', h1='IPTV Anbieter Vergleich 2026',
    lead='Was macht den besten IPTV Anbieter aus? Statt Werbeversprechen geben wir Ihnen eine Bewertungsmatrix, mit der Sie jeden Dienst selbst vergleichen können – auch uns.',
    answer='Den besten IPTV Anbieter erkennen Sie nicht an der Senderzahl, sondern an Stabilität zur Hauptsendezeit, Testzugang, deutscher Erreichbarkeit, klarer Laufzeit ohne Verlängerung und Kompatibilität mit Ihren Geräten. Bewerten Sie jeden Anbieter mit den acht Kriterien unten und testen Sie mindestens einen Abend lang.',
    sections=[
        ('methode', 'So vergleichen Sie IPTV Anbieter richtig', '''
<p>Vergleichsseiten mit „Testsieger“-Siegeln sind oft selbst Werbung. Belastbarer ist ein eigener Test über 24 Stunden mit festen Kriterien. Vergeben Sie für jedes Kriterium 0 bis 2 Punkte; ein guter Anbieter erreicht mindestens 12 von 16 Punkten.</p>
''' + table(['Kriterium', '0 Punkte', '2 Punkte'], [
            ['Stabilität am Abend', 'Puffern bei Live-Sport', 'Flüssig auch 20–23 Uhr'],
            ['Umschaltzeit', 'über 5 Sekunden', 'unter 2 Sekunden'],
            ['EPG &amp; Catch-Up', 'fehlt oder falsch', 'vollständig und korrekt'],
            ['Bildqualität', 'nur SD/HD', 'Full HD und 4K'],
            ['Geräte &amp; Apps', 'nur eine App', 'alle gängigen Apps und Geräte'],
            ['Support', 'keine Antwort', 'Antwort in Minuten auf Deutsch'],
            ['Preis &amp; Laufzeit', 'Auto-Verlängerung', 'klarer Festpreis'],
            ['Test', 'kein Test', 'kostenloser Test'],
        ], 'Bewertungsmatrix für IPTV Anbieter')),
        ('ablauf-test', 'Der 24-Stunden-Test in der Praxis', steps(
            'Testzugang auf Ihrem Hauptgerät einrichten, zum Beispiel <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> oder <a href="/iptv-samsung-tv/">Samsung TV</a>.',
            'Abends zur Hauptsendezeit 30 Minuten Live-Sport schauen – das ist die härteste Probe.',
            'Zehnmal zwischen Sendern umschalten und die Zeit stoppen.',
            'Programmführer prüfen: Stimmen Sendung und Uhrzeit?',
            'Eine Frage an den Support schicken und die Antwortzeit notieren.',
            'Bei 4K: Bandbreite mit dem Speedtest gegenprüfen (siehe <a href="/iptv-4k/">IPTV 4K</a>).')),
        ('foren', 'Was Reddit, Foren und Bewertungsportale verraten', '''
<p>In Diskussionen auf Reddit, in IPTV-Foren und auf Bewertungsportalen wie Trustpilot tauchen immer dieselben Muster auf: Nutzer loben Anbieter mit schnellem Support und stabilen Abenden, und sie warnen vor Diensten, die nach Zahlung nicht mehr antworten. Drei Tipps zum Lesen:</p>
''' + checks(
            'Achten Sie auf Bewertungen über mehrere Monate statt auf Wellen am selben Tag.',
            'Negative Bewertungen sind wertvoll: Wie hat der Anbieter reagiert?',
            'Konkrete Gerätenamen und Situationen („Fire TV, Bundesliga-Samstag“) sind glaubwürdiger als allgemeines Lob.') + '''
<p>Unsere eigenen Kundenstimmen von Trustpilot, Google und WhatsApp finden Sie auf der <a href="/#bewertungen">Startseite</a>.</p>'''),
        ('player', 'Bester IPTV Player: die App zählt mit', '''
<p>Ein guter Anbieter wirkt nur so gut wie die App, mit der Sie schauen. Für Android-TV und Fire TV ist <a href="/tivimate/">TiviMate</a> beliebt, für den Einstieg auf fast allen Geräten <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>, für Samsung und LG Fernseher Player wie <a href="/smart-iptv/">Smart IPTV</a>, <a href="/set-iptv/">SET IPTV</a> oder <a href="/flix-iptv/">Flix IPTV</a>. Die komplette Übersicht steht unter <a href="/iptv-apps/">beste IPTV Apps</a>.</p>'''),
        ('unser-angebot', 'Wie schneidet IPTV Kanal ab?', '''
<p>Wir laden Sie ein, uns mit genau dieser Matrix zu prüfen: Testzugang kostenlos, Laufzeit ohne Verlängerung, Pakete für 1 bis 5 Geräte, 4K-Sender, EPG mit Catch-Up und Support auf Deutsch. Starten Sie mit dem <a href="/kostenlos-testen/">kostenlosen Test</a> und vergleichen Sie danach in Ruhe die <a href="/iptv-kaufen/">Preise</a>.</p>'''),
    ],
    faq=[
        ('Welcher ist der beste IPTV Anbieter 2026?', 'Das hängt von Ihren Geräten und Sehgewohnheiten ab. Gute Anbieter erreichen in unserer Bewertungsmatrix mindestens 12 von 16 Punkten: stabil zur Hauptsendezeit, schneller Senderwechsel, korrektes EPG, 4K, deutscher Support und kein Abo mit automatischer Verlängerung.'),
        ('Kann ich Reddit-Empfehlungen für IPTV trauen?', 'Reddit und Foren sind gute Hinweisgeber für Probleme wie Ausfälle oder fehlenden Support. Empfehlungen sollten Sie trotzdem selbst mit einem kostenlosen Test prüfen, da sich Qualität schnell ändern kann.'),
        ('Wie lange sollte ich einen IPTV Anbieter testen?', 'Mindestens einen Abend zur Hauptsendezeit, idealerweise 24 Stunden. Live-Sport am Wochenende ist der härteste und aussagekräftigste Test.'),
        ('Ist ein teurer IPTV Anbieter automatisch besser?', 'Nein. Entscheidend sind Stabilität, Support und Laufzeitbedingungen. Ein fairer Jahrespreis mit Testmöglichkeit ist oft die bessere Wahl als ein teures Monatsabo.'),
    ],
    related=['iptv-anbieter', 'iptv-kaufen', 'iptv-apps', 'iptv-4k', 'tivimate', 'iptv-smarters-pro'],
    card=('IPTV Anbieter Vergleich', 'Bewertungsmatrix mit 8 Kriterien für den besten IPTV Anbieter.'),
))

# ---------------------------------------------------------------- 4K
PAGES.append(dict(
    slug='iptv-4k', parent='ratgeber', kind='guide',
    title='IPTV 4K: Premium IPTV in Ultra HD – Bandbreite & Geräte',
    description='IPTV in 4K Ultra HD: Wie viel Internet Sie brauchen, welche Geräte und Apps 4K können und warum 8K-IPTV meist ein Werbeversprechen ist. Mit Bandbreiten-Tabelle.',
    eyebrow='ULTRA HD', h1='IPTV in 4K: Premium IPTV in Ultra HD',
    lead='4K-IPTV zeigt viermal so viele Bildpunkte wie Full HD. Damit das Bild wirklich scharf und flüssig ankommt, müssen Leitung, Gerät und App zusammenpassen.',
    answer='Für IPTV in 4K brauchen Sie mindestens 25 Mbit/s pro Gerät, ein 4K-fähiges Abspielgerät mit HEVC-Decoder (z. B. Fire TV Stick 4K, aktuelle Smart-TVs, Apple TV 4K) und eine App, die 4K-Streams unterstützt. Ein LAN-Kabel oder WLAN mit 5 GHz verhindert Ruckler. Bei IPTV Kanal ist 4K in jedem Paket enthalten.',
    sections=[
        ('bandbreite', 'Wie viel Internet braucht IPTV in 4K?', table(['Qualität', 'Auflösung', 'Empfohlen pro Gerät', 'Datenverbrauch pro Stunde (ca.)'], [
            ['SD', '720 × 576', '5 Mbit/s', '1–1,5 GB'],
            ['HD', '1280 × 720', '10 Mbit/s', '2–3 GB'],
            ['Full HD', '1920 × 1080', '16 Mbit/s', '3–4 GB'],
            ['4K Ultra HD', '3840 × 2160', '25 Mbit/s', '7–10 GB'],
        ], 'Bandbreite für IPTV nach Bildqualität') + '''
<p>Die Werte gelten <strong>pro gleichzeitigem Stream</strong>. Schauen zwei Personen in 4K, sollten 50 Mbit/s frei sein – plus Reserve für andere Geräte im Haushalt. Messen Sie die Geschwindigkeit am Fernseher selbst, nicht am Handy neben dem Router.</p>'''),
        ('geraete', 'Welche Geräte können 4K-IPTV?', checks(
            '<a href="/iptv-fire-tv-stick/">Fire TV Stick 4K und 4K Max</a> – günstigster Weg zu 4K am Fernseher',
            '<a href="/iptv-samsung-tv/">Samsung</a> und <a href="/iptv-lg-tv/">LG</a> Smart-TVs ab etwa Baujahr 2018',
            '<a href="/iptv-box/">Android-TV-Boxen</a> wie Nvidia Shield, Formuler oder Homatics',
            '<a href="/iptv-apple-tv-iphone/">Apple TV 4K</a>',
            '<a href="/mag-box-iptv/">MAG-Boxen</a> der 4K-Serie wie MAG 524 und MAG 424') + tip('Der Stick muss in einem HDMI-Anschluss stecken, der 4K mit HDCP 2.2 unterstützt. Bei manchen Fernsehern ist das nur HDMI 1 oder 2.')),
        ('apps', 'Die richtige App für 4K', '''
<p>Nicht jede App spielt HEVC-Streams gleich gut ab. Auf Android-TV und Fire TV liefern <a href="/tivimate/">TiviMate</a> und <a href="/iptv-smarters-pro/">IPTV Smarters Pro</a> mit Hardware-Decoder die besten Ergebnisse. Auf Samsung und LG nutzen Sie Player wie <a href="/set-iptv/">SET IPTV</a> oder <a href="/flix-iptv/">Flix IPTV</a>. Am PC ist <a href="/iptv-pc-mac/">VLC</a> eine zuverlässige Wahl.</p>'''),
        ('8k', '8K- und 12K-IPTV: was dahintersteckt', '''
<p>Angebote mit „IPTV 8K“ oder gar „12K“ sind fast immer Marketing. Es gibt praktisch keine regulären Fernsehsender in 8K, und 12K existiert als Sendeformat nicht. Achten Sie lieber darauf, ob echte 4K-Sender und stabile Full-HD-Streams dabei sind.</p>'''),
        ('ruckeln', 'Wenn 4K ruckelt: schnelle Lösungen', steps(
            'Gerät per LAN-Kabel anschließen oder ins 5-GHz-WLAN wechseln.',
            'Andere Downloads und Streams im Haushalt pausieren.',
            'In der App den Hardware-Decoder aktivieren.',
            'Testweise die Full-HD-Version des Senders öffnen.',
            'Router und Stick einmal neu starten.')),
    ],
    faq=[
        ('Wie viel Mbit/s brauche ich für IPTV in 4K?', 'Mindestens 25 Mbit/s pro Gerät, das gleichzeitig in 4K schaut. Für zwei 4K-Streams sollten Sie mit 50 Mbit/s plus Reserve rechnen.'),
        ('Ist 4K bei IPTV Kanal im Preis enthalten?', 'Ja. 4K Ultra HD ist in allen Paketen enthalten, unabhängig von Laufzeit und Geräteanzahl. Welche Sender in 4K verfügbar sind, sehen Sie in der Senderliste Ihrer App.'),
        ('Warum ruckelt mein 4K-IPTV über WLAN?', 'WLAN-Signale schwanken durch Wände und Nachbarnetze. Ein LAN-Kabel, ein 5-GHz-Netz oder ein Mesh-Repeater in der Nähe des Fernsehers löst das Problem meist.'),
        ('Gibt es echtes 8K-IPTV?', 'Praktisch nein. Reguläre Fernsehsender senden nicht in 8K. Angebote mit 8K oder 12K im Namen sind in der Regel Werbebegriffe.'),
    ],
    related=['iptv-fire-tv-stick', 'iptv-box', 'iptv-kaufen', 'iptv-samsung-tv', 'tivimate', 'iptv-anbieter-vergleich'],
    card=('IPTV in 4K', 'Bandbreite, Geräte und Apps für Ultra HD – mit Tabelle.'),
))

# ---------------------------------------------------------------- ISP IPTV
PAGES.append(dict(
    slug='iptv-telekom-vodafone', parent='ratgeber', kind='guide',
    title='Fernsehen über Telekom, Vodafone, 1&1 & o2: IPTV erklärt',
    description='Fernsehen über Telekom (MagentaTV), Vodafone, 1&1 und o2: Wie das IPTV der Internetanbieter funktioniert, was Sie brauchen und welche Alternative ohne Vertrag es gibt.',
    eyebrow='IPTV DER INTERNETANBIETER', h1='Fernsehen über Telekom, Vodafone, 1&amp;1 und o2',
    lead='Die großen Internetanbieter verkaufen Fernsehen per IPTV als Zusatz zum Anschluss. Wir erklären, wie das funktioniert – und wann eine unabhängige Lösung besser passt.',
    answer='Telekom (MagentaTV), Vodafone, 1&1 und o2 bieten Fernsehen über die Internetleitung als Zusatzpaket an. Es läuft über eigene Receiver oder Apps und ist meist an einen Vertrag mit Mindestlaufzeit gekoppelt. Unabhängiges IPTV funktioniert dagegen mit jedem Anschluss und jeder Laufzeit.',
    sections=[
        ('telekom', 'Fernsehen über Telekom: MagentaTV', '''
<p>Die Telekom nennt ihr Fernsehangebot <strong>MagentaTV</strong>. Auf Telekom-Anschlüssen kann das Signal besonders effizient (per Multicast) über die eigene Leitung kommen; zusätzlich gibt es die MagentaTV-App für Smart-TVs, Streaming-Sticks und Smartphones. Je nach Tarif kommen Senderpakete und Mediatheken hinzu. Die aktuellen Tarife und Laufzeiten stehen direkt bei der Telekom.</p>'''),
        ('vodafone', 'Vodafone IPTV und Vodafone TV', '''
<p>Vodafone ist in Deutschland vor allem als Kabelnetzbetreiber bekannt. Zusätzlich bietet Vodafone TV-Produkte über App und Receiver an, die auch über DSL oder Glasfaser genutzt werden können. Wie bei der Telekom hängen Umfang und Preis vom gebuchten Tarif ab.</p>'''),
        ('1und1-o2', '1&amp;1 TV-Pakete und o2 TV', '''
<p>Auch 1&amp;1 und o2 bieten Fernsehpakete zu ihren Internet- oder Mobilfunktarifen an. Diese laufen über Apps auf Smart-TV, Stick oder Smartphone und setzen auf die Technik von TV-Streaming-Plattformen. Die Senderauswahl orientiert sich meist an deutschen Free- und Pay-TV-Programmen.</p>'''),
        ('vergleich', 'Provider-TV oder unabhängiges IPTV?', table(['', 'TV vom Internetanbieter', 'Unabhängiges IPTV (z. B. IPTV Kanal)'], [
            ['Anschluss', 'Meist nur mit eigenem Internetvertrag', 'Jeder Anschluss, auch Mobilfunk'],
            ['Vertrag', 'Oft mit Mindestlaufzeit', '1–12 Monate, keine Verlängerung'],
            ['Geräte', 'Eigener Receiver oder eigene App', 'Freie Wahl von Gerät und App'],
            ['Senderumfang', 'Deutsche Sender, Zusatzpakete', '20.000+ Sender, Filme und Serien'],
            ['Umzug / Anbieterwechsel', 'TV hängt am Anschluss', 'Zugang bleibt unverändert'],
        ], 'Vergleich von Provider-TV und unabhängigem IPTV') + '''
<p>Wer Provider-TV und Internet aus einer Hand möchte, ist bei seinem Internetanbieter gut aufgehoben. Wer flexibel bleiben will, ohne Vertragsbindung und mit freier Gerätewahl, fährt mit unabhängigem IPTV besser. Was IPTV technisch bedeutet, erklärt der Ratgeber <a href="/was-ist-iptv/">Was ist IPTV?</a>.</p>'''),
        ('wechsel', 'Vom Provider-TV wechseln: so geht es', steps(
            'Prüfen, wann Ihr TV-Zusatzpaket kündbar ist – oft unabhängig vom Internetvertrag.',
            'Unabhängiges IPTV parallel <a href="/kostenlos-testen/">kostenlos testen</a>.',
            'Passende App auf dem Fernseher installieren, z. B. auf <a href="/iptv-samsung-tv/">Samsung</a>, <a href="/iptv-lg-tv/">LG</a> oder dem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>.',
            'Erst nach erfolgreichem Test das alte TV-Paket kündigen und den Receiver zurückgeben.')),
    ],
    faq=[
        ('Ist MagentaTV IPTV?', 'Ja. MagentaTV der Telekom überträgt Fernsehen über das Internet-Protokoll, also per IPTV – entweder über den Telekom-Anschluss mit Receiver oder als App.'),
        ('Kann ich IPTV ohne Telekom- oder Vodafone-Vertrag nutzen?', 'Ja. Unabhängige IPTV-Dienste wie IPTV Kanal funktionieren mit jedem Internetanschluss, egal bei welchem Anbieter, und benötigen keinen zusätzlichen TV-Vertrag.'),
        ('Brauche ich für IPTV einen Receiver vom Anbieter?', 'Für Provider-TV oft ja. Für unabhängiges IPTV reicht ein Smart-TV, Fire TV Stick, eine Android-Box oder ein Smartphone mit passender App.'),
        ('Was sind die 1&1 TV-Pakete?', '1&1 bietet Fernsehpakete als Zusatz zu seinen Tarifen an, die per App auf Smart-TV, Stick oder Smartphone laufen. Aktuelle Inhalte und Preise nennt 1&1 auf der eigenen Website.'),
    ],
    related=['was-ist-iptv', 'iptv-anbieter', 'iptv-kaufen', 'iptv-smart-tv', 'iptv-fire-tv-stick', 'iptv-anbieter-vergleich'],
    card=('IPTV bei Telekom & Vodafone', 'MagentaTV, Vodafone, 1&1 und o2 – und die Alternative ohne Vertrag.'),
))

# ---------------------------------------------------------------- M3U
PAGES.append(dict(
    slug='m3u-playlist', parent='ratgeber', kind='guide',
    title='M3U Playlist & IPTV M3U Liste: Anleitung (Deutsch)',
    description='Was ist eine M3U Playlist? So laden Sie eine IPTV M3U Liste in VLC, Smarters, TiviMate & Smart IPTV, prüfen M3U8-Links und vermeiden unsichere Gratis-Listen.',
    eyebrow='M3U & M3U8', h1='M3U Playlist: IPTV-Listen verstehen und nutzen',
    lead='Die M3U-Datei ist das Rückgrat vieler IPTV-Apps. Wir zeigen, was in einer IPTV M3U Liste steckt, wie Sie sie laden und warum „beste M3U Liste deutsch gratis“ selten hält, was sie verspricht.',
    answer='Eine M3U Playlist ist eine Textdatei oder ein Link mit einer Liste von Streamadressen; jede Zeile steht für einen Sender oder Film. IPTV-Apps wie VLC, IPTV Smarters, TiviMate oder Smart IPTV lesen die Liste ein und zeigen daraus Ihre Senderliste. M3U8 ist dieselbe Liste in UTF-8 und wird auch für HLS-Streams genutzt.',
    sections=[
        ('aufbau', 'So ist eine M3U-Datei aufgebaut', '''
<p>Eine IPTV M3U Liste beginnt mit <code>#EXTM3U</code>. Danach folgt für jeden Sender eine Infozeile und die Streamadresse:</p>
<p><code>#EXTINF:-1 tvg-id="sender.de" tvg-logo="logo.png" group-title="Deutschland",Sendername</code><br><code>http://server.beispiel:8080/benutzer/passwort/12345</code></p>
<p><code>tvg-id</code> verknüpft den Sender mit dem Programmführer (EPG), <code>group-title</code> sortiert ihn in eine Kategorie, <code>tvg-logo</code> liefert das Senderlogo. Mit diesen drei Feldern entsteht in der App die übersichtliche Senderliste.</p>'''),
        ('m3u-m3u8', 'M3U, M3U8 und Xtream Codes im Vergleich', table(['Format', 'Was es ist', 'Typische Apps'], [
            ['M3U', 'Playlist als Datei oder Link', 'VLC, Smart IPTV, SS IPTV, Kodi'],
            ['M3U8', 'M3U in UTF-8, auch HLS-Streamformat', 'Browser, VLC, Apple-Geräte'],
            ['Xtream Codes', 'Login mit Server, Benutzer, Passwort', 'IPTV Smarters, TiviMate, XCIPTV'],
            ['MAG-Portal', 'Portal-URL, Freischaltung per MAC', 'MAG-Box, STBEmu'],
        ], 'IPTV-Formate im Vergleich') + '''
<p>Xtream Codes lädt zusätzlich Mediathek und EPG automatisch – mehr dazu unter <a href="/xtream-codes-iptv/">Xtream Codes IPTV</a>.</p>'''),
        ('laden', 'M3U Playlist laden: Anleitungen nach App', '''
<h3>VLC (PC, Mac, Handy)</h3>
<p>Medien → Netzwerkstream öffnen → M3U-Link einfügen → Wiedergabe. Details im Ratgeber <a href="/iptv-pc-mac/">IPTV am PC mit VLC</a>.</p>
<h3>IPTV Smarters Pro</h3>
<p>Neuen Nutzer hinzufügen → „M3U-URL laden“ → Name und Link eintragen. Siehe <a href="/iptv-smarters-pro/">IPTV Smarters Pro Anleitung</a>.</p>
<h3>TiviMate</h3>
<p>Playlist hinzufügen → „M3U-Playlist“ → URL eingeben → EPG-Quelle prüfen. Siehe <a href="/tivimate/">TiviMate einrichten</a>.</p>
<h3>Smart IPTV und SS IPTV (Samsung, LG)</h3>
<p>Die Liste wird über die Website des App-Entwicklers mit der MAC-Adresse oder einem Verbindungscode des Fernsehers verknüpft. Anleitungen: <a href="/smart-iptv/">Smart IPTV</a> und <a href="/ss-iptv/">SS IPTV</a>.</p>'''),
        ('gratis', 'Kostenlose M3U Listen: warum sie selten funktionieren', '''
<p>Suchanfragen wie „IPTV M3U Playlist deutsch“ oder „beste M3U Liste“ führen oft zu öffentlich geteilten Listen. Die Probleme sind immer dieselben:</p>
''' + checks(
            'Die Links sind nach Stunden oder Tagen tot.',
            'Viele Sender sind falsch beschriftet, ohne EPG und in schlechter Qualität.',
            'Öffentlich geteilte Listen stammen oft aus fremden, missbrauchten Zugängen.',
            'Downloads aus dubiosen Quellen können Schadsoftware enthalten.') + '''
<p>Seriöse Alternative: Deutsche Sender der öffentlich-rechtlichen Mediatheken sind frei im Netz verfügbar, und für ein vollständiges Angebot mit EPG und Support gibt es eine persönliche M3U-Liste im <a href="/iptv-kaufen/">IPTV-Abo</a> – vorher <a href="/kostenlos-testen/">kostenlos testbar</a>.</p>'''),
        ('checker', 'M3U-Liste prüfen: IPTV Checker & M3U online', '''
<p>Ob ein M3U-Link funktioniert, sehen Sie am schnellsten in VLC: Lädt die Senderliste und startet ein Sender, ist die Liste aktiv. Online-Tools („IPTV Checker online“) testen viele Streams auf einmal, sehen dafür aber Ihre Zugangsdaten. Geben Sie persönliche Listen deshalb nicht in fremde Websites ein.</p>'''),
    ],
    faq=[
        ('Was ist eine M3U Playlist?', 'Eine M3U Playlist ist eine Textliste mit Streamadressen. IPTV-Apps lesen sie ein und erzeugen daraus Ihre Senderliste mit Kategorien, Logos und Programmführer.'),
        ('Was ist der Unterschied zwischen M3U und M3U8?', 'M3U8 ist eine M3U-Datei mit UTF-8-Zeichenkodierung, wodurch Umlaute korrekt angezeigt werden. Zusätzlich verwendet das Streamingformat HLS Dateien mit der Endung M3U8.'),
        ('Wo bekomme ich eine funktionierende M3U Liste auf Deutsch?', 'Eine stabile, persönliche M3U-Liste erhalten Sie mit einem IPTV-Abo. Öffentliche Gratis-Listen sind meist nach kurzer Zeit offline, unvollständig und oft nicht rechtmäßig.'),
        ('Wie öffne ich eine M3U-Datei?', 'Am einfachsten mit VLC: Datei per Drag-and-drop öffnen oder den Link unter Netzwerkstream öffnen einfügen. Auf dem Fernseher nutzen Sie eine IPTV-App wie IPTV Smarters, TiviMate oder Smart IPTV.'),
        ('Kann ich eine M3U Liste online prüfen?', 'Ja, mit IPTV-Checker-Tools. Persönliche Listen enthalten aber Ihre Zugangsdaten – testen Sie diese besser lokal in VLC.'),
    ],
    related=['xtream-codes-iptv', 'iptv-smarters-pro', 'tivimate', 'smart-iptv', 'iptv-pc-mac', 'iptv-kaufen'],
    card=('M3U Playlist', 'IPTV M3U Listen verstehen, laden und prüfen.'),
))
