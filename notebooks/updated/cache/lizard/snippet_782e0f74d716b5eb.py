def convert_dict(d, cls=AttrDict):
    for k, v in d.items():
        if isinstance(v, Mapping):
            d[k] = convert_dict(v)
        elif isinstance(v, list):
            for i, e in enumerate(v):
                if isinstance(e, Mapping):
                    v[i] = convert_dict(e)
    return cls(d)