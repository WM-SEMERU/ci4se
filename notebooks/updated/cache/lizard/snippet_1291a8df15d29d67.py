def self_signed(self, value):
    self._self_signed = bool(value)
    if self._self_signed:
        self._issuer = None