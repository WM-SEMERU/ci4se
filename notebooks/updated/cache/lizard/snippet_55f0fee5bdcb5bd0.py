def gp_size(self, _gp_size):
    if not self._ptr:
        raise BfdException('BFD not initialized')
    return _bfd.set_gp_size(self._ptr, _gp_size)