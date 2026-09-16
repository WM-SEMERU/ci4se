def fit(self, X):
    if X.ndim > 2:
        X = X.reshape((np.prod(X.shape[:-1]), X.shape[-1]))
    self.mean = X.mean(0)
    self.std = X.std(0)
    self.is_fit = True
    return self