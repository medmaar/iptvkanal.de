"""City and region pages (keyword round 4, 24.11.2026).

One page per city and per region/state cluster: IPTV [Ort], IPTV kaufen/Anbieter/Abo/Test [Ort] and
"IPTV Deutschland [Ort]" are answered on the same page. Berlin, Hamburg and Bremen are both city and federal
state; their state keywords are covered on the city page instead of a second, near-identical page.
The facts per place live in data_local.py; the wording below is varied per page so pages stay distinct.
"""
import zlib

from .data_local import STATES, CITIES, REGIONS, BROADCASTER_SHOW, NATIONAL_ISP, NOMINATIVE
from .helpers import steps, checks, tip, table, chips
from .content_local_unique import CITY as LOCAL_CITY, REGION as LOCAL_REGION
from .content_audit import BROADCASTER_URL, LOCAL_SOURCES

PAGES = []

CITY = {c['k']: c for c in CITIES}
REGION = {r['k']: r for r in REGIONS}


def city_slug(c):
    return 'iptv-' + c['k']


def region_slug(r):
    if r['kind'] == 'state':
        return STATES[r['st']][1]
    return {'rheinmain': 'iptv-rhein-main', 'rheinneckar': 'iptv-rhein-neckar', 'rheinruhr': 'iptv-rhein-ruhr',
            'stuttgartmetro': 'iptv-metropolregion-stuttgart', 'heide': 'iptv-lueneburger-heide',
            'bergisch': 'iptv-bergisches-land', 'owl': 'iptv-ostwestfalen-lippe', 'hunsrueck': 'iptv-hunsrueck',
            'muensterland': 'iptv-muensterland', 'allgaeu': 'iptv-allgaeu'}.get(r['k'], 'iptv-' + r['k'])


def pick(key, options, salt=''):
    return options[zlib.crc32((key + salt).encode()) % len(options)]


def rotate(key, options, salt=''):
    """All options, starting with the one pick() would choose, so fit() prefers the varied choice."""
    i = zlib.crc32((key + salt).encode()) % len(options)
    return options[i:] + options[:i]


def fit(candidates, lo, hi):
    """First candidate whose length lies in [lo, hi]; else the closest one."""
    for c in candidates:
        if lo <= len(c) <= hi:
            return c
    return min(candidates, key=lambda c: abs(len(c) - (lo + hi) / 2))


def join_names(items):
    items = list(items)
    if len(items) <= 1:
        return ''.join(items)
    return ', '.join(items[:-1]) + ' und ' + items[-1]


def link_city(k):
    c = CITY[k]
    return f'<a href="/{city_slug(c)}/">{c["n"]}</a>'


def link_region(k):
    r = REGION[k]
    return f'<a href="/{region_slug(r)}/">{r["n"]}</a>'


def state_link(st):
    name, slug, prep, _ = STATES[st]
    return f'<a href="/{slug}/">{name}</a>' if slug else name


SPEED_TABLE = table(['Bildqualität', 'Empfohlene Bandbreite', 'Typisch für'], [
    ['SD', '3–5 Mbit/s', 'Schwache Leitung, Smartphone unterwegs'],
    ['HD (720p)', '6–10 Mbit/s', 'DSL 16, LTE-Router'],
    ['Full HD (1080p)', 'ab 16 Mbit/s', 'DSL 50, Kabel, Glasfaser'],
    ['4K / UHD', 'ab 25 Mbit/s', 'VDSL 100, Kabel, Glasfaser'],
], 'Bandbreite für IPTV nach Bildqualität')

DEVICE_CHECKS = checks(
    '<strong><a href="/iptv-fire-tv-stick/">Fire TV Stick</a>:</strong> günstig, an jeden HDMI-Fernseher anschließbar, mit TiviMate oder IPTV Smarters Pro.',
    '<strong><a href="/iptv-samsung-tv/">Samsung</a> und <a href="/iptv-lg-tv/">LG</a>:</strong> direkt mit einer Smart-TV-App wie SET IPTV oder Flix IPTV, ohne Zusatzgerät.',
    '<strong><a href="/iptv-google-tv/">Google TV</a> und <a href="/iptv-box/">Android-TV-Boxen</a>:</strong> volle App-Auswahl aus dem Play Store.',
    '<strong><a href="/iptv-apple-tv/">Apple TV</a>, iPhone und iPad:</strong> mit Apps wie IPTVX oder iPlayTV aus dem App Store.',
    '<strong><a href="/mag-box-iptv/">MAG-Box</a> oder <a href="/iptv-receiver/">Enigma2-Receiver</a>:</strong> für alle, die eine klassische Fernbedienung mit Receiver-Gefühl möchten.')


DEVICE_VARIANTS = [
    checks(
        '<strong><a href="/iptv-fire-tv-stick/">Fire TV Stick</a>:</strong> günstig, an jeden HDMI-Fernseher anschließbar, mit TiviMate oder IPTV Smarters Pro.',
        '<strong><a href="/iptv-samsung-tv/">Samsung</a> und <a href="/iptv-lg-tv/">LG</a>:</strong> direkt mit einer Smart-TV-App wie SET IPTV oder Flix IPTV, ohne Zusatzgerät.',
        '<strong><a href="/iptv-apple-tv/">Apple TV</a>, iPhone und iPad:</strong> mit Apps wie IPTVX oder iPlayTV aus dem App Store.'),
    '<p>Am häufigsten nutzen unsere Kunden einen <a href="/iptv-stick/">Streaming-Stick</a> am HDMI-Anschluss, weil er auch ältere Fernseher aufrüstet. '
    'Wer einen aktuellen <a href="/iptv-smart-tv/">Smart TV</a> hat, installiert die App direkt; für Fans der klassischen Fernbedienung gibt es '
    '<a href="/mag-box-iptv/">MAG-Boxen</a> und <a href="/iptv-receiver/">Enigma2-Receiver</a>.</p>',
    checks(
        '<strong><a href="/iptv-google-tv/">Google TV</a> oder <a href="/iptv-android/">Android TV</a>:</strong> größte App-Auswahl im Play Store, ideal für TiviMate.',
        '<strong><a href="/iptv-box/">Android-TV-Box</a> oder <a href="/iptv-nvidia-shield/">Nvidia Shield</a>:</strong> viel Leistung für große Senderlisten und 4K.',
        '<strong><a href="/iptv-pc-mac/">PC, Laptop oder Mac</a>:</strong> mit VLC oder im Browser – praktisch fürs Arbeitszimmer.'),
    '<p>Kurz gesagt: Für fast jeden Fernseher genügt ein <a href="/iptv-fire-tv-stick/">Fire TV Stick</a> mit <a href="/tivimate/">TiviMate</a> oder '
    '<a href="/iptv-smarters-pro/">IPTV Smarters Pro</a>. Auf Samsung- und LG-Geräten geht es auch ohne Stick, unterwegs reicht das Smartphone '
    'mit <a href="/iptv-android/">Android</a> oder <a href="/iptv-apple-tv-iphone/">iPhone</a>.</p>',
]

ORDER_VARIANTS = [
    '<p>So einfach geht es {place}: kostenlosen Test über <a href="/kostenlos-testen/">kostenlos testen</a> anfordern, Zugangsdaten in Ihre App eintragen, '
    'danach Laufzeit und Geräteanzahl auf der <a href="/preise/">Preisseite</a> wählen. Sie zahlen einmal – ohne Vertrag und ohne automatische Verlängerung.</p>',
    '<p>Der Ablauf {place} ist in wenigen Minuten erledigt: Test ohne Zahlungsdaten anfordern, App einrichten (unser Support hilft per E-Mail oder WhatsApp), '
    'Paket wählen. Wie Sie bezahlen können, erklärt <a href="/iptv-bezahlen/">IPTV bezahlen</a>.</p>',
    steps('<b>Testen:</b> Zugang über <a href="/kostenlos-testen/">kostenlos testen</a> anfordern – ohne Zahlungsdaten, auch {place}.',
          '<b>Einrichten:</b> Xtream-Login oder M3U-Link in die App eintragen; bei Fragen hilft der deutschsprachige Support.',
          '<b>Bestellen:</b> Paket auf der <a href="/preise/">Preisseite</a> wählen und einmalig bezahlen – keine automatische Verlängerung.'),
]


