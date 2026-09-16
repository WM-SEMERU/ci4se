def to_seconds(value, time_unit):
    if isinstance(value, bool):
        raise TypeError
    return float(value) * time_unit