def clean_time(time_string):
    time = dateutil.parser.parse(time_string)
    if not settings.USE_TZ:
        time = time.astimezone(timezone.utc).replace(tzinfo=None)
    return time