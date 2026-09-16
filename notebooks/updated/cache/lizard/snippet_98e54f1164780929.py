def _get_unit_factor(cls, unit):
    try:
        if isinstance(unit, str):
            unit = cls.UNIT_FACTOR_NAMES[unit]
        return cls.UNIT_FACTORS[unit]
    except KeyError:
        raise UnsupportedUnitError()