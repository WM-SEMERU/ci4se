def Marginal(self, i, name=''):
    pmf = Pmf(name=name)
    for vs, prob in self.Items():
        pmf.Incr(vs[i], prob)
    return pmf