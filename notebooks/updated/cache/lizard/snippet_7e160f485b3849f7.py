def choices(vals, n):
    if n == len(vals):
        yield tuple(vals)
    elif n > 1:
        n -= 1
        for i, v in enumerate(vals[:-n]):
            v = v,
            for c in choices(vals[i + 1:], n):
                yield v + c
    elif n == 1:
        for v in vals:
            yield v,
    elif n == 0:
        yield ()
    else:
        raise ValueError(n)