def flatten(items, enter=lambda x: isinstance(x, list)):
    for x in items:
        if enter(x):
            yield from flatten(x)
        else:
            yield x