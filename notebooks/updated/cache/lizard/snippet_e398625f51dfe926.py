def find(self, bs, start=None, end=None, bytealigned=None):
    bs = Bits(bs)
    if not bs.len:
        raise ValueError('Cannot find an empty bitstring.')
    start, end = self._validate_slice(start, end)
    if bytealigned is None:
        bytealigned = globals()['bytealigned']
    if bytealigned and not bs.len % 8 and not self._datastore.offset:
        p = self._findbytes(bs.bytes, start, end, bytealigned)
    else:
        p = self._findregex(re.compile(bs._getbin()), start, end, bytealigned)
    try:
        self._pos = p[0]
    except (AttributeError, IndexError):
        pass
    return p