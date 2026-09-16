def special(self, name, value=None, default=None):
    if not isinstance(name, basestring):
        raise TypeError('name must be a string')
    if not _specialName.match(name):
        raise ValueError('special name must match "%s"' % _specialSyntax)
    if value is None:
        try:
            return self._special[name]
        except KeyError:
            return default
    else:
        try:
            JSON.encode(value)
        except TypeError:
            raise ValueError('value can not be encoded to JSON')
        self._special[name] = value