def deterministic_dict(normal_dict):
    out = OrderedDict()
    for key in sorted(normal_dict.keys()):
        out[key] = normal_dict[key]
    return out