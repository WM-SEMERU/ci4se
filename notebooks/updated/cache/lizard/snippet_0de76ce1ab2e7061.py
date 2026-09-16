def normalizeIdentifier(value):
    if value is None:
        return value
    if not isinstance(value, basestring):
        raise TypeError('Identifiers must be strings, not %s.' % type(value
            ).__name__)
    if len(value) == 0:
        raise ValueError('The identifier string is empty.')
    if len(value) > 100:
        raise ValueError(
            'The identifier string has a length (%d) greater than the maximum allowed (100).'
             % len(value))
    for c in value:
        v = ord(c)
        if v < 32 or v > 126:
            raise ValueError(
                "The identifier string ('%s') contains a character out size of the range 0x20 - 0x7E."
                 % value)
    return unicode(value)