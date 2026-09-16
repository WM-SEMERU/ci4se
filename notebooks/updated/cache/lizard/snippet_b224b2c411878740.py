def localize(dt, tz):
    if not isinstance(tz, tzinfo):
        tz = pytz.timezone(tz)
    return tz.localize(dt)