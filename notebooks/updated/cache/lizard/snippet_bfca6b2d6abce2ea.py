def build_rrule(count=None, interval=None, bysecond=None, byminute=None,
    byhour=None, byweekno=None, bymonthday=None, byyearday=None, bymonth=
    None, until=None, bysetpos=None, wkst=None, byday=None, freq=None):
    result = {}
    if count is not None:
        result['COUNT'] = count
    if interval is not None:
        result['INTERVAL'] = interval
    if bysecond is not None:
        result['BYSECOND'] = bysecond
    if byminute is not None:
        result['BYMINUTE'] = byminute
    if byhour is not None:
        result['BYHOUR'] = byhour
    if byweekno is not None:
        result['BYWEEKNO'] = byweekno
    if bymonthday is not None:
        result['BYMONTHDAY'] = bymonthday
    if byyearday is not None:
        result['BYYEARDAY'] = byyearday
    if bymonth is not None:
        result['BYMONTH'] = bymonth
    if until is not None:
        result['UNTIL'] = until
    if bysetpos is not None:
        result['BYSETPOS'] = bysetpos
    if wkst is not None:
        result['WKST'] = wkst
    if byday is not None:
        result['BYDAY'] = byday
    if freq is not None:
        if freq not in vRecur.frequencies:
            raise ValueError('Frequency value should be one of: {0}'.format
                (vRecur.frequencies))
        result['FREQ'] = freq
    return result