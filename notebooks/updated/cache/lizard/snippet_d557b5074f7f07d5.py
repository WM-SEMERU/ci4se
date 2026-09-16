def sample(self, mu):
    return np.random.wald(mean=mu, scale=self.scale, size=None)