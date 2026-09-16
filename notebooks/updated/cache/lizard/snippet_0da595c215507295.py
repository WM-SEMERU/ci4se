def safe_nested_val(key_tuple, dict_obj, default_value=None):
    try:
        return get_nested_val(key_tuple, dict_obj)
    except (KeyError, IndexError, TypeError):
        return default_value