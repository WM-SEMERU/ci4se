def _analyze(self):
    if self.value is None or self.value == self.previous:
        pass
    elif self._operation == 'add':
        self._additions = self.value
    elif self._operation == 'remove':
        self._removals = self.value
    elif self.previous is None:
        self._assignments = self.value
    else:
        self._additions = self.value - self.previous or None
        self._removals = self.previous - self.value or None
    self._analyzed = True