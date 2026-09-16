def to_timestamp(val):
    if isinstance(val, numbers.Number):
        return val
    elif isinstance(val, six.string_types):
        dt = _parse_datetime_string(val)
    else:
        dt = val
    return time.mktime(dt.timetuple())