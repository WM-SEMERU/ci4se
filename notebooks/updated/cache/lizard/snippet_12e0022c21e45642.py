def bytes_to_long(s):
    if isinstance(s, int):
        return s
    acc = 0
    if USING_PYTHON2:
        acc = long(acc)
    unpack = struct.unpack
    length = len(s)
    if length % 4:
        extra = 4 - length % 4
        s = b'\x00' * extra + s
        length = length + extra
    for i in range(0, length, 4):
        acc = (acc << 32) + unpack(b'>I', s[i:i + 4])[0]
    return acc