def to_bytesize(value, default_unit=None, base=DEFAULT_BASE):
    if isinstance(value, (int, float)):
        return unitized(value, default_unit, base)
    if value is None:
        return None
    try:
        if value[-1].lower() == 'b':
            value = value[:-1]
        unit = value[-1:].lower()
        if unit.isdigit():
            unit = default_unit
        else:
            value = value[:-1]
        return unitized(to_number(float, value), unit, base)
    except (IndexError, TypeError, ValueError):
        return None