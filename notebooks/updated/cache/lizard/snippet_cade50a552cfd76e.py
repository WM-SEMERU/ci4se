def ilen(iterable):
    counter = count()
    deque(zip(iterable, counter), maxlen=0)
    return next(counter)