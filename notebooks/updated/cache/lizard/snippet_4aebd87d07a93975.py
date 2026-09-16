def _normalize_value_ms(cls, value):
    value = round(value / 1000) * 1000
    sorted_units = sorted(cls.UNITS_IN_MILLISECONDS.items(), key=lambda x:
        x[1], reverse=True)
    for unit, unit_in_ms in sorted_units:
        unit_value = value / unit_in_ms
        if unit_value.is_integer():
            return int(unit_value), unit
    return value, MILLISECOND