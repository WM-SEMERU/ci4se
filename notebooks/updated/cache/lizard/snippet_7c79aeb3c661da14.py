def noncentral_t_like(x, mu, lam, nu):
    R
    mu = np.asarray(mu)
    lam = np.asarray(lam)
    nu = np.asarray(nu)
    return flib.nct(x, mu, lam, nu)