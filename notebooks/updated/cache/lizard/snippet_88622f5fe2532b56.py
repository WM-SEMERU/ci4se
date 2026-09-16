def rguiding(self, *args, **kwargs):
    pot = kwargs.get('pot', self._orb.__dict__.get('_pot', None))
    if pot is None:
        raise RuntimeError(
            'You need to specify the potential as pot= to compute the guiding-center radius'
            )
    flatten_potential(pot)
    if _isNonAxi(pot):
        raise RuntimeError(
            'Potential given to rguiding is non-axisymmetric, but rguiding requires an axisymmetric potential'
            )
    _check_consistent_units(self, pot)
    Lz = self.Lz(*args, use_physical=False)
    return nu.array([rl(pot, lz, use_physical=False) for lz in Lz])