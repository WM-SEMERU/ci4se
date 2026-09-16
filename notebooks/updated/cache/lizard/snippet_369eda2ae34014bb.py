def _transform_new_data(self, X, subject):
    S = np.zeros_like(X)
    R = None
    for i in range(self.n_iter):
        R = self.w_[subject].T.dot(X - S)
        S = self._shrink(X - self.w_[subject].dot(R), self.lam)
    return R, S