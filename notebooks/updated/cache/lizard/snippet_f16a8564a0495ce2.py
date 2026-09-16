def merge_lists(src, new):
    l_min, l_max = (src, new) if len(src) < len(new) else (new, src)
    l_min.extend(None for i in range(len(l_min), len(l_max)))
    for i, val in enumerate(new):
        if isinstance(val, dict) and isinstance(src[i], dict):
            new[i] = merge_dicts(src[i], val)
        elif isinstance(val, list) and isinstance(src[i], list):
            new[i] = merge_lists(src[i], val)
        elif val is not None:
            new[i] = val
        else:
            new[i] = src[i]
    return new