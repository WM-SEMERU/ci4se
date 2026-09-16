def _read_mptcp_fastclose(self, bits, size):
    ____ = self._read_fileng(1)
    rkey = self._read_fileng(8)
    data = dict(subtype='MP_FASTCLOSE', fastclose=dict(rkey=rkey))
    return data