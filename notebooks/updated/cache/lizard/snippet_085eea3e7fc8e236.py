def vra(self, *args, **kwargs):
    from .OrbitTop import _check_roSet, _check_voSet
    _check_roSet(self, kwargs, 'vra')
    _check_voSet(self, kwargs, 'vra')
    dist = self._orb.dist(*args, **kwargs)
    if _APY_UNITS and isinstance(dist, units.Quantity):
        out = units.Quantity(dist.to(units.kpc).value * _K * self._orb.pmra
            (*args, **kwargs).to(units.mas / units.yr).value, unit=units.km /
            units.s)
    else:
        out = dist * _K * self._orb.pmra(*args, **kwargs)
    if len(out) == 1:
        return out[0]
    else:
        return out