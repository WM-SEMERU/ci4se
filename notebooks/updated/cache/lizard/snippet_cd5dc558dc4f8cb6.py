def sandbox():

    def fget(self):
        return self._options.get('sandbox', None)

    def fset(self, value):
        self._options['sandbox'] = value
    return locals()