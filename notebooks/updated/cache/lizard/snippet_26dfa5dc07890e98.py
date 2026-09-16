def parse(timestring):
    for parser in _PARSERS:
        match = parser['pattern'].match(timestring)
        if match:
            groups = match.groups()
            ints = tuple(map(int, groups))
            time = parser['factory'](ints)
            return time
    raise TimeError('Unsupported time format {}'.format(timestring))