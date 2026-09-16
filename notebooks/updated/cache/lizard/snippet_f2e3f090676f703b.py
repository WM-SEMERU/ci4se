def intervallookupone(table, start='start', stop='stop', value=None,
    include_stop=False, strict=True):
    tree = tupletree(table, start=start, stop=stop, value=value)
    return IntervalTreeLookupOne(tree, strict=strict, include_stop=include_stop
        )