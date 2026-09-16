def logpdf(self, mu):
    if self.transform is not None:
        mu = self.transform(mu)
    return ss.expon.logpdf(mu, self.lmd0)