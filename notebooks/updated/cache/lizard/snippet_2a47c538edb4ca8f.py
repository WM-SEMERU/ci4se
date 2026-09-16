def unpickle_args(items):
    pickled = items.pop('_pickled', None)
    if pickled is None:
        return items
    pickled_keys = pickled[0].split(',')
    ret = {}
    for key, vals in items.items():
        if key in pickled_keys:
            ret[key] = [pickle.loads(val) for val in vals]
        else:
            ret[key] = vals
    return ret