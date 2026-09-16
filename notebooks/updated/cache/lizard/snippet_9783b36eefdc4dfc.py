def b58decode(v, length):
    long_value = 0
    for i, c in enumerate(v[::-1]):
        long_value += __b58chars.find(c) * __b58base ** i
    result = b''
    while long_value >= 256:
        div, mod = divmod(long_value, 256)
        result = struct.pack('B', mod) + result
        long_value = div
    result = struct.pack('B', long_value) + result
    nPad = 0
    for c in v:
        if c == __b58chars[0]:
            nPad += 1
        else:
            break
    result = b'\x00' * nPad + result
    if length is not None and len(result) != length:
        return None
    return result