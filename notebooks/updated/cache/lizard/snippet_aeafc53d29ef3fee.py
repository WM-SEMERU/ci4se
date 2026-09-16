def _read_data_type_rpl(self, length):
    _cmpr = self._read_binary(1)
    _padr = self._read_binary(1)
    _resv = self._read_fileng(2)
    _inti = int(_cmpr[:4], base=2)
    _inte = int(_cmpr[4:], base=2)
    _plen = int(_padr[:4], base=2)
    _ilen = 16 - _inti
    _elen = 16 - _inte
    _addr = list()
    for _ in ((length - 4 - _elen - _plen) // _ilen):
        _addr.append(ipaddress.ip_address(self._read_fileng(_ilen)))
    _addr.append(ipaddress.ip_address(self._read_fileng(_elen)))
    _pads = self._read_fileng(_plen)
    data = dict(cmpri=_inti, cmpre=_inte, pad=_plen, ip=tuple(_addr))
    return data