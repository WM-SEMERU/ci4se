def sample(self, n, mass_min=0.1, mass_max=10.0, steps=10000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    d_mass = (mass_max - mass_min) / float(steps)
    mass = np.linspace(mass_min, mass_max, steps)
    cdf = np.insert(np.cumsum(d_mass * self.pdf(mass[1:], log_mode=False)),
        0, 0.0)
    cdf = cdf / cdf[-1]
    f = scipy.interpolate.interp1d(cdf, mass)
    return f(np.random.uniform(size=n))