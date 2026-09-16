def predict_moments(self, X):
    check_is_fitted(self, ['var_', 'regularizer_', 'weights_',
        'covariance_', 'hypers_'])
    X = check_array(X)
    Phi = self.basis.transform(X, *atleast_list(self.hypers_))
    Ey = Phi.dot(self.weights_)
    Vf = (Phi.dot(self.covariance_) * Phi).sum(axis=1)
    return Ey, Vf + self.var_