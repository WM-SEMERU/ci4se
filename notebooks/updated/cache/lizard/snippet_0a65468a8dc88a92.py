def duration(t, now=None, precision=1, pad=', ', words=None, justnow=
    datetime.timedelta(seconds=10)):
    if words is None:
        words = precision == 1
    t1 = _to_datetime(t)
    t2 = _to_datetime(now or datetime.datetime.now())
    if t1 < t2:
        format = _('%s ago')
    else:
        format = _('%s from now')
    result, remains = delta(t1, t2, words=words, justnow=justnow)
    if result in (_('just now'), _('yesterday'), _('tomorrow'), _(
        'last week'), _('next week')):
        return result
    elif precision > 1 and remains:
        t3 = t2 - datetime.timedelta(seconds=remains)
        return pad.join([result, duration(t2, t3, precision - 1, pad, words
            =False)])
    else:
        return format % (result,)