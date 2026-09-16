def merge_dicts(dict_a, dict_b):
    obj = {}
    for key, value in iteritems(dict_a):
        if key in dict_b:
            if isinstance(dict_b[key], dict):
                obj[key] = merge_dicts(value, dict_b.pop(key))
        else:
            obj[key] = value
    for key, value in iteritems(dict_b):
        obj[key] = value
    return obj