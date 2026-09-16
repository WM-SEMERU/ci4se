def _sample_coef(self, X, y, weights=None, n_draws=100, n_bootstraps=1,
    objective='auto'):
    if not self._is_fitted:
        raise AttributeError('GAM has not been fitted. Call fit first.')
    if n_bootstraps < 1:
        raise ValueError('n_bootstraps must be >= 1; got {}'.format(
            n_bootstraps))
    if n_draws < 1:
        raise ValueError('n_draws must be >= 1; got {}'.format(n_draws))
    coef_bootstraps, cov_bootstraps = self._bootstrap_samples_of_smoothing(X,
        y, weights=weights, n_bootstraps=n_bootstraps, objective=objective)
    coef_draws = self._simulate_coef_from_bootstraps(n_draws,
        coef_bootstraps, cov_bootstraps)
    return coef_draws