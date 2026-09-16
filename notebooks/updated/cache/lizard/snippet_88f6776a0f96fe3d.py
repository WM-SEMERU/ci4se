def _validate(self):
    self._disable_patching = True
    self._validate_base(self)
    self._disable_patching = False