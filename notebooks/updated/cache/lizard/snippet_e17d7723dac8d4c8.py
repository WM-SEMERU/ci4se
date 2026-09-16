def validate(self):
    super(TaggedAsFilter, self).validate()
    self._value = self._value.lower()
    if self._value.startswith('='):
        self._exact = True
        self._value = self._value[1:]
    else:
        self._exact = not self._value
    if self._exact:
        self._value = set((self._value,)) if self._value else set()