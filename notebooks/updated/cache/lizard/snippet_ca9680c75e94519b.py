def join(iterable, sep):
    i = 0
    for i, item in enumerate(iterable):
        if i == 0:
            yield item
        else:
            yield sep
            yield item