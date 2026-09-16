def _from_derivatives(xi, yi, x, order=None, der=0, extrapolate=False):
    from scipy import interpolate
    method = interpolate.BPoly.from_derivatives
    m = method(xi, yi.reshape(-1, 1), orders=order, extrapolate=extrapolate)
    return m(x)