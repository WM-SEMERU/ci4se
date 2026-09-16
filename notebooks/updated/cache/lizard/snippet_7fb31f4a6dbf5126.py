def get_escape_code(self, codetype, value):
    valuefmt = str(value).lower()
    code = codes[codetype].get(valuefmt, None)
    if code:
        return code
    named_funcs = {'fore': format_fore, 'back': format_back, 'style':
        format_style}
    converter = named_funcs.get(codetype, None)
    if converter is None:
        raise ValueError('Invalid code type. Expecting {}, got: {!r}'.
            format(', '.join(named_funcs), codetype))
    with suppress(ValueError):
        value = int(hex2term(value, allow_short=True))
        return converter(value, extended=True)
    named_data = name_data.get(valuefmt, None)
    if named_data is not None:
        try:
            return converter(named_data['code'], extended=True)
        except TypeError:
            if codetype == 'style':
                raise InvalidStyle(value)
            raise
    try:
        r, g, b = (int(x) for x in value)
    except (TypeError, ValueError):
        if codetype == 'style':
            raise InvalidStyle(value)
    try:
        escapecode = converter(value)
    except ValueError as ex:
        raise InvalidColr(value) from ex
    return escapecode