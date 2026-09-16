def decode_tag(stream):
    reserved, tag = unpack_value('>cc', stream)
    if reserved != b'\x00':
        raise DeserializationError('Invalid tag: reserved byte is not null')
    return tag