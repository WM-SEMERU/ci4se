def _get_s16(self, msb, lsb):
    buf = struct.pack('>bB', self._get_s8(msb), self._get_u8(lsb))
    return int(struct.unpack('>h', buf)[0])