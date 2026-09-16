def _get_sub_prop(container, keys, default=None):
    sub_val = container
    for key in keys:
        if key not in sub_val:
            return default
        sub_val = sub_val[key]
    return sub_val