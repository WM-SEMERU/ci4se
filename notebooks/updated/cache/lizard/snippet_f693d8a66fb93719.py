def _compute_mixing_probabilities(self):
    self.cbar = dot(self.mu, self.M)
    for i in range(self.N):
        for j in range(self.N):
            self.omega[i, j] = self.M[i, j] * self.mu[i] / self.cbar[j]