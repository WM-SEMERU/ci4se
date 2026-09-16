def match_url_vars_type(url_vars, type_hints):
    typed_url_vars = {}
    try:
        for k, v in url_vars.items():
            arg_type = type_hints.get(k)
            if arg_type and arg_type != str:
                typed_url_vars[k] = arg_type(v)
            else:
                typed_url_vars[k] = v
    except ValueError:
        return False, {}
    return True, typed_url_vars