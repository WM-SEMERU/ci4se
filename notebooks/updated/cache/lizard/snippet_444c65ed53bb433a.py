def chunks(iterable, n):
    for i in np.arange(0, len(iterable), n):
        yield iterable[i:i + n]