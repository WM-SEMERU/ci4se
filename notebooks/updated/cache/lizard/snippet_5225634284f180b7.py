def xyinterp(x, y, xval):
    if len(x) != len(y):
        raise ValueError('Input arrays must be equal lengths')
    if xval < x[0]:
        raise ValueError('Value %f < min(x) %f: Extrapolation unsupported' %
            (xval, x[0]))
    if xval > x[-1]:
        raise ValueError('Value > max(x): Extrapolation unsupported')
    if x.argsort().all() != N.arange(len(x)).all():
        raise ValueError('Input array x must be sorted')
    hi = x.searchsorted(xval)
    lo = hi - 1
    try:
        seg = (float(xval) - x[lo]) / (x[hi] - x[lo])
    except ZeroDivisionError:
        seg = 0.0
    yval = y[lo] + seg * (y[hi] - y[lo])
    return yval