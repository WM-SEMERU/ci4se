def encode(self, packet):
    id = identifier.get_packet_id(packet)
    if id is None:
        raise EncoderException('unknown packet')
    self._write_variunt(id)
    self._write(packet.SerializeToString())
    return bytes(self.buffer)