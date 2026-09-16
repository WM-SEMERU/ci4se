def _parse_option(line):
    match = _OPTION_REGEX.match(line)
    if not match:
        raise ValueError('Invalid syntax')
    for name, type_ in _OPTIONS:
        if name == match.group(1):
            return name, type_(match.group(2))
    raise ValueError('Unknown option')