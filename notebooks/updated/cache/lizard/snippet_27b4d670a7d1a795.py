def n_outcomes(self, expparams):
    n = expparams['n_meas']
    k = self.n_sides
    return scipy.special.binom(n + k - 1, k - 1)