def newton_secant(func, x0, args=(), tol=1.48e-08, maxiter=50, disp=True):
    if tol <= 0:
        raise ValueError('tol is too small <= 0')
    if maxiter < 1:
        raise ValueError('maxiter must be greater than 0')
    p0 = 1.0 * x0
    funcalls = 0
    status = _ECONVERR
    if x0 >= 0:
        p1 = x0 * (1 + 0.0001) + 0.0001
    else:
        p1 = x0 * (1 + 0.0001) - 0.0001
        q0 = func(p0, *args)
    funcalls += 1
    q1 = func(p1, *args)
    funcalls += 1
    for itr in range(maxiter):
        if q1 == q0:
            p = (p1 + p0) / 2.0
            status = _ECONVERGED
            break
        else:
            p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if np.abs(p - p1) < tol:
            status = _ECONVERGED
            break
        p0 = p1
        q0 = q1
        p1 = p
        q1 = func(p1, *args)
        funcalls += 1
    if disp and status == _ECONVERR:
        msg = 'Failed to converge'
        raise RuntimeError(msg)
    return _results((p, funcalls, itr + 1, status))