def rhochange(self):
    if self.opt['HighMemSolve'] and self.cri.Cd == 1:
        self.c = sl.solvedbd_sm_c(self.Df, np.conj(self.Df), self.mu / self
            .rho * self.GHGf + 1.0, self.cri.axisM)