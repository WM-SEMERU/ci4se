def _read_mode_pocsp(self, size, kind):
    temp = self._read_binary(size)
    data = dict(kind=kind, length=size, start=True if int(temp[0]) else
        False, end=True if int(temp[1]) else False, filler=bytes(chr(int(
        temp[2:], base=2)), encoding='utf-8'))
    return data