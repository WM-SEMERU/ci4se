def fit(self, frequency, recency, T, weights=None, iterative_fitting=1,
    initial_params=None, verbose=False, tol=0.0001, index=None, fit_method=
    'Nelder-Mead', maxiter=2000, **kwargs):
    frequency = asarray(frequency).astype(int)
    recency = asarray(recency)
    T = asarray(T)
    if weights is None:
        weights = np.ones(recency.shape[0], dtype=np.int64)
    else:
        weights = asarray(weights)
    _check_inputs(frequency, recency, T)
    self._scale = _scale_time(T)
    scaled_recency = recency * self._scale
    scaled_T = T * self._scale
    params, self._negative_log_likelihood_ = self._fit((frequency,
        scaled_recency, scaled_T, weights, self.penalizer_coef),
        iterative_fitting, initial_params, 4, verbose, tol, fit_method,
        maxiter, **kwargs)
    self._hessian_ = None
    self.params_ = pd.Series(*(params, ['r', 'alpha', 's', 'beta']))
    self.params_['alpha'] /= self._scale
    self.params_['beta'] /= self._scale
    self.data = DataFrame({'frequency': frequency, 'recency': recency, 'T':
        T, 'weights': weights}, index=index)
    self.generate_new_data = lambda size=1: pareto_nbd_model(T, *self.
        _unload_params('r', 'alpha', 's', 'beta'), size=size)
    self.predict = self.conditional_expected_number_of_purchases_up_to_time
    return self