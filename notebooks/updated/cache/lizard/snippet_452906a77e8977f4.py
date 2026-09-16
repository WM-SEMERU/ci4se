def ru_strftime(format='%d.%m.%Y', date=None, inflected=False,
    inflected_day=False, preposition=False):
    if date is None:
        date = datetime.datetime.today()
    weekday = date.weekday()
    prepos = preposition and DAY_NAMES[weekday][3] or ''
    month_idx = inflected and 2 or 1
    day_idx = (inflected_day or preposition) and 2 or 1
    if '%b' in format or '%B' in format:
        format = format.replace('%d', six.text_type(date.day))
    format = format.replace('%a', prepos + DAY_NAMES[weekday][0])
    format = format.replace('%A', prepos + DAY_NAMES[weekday][day_idx])
    format = format.replace('%b', MONTH_NAMES[date.month - 1][0])
    format = format.replace('%B', MONTH_NAMES[date.month - 1][month_idx])
    if six.PY2:
        s_format = format.encode('utf-8')
        s_res = date.strftime(s_format)
        u_res = s_res.decode('utf-8')
    else:
        u_res = date.strftime(format)
    return u_res