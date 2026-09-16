def encode(cls, value):
    try:
        if float(value) + 0 == value:
            return repr(value)
    except (TypeError, ValueError):
        pass
    raise InvalidValue('not a float')