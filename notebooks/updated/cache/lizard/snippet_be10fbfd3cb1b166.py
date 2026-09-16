def flatten(d, *keys):
    flat = {}
    for k in keys:
        flat = merge(flat, d.pop(k, {}))
    return flat