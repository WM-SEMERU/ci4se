def setbit(self, key, offset, value):
    if not isinstance(offset, int):
        raise TypeError('offset argument must be int')
    if offset < 0:
        raise ValueError('offset must be greater equal 0')
    if value not in (0, 1):
        raise ValueError('value argument must be either 1 or 0')
    return self.execute(b'SETBIT', key, offset, value)