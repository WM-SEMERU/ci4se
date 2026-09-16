def _get_framed(self, buf, offset, insert_payload):
    header_offset = offset + self._header_len
    self.length = insert_payload(buf, header_offset, self.payload)
    struct.pack_into(self._header_fmt, buf, offset, self.preamble, self.
        msg_type, self.sender, self.length)
    crc_offset = header_offset + self.length
    preamble_bytes = 1
    crc_over_len = self._header_len + self.length - preamble_bytes
    self.crc = crc16jit(buf, offset + 1, 0, crc_over_len)
    struct.pack_into(self._crc_fmt, buf, crc_offset, self.crc)
    length = preamble_bytes + crc_over_len + self._crc_len
    return length