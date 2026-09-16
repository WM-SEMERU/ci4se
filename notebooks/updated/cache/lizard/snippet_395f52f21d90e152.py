def fit(self, X, y, weights=None):
    self._validate_params()
    y = check_y(y, self.link, self.distribution, verbose=self.verbose)
    X = check_X(X, verbose=self.verbose)
    check_X_y(X, y)
    if weights is not None:
        weights = np.array(weights).astype('f').ravel()
        weights = check_array(weights, name='sample weights', ndim=1,
            verbose=self.verbose)
        check_lengths(y, weights)
    else:
        weights = np.ones_like(y).astype('float64')
    self._validate_data_dep_params(X)
    if not hasattr(self, 'logs_'):
        self.logs_ = defaultdict(list)
    self.statistics_ = {}
    self.statistics_['n_samples'] = len(y)
    self.statistics_['m_features'] = X.shape[1]
    self._pirls(X, y, weights)
    return self