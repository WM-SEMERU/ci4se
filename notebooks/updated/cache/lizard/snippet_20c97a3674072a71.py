def __int(value):
    valid, _value = False, value
    try:
        _value = int(value)
        valid = True
    except ValueError:
        pass
    return valid, _value, 'integer'