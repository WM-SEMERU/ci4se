def _make_plus_helper(obj, fields):
    new_obj = {}
    for key, value in obj.items():
        if key in fields or key.startswith('_'):
            if fields.get(key):
                if isinstance(value, list):
                    value = [_make_plus_helper(item, fields[key]) for item in
                        value]
            new_obj[key] = value
        else:
            new_obj['+%s' % key] = value
    return new_obj