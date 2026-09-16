def natsort_key(val, key, string_func, bytes_func, num_func):
    if key is not None:
        val = key(val)
    try:
        return string_func(val)
    except (TypeError, AttributeError):
        if type(val) in (bytes,):
            return bytes_func(val)
        try:
            return tuple(natsort_key(x, None, string_func, bytes_func,
                num_func) for x in val)
        except TypeError:
            return num_func(val)