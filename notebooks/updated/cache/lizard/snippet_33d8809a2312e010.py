def update_gradients_full(self, dL_dK, X, X2=None, reset=True):
    self.variance.gradient = np.sum(self.K(X, X2) * dL_dK) / self.variance
    dL_dr = self.dK_dr_via_X(X, X2) * dL_dK
    if self.ARD:
        tmp = dL_dr * self._inv_dist(X, X2)
        if X2 is None:
            X2 = X
        if use_stationary_cython:
            self.lengthscale.gradient = self._lengthscale_grads_cython(tmp,
                X, X2)
        else:
            self.lengthscale.gradient = self._lengthscale_grads_pure(tmp, X, X2
                )
    else:
        r = self._scaled_dist(X, X2)
        self.lengthscale.gradient = -np.sum(dL_dr * r) / self.lengthscale