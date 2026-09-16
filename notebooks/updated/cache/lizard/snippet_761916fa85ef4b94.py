def rewrap(s, width=COLS):
    s = ' '.join([l.strip() for l in s.strip().split('\n')])
    return '\n'.join(textwrap.wrap(s, width))