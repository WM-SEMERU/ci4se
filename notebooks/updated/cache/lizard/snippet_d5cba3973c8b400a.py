def compress(t, sign=False, pad=''):
    if isinstance(t, datetime.timedelta):
        seconds = t.seconds + t.days * 86400
    elif isinstance(t, six.integer_types + (float,)):
        return compress(datetime.timedelta(seconds=t), sign, pad)
    else:
        return compress(datetime.datetime.now() - _to_datetime(t), sign, pad)
    parts = []
    if sign:
        parts.append('-' if t.days < 0 else '+')
    weeks, seconds = divmod(seconds, TIME_WEEK)
    days, seconds = divmod(seconds, TIME_DAY)
    hours, seconds = divmod(seconds, TIME_HOUR)
    minutes, seconds = divmod(seconds, TIME_MINUTE)
    if weeks:
        parts.append(_('%dw') % (weeks,))
    if days:
        parts.append(_('%dd') % (days,))
    if hours:
        parts.append(_('%dh') % (hours,))
    if minutes:
        parts.append(_('%dm') % (minutes,))
    if seconds:
        parts.append(_('%ds') % (seconds,))
    return pad.join(parts)