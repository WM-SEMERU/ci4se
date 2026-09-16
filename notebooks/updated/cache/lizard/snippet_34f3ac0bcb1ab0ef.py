def to_bytes(self):
    rawlist = []
    i = len(self._headers) - 1
    while i >= 0:
        self._headers[i].pre_serialize(b''.join(rawlist), self, i)
        rawlist.insert(0, self._headers[i].to_bytes())
        i -= 1
    self._raw = b''.join(rawlist)
    return self._raw