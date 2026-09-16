def pack(value, nbits=None):
    if nbits is None:
        nbits = pack_size(value) * BITS_PER_BYTE
    elif nbits <= 0:
        raise ValueError('Given number of bits must be greater than 0.')
    buf_size = int(math.ceil(nbits / float(BITS_PER_BYTE)))
    buf = (ctypes.c_uint8 * buf_size)()
    for idx, _ in enumerate(buf):
        buf[idx] = value >> idx * BITS_PER_BYTE & 255
    return buf