def indexof(coll, item, start=0, default=None):
    if item in coll[start:]:
        return list(coll).index(item, start)
    else:
        return default