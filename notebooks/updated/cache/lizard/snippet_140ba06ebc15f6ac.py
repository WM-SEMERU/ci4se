def append_sint32(self, value):
    zigzag_value = wire_format.zig_zag_encode(value)
    self._stream.append_var_uint32(zigzag_value)