def mkron(a, *args):
    if not isinstance(a, list):
        a = [a]
    a = list(a)
    for i in args:
        if isinstance(i, list):
            a.extend(i)
        else:
            a.append(i)
    c = _vector.vector()
    c.d = 0
    c.n = _np.array([], dtype=_np.int32)
    c.r = _np.array([], dtype=_np.int32)
    c.core = []
    for t in a:
        thetensor = t.tt if isinstance(t, _matrix.matrix) else t
        c.d += thetensor.d
        c.n = _np.concatenate((c.n, thetensor.n))
        c.r = _np.concatenate((c.r[:-1], thetensor.r))
        c.core = _np.concatenate((c.core, thetensor.core))
    c.get_ps()
    return c