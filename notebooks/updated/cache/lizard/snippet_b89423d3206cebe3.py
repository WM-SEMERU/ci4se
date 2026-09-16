def popwhile(predicate, iterable):
    while iterable:
        item = iterable.pop()
        if predicate(item):
            yield item
        else:
            break