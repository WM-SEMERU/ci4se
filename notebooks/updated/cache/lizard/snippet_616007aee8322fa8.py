def validate_non_negative_int_or_basestring(option, value):
    if isinstance(value, integer_types):
        return value
    elif isinstance(value, string_type):
        try:
            val = int(value)
        except ValueError:
            return value
        return validate_non_negative_integer(option, val)
    raise TypeError(
        'Wrong type for %s, value must be an non negative integer or a string'
         % (option,))