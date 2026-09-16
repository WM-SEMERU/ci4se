def predictive_gradients(self, Xnew, kern=None):
    if kern is None:
        kern = self.kern
    mean_jac = np.empty((Xnew.shape[0], Xnew.shape[1], self.output_dim))
    for i in range(self.output_dim):
        mean_jac[:, :, (i)] = kern.gradients_X(self.posterior.
            woodbury_vector[:, i:i + 1].T, Xnew, self._predictive_variable)
    dv_dX = kern.gradients_X_diag(np.ones(Xnew.shape[0]), Xnew)
    if self.posterior.woodbury_inv.ndim == 3:
        var_jac = np.empty(dv_dX.shape + (self.posterior.woodbury_inv.shape
            [2],))
        var_jac[:] = dv_dX[:, :, (None)]
        for i in range(self.posterior.woodbury_inv.shape[2]):
            alpha = -2.0 * np.dot(kern.K(Xnew, self._predictive_variable),
                self.posterior.woodbury_inv[:, :, (i)])
            var_jac[:, :, (i)] += kern.gradients_X(alpha, Xnew, self.
                _predictive_variable)
    else:
        var_jac = dv_dX
        alpha = -2.0 * np.dot(kern.K(Xnew, self._predictive_variable), self
            .posterior.woodbury_inv)
        var_jac += kern.gradients_X(alpha, Xnew, self._predictive_variable)
    return mean_jac, var_jac