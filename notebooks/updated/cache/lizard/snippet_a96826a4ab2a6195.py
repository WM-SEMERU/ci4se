def htmlize_list(items):
    out = ['<ul>']
    for item in items:
        out.append('<li>' + htmlize(item) + '</li>')
    out.append('</ul>')
    return '\n'.join(out)