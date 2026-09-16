def time_limited(limit_seconds, iterable):
    if limit_seconds < 0:
        raise ValueError('limit_seconds must be positive')
    start_time = monotonic()
    for item in iterable:
        if monotonic() - start_time > limit_seconds:
            break
        yield item