def unpack(cls, data):
    header, data = APPHeader.unpack(data)
    if len(data) < header.payload_length:
        raise ProtocolViolation('Payload too small')
    payload = data[:header.payload_length]
    body = cls()
    body._header = header
    body._payload = payload
    return body, data[header.payload_length:]