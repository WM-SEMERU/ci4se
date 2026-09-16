def range(start, stop):
    length = stop - start
    out = list(length=length)
    index = 0
    orig_start = start
    while start < stop:
        val = index + orig_start
        out[index] = val
        index = index + 1
        start = orig_start + index
    return out