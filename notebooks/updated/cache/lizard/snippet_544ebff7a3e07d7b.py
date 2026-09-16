def read(self, num):
    start_pos = self.tell()
    if self.padded:
        self._bits.clear()
        res = utils.binary(self._stream.read(num))
    else:
        bits = self.read_bits(num * 8)
        res = bits_to_bytes(bits)
        res = utils.binary(res)
    end_pos = self.tell()
    self._update_consumed_ranges(start_pos, end_pos)
    return res