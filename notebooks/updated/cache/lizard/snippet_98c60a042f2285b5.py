def fromHexString(cls, value, internalFormat=False, prepend=None):
    try:
        value = SizedInteger(value, 16).setBitLength(len(value) * 4)
    except ValueError:
        raise error.PyAsn1Error('%s.fromHexString() error: %s' % (cls.
            __name__, sys.exc_info()[1]))
    if prepend is not None:
        value = SizedInteger(SizedInteger(prepend) << len(value) | value
            ).setBitLength(len(prepend) + len(value))
    if not internalFormat:
        value = cls(value)
    return value