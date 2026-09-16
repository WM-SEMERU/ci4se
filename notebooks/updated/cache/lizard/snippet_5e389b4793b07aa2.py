def is_unit_or_unitstring(value):
    if is_unit(value)[0]:
        return True, value
    try:
        unit = units.Unit(value)
    except:
        return False, value
    else:
        return True, unit