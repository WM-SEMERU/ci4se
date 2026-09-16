def flatten_dict(x):
    out = {}
    for k, v in x.items():
        out = _recur_flatten(k, v, out)
    return out