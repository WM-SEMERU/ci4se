def _resample_nu(self, tau, N_steps=100, prop_std=0.1, alpha=1, beta=1):
    taus = [tau] if isinstance(tau, np.ndarray) else tau
    N = 0
    E_tau = 0
    E_logtau = 0
    for tau in taus:
        bad = ~np.isfinite(tau)
        N += np.sum(~bad)
        E_tau += np.sum(tau[~bad])
        E_logtau += np.sum(np.log(tau[~bad]))
    if N > 0:
        E_tau /= N
        E_logtau /= N
    lprior = lambda nu: (alpha - 1) * np.log(nu) - alpha * nu
    ll = lambda nu: N * (nu / 2 * np.log(nu / 2) - gammaln(nu / 2) + (nu / 
        2 - 1) * E_logtau - nu / 2 * E_tau)
    lp = lambda nu: ll(nu) + lprior(nu)
    lp_curr = lp(self.nu)
    for step in range(N_steps):
        nu_new = self.nu + prop_std * np.random.randn()
        if nu_new < 0.001:
            continue
        lp_new = lp(nu_new)
        if np.log(np.random.rand()) < lp_new - lp_curr:
            self.nu = nu_new
            lp_curr = lp_new