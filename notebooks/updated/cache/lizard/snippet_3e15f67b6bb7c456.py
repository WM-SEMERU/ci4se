def e(self, analytic=False, pot=None):
    if analytic:
        self._setupaA(pot=pot, type='adiabatic')
        rperi, rap = self._aA.calcRapRperi(self)
        return (rap - rperi) / (rap + rperi)
    if not hasattr(self, 'orbit'):
        raise AttributeError(
            'Integrate the orbit first or use analytic=True for approximate eccentricity'
            )
    if not hasattr(self, 'rs'):
        self.rs = self.orbit[:, (0)]
    return (nu.amax(self.rs) - nu.amin(self.rs)) / (nu.amax(self.rs) + nu.
        amin(self.rs))