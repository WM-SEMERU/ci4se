def minmax(self, minimum=None, maximum=None):
    if minimum is None and maximum is None:
        return {'minimum': self._minimum, 'maximum': self._maximum}
    if minimum is not None:
        if not isinstance(minimum, (int, long)):
            if isinstance(minimum, basestring) and _typeToRegex['int'].match(
                minimum):
                minimum = int(minimum, 0)
            else:
                raise ValueError('minimum')
        if minimum < 0:
            raise ValueError('minimum')
        self._minimum = minimum
    if maximum is not None:
        if not isinstance(maximum, (int, long)):
            if isinstance(maximum, basestring) and _typeToRegex['int'].match(
                maximum):
                maximum = int(maximum, 0)
            else:
                raise ValueError('minimum')
        if maximum < 0:
            raise ValueError('maximum')
        if self._minimum and maximum < self._minimum:
            raise ValueError('maximum')
        self._maximum = maximum