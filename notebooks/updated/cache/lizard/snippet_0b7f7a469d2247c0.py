def rebase_array(d, recursive=False):
    arr = []
    min_val, max_val = _extremes(d.keys())
    for idx in range(min_val, max_val + 1):
        v = d[idx]
        if recursive and _is_dict(v):
            v = rebase_array(v)
        arr.append(v)
    return arr