def _get_kind_name(param_type, is_list):
    if issubclass(param_type, bool):
        typename = 'bool'
    elif issubclass(param_type, six.integer_types):
        typename = 'int64'
    elif issubclass(param_type, (six.string_types, six.binary_type)):
        typename = 'bytes'
    elif issubclass(param_type, float):
        typename = 'float'
    else:
        raise ValueError('Unsupported parameter type: %s' % str(param_type))
    suffix = 'list' if is_list else 'value'
    return '_'.join([typename, suffix])