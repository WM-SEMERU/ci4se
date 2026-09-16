def data(self, value):
    if value == self._defaults['data'] and 'data' in self._values:
        del self._values['data']
    else:
        self._values['data'] = value