def order_steps(place):
    return steps(
        f'<b>Kostenlos testen:</b> Test über <a href="/kostenlos-testen/">kostenlos testen</a> anfordern – ohne Zahlungsdaten, auch {place}.',
        '<b>App einrichten:</b> Zugangsdaten (Xtream Codes oder M3U) in Ihrer IPTV-App eintragen; unser Support hilft per E-Mail oder WhatsApp.',
        '<b>Paket wählen:</b> Laufzeit und Anzahl der Geräte auf der <a href="/preise/">Preisseite</a> auswählen – ab 9 € für einen Monat.',
        '<b>Einmal zahlen:</b> Keine automatische Verlängerung, kein Vertrag. Zahlungswege erklärt <a href="/iptv-bezahlen/">IPTV bezahlen</a>.')


# ====================================================================== CITY PAGES
def city_page(i, c):
    k, name = c['k'], c['n']
    short = c.get('short', name)
    name_, slug, prep, bc = STATES[c['st']]
    d = c['d']
    clubs = join_names(c['clubs'])
    is_citystate = slug is None
    isp_regional = c['isp']

    title = fit(rotate(k, [f'IPTV {name}: Anbieter, Abo ab 9 € & kostenloser Test',
                           f'IPTV {name} – Abo kaufen, Anbieter & kostenloser Test',
                           f'IPTV in {name}: Anbieter, Preise & kostenloser Test']) + [
        f'IPTV {name}: Anbieter, Abo & kostenloser Test',
        f'IPTV {name}: Anbieter, Abo & Test',
        f'IPTV {short}: Anbieter, Abo & Test',
    ], 50, 60)
    description = fit(rotate(k, [
        f'IPTV in {name}: Live-TV, Filme und Serien bis 4K über Ihre Internetleitung – ohne Schüssel und ohne Vertrag. Abo ab 9 €, kostenloser Test.',
        f'IPTV {name}: Fernsehen bis 4K über das Internet, ohne Kabelvertrag und Schüssel. Anbieter, Geräte, Abo ab 9 € und kostenloser Test.',
        f'IPTV in {name} einrichten: welche Leitung reicht, welches Gerät passt und wie Sie ohne Vertrag ab 9 € schauen. Jetzt kostenlos testen.',
    ], 'desc') + [
        f'IPTV in {name}: Fernsehen bis 4K über das Internet, ohne Schüssel und Vertrag. Anbieter, Abo ab 9 € und kostenloser Test.',
        f'IPTV in {short}: TV bis 4K über das Internet, ohne Schüssel und Vertrag. Abo ab 9 €, kostenloser Test.',
    ], 120, 155)
    h1 = pick(k, [f'IPTV in {name}', f'IPTV {name}: Fernsehen über das Internet', f'IPTV in {name}: Anbieter, Abo und Test'], 'h1')
    lead = pick(k, [
        f'Fernsehen über das Internet funktioniert in {name} in jedem Stadtteil – von {d[0]} bis {d[-1]}. Hier erfahren Sie, welche Leitung Sie brauchen, welche Geräte passen und wie Sie IPTV in {short} kostenlos testen.',
        f'Ob in {d[0]}, {d[1]} oder {d[-1]}: IPTV bringt Live-TV, Filme und Serien in {name} über Ihre Internetleitung auf den Fernseher. So finden Sie den passenden Anbieter, das richtige Abo und testen vorab kostenlos.',
        f'Sie wohnen in {name} und möchten fernsehen ohne Kabelvertrag und Schüssel? Dieser Ratgeber zeigt, was Sie für IPTV in {short} brauchen – vom Internet in {d[0]} bis zum Test auf Ihrem Gerät.',
    ], 'lead')
    answer = (f'IPTV funktioniert überall in {name}, in {d[0]} ebenso wie in {d[1]} oder {d[2]}. Sie brauchen nur eine Internetleitung '
              f'mit etwa 16 Mbit/s für Full HD (25 Mbit/s für 4K), ein Gerät wie Fire TV Stick, Smart TV oder Android-Box und einen IPTV-Zugang. '
              f'Bei IPTV Kanal kostet ein Abo ab 9 € im Monat ohne Vertrag; vorher testen Sie kostenlos und ohne Zahlungsdaten.')

    # 1 overview
    general = pick(k, [
        f'<p>Bei IPTV (Internet Protocol Television) kommen Sender nicht per Satellit oder Kabel, sondern als Datenstrom über Ihren Internetanschluss. Für {short} heißt das: Sie brauchen keinen Kabelvertrag, keine Schüssel und keinen Techniker. Seit Juli 2024 dürfen Vermieter den Kabelanschluss zudem nicht mehr über die Nebenkosten abrechnen – viele Haushalte in {name} haben sich deshalb neu entschieden, wie sie fernsehen. Mehr zu den Grundlagen im Ratgeber <a href="/was-ist-iptv/">Was ist IPTV?</a></p>',
        f'<p>IPTV überträgt Fernsehprogramme über das Internet statt über Antenne, Kabel oder Satellit. In {name} genügt deshalb der Anschluss, den Sie ohnehin für Surfen und Streaming nutzen. Weil das Nebenkostenprivileg für Kabelfernsehen im Juli 2024 entfallen ist, zahlen Mieter den Kabelanschluss nicht mehr automatisch mit – ein guter Moment, IPTV als Alternative zu prüfen. Wie die Technik funktioniert, erklärt <a href="/was-ist-iptv/">Was ist IPTV?</a></p>',
        f'<p>Das Prinzip ist einfach: Eine App auf Ihrem Fernseher, Stick oder Smartphone lädt Senderliste, Programmführer und Mediathek über Ihre Internetleitung. Ob Altbau, Neubau oder Einfamilienhaus in {short} – es zählt nur die Leitung, nicht der Kabel- oder Satellitenanschluss. Seit dem Wegfall des Nebenkostenprivilegs im Juli 2024 schauen sich viele Mieter in {name} nach solchen Alternativen um. Grundlagen: <a href="/was-ist-iptv/">Was ist IPTV?</a></p>',
    ], 'gen')
    overview = f'<p>{c["intro"]}</p>\n{general}'
    if c.get('extra'):
        overview += f'\n<p>{c["extra"]}</p>'

    # 2 internet
    isp_text = (f'Neben den bundesweiten Netzen von {NATIONAL_ISP} sind in {short} auch regionale Anbieter wie {join_names(isp_regional)} aktiv.'
                if isp_regional else f'In {short} sind die bundesweiten Netze von {NATIONAL_ISP} verfügbar, dazu je nach Straße Stadtwerke oder regionale Glasfaseranbieter.')
    internet = pick(k, [
        f'<p>Für IPTV zählt nicht der Name des Anbieters, sondern die tatsächliche Geschwindigkeit am Abend, wenn in {name} alle gleichzeitig streamen. {isp_text} Welche Leitung an Ihrer Adresse verfügbar ist, zeigt der Verfügbarkeitscheck der Anbieter oder der Breitbandatlas der Bundesnetzagentur.</p>',
        f'<p>Die gute Nachricht für {short}: In einer Großstadt reicht die vorhandene Leitung fast immer. {isp_text} Messen Sie am besten am Abend zwischen 20 und 22 Uhr, wenn die Netze am stärksten ausgelastet sind – zum Beispiel mit der Breitbandmessung der Bundesnetzagentur.</p>',
        f'<p>Wie schnell Ihr Internet in {d[0]} oder {d[-1]} wirklich ist, hängt von Straße und Hausverkabelung ab. {isp_text} Ein Speedtest direkt am Fernseher oder Stick verrät mehr als die Angabe im Vertrag.</p>',
    ], 'net') + SPEED_TABLE + pick(k, [
        f'<p>Schauen mehrere Personen gleichzeitig, addiert sich der Bedarf: Zwei Fernseher in Full HD brauchen rund 32 Mbit/s. Verbinden Sie den Fernseher oder Stick möglichst per LAN-Kabel – gerade in Altbauten mit dicken Wänden ist WLAN der häufigste Grund für Ruckler. Mehr dazu in <a href="/iptv-4k/">IPTV in 4K</a>.</p>',
        f'<p>Tipp für Mehrfamilienhäuser in {short}: Viele Nachbar-WLANs auf demselben Kanal bremsen. Ein LAN-Kabel oder ein WLAN im 5-GHz-Band schafft Abhilfe. Für mehrere Fernseher gleichzeitig addieren Sie die Bandbreiten aus der Tabelle; Details in <a href="/iptv-4k/">IPTV in 4K</a>.</p>',
    ], 'net2')

    # 3 regional programme and sport
    show = BROADCASTER_SHOW[bc]
    vom = 'von Radio Bremen' if bc == 'Radio Bremen' else f'vom {bc}'
    der = 'Radio Bremen' if bc == 'Radio Bremen' else f'der {bc}'
    other = f' Neben dem Fußball verfolgen viele {c["other_sport"]}.' if c.get('other_sport') else ''
    regional = pick(k, [
        f'<p>Per IPTV empfangen Sie in {name} dieselben öffentlich-rechtlichen und privaten Sender wie über Kabel – inklusive {bc} mit seinem Regionalprogramm, etwa {show}. Ihr eigener Zugang bestimmt, welche weiteren deutschen und internationalen Sender enthalten sind; das sehen Sie vollständig im <a href="/kostenlos-testen/">kostenlosen Test</a>.</p>',
        f'<p>Das Regionalfernsehen kommt in {short} {vom}. Wer {show} schauen möchte, findet den Sender per IPTV genauso in der Senderliste wie ARD, ZDF und die Privaten. Eine Übersicht der Sendergruppen zeigt die <a href="/iptv-senderliste/">IPTV Senderliste</a>.</p>',
    ], 'reg') + pick(k, [
        f'<p>Für Sportfans in {short} dreht sich vieles um {clubs}.{other} Welche Spiele bei welchem Rechteinhaber laufen und wie Sie Fußball ohne Verzögerung schauen, erklärt der Ratgeber <a href="/iptv-fussball/">Fußball per IPTV</a>; weitere Sportarten finden Sie unter <a href="/iptv-sport/">Sport per IPTV</a>.</p>',
        f'<p>Sport ist in {name} ein großes Thema – allen voran {clubs}.{other} Damit Live-Spiele flüssig laufen, gelten dieselben Regeln wie überall: LAN-Kabel, 50-Hz-Bildwiederholrate und ein aktuelles Gerät. Wer welche Rechte hat, steht im Ratgeber <a href="/iptv-fussball/">Fußball per IPTV</a>; mehr unter <a href="/iptv-sport/">Sport per IPTV</a>.</p>',
    ], 'sport')

    # 4 devices
    devices = pick(k, [
        f'<p>Welches Gerät in Ihrer Wohnung in {short} am besten passt, hängt vor allem vom Fernseher ab. Neuere Samsung- und LG-Modelle können IPTV direkt, bei allen anderen ist ein Stick die günstigste Lösung:</p>',
        f'<p>Sie brauchen in {name} kein spezielles Gerät aus dem Fachhandel. Fast jeder Fernseher der letzten Jahre lässt sich nutzen – entweder direkt oder mit einem Stick am HDMI-Anschluss:</p>',
        f'<p>Ob Wohnzimmer in {d[0]} oder Schlafzimmer in {d[-1]}: IPTV läuft auf fast allen modernen Geräten. Die wichtigsten Optionen im Überblick:</p>',
    ], 'dev') + pick(k, DEVICE_VARIANTS, 'devlist') + pick(k, [
        '<p>Alle Geräte und Apps vergleicht die <a href="/iptv-geraete/">Geräteübersicht</a>; den passenden Player finden Sie bei den <a href="/iptv-apps/">IPTV Apps</a>.</p>',
        '<p>Welche App auf welchem Gerät am besten läuft, zeigt der Vergleich <a href="/bester-iptv-player/">Bester IPTV Player</a>.</p>',
        '<p>Eine Schritt-für-Schritt-Anleitung für jedes Gerät finden Sie unter <a href="/iptv-einrichten/">IPTV einrichten</a>.</p>',
    ], 'dev2')

    # 5 buying
    buy = pick(k, [
        f'<p>„IPTV kaufen {short}“ heißt nicht, dass Sie in ein Geschäft gehen müssen. Ein IPTV-Abo wird online gebucht und funktioniert in ganz Deutschland gleich – Sie bekommen Ihre Zugangsdaten per E-Mail oder WhatsApp und können sofort loslegen. Bei IPTV Kanal kostet ein Monat 9 €, das Jahresabo für ein Gerät 49 € (rund 4,08 € pro Monat), jeweils ohne automatische Verlängerung.</p>',
        f'<p>Einen IPTV Anbieter in {name} vor Ort brauchen Sie nicht: Der Zugang wird online bestellt und gilt deutschlandweit, auch wenn Sie umziehen oder verreisen. IPTV Kanal bietet Pakete von 1 bis 12 Monaten für 1 bis 5 Geräte – ab 9 € im Monat oder 49 € im Jahr, mit einmaliger Zahlung statt Vertrag.</p>',
        f'<p>Ein IPTV Abo für {short} schließen Sie bequem online ab. Wichtig ist, vorher zu testen, ob alles auf Ihrem Gerät und mit Ihrer Leitung läuft. Bei IPTV Kanal geht das kostenlos; danach wählen Sie zwischen 1, 3, 6 oder 12 Monaten – ab 9 € bzw. 49 € im Jahr, ohne Verlängerung.</p>',
    ], 'buy') + pick(k, ORDER_VARIANTS, 'order').format(place='in ' + short) + pick(k, [
        '<p>Woran Sie einen seriösen Anbieter erkennen, zeigt der <a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>.</p>',
        '<p>Worauf Sie bei der Anbieterwahl achten sollten, steht im Ratgeber <a href="/iptv-anbieter/">IPTV Anbieter</a>.</p>',
        '<p>Alle Pakete und Laufzeiten erklärt der Ratgeber <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>',
    ], 'buy2')

    # 6 surroundings
    regions = [a for a in c['ar'] if REGION.get(a)]
    near = chips(*[(f'/{city_slug(CITY[n])}/', f'IPTV {CITY[n].get("short", CITY[n]["n"])}') for n in c['nb']],
                 *[(f'/{region_slug(REGION[a])}/', f'IPTV {REGION[a]["n"]}') for a in regions])
    if is_citystate:
        around = f'<p>{name} ist eine Stadt und ein Bundesland zugleich. Für das Umland und die Nachbarstädte gelten dieselben Bedingungen – hier die passenden Seiten:</p>'
    else:
        around = pick(k, [
            f'<p>{name} liegt {prep}. Wer im Umland oder in einer Nachbarstadt wohnt, findet hier die passenden Seiten:</p>',
            f'<p>Ihr Zugang funktioniert nicht nur in {short}, sondern überall {prep} und in ganz Deutschland. Weitere Städte und Regionen in der Nähe:</p>',
        ], 'nb')
    around += near

    sections = [
        ('ueberblick', pick(k, [f'IPTV in {short}: so funktioniert es', f'Fernsehen über das Internet in {short}', f'Was IPTV in {short} bietet'], 's1'), overview),
        ('vor-ort', LOCAL_CITY[k][0], LOCAL_CITY[k][1].strip()),
        ('internet', pick(k, [f'Internet in {short}: welche Leitung reicht für IPTV?', f'Welche Internetgeschwindigkeit brauchen Sie in {short}?'], 's2'), internet),
        ('regional', pick(k, [f'Regionalprogramm und Sport in {short}', f'{bc}, Lokalnachrichten und Sport aus {short}'], 's3'), regional),
        ('geraete', pick(k, [f'Die passenden Geräte für IPTV in {short}', f'Auf welchen Geräten läuft IPTV in {short}?'], 's4'), devices),
        ('kaufen', pick(k, [f'IPTV kaufen in {short}: Abo, Preise und Test', f'IPTV Abo in {short}: Preise und kostenloser Test', f'IPTV Anbieter in {short}: so bestellen Sie'], 's5'), buy),
        ('umgebung', f'IPTV rund um {short}', around),
    ]

    faq = [
        (pick(k, [f'Gibt es IPTV in {name}?', f'Funktioniert IPTV überall in {name}?'], 'f1'),
         f'Ja. IPTV funktioniert in allen Stadtteilen von {name}, etwa in {d[0]}, {d[1]} oder {d[-1]}, sobald eine Internetleitung mit mindestens 10 bis 16 Mbit/s anliegt. Kabelanschluss oder Satellitenschüssel sind nicht nötig.'),
        (pick(k, [f'Welcher IPTV Anbieter ist der beste in {short}?', f'Brauche ich einen IPTV Anbieter aus {short}?'], 'f2'),
         pick(k, [f'Ein lokaler Anbieter ist nicht nötig: IPTV-Zugänge funktionieren deutschlandweit gleich. Achten Sie auf einen kostenlosen Test, transparente Preise ohne automatische Verlängerung und deutschsprachigen Support – so wie bei IPTV Kanal.',
                  f'Nein, ein Anbieter mit Sitz in {short} bringt keinen Vorteil, denn der Stream kommt über das Internet. Entscheidend sind stabile Server, ein Test vor dem Kauf, Preise ohne Abofalle und Support auf Deutsch.',
                  f'Der beste Anbieter für {short} ist der, der mit Ihrer Leitung und Ihrem Gerät im Test überzeugt. Prüfen Sie außerdem, ob Sie einmalig zahlen und ob der Support auf Deutsch per E-Mail oder WhatsApp erreichbar ist.'], 'fa2')),
        (f'Kann ich IPTV in {short} kostenlos testen?',
         pick(k, ['Ja. Bei IPTV Kanal fordern Sie einen kostenlosen Test ohne Zahlungsdaten an und prüfen Sender, Bildqualität und App direkt auf Ihrem Gerät und mit Ihrer eigenen Leitung.',
                  f'Ja. Den Test fordern Sie online an, die Zugangsdaten kommen per E-Mail oder WhatsApp. So sehen Sie vor dem Kauf, wie Sender und Bild an Ihrem Anschluss in {short} laufen.',
                  'Ja, kostenlos und ohne Zahlungsdaten. Testen Sie am besten abends, wenn die Netze am stärksten ausgelastet sind – dann wissen Sie, wie IPTV im Alltag läuft.'], 'fa3')),
        (pick(k, [f'Was kostet ein IPTV Abo in {short}?', f'Wie teuer ist IPTV in {short}?'], 'f4'),
         pick(k, ['Bei IPTV Kanal kostet ein Monat 9 €, drei Monate 29 €, sechs Monate 39 € und zwölf Monate 49 € für ein Gerät. Sie zahlen einmal, es gibt keine automatische Verlängerung.',
                  'Für ein Gerät zahlen Sie 9 € für einen Monat oder 49 € für ein Jahr, also rund 4 € im Monat. Pakete für bis zu fünf Geräte gibt es ebenfalls; abgerechnet wird einmalig ohne Vertrag.',
                  'Die Preise sind überall in Deutschland gleich: ab 9 € pro Monat, 29 € für drei, 39 € für sechs und 49 € für zwölf Monate bei einem Gerät. Eine automatische Verlängerung gibt es nicht.'], 'fa4')),
        (pick(k, [f'Kann ich {bc} und Lokalnachrichten aus {short} per IPTV sehen?', f'Empfange ich das Regionalprogramm für {short} per IPTV?'], 'f5'),
         f'Ja, {der} gehört wie ARD und ZDF zu den Sendern, die per IPTV übertragen werden. Welche Regionalfenster und weiteren Sender Ihr Zugang enthält, sehen Sie im kostenlosen Test.'),
    ]
    related = ([slug] if slug else []) + [city_slug(CITY[n]) for n in c['nb'][:2]] + ['iptv-kaufen', 'iptv-fire-tv-stick', 'iptv-staedte']
    card_text = pick(k, [f'Anbieter, Abo und kostenloser Test in {short}.', f'Internet, Geräte und Abo für {short}.', f'IPTV in {short}: Leitung, Sender und Test.'], 'card')
    sources = [(f'{bc}: Regionalprogramm', BROADCASTER_URL[bc])] + LOCAL_SOURCES
    return dict(slug=city_slug(c), parent='staedte', kind='guide', title=title, description=description,
                eyebrow='IPTV IN IHRER STADT', h1=h1, lead=lead, answer=answer, sections=sections, faq=faq,
                related=related, card=(f'IPTV {short}', card_text), sources=sources)


