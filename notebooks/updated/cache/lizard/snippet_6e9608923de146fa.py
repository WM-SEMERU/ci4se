def path_lookup(data_obj, xj_path, create_dict_path=False):
    if not xj_path or xj_path == '.':
        return data_obj, True
    res = list(split(xj_path, '.', maxsplit=1))
    top_key = res[0]
    leftover = res[1] if len(res) > 1 else None
    if top_key == '*':
        return _full_sub_array(data_obj, leftover, create_dict_path)
    elif top_key.startswith('@'):
        return _single_array_element(data_obj, leftover, top_key,
            create_dict_path)
    else:
        val_type, top_key = _clean_key_type(top_key)
        top_key = unescape(top_key)
        if top_key in data_obj:
            value = data_obj[top_key]
            if val_type is not None and not isinstance(value, val_type):
                raise XJPathError(
                    'Key %s expects type "%s", but found value type is "%s"' %
                    (top_key, val_type.__name__, type(value).__name__))
            if leftover:
                return path_lookup(value, leftover, create_dict_path)
            else:
                return value, True
        else:
            if val_type is not None:
                if not isinstance(data_obj, dict):
                    raise XJPathError(
                        'Accessed object must be a dict type for the key: "%s"'
                         % top_key)
                if create_dict_path:
                    data_obj[top_key] = val_type()
                else:
                    return None, False
                if leftover:
                    return path_lookup(data_obj[top_key], leftover,
                        create_dict_path)
                else:
                    return data_obj[top_key], True
            return None, False