def update(self, z):
    for i, f in enumerate(self.filters):
        f.update(z)
        self.likelihood[i] = f.likelihood
    self.mu = self.cbar * self.likelihood
    self.mu /= np.sum(self.mu)
    self._compute_mixing_probabilities()
    self._compute_state_estimate()
    self.x_post = self.x.copy()
    self.P_post = self.P.copy()