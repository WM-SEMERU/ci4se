def timestamp_localize(value):
    if isinstance(value, datetime.datetime):
        if not value.tzinfo:
            value = pytz.UTC.localize(value)
        else:
            value = value.astimezone(pytz.UTC)
        value = calendar.timegm(value.timetuple()
            ) + value.microsecond / 1000000.0
    return value