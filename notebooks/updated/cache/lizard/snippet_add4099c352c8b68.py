def accuracy(self, X=None, y=None, mu=None):
    if not self._is_fitted:
        raise AttributeError('GAM has not been fitted. Call fit first.')
    y = check_y(y, self.link, self.distribution, verbose=self.verbose)
    if X is not None:
        X = check_X(X, n_feats=self.statistics_['m_features'], edge_knots=
            self.edge_knots_, dtypes=self.dtype, features=self.feature,
            verbose=self.verbose)
    if mu is None:
        mu = self.predict_mu(X)
    check_X_y(mu, y)
    return ((mu > 0.5).astype(int) == y).mean()