def _seconds_as_string(seconds):
    TIME_UNITS = [('s', 60), ('m', 60), ('h', 24), ('d', None)]
    unit_strings = []
    cur = max(int(seconds), 1)
    for suffix, size in TIME_UNITS:
        if size is not None:
            cur, rest = divmod(cur, size)
        else:
            rest = cur
        if rest > 0:
            unit_strings.insert(0, '%d%s' % (rest, suffix))
    return ' '.join(unit_strings)