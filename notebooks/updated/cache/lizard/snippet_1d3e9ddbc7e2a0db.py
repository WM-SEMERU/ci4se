def calc_uv(self, x, y, prev=False):
    assert len(x) == self.N
    assert len(y) == self.N
    u = np.zeros(self.N, self.x.dtype)
    v = np.zeros(self.N, self.y.dtype)
    for n in xrange(self.N):
        if prev:
            x0 = self.xprev[np.r_[:n, n + 1:self.N]]
            y0 = self.yprev[np.r_[:n, n + 1:self.N]]
        else:
            x0 = self.x[np.r_[:n, n + 1:self.N]]
            y0 = self.y[np.r_[:n, n + 1:self.N]]
        s0 = self.s[np.r_[:n, n + 1:self.N]]
        u0, v0 = self.uv_at_xy(x[n], y[n], x0, y0, s0)
        u[n] = u0.sum()
        v[n] = v0.sum()
    return u, v