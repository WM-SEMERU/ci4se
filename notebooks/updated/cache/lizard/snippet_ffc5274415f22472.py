def render_delta(d):
    s = '' if d >= 0 else '-'
    d = abs(d)
    for unit in _SORTED_UNITS:
        span = __timedelta_millis(unit[1])
        if d >= span:
            count = int(d // span)
            s += '{0}{1}'.format(count, unit[0])
            d -= count * span
    if d or not s:
        s += str(d)
    return s