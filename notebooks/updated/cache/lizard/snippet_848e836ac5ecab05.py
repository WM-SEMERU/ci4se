def domain(self, expparams):
    return [MultinomialDomain(n_elements=self.n_sides, n_meas=ep['n_meas']) for
        ep in expparams]