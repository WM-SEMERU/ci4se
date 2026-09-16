def pre_delayed(values, delay):
    values = _normalize(values)
    if delay < 0:
        raise ValueError('delay must be 0 or larger')
    for v in values:
        sleep(delay)
        yield v