def replace_env_vars(conf):
    d = deepcopy(conf)
    for key, value in d.items():
        if type(value) == dict:
            d[key] = replace_env_vars(value)
        elif type(value) == str:
            if value[0] == '$':
                var_name = value[1:]
                d[key] = os.environ[var_name]
    return d