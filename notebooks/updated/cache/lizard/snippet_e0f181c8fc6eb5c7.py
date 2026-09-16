def hexstr(x, onlyasc=0, onlyhex=0, color=False):
    x = bytes_encode(x)
    _sane_func = sane_color if color else sane
    s = []
    if not onlyasc:
        s.append(' '.join('%02X' % orb(b) for b in x))
    if not onlyhex:
        s.append(_sane_func(x))
    return '  '.join(s)