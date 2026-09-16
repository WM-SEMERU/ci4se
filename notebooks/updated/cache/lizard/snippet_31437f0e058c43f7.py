def e(self, analytic=False, pot=None, **kwargs):
    if analytic:
        self._setupaA(pot=pot, **kwargs)
        return float(self._aA.EccZmaxRperiRap(self)[0])
    if not hasattr(self, 'orbit'):
        raise AttributeError(
            'Integrate the orbit first or use analytic=True for approximate eccentricity'
            )
    if not hasattr(self, 'rs'):
        self.rs = nu.sqrt(self.orbit[:, (0)] ** 2.0 + self.orbit[:, (3)] ** 2.0
            )
    return (nu.amax(self.rs) - nu.amin(self.rs)) / (nu.amax(self.rs) + nu.
        amin(self.rs))