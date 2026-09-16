def _encode_uvarint(data, n):
    if n < 0:
        raise ValueError('only support positive integer')
    while True:
        this_byte = n & 127
        n >>= 7
        if n == 0:
            data.append(this_byte)
            break
        data.append(this_byte | 128)