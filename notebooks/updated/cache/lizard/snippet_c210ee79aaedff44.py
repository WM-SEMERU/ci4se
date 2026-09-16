def deposit(self, pos, val):
    if not isinstance(val, BinWord):
        raise TypeError('deposit needs a BinWord')
    pos = operator.index(pos)
    if pos < 0:
        raise ValueError('depositing out of range')
    res = self
    res &= ~(val.mask << pos)
    res |= val.to_uint() << pos
    return res