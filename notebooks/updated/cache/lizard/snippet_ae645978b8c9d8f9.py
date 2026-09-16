def admm_linearized_simple(x, f, g, L, tau, sigma, niter, **kwargs):
    callback = kwargs.pop('callback', None)
    z = L.range.zero()
    u = L.range.zero()
    for _ in range(niter):
        x[:] = f.proximal(tau)(x - tau / sigma * L.adjoint(L(x) + u - z))
        z = g.proximal(sigma)(L(x) + u)
        u = L(x) + u - z
        if callback is not None:
            callback(x)