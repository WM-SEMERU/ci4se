def deep_update(d, d_update):
    for k, v in list(d_update.items()):
        if isinstance(v, dict):
            if k in d:
                deep_update(d[k], v)
            else:
                d[k] = v
        elif isinstance(d, list):
            d.append({k: v})
        else:
            d[k] = v
    return d