def logpdf(self, mu):
    if self.transform is not None:
        mu = self.transform(mu)
    return ss.poisson.logpmf(mu, self.lmd0)