# ====================================================================== REGION PAGES
TOURIST = {'mv', 'sh', 'sauerland', 'eifel', 'allgaeu', 'schwarzwald', 'bodensee', 'ostfriesland', 'harz', 'heide',
           'erzgebirge', 'oberbayern', 'pfalz', 'hunsrueck', 'vogtland', 'westerwald'}


def region_page(i, r):
    k, name = r['k'], r['n']
    nom = NOMINATIVE.get(k, name)
    alt = r.get('alt')
    st_name, st_slug, st_prep, bc = STATES[r['st']]
    prep = {'state': STATES[r['st']][2]}.get(r['kind']) if r['kind'] == 'state' else REGION_PREP.get(k, f'in {name}')
    towns = r['towns']
    city_links = [link_city(c) for c in r['cities']]
    near = r.get('near', [])
    near_links = [link_city(c) for c in near]
    clubs = []
    for c in r['cities']:
        clubs += CITY[c]['clubs'][:1]
    clubs = clubs[:4]
    label = f'{name} ({alt})' if alt and len(alt) < 6 else name

    title = fit(rotate(k, [f'IPTV {prep}: Anbieter, Abo ab 9 € & kostenloser Test',
                           f'IPTV {name}: Anbieter, Abo & kostenloser Test 2026',
                           f'IPTV {prep}: Abo kaufen, Anbieter & kostenloser Test']) + [
        f'IPTV {name}: Anbieter, Abo & kostenloser Test',
        f'IPTV {prep}: Anbieter, Abo & Gratis-Test',
        f'IPTV {name}: Anbieter, Abo & Test',
    ], 50, 60)
    description = fit(rotate(k, [
        f'IPTV {prep}: Fernsehen bis 4K über das Internet – auch auf dem Land. Bandbreite, Geräte, Regionalprogramm, Abo ab 9 € und Test.',
        f'IPTV {prep}: Live-TV, Filme und Serien über Ihre Internetleitung, in Stadt und Dorf. Leitung prüfen, Gerät wählen, ab 9 € kostenlos testen.',
        f'IPTV {prep} ohne Kabel und Schüssel: welche Bandbreite reicht, welche Geräte passen und wie Sie ab 9 € ohne Vertrag schauen. Gratis testen.',
    ], 'desc') + [
        f'IPTV {prep}: TV bis 4K über das Internet, auch auf dem Land. Bandbreite, Geräte, Abo ab 9 € und kostenloser Test.',
        f'IPTV {prep}: TV bis 4K über das Internet. Bandbreite, Geräte, Abo ab 9 € und kostenloser Test.',
    ], 120, 155)
    h1 = pick(k, [f'IPTV {prep}', f'IPTV {name}: Fernsehen über das Internet', f'IPTV {prep}: Anbieter, Abo und Test'], 'h1')
    h1 = h1[0].upper() + h1[1:]
    place_list = join_names(([CITY[c].get('short', CITY[c]['n']) for c in r['cities'][:3]] + towns)[:4])
    lead = pick(k, [
        f'Von {place_list}: IPTV bringt Live-TV, Filme und Serien {prep} über Ihre Internetleitung auf den Fernseher – in der Stadt ebenso wie im Dorf.',
        f'Sie wohnen {prep}, etwa in {place_list}? Hier lesen Sie, welche Leitung Sie für IPTV brauchen, welche Geräte passen und wie Sie vorab kostenlos testen.',
        f'IPTV {prep} funktioniert überall dort, wo Internet anliegt – in {place_list} genauso wie in kleineren Orten. So finden Sie Abo, Gerät und Einstellungen.',
    ], 'lead')
    answer = (f'IPTV funktioniert {prep} überall, wo eine Internetleitung liegt – in {place_list} ebenso wie in kleineren Gemeinden. '
              f'Für HD reichen 6 bis 10 Mbit/s, für Full HD etwa 16 Mbit/s und für 4K 25 Mbit/s. Sie brauchen ein Gerät wie Fire TV Stick oder Smart TV '
              f'und einen Zugang; bei IPTV Kanal ab 9 € im Monat ohne Vertrag, vorher kostenlos testen.')

    # 1 overview with kind-specific angle
    angle = {
        'state': pick(k, [
            f'<p>Als Bundesland hat {name} ein eigenes Landesprogramm beim {bc}. Per IPTV empfangen Sie es genauso wie die überregionalen Sender – egal, ob Sie in der Landeshauptstadt, in einer Kreisstadt oder auf dem Dorf wohnen. Weil IPTV über das Internet kommt, ist weder ein Kabelanschluss noch eine Schüssel nötig; das ist besonders praktisch, seit Vermieter den Kabelanschluss nicht mehr über die Nebenkosten abrechnen dürfen (seit Juli 2024).</p>',
            f'<p>Für Haushalte {prep} bedeutet IPTV vor allem Unabhängigkeit: Sie brauchen keinen Kabelanschluss und keine Satellitenschüssel, sondern nur Ihre Internetleitung. Das Landesprogramm des {bc} gehört ebenso zum Empfang wie ARD, ZDF und die privaten Sender. Seit dem Ende des Nebenkostenprivilegs im Juli 2024 überlegen viele Mieter {prep}, wie sie künftig fernsehen.</p>',
        ], 'ang'),
        'metro': pick(k, [
            f'<p>In einem Ballungsraum wie {name} ist die Netzinfrastruktur dicht – Kabel, VDSL und Glasfaser liegen in den meisten Straßen. Die Herausforderung ist eher die Auslastung am Abend, wenn viele Haushalte gleichzeitig streamen. Ein guter IPTV-Zugang gleicht das mit leistungsfähigen Servern aus; zuhause hilft ein LAN-Kabel zum Fernseher.</p>',
            f'<p>Wer {prep} lebt, hat meist mehrere Netzanbieter zur Auswahl und selten ein Bandbreitenproblem. Wichtiger ist, dass das WLAN in dicht bebauten Mehrfamilienhäusern nicht von Nachbarnetzen ausgebremst wird. Für IPTV gilt deshalb: Fernseher oder Stick per Kabel anschließen oder das 5-GHz-Band nutzen.</p>',
        ], 'ang'),
        'landscape': pick(k, [
            f'<p>{nom} ist keine Verwaltungseinheit, sondern eine gewachsene Region mit eigener Identität. Für IPTV spielt die Grenze keine Rolle: Der Zugang funktioniert in jedem Ort gleich. Entscheidend ist allein die Leitung – und die ist zwischen Kleinstadt und Dorf oft unterschiedlich.</p>',
            f'<p>Wer {prep} wohnt, kennt das: In der Kreisstadt ist das Internet schnell, im Nachbardorf deutlich langsamer. IPTV kommt mit beidem zurecht, weil sich die Bildqualität an die Bandbreite anpassen lässt. Satellitenempfang bleibt eine Alternative, ist in Tälern oder bei Bäumen vor dem Haus aber nicht immer möglich.</p>',
        ], 'ang'),
        'district': pick(k, [
            f'<p>{name} ist ein Regierungsbezirk in Bayern, das Regionalprogramm kommt vom BR. Per IPTV empfangen Sie es genauso wie die überregionalen Sender, ob in der Bezirkshauptstadt oder im kleinsten Ortsteil. Kabelanschluss oder Schüssel brauchen Sie dafür nicht.</p>',
            f'<p>Zwischen den Städten und den ländlichen Gemeinden {prep} schwankt die Internetversorgung deutlich. Bayern fördert seit Jahren den Ausbau, trotzdem sind manche Orte noch auf DSL angewiesen. IPTV funktioniert dort ebenfalls – mit HD statt 4K.</p>',
        ], 'ang'),
    }[r['kind']]
    overview = f'<p>{r["intro"]}</p>\n{angle}<p>Wie IPTV technisch funktioniert, erklärt der Ratgeber <a href="/was-ist-iptv/">Was ist IPTV?</a></p>'

    # 2 cities and towns
    if city_links:
        cities = pick(k, [
            f'<p>Für die größeren Städte {prep} gibt es eigene Seiten mit lokalen Details zu Leitung, Sendern und Sport: {join_names(city_links)}. Daneben funktioniert IPTV genauso in {join_names(towns)} und allen anderen Orten der Region.</p>',
            f'<p>Detaillierte Informationen finden Sie auf den Stadtseiten für {join_names(city_links)}. Für {join_names(towns)} und die kleineren Gemeinden gilt dasselbe: Sobald die Leitung stimmt, läuft IPTV.</p>',
        ], 'cit')
    else:
        cities = f'<p>Zu den wichtigsten Orten {prep} gehören {join_names(towns)}. In allen funktioniert IPTV gleich, sobald die Internetleitung die nötige Bandbreite liefert.</p>'
    if near_links:
        cities += f'<p>Größere Städte in der Nähe mit eigenen Seiten: {join_names(near_links)}.</p>'

    # 3 bandwidth (rural angle)
    bandwidth = pick(k, [
        f'<p>{prep[0].upper() + prep[1:]} gibt es alle Anschlussarten: Glasfaser in Neubaugebieten und ausgebauten Orten, VDSL und Kabel in den Städten, DSL in vielen Dörfern. Wo das Festnetz langsam ist, können ein LTE- oder 5G-Router oder Satelliteninternet wie Starlink eine Alternative sein – IPTV funktioniert auch darüber, solange die Bandbreite stabil ist.</p>',
        f'<p>Für IPTV {prep} gilt: Messen statt schätzen. Ein Speedtest am Abend zeigt, ob Ihre Leitung für Full HD reicht. Wo nicht, wählen Sie in der App eine niedrigere Qualität oder nutzen einen LTE- bzw. 5G-Router. In vielen Orten bauen Telekom, Deutsche Glasfaser oder regionale Anbieter gerade Glasfaser aus – der Breitbandatlas der Bundesnetzagentur zeigt den Stand.</p>',
    ], 'bw') + SPEED_TABLE

    # 4 programme
    show = BROADCASTER_SHOW[bc] if r['kind'] != 'district' else BROADCASTER_SHOW['BR']
    bc_name = bc if r['kind'] != 'district' else 'BR'
    sport = (f' Für Fußballfans {prep} stehen Vereine wie {join_names(clubs)} im Mittelpunkt – wie Sie Spiele flüssig schauen, erklärt <a href="/iptv-fussball/">Fußball per IPTV</a>.'
             if clubs else ' Wie Sie Fußball und andere Sportarten flüssig schauen, erklärt <a href="/iptv-sport/">Sport per IPTV</a>.')
    programme = pick(k, [
        f'<p>Das Regionalprogramm {prep} kommt vom {bc_name}, mit Sendungen wie {show}. Per IPTV empfangen Sie es zusammen mit ARD, ZDF, den Privatsendern und – je nach Zugang – vielen internationalen Programmen.{sport}</p>',
        f'<p>Regionalnachrichten liefert {prep} der {bc_name}, etwa {show}. Diese Sender gehören beim IPTV-Empfang ebenso dazu wie das Programm der großen deutschen Sender.{sport}</p>',
    ], 'prog')

    # 5 holiday or household
    if k in TOURIST:
        extra_sec = ('ferienwohnung', pick(k, [f'IPTV in der Ferienwohnung {prep}', f'IPTV im Urlaub {prep}', f'Checkliste für Gäste und Vermieter {prep}'], 'fw'), pick(k, [
            '<p>Damit IPTV im Urlaub klappt, packen Sie Stick, Netzteil und Fernbedienung ein und notieren sich vorab Ihre Zugangsdaten. Fragen Sie die Unterkunft nach einem freien HDMI-Anschluss und nach dem WLAN-Passwort. Läuft das Bild ruckelig, wählen Sie in der App die HD-Variante des Senders. Wie Sie einen Stick in wenigen Minuten einrichten, zeigt <a href="/iptv-stick/">IPTV Stick</a>.</p>',
            '<p>Für Vermieter lohnt sich ein Fernseher, auf dem Gäste Apps installieren können – etwa mit <a href="/iptv-google-tv/">Google TV</a> oder einem <a href="/iptv-fire-tv-stick/">Fire TV Stick</a>. Ein eigenes Gäste-WLAN ohne Drosselung und ein gut sichtbarer HDMI-Anschluss machen den Aufenthalt angenehmer. Gäste melden sich mit ihren eigenen Zugangsdaten an und nach der Abreise wieder ab.</p>',
            '<p>Zwei Dinge sollten Sie im Urlaub beachten: Erstens zählt jedes gleichzeitig schauende Gerät – schaut zuhause jemand weiter, brauchen Sie ein Paket für zwei Geräte. Zweitens ist mobiles Internet nicht unbegrenzt; Full HD verbraucht grob 3 bis 7 GB pro Stunde. Mehr zu passenden Geräten im Ratgeber <a href="/iptv-geraete/">IPTV Geräte</a>.</p>',
        ], 'fwt'))
    else:
        extra_sec = ('haushalt', pick(k, ['IPTV für mehrere Geräte im Haushalt', 'Mehrere Fernseher, ein Zugang?'], 'hh'),
                     pick(k, [
                         f'<p>In vielen Haushalten {prep} läuft der Fernseher im Wohnzimmer, während im Kinderzimmer oder auf dem Tablet ein anderes Programm geschaut wird. Bei IPTV Kanal wählen Sie deshalb zwischen Paketen für 1 bis 5 Geräte, die gleichzeitig schauen können. Jedes Gerät braucht seine eigene Bandbreite – zwei Full-HD-Streams also rund 32 Mbit/s.</p>'
                         + checks('Ein Gerät: 9 € pro Monat oder 49 € pro Jahr.',
                                  'Zwei Geräte: 18 € pro Monat oder 89 € pro Jahr.',
                                  'Bis zu fünf Geräte: 45 € pro Monat oder 225 € pro Jahr.'),
                         f'<p>Familien {prep} schauen selten nur auf einem Bildschirm. Ein Paket für zwei oder drei Geräte erlaubt, dass im Wohnzimmer Fußball läuft und gleichzeitig im Kinderzimmer ein Film. Das Jahrespaket für zwei Geräte kostet 89 €, für drei Geräte 135 € – jeweils einmal bezahlt, ohne Verlängerung.</p>',
                         f'<p>Ob WG, Familie oder Paar mit Homeoffice: Wer {prep} auf mehreren Geräten gleichzeitig schauen möchte, wählt einfach die passende Geräteanzahl. Planen Sie pro Full-HD-Stream etwa 16 Mbit/s ein und verbinden Sie den Hauptfernseher per LAN-Kabel – dann bleiben auch parallele Streams stabil.</p>',
                     ], 'hhv')
                     + '<p>Alle Kombinationen stehen auf der <a href="/preise/">Preisseite</a>; was zu welchem Gerät passt, zeigt die <a href="/iptv-geraete/">Geräteübersicht</a>.</p>')

    # 6 buying
    buy = pick(k, [
        f'<p>Einen IPTV Anbieter {prep} vor Ort brauchen Sie nicht. IPTV-Abos werden online gebucht und funktionieren in ganz Deutschland – Sie erhalten die Zugangsdaten per E-Mail oder WhatsApp. Testen Sie vorher, ob Sender, Bild und App mit Ihrer Leitung zusammenpassen.</p>',
        f'<p>„IPTV kaufen {name}“ läuft komplett online: Test anfordern, App einrichten, Paket wählen. Weil IPTV über das Internet kommt, ist es egal, ob Sie in der Stadt oder auf dem Land wohnen – entscheidend ist der kostenlose Test mit Ihrer eigenen Leitung.</p>',
    ], 'buy') + pick(k, ORDER_VARIANTS, 'order').format(place=prep) + pick(k, [
        '<p>Worauf Sie bei der Wahl achten sollten, zeigt der <a href="/iptv-anbieter-vergleich/">IPTV Anbieter Vergleich</a>.</p>',
        '<p>Mehr zu Laufzeiten und Preisen im Ratgeber <a href="/iptv-kaufen/">IPTV kaufen</a>.</p>',
    ], 'buy2')

    # 7 neighbours
    neigh_keys = list(r['sub'])
    if r['kind'] != 'state' and st_slug and REGION.get(r['st']):
        neigh_keys = [r['st']] + neigh_keys
    for other in REGIONS:  # parent regions that list this one as a sub-region
        if k in other['sub'] and other['k'] not in neigh_keys:
            neigh_keys.append(other['k'])
    neigh_keys += [n for n in NEIGHBOURS.get(k, []) if n not in neigh_keys]
    neigh_keys = [n for n in neigh_keys if n != k]
    neigh = chips(*[(f'/{region_slug(REGION[n])}/', f'IPTV {REGION[n]["n"]}') for n in neigh_keys],
                  *[(f'/{city_slug(CITY[c])}/', f'IPTV {CITY[c].get("short", CITY[c]["n"])}') for c in (r['cities'] + near)[:6]])
    neighbours = pick(k, [
        f'<p>Weitere Regionen und Städte {prep} und in der Nähe:</p>',
        f'<p>Wohnen Sie am Rand der Region? Hier finden Sie die angrenzenden Regionen und die größeren Städte:</p>',
    ], 'nb') + neigh + '<p>Alle Seiten nach Ort finden Sie unter <a href="/iptv-regionen/">IPTV nach Region</a> und <a href="/iptv-staedte/">IPTV nach Stadt</a>.</p>'

    sections = [
        ('ueberblick', pick(k, [f'IPTV {prep}: das Wichtigste', f'Fernsehen über das Internet {prep}'], 's1'), overview),
        ('vor-ort', LOCAL_REGION[k][0], LOCAL_REGION[k][1].strip()),
        ('orte', pick(k, [f'Städte und Orte {prep}', f'IPTV in den Städten {prep}'], 's2'), cities),
        ('internet', pick(k, [f'Internet {prep}: reicht die Leitung für IPTV?', f'Bandbreite {prep}: Stadt und Land'], 's3'), bandwidth),
        ('programm', pick(k, [f'Regionalprogramm und Sport {prep}', f'{bc_name}, Regionalnachrichten und Sport'], 's4'), programme),
        extra_sec,
        ('kaufen', pick(k, [f'IPTV Abo {prep}: Preise und kostenloser Test', f'IPTV kaufen {prep}: so geht es'], 's6'), buy),
        ('nachbarn', 'Nachbarregionen und Städte', neighbours),
    ]
    faq = [
        (pick(k, [f'Gibt es IPTV {prep}?', f'Funktioniert IPTV überall {prep}?'], 'f1'),
         f'Ja. IPTV funktioniert {prep} überall, wo eine Internetleitung mit mindestens 6 bis 10 Mbit/s für HD anliegt – in Städten wie {place_list} ebenso wie in kleineren Orten.'),
        (pick(k, [f'Reicht das Internet auf dem Land {prep} für IPTV?', f'Was tun bei langsamem Internet {prep}?'], 'f2'),
         pick(k, ['Für HD reichen 6 bis 10 Mbit/s, für Full HD rund 16 Mbit/s. Ist die Leitung langsamer, wählen Sie in der App eine niedrigere Qualität oder nutzen einen LTE- bzw. 5G-Router mit unbegrenztem Datenvolumen.',
                  f'Meist ja. Schon mit 6 bis 10 Mbit/s läuft HD stabil; Full HD braucht etwa 16 Mbit/s. Wo das Festnetz {prep} schwächelt, sind ein 5G-Router oder Satelliteninternet eine Option.',
                  'Messen Sie zuerst abends die tatsächliche Geschwindigkeit. Reicht sie nicht für Full HD, schauen Sie in HD, verbinden das Gerät per LAN-Kabel oder ergänzen einen LTE- bzw. 5G-Router.'], 'fa2')),
        (pick(k, [f'Welcher IPTV Anbieter ist {prep} empfehlenswert?', f'Brauche ich einen regionalen IPTV Anbieter {prep}?'], 'f3'),
         pick(k, ['Ein regionaler Anbieter ist nicht nötig, IPTV-Zugänge funktionieren deutschlandweit. Wichtig sind ein kostenloser Test, klare Preise ohne automatische Verlängerung und erreichbarer deutschsprachiger Support.',
                  f'Nein. Ob Sie {prep} oder anderswo wohnen, der Stream kommt immer über das Internet. Achten Sie auf Testmöglichkeit, Einmalzahlung statt Abo und Hilfe auf Deutsch.'], 'fa3')),
        (f'Kann ich den {bc_name} per IPTV schauen?',
         f'Ja. Der {bc_name} gehört wie ARD und ZDF zu den Sendern, die per IPTV übertragen werden. Welche Regionalfenster und weiteren Sender Ihr Zugang enthält, zeigt der kostenlose Test.'),
        (pick(k, [f'Was kostet IPTV {prep}?', f'Kann ich IPTV {prep} kostenlos testen?'], 'f5'),
         pick(k, ['Bei IPTV Kanal testen Sie zuerst kostenlos und ohne Zahlungsdaten. Danach kostet ein Monat 9 € und ein Jahr 49 € für ein Gerät – einmalig bezahlt, ohne automatische Verlängerung.',
                  f'Die Preise gelten {prep} wie überall: 9 € für einen Monat, 49 € für zwölf Monate bei einem Gerät. Vorher testen Sie kostenlos, eine automatische Verlängerung gibt es nicht.'], 'fa5')),
    ]
    related = [region_slug(REGION[n]) for n in neigh_keys[:2]] + [city_slug(CITY[c]) for c in (r['cities'] + near)[:2]] + ['iptv-kaufen', 'iptv-regionen']
    related = list(dict.fromkeys(related))[:6]
    card_text = pick(k, [f'Leitung, Geräte und Abo {prep}.', f'IPTV {prep}: Stadt, Land und Test.', f'Bandbreite, Sender und Test {prep}.'], 'card')
    group = {'state': 'Bundesländer', 'metro': 'Metropolregionen', 'landscape': 'Regionen und Landschaften',
             'district': 'Bayerische Regierungsbezirke und Franken'}[r['kind'] if k != 'franken' else 'district']
    sources = [(f'{bc_name}: Regionalprogramm', BROADCASTER_URL[bc_name])] + LOCAL_SOURCES
    return dict(slug=region_slug(r), parent='regionen', kind='guide', group=group, title=title, description=description,
                eyebrow='IPTV IN IHRER REGION', h1=h1, lead=lead, answer=answer, sections=sections, faq=faq,
                related=related, card=(f'IPTV {label}', card_text), sources=sources)


