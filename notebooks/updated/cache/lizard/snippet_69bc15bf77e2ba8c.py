def backward(self, out_grads=None):
    assert self.binded and self.params_initialized
    self._curr_module.backward(out_grads=out_grads)