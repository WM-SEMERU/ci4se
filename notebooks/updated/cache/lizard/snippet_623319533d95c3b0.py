def predict(self, X):
    K = self._get_kernel(X, self.X_fit_)
    pred = -numpy.dot(self.coef_, K.T)
    return pred.ravel()