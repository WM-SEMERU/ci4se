def queued(values, qsize):
    values = [_normalize(v) for v in values]
    if qsize < 1:
        raise ValueError('qsize must be 1 or larger')
    q = []
    it = iter(values)
    try:
        for i in range(qsize):
            q.append(next(it))
        for i in cycle(range(qsize)):
            yield q[i]
            q[i] = next(it)
    except StopIteration:
        pass