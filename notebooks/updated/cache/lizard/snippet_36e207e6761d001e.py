def project_result(self, X):
    X = np.asarray(X)
    if self.normalizer is not None:
        X = self.normalizer.inverse_transform(X)
    return self.clip(X)