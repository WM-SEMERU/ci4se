def backoff_iter(start, stop, count=None, factor=2.0, jitter=False):
    start = float(start)
    stop = float(stop)
    factor = float(factor)
    if start < 0.0:
        raise ValueError('expected start >= 0, not %r' % start)
    if factor < 1.0:
        raise ValueError('expected factor >= 1.0, not %r' % factor)
    if stop == 0.0:
        raise ValueError('expected stop >= 0')
    if stop < start:
        raise ValueError('expected stop >= start, not %r' % stop)
    if count is None:
        denom = start if start else 1
        count = 1 + math.ceil(math.log(stop / denom, factor))
        count = count if start else count + 1
    if count != 'repeat' and count < 0:
        raise ValueError('count must be positive or "repeat", not %r' % count)
    if jitter:
        jitter = float(jitter)
        if not -1.0 <= jitter <= 1.0:
            raise ValueError('expected jitter -1 <= j <= 1, not: %r' % jitter)
    cur, i = start, 0
    while count == 'repeat' or i < count:
        if not jitter:
            cur_ret = cur
        elif jitter:
            cur_ret = cur - cur * jitter * random.random()
        yield cur_ret
        i += 1
        if cur == 0:
            cur = 1
        elif cur < stop:
            cur *= factor
        if cur > stop:
            cur = stop
    return