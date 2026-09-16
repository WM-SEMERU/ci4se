def sample_radius(self, n):
    edge = (self.edge if self.edge < 20 * self.extension else 20 * self.
        extension)
    radius = np.linspace(0, edge, 100000.0)
    pdf = self._pdf(radius) * np.sin(np.radians(radius))
    cdf = np.cumsum(pdf)
    cdf /= cdf[-1]
    fn = scipy.interpolate.interp1d(cdf, list(range(0, len(cdf))))
    index = np.floor(fn(np.random.uniform(size=n))).astype(int)
    return radius[index]