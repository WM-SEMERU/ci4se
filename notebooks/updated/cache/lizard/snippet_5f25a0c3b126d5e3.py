def line_search_armijo(f, xk, pk, gfk, old_fval, args=(), c1=0.0001, alpha0
    =0.99):
    xk = np.atleast_1d(xk)
    fc = [0]

    def phi(alpha1):
        fc[0] += 1
        return f(xk + alpha1 * pk, *args)
    if old_fval is None:
        phi0 = phi(0.0)
    else:
        phi0 = old_fval
    derphi0 = np.sum(pk * gfk)
    alpha, phi1 = scalar_search_armijo(phi, phi0, derphi0, c1=c1, alpha0=alpha0
        )
    return alpha, fc[0], phi1