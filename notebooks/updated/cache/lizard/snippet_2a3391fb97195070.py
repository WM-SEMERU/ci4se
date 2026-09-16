def _truncateend(self, bits):
    assert 0 <= bits <= self.len
    if not bits:
        return
    if bits == self.len:
        self._clear()
        return
    newlength_in_bytes = (self._offset + self.len - bits + 7) // 8
    self._setbytes_unsafe(self._datastore.getbyteslice(0,
        newlength_in_bytes), self.len - bits, self._offset)
    assert self._assertsanity()