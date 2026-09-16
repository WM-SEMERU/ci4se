def probability_density(self, X):
    self.check_fit()
    return norm.pdf(X, loc=self.mean, scale=self.std)