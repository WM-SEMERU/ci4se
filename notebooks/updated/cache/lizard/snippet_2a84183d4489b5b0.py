def _gen_packet(self, sequence, payloadtype, payload=None):
    contents = self._gen_header(sequence, payloadtype)
    if payload:
        contents.extend(payload)
    size = pack('<H', len(contents) + 2)
    packet = bytearray(size)
    packet.extend(contents)
    return packet