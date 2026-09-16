def _read_protos(self, size):
    _byte = self._read_unpack(4, lilendian=True)
    _prot = LINKTYPE.get(_byte)
    return _prot