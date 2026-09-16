def to_bytes(self):
    self.sanitize()
    bitstream = BitArray('uint:4=%d' % self.message_type)
    bitstream += BitArray('bool=%d' % self.is_reply)
    bitstream += self._reserved1
    bitstream += BitArray(bytes=self.nonce)
    bitstream += BitArray('uint:16=%d, uint:16=%d, hex=%s' % (self.key_id,
        len(self.authentication_data), self.authentication_data.encode('hex')))
    bitstream += BitArray('uint:32=%d' % self.ttl)
    bitstream += self._reserved2
    bitstream += BitArray('uint:8=%d' % self.eid_prefix.prefixlen)
    bitstream += get_bitstream_for_afi_address(self.eid_prefix)
    bitstream += get_bitstream_for_afi_address(self.reply)
    return bitstream.bytes