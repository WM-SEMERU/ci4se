def ensure(data_type, check_value, default_value=None):
    if default_value is not None and not isinstance(default_value, data_type):
        raise ValueError(
            'default_value must be the value in the given data type.')
    elif isinstance(check_value, data_type):
        return check_value
    try:
        new_value = data_type(check_value)
    except:
        return default_value
    return new_value