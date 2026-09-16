def _chunk(iterable, size):
    args = (iter(iterable),) * size
    return (itertools.takewhile(lambda x: x is not None, group) for group in
        itertools.zip_longest(*args))