NEIGHBOURS = {
    'nrw': ['nds', 'hessen', 'rlp'], 'bayern': ['bw', 'hessen', 'th', 'sachsen'], 'bw': ['bayern', 'hessen', 'rlp'],
    'nds': ['nrw', 'hessen', 'th', 'st', 'bb', 'mv', 'sh'], 'hessen': ['nrw', 'nds', 'th', 'bayern', 'bw', 'rlp'],
    'rlp': ['nrw', 'hessen', 'bw', 'saarland'], 'sachsen': ['bayern', 'th', 'st', 'bb'], 'sh': ['nds', 'mv'],
    'bb': ['mv', 'nds', 'st', 'sachsen'], 'st': ['nds', 'bb', 'sachsen', 'th'], 'th': ['hessen', 'nds', 'st', 'sachsen', 'bayern'],
    'mv': ['sh', 'nds', 'bb'], 'saarland': ['rlp'],
    'siegerland': ['sauerland', 'westerwald'], 'sauerland': ['siegerland', 'muensterland'], 'westerwald': ['siegerland', 'hunsrueck'],
    'niederbayern': ['oberpfalz', 'oberbayern'], 'oberpfalz': ['niederbayern', 'oberfranken', 'mittelfranken'],
    'oberbayern': ['niederbayern', 'schwaben'], 'eifel': ['hunsrueck', 'rheinland'], 'hunsrueck': ['eifel', 'westerwald'],
    'vogtland': ['erzgebirge', 'oberfranken'], 'erzgebirge': ['vogtland', 'lausitz'], 'lausitz': ['erzgebirge'],
    'allgaeu': ['bodensee'], 'bodensee': ['allgaeu', 'schwarzwald'], 'schwarzwald': ['bodensee'],
    'harz': ['heide'], 'heide': ['harz', 'ostfriesland'], 'ostfriesland': ['heide'],
    'owl': ['muensterland', 'sauerland'], 'muensterland': ['owl', 'ruhr'], 'niederrhein': ['ruhr', 'muensterland'],
    'pfalz': ['rheinhessen', 'rheinneckar'], 'rheinhessen': ['pfalz', 'rheinmain'],
}


