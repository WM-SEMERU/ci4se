def difference(iterable, func=sub):
    a, b = tee(iterable)
    try:
        item = next(b)
    except StopIteration:
        return iter([])
    return chain([item], map(lambda x: func(x[1], x[0]), zip(a, b)))