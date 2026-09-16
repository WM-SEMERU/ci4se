def predict_withGradients(self, X):
    if X.ndim == 1:
        X = X[(None), :]
    m, v = self.model.predict(X)
    v = np.clip(v, 1e-10, np.inf)
    dmdx, dvdx = self.model.predictive_gradients(X)
    dmdx = dmdx[:, :, (0)]
    dsdx = dvdx / (2 * np.sqrt(v))
    return m, np.sqrt(v), dmdx, dsdx