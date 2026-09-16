def _surfdens(self, R, z, phi=0.0, t=0.0):
    return 2.0 * nu.exp(-self._alpha * R) / self._beta * (1.0 - nu.exp(-
        self._beta * nu.fabs(z)))