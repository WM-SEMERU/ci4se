def fit(self, X):
    self.constant_value = self._get_constant_value(X)
    if self.constant_value is None:
        self.model = scipy.stats.gaussian_kde(X)
    else:
        self._replace_constant_methods()
    self.fitted = True