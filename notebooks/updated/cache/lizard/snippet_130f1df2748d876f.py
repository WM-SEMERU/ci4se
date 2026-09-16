def _mdens_deriv(self, m):
    return -self._mdens(m) * (self.a * self.alpha + self.beta * m) / m / (self
        .a + m)