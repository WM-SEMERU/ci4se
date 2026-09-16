def _adapt_WSDateTime(dt):
    try:
        ts = int((dt.replace(tzinfo=pytz.utc) - datetime(1970, 1, 1, tzinfo
            =pytz.utc)).total_seconds())
    except (OverflowError, OSError):
        if dt < datetime.now():
            ts = 0
        else:
            ts = 2 ** 63 - 1
    return ts