def tags(self, value):
    if value == self._defaults['tags'] and 'tags' in self._values:
        del self._values['tags']
    else:
        self._values['tags'] = value