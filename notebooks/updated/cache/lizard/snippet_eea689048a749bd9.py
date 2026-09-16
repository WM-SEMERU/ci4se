def dvcircdR(self, R, phi=None):
    return 0.5 * (-self.Rforce(R, 0.0, phi=phi, use_physical=False) + R *
        self.R2deriv(R, 0.0, phi=phi, use_physical=False)) / self.vcirc(R,
        phi=phi, use_physical=False)