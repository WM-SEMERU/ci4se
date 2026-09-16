def is_thin_archieve(self):
    if not self._ptr:
        raise BfdException('BFD not initialized')
    return _bfd.get_bfd_attribute(self._ptr, BfdAttributes.IS_THIN_ARCHIEVE)