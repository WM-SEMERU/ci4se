def interpn(*args, **kw):
    method = kw.pop('method', 'cubic')
    if kw:
        raise ValueError('Unknown arguments: ' % kw.keys())
    nd = (len(args) - 1) // 2
    if len(args) != 2 * nd + 1:
        raise ValueError('Wrong number of arguments')
    q = args[:nd]
    qi = args[nd + 1:]
    a = args[nd]
    for j in range(nd):
        a = interp1d(q[j], a, axis=j, kind=method)(qi[j])
    return a