def validate_non_negative_integer(option, value):
    val = validate_integer(option, value)
    if val < 0:
        raise ValueError('The value of %s must be a non negative integer' %
            (option,))
    return val