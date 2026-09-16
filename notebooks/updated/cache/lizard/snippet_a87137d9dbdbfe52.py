def dom_processing(self, value):
    if value == self._defaults['domProcessing'
        ] and 'domProcessing' in self._values:
        del self._values['domProcessing']
    else:
        self._values['domProcessing'] = value