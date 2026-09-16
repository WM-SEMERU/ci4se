def _read_para_echo_request_unsigned(self, code, cbit, clen, *, desc,
    length, version):
    _data = self._read_fileng(clen)
    echo_request_unsigned = dict(type=desc, critical=cbit, length=clen,
        data=_data)
    _plen = length - clen
    if _plen:
        self._read_fileng(_plen)
    return echo_request_unsigned