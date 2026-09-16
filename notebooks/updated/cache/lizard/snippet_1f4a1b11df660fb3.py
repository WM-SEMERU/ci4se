def ystep(self):
    r
    self.Y[(...), 0:-1] = sp.prox_l2(self.AX[(...), 0:-1] + self.U[(...), 0
        :-1], self.lmbda / self.rho * self.Wtvna, axis=self.saxes)
    self.Y[..., -1] = sp.prox_l1(self.AX[..., -1] + self.U[..., -1] - self.
        S, 1.0 / self.rho * self.Wdf)