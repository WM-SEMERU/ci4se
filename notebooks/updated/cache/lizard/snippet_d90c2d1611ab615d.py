def coerce(cls, arg):
    try:
        return cls(arg).value
    except (ValueError, TypeError):
        raise InvalidParameterDatatype('%s coerce error' % (cls.__name__,))