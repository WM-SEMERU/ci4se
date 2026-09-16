def _set_default_value(dict_obj, keys, value):
    variable = dict_obj
    if len(keys) == 1:
        if not variable.get(keys[0]):
            variable[keys[0]] = value
    else:
        for idx, field in enumerate(keys):
            if idx < len(keys) - 1:
                variable = variable[field]
        if not variable.get(keys[-1]):
            variable[keys[-1]] = value