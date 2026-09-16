def extend_is_dir(value, minimum=None, maximum=None):
    u
    if isinstance(value, list):
        return [is_dir(member) for member in validate.is_list(value,
            minimum, maximum)]
    else:
        return is_dir(value)