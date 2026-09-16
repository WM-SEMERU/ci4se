def bootstrap_alert(visitor, items):
    txt = []
    for x in items:
        cls = x['kwargs'].get('class', '')
        if cls:
            cls = 'alert-%s' % cls
        txt.append('<div class="alert %s">' % cls)
        if 'close' in x['kwargs']:
            txt.append(
                '<button class="close" data-dismiss="alert">&times;</button>')
        text = visitor.parse_text(x['body'], 'article')
        txt.append(text)
        txt.append('</div>')
    return '\n'.join(txt)