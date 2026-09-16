def replace(iterable, pred, substitutes, count=None, window_size=1):
    if window_size < 1:
        raise ValueError('window_size must be at least 1')
    substitutes = tuple(substitutes)
    it = chain(iterable, [_marker] * (window_size - 1))
    windows = windowed(it, window_size)
    n = 0
    for w in windows:
        if pred(*w):
            if count is None or n < count:
                n += 1
                yield from substitutes
                consume(windows, window_size - 1)
                continue
        if w and w[0] is not _marker:
            yield w[0]