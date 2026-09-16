def xistep(self, i):
    r
    self.YU[:] = self.Y - self.U[..., i]
    b = np.take(self.ZSf, [i], axis=self.cri.axisK) + self.rho * sl.rfftn(self
        .YU, None, self.cri.axisN)
    self.Xf[..., i] = sl.solvedbi_sm(np.take(self.Zf, [i], axis=self.cri.
        axisK), self.rho, b, axis=self.cri.axisM)
    self.X[..., i] = sl.irfftn(self.Xf[..., i], self.cri.Nv, self.cri.axisN)