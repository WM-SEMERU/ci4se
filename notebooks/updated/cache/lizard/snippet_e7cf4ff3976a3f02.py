def base_type(self, value):
    if value == self._defaults['baseType'] and 'baseType' in self._values:
        del self._values['baseType']
    else:
        self._values['baseType'] = value