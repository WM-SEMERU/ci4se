def fit(self, X, y):
    X, event, time = check_arrays_survival(X, y)
    if self.alpha <= 0:
        raise ValueError('alpha must be positive')
    if not 0 <= self.rank_ratio <= 1:
        raise ValueError('rank_ratio must be in [0; 1]')
    if self.fit_intercept and self.rank_ratio == 1.0:
        raise ValueError(
            'fit_intercept=True is only meaningful if rank_ratio < 1.0')
    if self.rank_ratio < 1.0:
        if self.optimizer in {'simple', 'PRSVM'}:
            raise ValueError(
                "optimizer '%s' does not implement regression objective" %
                self.optimizer)
        if (time <= 0).any():
            raise ValueError(
                'observed time contains values smaller or equal to zero')
        time = numpy.log(time)
        assert numpy.isfinite(time).all()
    random_state = check_random_state(self.random_state)
    samples_order = BaseSurvivalSVM._argsort_and_resolve_ties(time,
        random_state)
    opt_result = self._fit(X, time, event, samples_order)
    coef = opt_result.x
    if self.fit_intercept:
        self.coef_ = coef[1:]
        self.intercept_ = coef[0]
    else:
        self.coef_ = coef
    if not opt_result.success:
        warnings.warn('Optimization did not converge: ' + opt_result.
            message, category=ConvergenceWarning, stacklevel=2)
    self.optimizer_result_ = opt_result
    return self