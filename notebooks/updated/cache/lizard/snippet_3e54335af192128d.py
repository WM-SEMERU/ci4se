def is_int(arg):
    return is_int(mag(arg)) if is_quantity(arg) else True if isinstance(arg,
        six.integer_types) else is_npscalar(arg, 'int') or is_npvalue(arg,
        'int')