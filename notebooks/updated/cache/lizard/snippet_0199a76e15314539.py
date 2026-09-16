def predict(self, X):
    jll = self._joint_log_likelihood(X)
    return delayed(self.classes_)[da.argmax(jll, axis=1)]