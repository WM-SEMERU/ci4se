def nl_groups(self, value):
    self.bytearray[self._get_slicers(3)] = bytearray(c_uint32(value or 0))