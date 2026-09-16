def store(data, arr, start=0, stop=None, offset=0, blen=None):
    blen = _util.get_blen_array(data, blen)
    if stop is None:
        stop = len(data)
    else:
        stop = min(stop, len(data))
    length = stop - start
    if length < 0:
        raise ValueError('invalid stop/start')
    for bi in range(start, stop, blen):
        bj = min(bi + blen, stop)
        bl = bj - bi
        arr[offset:offset + bl] = data[bi:bj]
        offset += bl