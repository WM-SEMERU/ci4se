def _getLaplaceCovar(self):
    assert self.init, 'GP not initialised'
    assert self.fast == False, 'Not supported for fast implementation'
    if self.cache['Sigma'] is None:
        self.cache['Sigma'] = sp.linalg.inv(self._getHessian())
    return self.cache['Sigma']