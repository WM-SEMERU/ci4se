def predict_proba(self, X):
    y_probas = []
    for yp in self.forward_iter(X, training=False):
        yp = yp[0] if isinstance(yp, tuple) else yp
        y_probas.append(to_numpy(yp))
    y_proba = np.concatenate(y_probas, 0)
    return y_proba