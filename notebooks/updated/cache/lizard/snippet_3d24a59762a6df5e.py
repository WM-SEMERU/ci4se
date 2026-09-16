def ikey(self, value):
    if value == self._defaults['iKey'] and 'iKey' in self._values:
        del self._values['iKey']
    else:
        self._values['iKey'] = value