def _compute_state_estimate(self):
    self.x.fill(0)
    for f, mu in zip(self.filters, self.mu):
        self.x += f.x * mu
    self.P.fill(0)
    for f, mu in zip(self.filters, self.mu):
        y = f.x - self.x
        self.P += mu * (outer(y, y) + f.P)