def filter(cls, filters, iterable):
    if isinstance(filters, Filter):
        filters = [filters]
    for filter in filters:
        iterable = filter.generator(iterable)
    return iterable