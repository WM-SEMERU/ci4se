def _R2deriv(self, R, phi=0.0, t=0.0):
    return self._Pot.R2deriv(R, 0.0, phi=phi, t=t, use_physical=False)