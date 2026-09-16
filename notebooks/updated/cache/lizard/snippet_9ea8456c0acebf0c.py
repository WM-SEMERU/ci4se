def read(self, offset, length):
    if not isinstance(offset, (int, long)):
        raise TypeError('Invalid offset type, should be integer.')
    offset = self._adjust_offset(offset)
    self._validate_offset(offset, length)
    return bytes(self.mapping[offset:offset + length])