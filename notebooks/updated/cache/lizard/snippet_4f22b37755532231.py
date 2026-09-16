def _parse_packet_v2(self, data):
    from pymacaroons.exceptions import MacaroonDeserializationException
    ft, n = _decode_uvarint(data)
    data = data[n:]
    if ft == self._EOS:
        return data, PacketV2(ft, None)
    payload_len, n = _decode_uvarint(data)
    data = data[n:]
    if payload_len > len(data):
        raise MacaroonDeserializationException(
            'field data extends past end of buffer')
    return data[payload_len:], PacketV2(ft, data[0:payload_len])