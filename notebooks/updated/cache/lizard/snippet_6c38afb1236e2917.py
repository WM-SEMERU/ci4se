def last(iterable, default=None):
    result = default
    iterator = iter(iterable)
    while True:
        try:
            result = next(iterator)
        except StopIteration:
            break
    return result