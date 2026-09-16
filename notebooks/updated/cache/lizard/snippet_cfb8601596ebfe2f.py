def _combine(n, rs):
    try:
        r, rs = peek(rs)
    except StopIteration:
        yield n
        return
    if overlap(n, r):
        yield merge(n, r)
        next(rs)
        for r in rs:
            yield r
    else:
        yield n
        for r in rs:
            yield r