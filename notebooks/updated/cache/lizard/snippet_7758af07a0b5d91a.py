def _get_val_str(obj, path_list=None, reverse=False):
    val_list = _get_val_list(obj, path_list or [], reverse)
    return '<not found>' if obj is None else ' / '.join(map(str, val_list))