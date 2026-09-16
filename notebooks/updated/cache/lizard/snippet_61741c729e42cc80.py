def load_key(filename, delimiter='\\s+'):
    r
    scale, mode = load_delimited(filename, [str, str], delimiter)
    if len(scale) != 1:
        raise ValueError('Key file should contain only one line.')
    scale, mode = scale[0], mode[0]
    key_string = '{} {}'.format(scale, mode)
    try:
        key.validate_key(key_string)
    except ValueError as error:
        warnings.warn(error.args[0])
    return key_string