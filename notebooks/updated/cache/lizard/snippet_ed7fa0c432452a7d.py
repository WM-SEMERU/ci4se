def get_env_value(obj, attribute):
    varname = get_env_key(obj, attribute)
    var = os.environ.get(varname)
    if not var:
        raise ValueError('%s must be set in your environment.' % varname)
    return var