def accumulate_items(items, reduce_each=False):
    if not items:
        return {}
    accumulated = defaultdict(list)
    for key, val in items:
        accumulated[key].append(val)
    if not reduce_each:
        return accumulated
    else:
        return {k: reduce_value(v, v) for k, v in iteritems(accumulated)}