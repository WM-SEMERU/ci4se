def set_unit(self, unit):
    if unit is None or isinstance(unit, units.NamedUnit
        ) and unit.physical_type == 'time':
        self._unit = unit
        return
    if isinstance(unit, Number):
        unit = units.Unit(unit * units.second)
    try:
        unit = units.Unit(unit)
    except ValueError as exc:
        try:
            unit = units.Unit(str(unit).rstrip('s'))
        except ValueError:
            raise exc
    dec = unit.decompose()
    if dec.bases != [units.second]:
        raise ValueError('Cannot set GPS unit to %s' % unit)
    for other in TIME_UNITS:
        if other.decompose().scale == dec.scale:
            self._unit = other
            return
    raise ValueError('Unrecognised unit: %s' % unit)