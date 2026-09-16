def parameters_changed(self):
    self.posterior, self._log_marginal_likelihood, self.grad_dict = (self.
        inference_method.inference(self.kern, self.X, self.likelihood, self
        .Y_normalized, self.Y_metadata))
    self.likelihood.update_gradients(self.grad_dict['dL_dthetaL'])
    self.kern.update_gradients_direct(self.grad_dict['dL_dVar'], self.
        grad_dict['dL_dLen'])