def set_params(self, l2_regularization=0.0, optimizer=None,
    optimizer_kwargs=None):
    self.l2_regularization = l2_regularization
    self._optimizer = optimizer
    self._optimizer_kwargs = optimizer_kwargs
    return self