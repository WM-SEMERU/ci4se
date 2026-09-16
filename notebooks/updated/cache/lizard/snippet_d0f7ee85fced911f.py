def _timestamp_to_json_parameter(value):
    if isinstance(value, datetime.datetime):
        if value.tzinfo not in (None, UTC):
            value = value.replace(tzinfo=None) - value.utcoffset()
        value = '%s %s+00:00' % (value.date().isoformat(), value.time().
            isoformat())
    return value