def unpack(n, r=32):
    if r < 1:
        raise ValueError('unpack needs r > 0')
    mask = (1 << r) - 1
    while n:
        yield n & mask
        n >>= r