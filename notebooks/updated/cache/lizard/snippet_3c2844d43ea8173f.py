def inv(self):
    self.v = 1 / self.v
    tmp = self.v ** 2
    if self.deriv > 1:
        self.dd[:] = tmp * (2 * self.v * np.outer(self.d, self.d) - self.dd)
    if self.deriv > 0:
        self.d[:] = -tmp * self.d[:]