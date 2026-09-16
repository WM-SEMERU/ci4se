def _read_mode_mptcp(self, size, kind):
    bins = self._read_binary(1)
    subt = int(bins[:4], base=2)
    bits = bins[4:]
    dlen = size - 1
    func = mptcp_opt.get(subt)
    if func is None:
        temp = self._read_fileng(dlen)
        data = dict(kind=kind, length=size, subtype='Unknown', data=bytes(
            chr(int(bits[:4], base=2)), encoding='utf-8') + temp)
    else:
        data = func(self, bits, dlen, kind)
    return data