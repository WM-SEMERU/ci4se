def sample(self, mu):
    standard_deviation = self.scale ** 0.5 if self.scale else 1.0
    return np.random.normal(loc=mu, scale=standard_deviation, size=None)