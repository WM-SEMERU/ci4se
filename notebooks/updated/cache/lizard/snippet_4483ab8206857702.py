def int_to_string(x):
    assert x >= 0
    if x == 0:
        return b('\x00')
    result = []
    while x:
        ordinal = x & 255
        result.append(int2byte(ordinal))
        x >>= 8
    result.reverse()
    return b('').join(result)