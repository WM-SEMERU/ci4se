def bingham_pdf(fit):
    e = fit.hyperbolic_axes
    e = e[2] ** 2 / e
    kappa = (e - e[2])[:-1]
    kappa /= kappa[-1]
    F = N.sqrt(N.pi) * confluent_hypergeometric_function(*kappa)
    ax = fit.axes
    Z = 1 / e
    M = ax
    F = 1 / hyp1f1(*(1 / Z))

    def pdf(coords):
        lon, lat = coords
        I = lat
        D = lon
        xhat = N.array(sph2cart(lon, lat)).T
        return 1 / (F * N.exp(dot(xhat.T, M, N.diag(Z), M.T, xhat)))
    return pdf