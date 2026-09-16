def source(self, value):
    if value == self._defaults['source'] and 'source' in self._values:
        del self._values['source']
    else:
        self._values['source'] = value