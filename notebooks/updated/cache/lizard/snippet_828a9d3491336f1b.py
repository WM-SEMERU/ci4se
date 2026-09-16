def _evaluate_fits(self, x, fit_key):
    fit = self.fits[fit_key]
    fit_params = self._get_fit_params(np.copy(x), fit_key)
    if type(fit) == list:
        res = []
        for i in range(len(fit)):
            res.append(fit[i](fit_params))
        return np.array(res)
    else:
        return fit(fit_params)