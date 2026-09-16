def skip_first(pipe, items=1):
    pipe = iter(pipe)
    for i in skip(pipe, items):
        yield i