def set_offset(self, offset):
    if not isinstance(offset, int) or offset < 0:
        raise DaftException('Offset should be a positive integer.')
    self._offset = str(offset)