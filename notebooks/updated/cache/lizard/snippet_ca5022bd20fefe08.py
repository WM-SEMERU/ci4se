def apply_to_last(stream, fn):
    assert iterable(stream), 'apply_to_last needs stream to be iterable'
    assert callable(fn), 'apply_to_last needs fn to be callable'
    stream = iter(stream)
    previous = next(stream)
    for current in stream:
        yield previous
        previous = current
    yield fn(previous)