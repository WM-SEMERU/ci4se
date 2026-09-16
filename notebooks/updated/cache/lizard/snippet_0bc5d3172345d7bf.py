def bisect(f, a, b, args=(), xtol=_xtol, rtol=_rtol, maxiter=_iter, disp=True):
    if xtol <= 0:
        raise ValueError('xtol is too small (<= 0)')
    if maxiter < 1:
        raise ValueError('maxiter must be greater than 0')
    xa = a * 1.0
    xb = b * 1.0
    fa = f(xa, *args)
    fb = f(xb, *args)
    funcalls = 2
    root, status = _bisect_interval(xa, xb, fa, fb)
    if status == _ECONVERGED:
        itr = 0
    else:
        dm = xb - xa
        for itr in range(maxiter):
            dm *= 0.5
            xm = xa + dm
            fm = f(xm, *args)
            funcalls += 1
            if fm * fa >= 0:
                xa = xm
            if fm == 0 or abs(dm) < xtol + rtol * abs(xm):
                root = xm
                status = _ECONVERGED
                itr += 1
                break
    if disp and status == _ECONVERR:
        raise RuntimeError('Failed to converge')
    return _results((root, funcalls, itr, status))