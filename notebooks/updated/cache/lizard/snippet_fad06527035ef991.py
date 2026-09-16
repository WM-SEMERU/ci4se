def fuzzy_get_value(obj, approximate_key, default=None, **kwargs):
    dict_obj = OrderedDict(obj)
    try:
        return dict_obj[list(dict_obj.keys())[int(approximate_key)]]
    except (ValueError, IndexError):
        pass
    return fuzzy_get(dict_obj, approximate_key, key_and_value=False, **kwargs)