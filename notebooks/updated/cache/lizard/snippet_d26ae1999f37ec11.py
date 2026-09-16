def dispatch(t):
    if not t:
        return t
    else:
        t = list(t)
    assert len(t) >= 2
    if len(t) == 2:
        t.insert(0, 'basic')
    if isinstance(t[0], basestring):
        if t[0] in ('basic', 'forced_basic'):
            t[0] = http_basic
        elif t[0] in ('digest',):
            t[0] = http_digest
    return t[0], tuple(t[1:])