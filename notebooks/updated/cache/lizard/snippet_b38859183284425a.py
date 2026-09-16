def validate_text(value):
    possible_transform = ['axes', 'fig', 'data']
    validate_transform = ValidateInStrings('transform', possible_transform,
        True)
    tests = [validate_float, validate_float, validate_str,
        validate_transform, dict]
    if isinstance(value, six.string_types):
        xpos, ypos = rcParams['texts.default_position']
        return [(xpos, ypos, value, 'axes', {'ha': 'right'})]
    elif isinstance(value, tuple):
        value = [value]
    try:
        value = list(value)[:]
    except TypeError:
        raise ValueError('Value must be string or list of tuples!')
    for i, val in enumerate(value):
        try:
            val = tuple(val)
        except TypeError:
            raise ValueError(
                'Text must be an iterable of the form (x, y, s[, trans, params])!'
                )
        if len(val) < 3:
            raise ValueError(
                'Text tuple must at least be like [x, y, s], with floats x, y and string s!'
                )
        elif len(val) == 3 or isinstance(val[3], dict):
            val = list(val)
            val.insert(3, 'data')
            if len(val) == 4:
                val += [{}]
            val = tuple(val)
        if len(val) > 5:
            raise ValueError(
                'Text tuple must not be longer then length 5. It can be like (x, y, s[, trans, params])!'
                )
        value[i] = (validate(x) for validate, x in zip(tests, val))
    return value