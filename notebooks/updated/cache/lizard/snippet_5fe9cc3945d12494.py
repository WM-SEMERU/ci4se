def env_string(name, required=False, default=empty):
    value = get_env_value(name, default=default, required=required)
    if value is empty:
        value = ''
    return value