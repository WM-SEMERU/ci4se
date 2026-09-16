def partition(data, chunk_size):
    iterable = iter(data)
    while True:
        next_chunk = list(itertools.islice(iterable, chunk_size))
        if not next_chunk:
            return
        yield next_chunk