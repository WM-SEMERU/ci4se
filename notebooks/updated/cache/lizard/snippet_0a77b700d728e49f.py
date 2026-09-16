def convert_timezone(obj, timezone):
    if timezone is None:
        return obj.replace(tzinfo=None)
    return pytz.timezone(timezone).localize(obj)