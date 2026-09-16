def _normalize_utf8_keys(kwargs):
    if any(type(key) is binary_type for key in kwargs.keys()):
        dict_type = type(kwargs)
        return dict_type([(text_type(k), v) for k, v in kwargs.items()])
    return kwargs