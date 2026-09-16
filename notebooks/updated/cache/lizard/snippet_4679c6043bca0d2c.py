def size_in_bytes(insize):
    if insize is None or insize.strip() == '':
        raise ValueError('no string specified')
    units = {'k': 1024, 'm': 1024 ** 2, 'g': 1024 ** 3, 't': 1024 ** 4, 'p':
        1024 ** 5}
    match = re.search('^\\s*([0-9\\.]+)\\s*([kmgtp])?', insize, re.I)
    if match is None:
        raise ValueError('match not found')
    size, unit = match.groups()
    if size:
        size = float(size)
    if unit:
        size = size * units[unit.lower().strip()]
    return int(size)