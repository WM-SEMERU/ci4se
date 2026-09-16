def decode(self, s, _w=WHITESPACE.match):
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    end = _w(s, end).end()
    if end != len(s):
        raise JSONDecodeError('Extra data', s, end, len(s))
    return obj