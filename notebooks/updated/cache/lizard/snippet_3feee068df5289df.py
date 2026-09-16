def log_pdf(self, y, mu, weights=None):
    if weights is None:
        weights = np.ones_like(mu)
    nu = weights / self.scale
    return sp.stats.gamma.logpdf(x=y, a=nu, scale=mu / nu)