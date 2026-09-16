def set_bitfield_padded(self, val):
    self._padded_bitfield = val
    self._stream.padded = val
    self._ctxt._pfp__padded_bitfield = val