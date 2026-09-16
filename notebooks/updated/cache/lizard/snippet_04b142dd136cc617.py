def _decompose_slice(key, size):
    start, stop, step = key.indices(size)
    if step > 0:
        return key, slice(None)
    else:
        stop = start + int((stop - start - 1) / step) * step + 1
        start, stop = stop + 1, start + 1
        return slice(start, stop, -step), slice(None, None, -1)