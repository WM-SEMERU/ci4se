def _validate(self, val):
    if self.allow_None and val is None:
        return
    super(Range, self)._validate(val)
    self._checkBounds(val)