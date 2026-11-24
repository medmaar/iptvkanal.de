"""Small HTML helpers for the guide pages. Output uses the site's existing component classes."""


def steps(*items):
    return '<ol class="howto">' + ''.join(f'<li>{item}</li>' for item in items) + '</ol>'


def checks(*items):
    return '<ul class="check-list">' + ''.join(
        f'<li><svg aria-hidden="true"><use href="#i-check-c"/></svg><span>{item}</span></li>' for item in items) + '</ul>'


def tip(text, label='Tipp'):
    return f'<div class="tip"><p><strong>{label}:</strong> {text}</p></div>'


def table(head, rows, caption=''):
    cap = f'<caption class="sr-only">{caption}</caption>' if caption else ''
    thead = '<thead><tr>' + ''.join(f'<th scope="col">{h}</th>' for h in head) + '</tr></thead>'
    body = '<tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows) + '</tbody>'
    return f'<div class="matrix"><div class="matrix-scroll"><table>{cap}{thead}{body}</table></div></div>'


def proscons(pros, cons, pro_title='Stärken', con_title='Grenzen'):
    def col(title, items):
        return f'<div><h3>{title}</h3><ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul></div>'
    return '<div class="pros-cons">' + col(pro_title, pros) + col(con_title, cons) + '</div>'


def chips(*links):
    return '<ul class="chip-list">' + ''.join(f'<li><a href="{href}">{label}</a></li>' for href, label in links) + '</ul>'
