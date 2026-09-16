def TrTp(self, pot=None, **kwargs):
    if not pot is None:
        pot = flatten_potential(pot)
    _check_consistent_units(self, pot)
    self._orb._setupaA(pot=pot, **kwargs)
    if self._orb._aAType.lower() == 'isochroneapprox':
        return float(self._orb._aA.actionsFreqs(self())[4][0] / self._orb.
            _aA.actionsFreqs(self())[3][0] * nu.pi)
    else:
        return float(self._orb._aA.actionsFreqs(self)[4][0] / self._orb._aA
            .actionsFreqs(self)[3][0] * nu.pi)