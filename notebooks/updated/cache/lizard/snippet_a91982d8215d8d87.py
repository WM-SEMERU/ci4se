def flatten(iterable):
    iterable = iter(iterable)
    while True:
        try:
            item = next(iterable)
        except StopIteration:
            break
        if isinstance(item, six.string_types):
            yield item
            continue
        try:
            data = iter(item)
            iterable = itertools.chain(data, iterable)
        except:
            yield item