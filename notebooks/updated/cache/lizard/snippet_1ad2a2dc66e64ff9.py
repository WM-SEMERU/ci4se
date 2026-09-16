def set_value(self, value, force=False):
    if force:
        self._value = value
        return
    if value is None:
        self._value = value
        return
    if isinstance(value, six.integer_types):
        self._value = value
        return
    if isinstance(value, six.string_types):
        for v, n in self.enums.items():
            if n == value:
                self._value = v
                return
        raise ValueError('Unable to find value name in enum list')
    raise TypeError(
        "Value for '%s' must by of type String or Integer not '%s'" % (self
        .name, type(value)))