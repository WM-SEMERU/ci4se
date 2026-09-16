def _setbin_safe(self, binstring):
    binstring = tidy_input_string(binstring)
    binstring = binstring.replace('0b', '')
    self._setbin_unsafe(binstring)