REGION_PREP = {
    'ruhr': 'im Ruhrgebiet', 'rheinruhr': 'in der Region Rhein-Ruhr', 'rheinmain': 'im Rhein-Main-Gebiet',
    'rheinneckar': 'in der Metropolregion Rhein-Neckar', 'stuttgartmetro': 'in der Metropolregion Stuttgart',
    'rheinland': 'im Rheinland', 'niederrhein': 'am Niederrhein', 'muensterland': 'im Münsterland',
    'owl': 'in Ostwestfalen-Lippe', 'sauerland': 'im Sauerland', 'bergisch': 'im Bergischen Land',
    'siegerland': 'im Siegerland', 'eifel': 'in der Eifel', 'hunsrueck': 'im Hunsrück', 'westerwald': 'im Westerwald',
    'pfalz': 'in der Pfalz', 'rheinhessen': 'in Rheinhessen', 'franken': 'in Franken', 'oberfranken': 'in Oberfranken',
    'mittelfranken': 'in Mittelfranken', 'unterfranken': 'in Unterfranken', 'oberbayern': 'in Oberbayern',
    'niederbayern': 'in Niederbayern', 'oberpfalz': 'in der Oberpfalz', 'schwaben': 'in Schwaben', 'allgaeu': 'im Allgäu',
    'schwarzwald': 'im Schwarzwald', 'bodensee': 'am Bodensee', 'ostfriesland': 'in Ostfriesland', 'harz': 'im Harz',
    'heide': 'in der Lüneburger Heide', 'vogtland': 'im Vogtland', 'erzgebirge': 'im Erzgebirge', 'lausitz': 'in der Lausitz',
}


