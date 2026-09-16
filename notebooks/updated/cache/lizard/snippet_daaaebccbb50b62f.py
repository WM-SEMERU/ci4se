def value(self, key, default=None):
    if self._customFormat:
        return self._customFormat.value(key, default)
    else:
        return unwrapVariant(super(XSettings, self).value(key))