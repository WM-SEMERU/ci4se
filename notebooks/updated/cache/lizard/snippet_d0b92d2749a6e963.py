def size_of_varint_1(value):
    value = value << 1 ^ value >> 63
    res = 0
    while True:
        res += 1
        value = value >> 7
        if value == 0:
            break
    return res