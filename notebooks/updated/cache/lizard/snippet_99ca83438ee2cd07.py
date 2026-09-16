def inference(self, kern, X, likelihood, Y, mean_function=None, Y_metadata=None
    ):
    assert mean_function is None, 'inference with a mean function not implemented'
    K = kern.K(X)
    if self.bad_fhat or self.first_run:
        Ki_f_init = np.zeros_like(Y)
        self.first_run = False
    else:
        Ki_f_init = self._previous_Ki_fhat
    Ki_f_init = np.zeros_like(Y)
    f_hat, Ki_fhat = self.rasm_mode(K, Y, likelihood, Ki_f_init, Y_metadata
        =Y_metadata)
    log_marginal, woodbury_inv, dL_dK, dL_dthetaL = self.mode_computations(
        f_hat, Ki_fhat, K, Y, likelihood, kern, Y_metadata)
    self._previous_Ki_fhat = Ki_fhat.copy()
    return Posterior(woodbury_vector=Ki_fhat, woodbury_inv=woodbury_inv, K=K
        ), log_marginal, {'dL_dK': dL_dK, 'dL_dthetaL': dL_dthetaL}