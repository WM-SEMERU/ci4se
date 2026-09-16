def get_overlay_spec(o, k, v):
    k = wrap_tuple(k)
    return (type(v).__name__, v.group, v.label) + k if len(o.kdims) else (type
        (v).__name__,) + k