def _parseResource(name, value):
    assert name in ('memory', 'disk', 'cores')
    if value is None:
        return value
    elif isinstance(value, (str, bytes)):
        value = human2bytes(value)
    if isinstance(value, int):
        return value
    elif isinstance(value, float) and name == 'cores':
        return value
    else:
        raise TypeError(
            "The '%s' requirement does not accept values that are of %s" %
            (name, type(value)))