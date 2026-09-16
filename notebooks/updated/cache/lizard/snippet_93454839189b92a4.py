def eye(n, d=None):
    c = _matrix.matrix()
    c.tt = _vector.vector()
    if d is None:
        n0 = _np.asanyarray(n, dtype=_np.int32)
        c.tt.d = n0.size
    else:
        n0 = _np.asanyarray([n] * d, dtype=_np.int32)
        c.tt.d = d
    c.n = n0.copy()
    c.m = n0.copy()
    c.tt.n = c.n * c.m
    c.tt.r = _np.ones((c.tt.d + 1,), dtype=_np.int32)
    c.tt.get_ps()
    c.tt.alloc_core()
    for i in xrange(c.tt.d):
        c.tt.core[c.tt.ps[i] - 1:c.tt.ps[i + 1] - 1] = _np.eye(c.n[i]).flatten(
            )
    return c