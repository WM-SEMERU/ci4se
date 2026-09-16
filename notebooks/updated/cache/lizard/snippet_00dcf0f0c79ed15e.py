def round_datetime(when=None, precision=60, rounding=ROUND_NEAREST):
    when = when or djtz.now()
    weekday = WEEKDAYS.get(precision, WEEKDAYS['MON'])
    if precision in WEEKDAYS:
        precision = int(timedelta(days=7).total_seconds())
    elif isinstance(precision, timedelta):
        precision = int(precision.total_seconds())
    when_min = when.min + timedelta(days=weekday)
    if djtz.is_aware(when):
        when_min = datetime(*when_min.timetuple()[:3], tzinfo=when.tzinfo)
    delta = when - when_min
    remainder = int(delta.total_seconds()) % precision
    when -= timedelta(seconds=remainder, microseconds=when.microsecond)
    if (rounding == ROUND_UP or rounding == ROUND_NEAREST and remainder >= 
        precision / 2):
        when += timedelta(seconds=precision)
    return when