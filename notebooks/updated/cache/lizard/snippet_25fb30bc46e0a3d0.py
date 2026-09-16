def _solve_location_param(self):
    params = copy.copy(self.params)
    del params['loc']
    f = lambda location: self.distr_f.ppf(0.5, loc=location, **params) - 1
    return optimize.brentq(f, -10, 10)