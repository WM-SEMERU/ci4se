def to_bytes(self):
    r
    self.sanitize()
    bitstream = BitArray('uint:4=%d' % self.message_type)
    bitstream += BitArray('bool=%d, bool=%d' % (self.security, self.
        ddt_originated))
    bitstream += self._reserved1
    payload = self.payload
    if hasattr(payload, 'to_bytes'):
        payload = payload.to_bytes()
    return bitstream.bytes + payload