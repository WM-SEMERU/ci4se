def _broydens_direction(s, y, x, hessinv_estimate=None, impl='first'):
    r
    assert len(s) == len(y)
    if hessinv_estimate is not None:
        r = hessinv_estimate(x)
    else:
        r = x.copy()
    for i in range(len(s)):
        if impl == 'first':
            r.lincomb(1, r, y[i].inner(r), s[i])
        elif impl == 'second':
            r.lincomb(1, r, y[i].inner(x), s[i])
        else:
            raise RuntimeError('unknown `impl`')
    return r