def _reverse(self):
    n = [BYTE_REVERSAL_DICT[b] for b in self._datastore.rawbytes]
    n.reverse()
    newoffset = 8 - (self._offset + self.len) % 8
    if newoffset == 8:
        newoffset = 0
    self._setbytes_unsafe(bytearray().join(n), self.length, newoffset)