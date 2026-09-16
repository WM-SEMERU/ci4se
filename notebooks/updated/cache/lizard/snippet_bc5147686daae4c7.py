def rmean(self):
    if not _np.all(self.n):
        return 0
    a = _np.sum(self.n[1:-1])
    b = self.n[0] + self.n[-1]
    c = -_np.sum(self.n * self.r[1:] * self.r[:-1])
    D = b ** 2 - 4 * a * c
    r = 0.5 * (-b + _np.sqrt(D)) / a
    return r