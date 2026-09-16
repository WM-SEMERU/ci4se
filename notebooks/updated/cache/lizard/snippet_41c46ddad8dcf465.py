def groupby(fn, coll):
    d = collections.defaultdict(list)
    for item in coll:
        key = fn(item)
        d[key].append(item)
    return dict(d)