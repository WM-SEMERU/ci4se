def fit(self, X, y=None, **fit_params):
    X = numpy.asarray(X)
    self._fit_estimators(X, y, **fit_params)
    Xt = self._predict_estimators(X)
    self.meta_estimator.fit(Xt, y)
    return self