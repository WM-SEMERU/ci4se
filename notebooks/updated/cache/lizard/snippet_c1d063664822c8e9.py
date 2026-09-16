def strict_path_lookup(data_obj, xj_path, force_type=None):
    value, exists = path_lookup(data_obj, xj_path)
    if exists:
        if force_type is not None:
            if not isinstance(value, force_type):
                raise XJPathError('Found value is a wrong type', (xj_path,
                    force_type))
        return value
    else:
        raise XJPathError('Path does not exist', (xj_path,))