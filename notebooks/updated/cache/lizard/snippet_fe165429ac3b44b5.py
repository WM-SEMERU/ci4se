def decode_varint(f, max_bytes=4):
    num_bytes_consumed = 0
    value = 0
    m = 1
    while True:
        buf = f.read(1)
        if len(buf) == 0:
            raise UnderflowDecodeError()
        u8, = FIELD_U8.unpack(buf)
        value += (u8 & 127) * m
        m *= 128
        num_bytes_consumed += 1
        if u8 & 128 == 0:
            break
        elif max_bytes is not None and num_bytes_consumed >= max_bytes:
            raise DecodeError(
                'Variable integer contained more than maximum bytes ({}).'.
                format(max_bytes))
    return num_bytes_consumed, value