# ====================================================================== HUBS
def _hub(slug, hub, title, description, h1, lead, answer, sections, faq, related, card):
    return dict(slug=slug, parent='ratgeber', kind='hub', hub=hub, title=title, description=description,
                eyebrow='IPTV IN DEUTSCHLAND', h1=h1, lead=lead, answer=answer, sections=sections, faq=faq,
                related=related, card=card)


PAGES.append(_hub(
    'iptv-staedte', 'staedte', 'IPTV nach Stadt: Berlin, Hamburg, München & 47 weitere',
    'IPTV in Ihrer Stadt: Seiten für die 50 größten deutschen Städte – von Berlin bis Osnabrück. Internet, Geräte, Regionalprogramm, Abo und Test.',
    'IPTV in Ihrer Stadt',
    'Von Berlin bis Osnabrück: Für die 50 größten Städte Deutschlands zeigen wir, was Sie für IPTV vor Ort wissen sollten – Leitung, Regionalprogramm, Sport und Test.',
    'IPTV funktioniert in jeder deutschen Stadt gleich: Sie brauchen eine Internetleitung (ab 16 Mbit/s für Full HD), ein Gerät wie Fire TV Stick oder Smart TV und einen Zugang. Die Stadtseiten ergänzen das um lokale Details – regionale Netzanbieter, das zuständige Regionalprogramm und die Vereine vor Ort.',
    [('ueberblick', 'Warum eigene Seiten pro Stadt?', '<p>Technisch ist IPTV überall gleich. Unterschiede gibt es bei den Netzbetreibern, beim Regionalprogramm der ARD-Anstalt und beim Sport. Auf jeder Stadtseite finden Sie diese Details, dazu Tipps für Altbau und Mehrfamilienhaus und den Weg zum kostenlosen Test.</p>'
      '<p>Regionen und Bundesländer stehen auf einer eigenen Übersicht: <a href="/iptv-regionen/">IPTV nach Region</a>.</p>')],
    [('Brauche ich einen IPTV Anbieter aus meiner Stadt?', 'Nein. IPTV-Zugänge funktionieren deutschlandweit gleich. Wichtig sind ein kostenloser Test, klare Preise und deutschsprachiger Support.'),
     ('Funktioniert mein Zugang auch, wenn ich umziehe?', 'Ja. Der Zugang ist an Ihre Zugangsdaten gebunden, nicht an eine Adresse. Nach einem Umzug richten Sie Ihr Gerät einfach am neuen Anschluss ein.'),
     ('Meine Stadt fehlt – funktioniert IPTV trotzdem?', 'Ja, in jeder Stadt und jeder Gemeinde in Deutschland. Die Seiten für Bundesländer und Regionen helfen bei kleineren Orten weiter.')],
    ['iptv-regionen', 'iptv-kaufen', 'was-ist-iptv', 'iptv-fire-tv-stick', 'iptv-4k', 'iptv-anbieter'],
    ('IPTV nach Stadt', 'Die 50 größten Städte von Berlin bis Osnabrück.')))

