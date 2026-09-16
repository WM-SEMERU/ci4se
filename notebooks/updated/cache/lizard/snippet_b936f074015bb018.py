def format_h1(s, format='text', indents=0):
    _CHAR = '='
    if format.startswith('text'):
        return format_underline(s, _CHAR, indents)
    elif format.startswith('markdown'):
        return ['# {}'.format(s)]
    elif format.startswith('rest'):
        return format_underline(s, _CHAR, 0)