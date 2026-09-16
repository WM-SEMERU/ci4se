def memorized_datetime(seconds):
    try:
        return _datetime_cache[seconds]
    except KeyError:
        dt = _epoch + timedelta(seconds=seconds)
        _datetime_cache[seconds] = dt
        return dt