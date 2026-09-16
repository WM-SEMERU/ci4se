def _checkString(inputstring, description, minlength=0, maxlength=None):
    if not isinstance(description, str):
        raise TypeError('The description should be a string. Given: {0!r}'.
            format(description))
    if not isinstance(inputstring, str):
        raise TypeError('The {0} should be a string. Given: {1!r}'.format(
            description, inputstring))
    if not isinstance(maxlength, (int, type(None))):
        raise TypeError(
            'The maxlength must be an integer or None. Given: {0!r}'.format
            (maxlength))
    _checkInt(minlength, minvalue=0, maxvalue=None, description='minlength')
    if len(inputstring) < minlength:
        raise ValueError(
            'The {0} is too short: {1}, but minimum value is {2}. Given: {3!r}'
            .format(description, len(inputstring), minlength, inputstring))
    if not maxlength is None:
        if maxlength < 0:
            raise ValueError('The maxlength must be positive. Given: {0}'.
                format(maxlength))
        if maxlength < minlength:
            raise ValueError(
                'The maxlength must not be smaller than minlength. Given: {0} and {1}'
                .format(maxlength, minlength))
        if len(inputstring) > maxlength:
            raise ValueError(
                'The {0} is too long: {1}, but maximum value is {2}. Given: {3!r}'
                .format(description, len(inputstring), maxlength, inputstring))