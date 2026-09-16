def sliding_impl(wrap, size, step, sequence):
    i = 0
    n = len(sequence)
    while i + size <= n or step != 1 and i < n:
        yield wrap(sequence[i:i + size])
        i += step