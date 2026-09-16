def local_dt(dt):
    if not dt.tzinfo:
        dt = pytz.utc.localize(dt)
    return LOCALTZ.normalize(dt.astimezone(LOCALTZ))