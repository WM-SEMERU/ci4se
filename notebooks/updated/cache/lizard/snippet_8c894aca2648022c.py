def randsphere(n, rstate=None):
    if rstate is None:
        rstate = np.random
    z = rstate.randn(n)
    zhat = z / lalg.norm(z)
    xhat = zhat * rstate.rand() ** (1.0 / n)
    return xhat