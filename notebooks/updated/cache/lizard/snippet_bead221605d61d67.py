def _read_mptcp_add(self, bits, size, kind):
    vers = int(bits, base=2)
    adid = self._read_unpack(1)
    ipad = self._read_fileng(4) if vers == 4 else self._read_fileng(16)
    ip_l = 4 if vers == 4 else 16
    pt_l = size - 1 - ip_l
    port = self._read_unpack(2) if pt_l else None
    data = dict(kind=kind, length=size + 1, subtype='ADD_ADDR', addaddr=
        dict(ipver=vers, addrid=adid, addr=ipaddress.ip_address(ipad), port
        =port))
    return data