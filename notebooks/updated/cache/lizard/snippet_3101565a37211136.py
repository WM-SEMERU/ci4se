def allclose(a, b, align=False, rtol=1e-05, atol=1e-08):
    return np.alltrue(isclose(a, b, align=align, rtol=rtol, atol=atol))