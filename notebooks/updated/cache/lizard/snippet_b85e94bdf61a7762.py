def toposort(data):
    if len(data) == 0:
        return
    data = data.copy()
    for k, v in data.items():
        v.discard(k)
    extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
    data.update(dict((item, set()) for item in extra_items_in_deps))
    while True:
        ordered = set(item for item, dep in data.items() if len(dep) == 0)
        if not ordered:
            break
        yield ordered
        data = dict((item, dep - ordered) for item, dep in data.items() if 
            item not in ordered)
    if len(data) != 0:
        raise CyclicDependency(data)