def visit(spht, node):
    html_attrs_bq = {'async': '', 'src': '//s.imgur.com/min/embed.js',
        'charset': 'utf-8'}
    spht.body.append(spht.starttag(node, 'script', '', **html_attrs_bq))