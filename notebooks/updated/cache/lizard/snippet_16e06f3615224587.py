def bisect(func, a, b, xtol=1e-12, maxiter=100):
    fa = func(a)
    if fa == 0.0:
        return a
    fb = func(b)
    if fb == 0.0:
        return b
    assert sign(fa) != sign(fb)
    for i in xrange(maxiter):
        c = (a + b) / 2.0
        fc = func(c)
        if fc == 0.0 or abs(b - a) / 2.0 < xtol:
            return c
        if sign(fc) == sign(func(a)):
            a = c
        else:
            b = c
    else:
        raise RuntimeError('Failed to converge after %d iterations.' % maxiter)