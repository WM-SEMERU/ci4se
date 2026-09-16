def Var(self, mu=None):
    if mu is None:
        mu = self.Mean()
    var = 0.0
    for x, p in self.d.iteritems():
        var += p * (x - mu) ** 2
    return var