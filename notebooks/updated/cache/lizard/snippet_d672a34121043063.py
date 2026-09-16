def _validate(self, value):
    if not isinstance(value, self._enum_type):
        raise TypeError('Expected a %s instance, got %r instead' % (self.
            _enum_type.__name__, value))