PAGES.append(_hub(
    'iptv-regionen', 'regionen', 'IPTV nach Region: Bundesländer & Regionen in Deutschland',
    'IPTV in Ihrer Region: alle 16 Bundesländer und 34 Regionen von Ruhrgebiet bis Allgäu – Bandbreite auf dem Land, Regionalprogramm, Abo und Test.',
    'IPTV in Ihrer Region',
    'Alle Bundesländer und die wichtigsten Regionen – vom Ruhrgebiet über die Eifel bis ins Allgäu. Mit Tipps für langsame Leitungen auf dem Land und für die Ferienwohnung.',
    'IPTV funktioniert in jedem Bundesland und jeder Region gleich, entscheidend ist die Internetleitung vor Ort. Auf dem Land reichen 6 bis 10 Mbit/s für HD; wo das Festnetz langsam ist, helfen LTE- oder 5G-Router. Die Regionalseiten zeigen, was in Ihrer Gegend wichtig ist.',
    [('ueberblick', 'Bundesländer, Metropolregionen und Landschaften', '<p>Die Seiten sind nach drei Arten gegliedert: Bundesländer mit ihrem Landesprogramm, Ballungsräume wie Ruhrgebiet oder Rhein-Main mit dichter Netzinfrastruktur, und ländliche oder touristische Regionen wie Eifel, Schwarzwald oder Ostfriesland, in denen Bandbreite und Ferienwohnung die großen Themen sind.</p>'
      '<p>Berlin, Hamburg und Bremen sind Stadt und Bundesland zugleich – sie finden Sie unter <a href="/iptv-staedte/">IPTV nach Stadt</a>.</p>')],
    [('Funktioniert IPTV auch auf dem Land?', 'Ja, sobald eine Internetleitung mit mindestens 6 bis 10 Mbit/s anliegt. Für Full HD sind rund 16 Mbit/s, für 4K 25 Mbit/s empfehlenswert.'),
     ('Kann ich IPTV in der Ferienwohnung nutzen?', 'Ja. Nehmen Sie Ihren Fire TV Stick mit und verbinden Sie ihn mit dem WLAN der Unterkunft. Es dürfen nicht mehr Geräte gleichzeitig schauen, als Ihr Paket umfasst.'),
     ('Empfange ich mein Regionalprogramm per IPTV?', 'Ja, die Dritten Programme wie WDR, BR, NDR oder MDR gehören zu den Sendern, die per IPTV übertragen werden. Den Umfang Ihres Zugangs zeigt der kostenlose Test.')],
    ['iptv-staedte', 'iptv-kaufen', 'was-ist-iptv', 'iptv-stick', 'iptv-4k', 'iptv-anbieter'],
    ('IPTV nach Region', 'Alle Bundesländer und 34 Regionen in Deutschland.')))

for _i, _c in enumerate(CITIES):
    PAGES.append(city_page(_i, _c))
for _i, _r in enumerate(REGIONS):
    PAGES.append(region_page(_i, _r))
