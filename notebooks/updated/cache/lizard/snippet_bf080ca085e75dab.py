def unpack_rgb(data, dtype=None, bitspersample=None, rescale=True):
    if bitspersample is None:
        bitspersample = 5, 6, 5
    if dtype is None:
        dtype = '<B'
    dtype = numpy.dtype(dtype)
    bits = int(numpy.sum(bitspersample))
    if not (bits <= 32 and all(i <= dtype.itemsize * 8 for i in bitspersample)
        ):
        raise ValueError('sample size not supported: %s' % str(bitspersample))
    dt = next(i for i in 'BHI' if numpy.dtype(i).itemsize * 8 >= bits)
    data = numpy.frombuffer(data, dtype.byteorder + dt)
    result = numpy.empty((data.size, len(bitspersample)), dtype.char)
    for i, bps in enumerate(bitspersample):
        t = data >> int(numpy.sum(bitspersample[i + 1:]))
        t &= int('0b' + '1' * bps, 2)
        if rescale:
            o = (dtype.itemsize * 8 // bps + 1) * bps
            if o > data.dtype.itemsize * 8:
                t = t.astype('I')
            t *= (2 ** o - 1) // (2 ** bps - 1)
            t //= 2 ** (o - dtype.itemsize * 8)
        result[:, (i)] = t
    return result.reshape(-1)