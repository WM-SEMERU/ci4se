def variable_name(value, allow_empty=False, **kwargs):
    if not value and not allow_empty:
        raise errors.EmptyValueError('value (%s) was empty' % value)
    elif not value:
        return None
    try:
        parse('%s = None' % value)
    except (SyntaxError, ValueError, TypeError):
        raise errors.InvalidVariableNameError(
            'value (%s) is not a valid variable name' % value)
    return value