def to_timestamp(dt, timestamp):
    if dt.tzinfo:
        raise TypeError(
            'Cannot store a timezone aware datetime. Convert to UTC and store the naive datetime.'
            )
    timestamp.seconds = calendar.timegm(dt.timetuple())
    timestamp.nanos = dt.microsecond * _NANOS_PER_MICRO