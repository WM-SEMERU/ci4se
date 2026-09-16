def lz4_encode_old_kafka(payload):
    assert xxhash is not None
    data = lz4_encode(payload)
    header_size = 7
    flg = data[4]
    if not isinstance(flg, int):
        flg = ord(flg)
    content_size_bit = flg >> 3 & 1
    if content_size_bit:
        flg -= 8
        data = bytearray(data)
        data[4] = flg
        data = bytes(data)
        payload = data[header_size + 8:]
    else:
        payload = data[header_size:]
    hc = xxhash.xxh32(data[0:header_size - 1]).digest()[-2:-1]
    return b''.join([data[0:header_size - 1], hc, payload])