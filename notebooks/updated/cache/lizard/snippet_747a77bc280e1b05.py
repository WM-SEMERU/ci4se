def propose(self):
    self.current_kernel = sum(self.cum_probs < random())
    kernel = self.kernels[self.current_kernel]
    self.phi = random(self._len) < self.p
    kernel()