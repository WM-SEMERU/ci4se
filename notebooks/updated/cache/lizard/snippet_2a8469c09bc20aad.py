def kv_format_object(o, keys=None, separator=DEFAULT_SEPARATOR):
    if keys is None:
        key_values = []
        for k, v in ((x, getattr(o, x)) for x in sorted(dir(o))):
            if k.startswith('_') or isroutine(v):
                continue
            key_values += (k, v),
    else:
        key_values = ((k, getattr(o, k)) for k in keys)
    return kv_format_pairs(key_values, separator)