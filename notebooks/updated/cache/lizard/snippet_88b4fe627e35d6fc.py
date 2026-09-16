def E(self, *args, **kwargs):
    if not kwargs.get('pot', None) is None:
        kwargs['pot'] = flatten_potential(kwargs.get('pot'))
    _check_consistent_units(self, kwargs.get('pot', None))
    return self._orb.E(*args, **kwargs)