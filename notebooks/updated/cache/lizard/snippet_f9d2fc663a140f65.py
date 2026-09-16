def _mdens_deriv(self, m):
    return -self.a3 * (self.a + 3.0 * m) / m ** 2 / (self.a + m) ** 3