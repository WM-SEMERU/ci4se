def decode_utf8(f):
    decode = codecs.getdecoder('utf8')
    buf = f.read(FIELD_U16.size)
    if len(buf) < FIELD_U16.size:
        raise UnderflowDecodeError()
    num_utf8_bytes, = FIELD_U16.unpack_from(buf)
    num_bytes_consumed = FIELD_U16.size + num_utf8_bytes
    buf = f.read(num_utf8_bytes)
    if len(buf) < num_utf8_bytes:
        raise UnderflowDecodeError()
    try:
        s, num_chars = decode(buf, 'strict')
    except UnicodeError as e:
        raise Utf8DecodeError(e)
    return num_bytes_consumed, s