def first(pipe, items=1):
    pipe = iter(pipe)
    return next(pipe) if items == 1 else islice(pipe, 0, items)