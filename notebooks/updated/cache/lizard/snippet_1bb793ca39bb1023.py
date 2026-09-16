def write8(self, offset, value):
    if not isinstance(offset, (int, long)):
        raise TypeError('Invalid offset type, should be integer.')
    if not isinstance(value, (int, long)):
        raise TypeError('Invalid value type, should be integer.')
    if value < 0 or value > 255:
        raise ValueError('Value out of bounds.')
    offset = self._adjust_offset(offset)
    self._validate_offset(offset, 1)
    self.mapping[offset:offset + 1] = struct.pack('B', value)