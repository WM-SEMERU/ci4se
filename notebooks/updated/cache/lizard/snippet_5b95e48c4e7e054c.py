def loglike(self, y, f, n):
    r
    ll = binom.logpmf(y, n=n, p=expit(f))
    return ll