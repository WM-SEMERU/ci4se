def rnormal(mu, tau, size=None):
    return np.random.normal(mu, 1.0 / np.sqrt(tau), size)