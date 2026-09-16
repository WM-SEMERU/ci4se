def timestamp_from_datetime(date_time):
    if date_time.tzinfo is None:
        return time.mktime((date_time.year, date_time.month, date_time.day,
            date_time.hour, date_time.minute, date_time.second, -1, -1, -1)
            ) + date_time.microsecond / 1000000.0
    return (date_time - _EPOCH).total_seconds()