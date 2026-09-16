def leb128_encode(value):
    if value == 0:
        return b'\x00'
    result = []
    while value != 0:
        byte = value & 127
        value >>= 7
        if value != 0:
            byte |= 128
        result.append(byte)
    return bytes(result)