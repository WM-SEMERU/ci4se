def _parse_variable_defaults(cls, defaults):
    default_dict = {}
    for item in defaults:
        key = next(iter(item))
        value = item[key]
        if key in default_dict:
            raise RecipeFileInvalid('Default variable value specified twice',
                name=key, old_value=default_dict[key], new_value=value)
        default_dict[key] = value
    return default_dict