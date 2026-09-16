def kv_format_dict(d, keys=None, separator=DEFAULT_SEPARATOR):
    return _format_pairs(dump_dict(d, keys), separator=separator)