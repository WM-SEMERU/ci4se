def update_gradients(self, grads):
    self.sigma2.gradient = grads[0]
    self.v.gradient = grads[1]