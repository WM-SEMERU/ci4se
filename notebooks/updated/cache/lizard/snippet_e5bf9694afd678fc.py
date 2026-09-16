def get_date_range(year=None, month=None, day=None):
    if year is None:
        return None
    if month is None:
        start = datetime(year, 1, 1, 0, 0, 0, tzinfo=utc)
        end = datetime(year, 12, 31, 23, 59, 59, 999, tzinfo=utc)
        return start, end
    if day is None:
        start = datetime(year, month, 1, 0, 0, 0, tzinfo=utc)
        end = start + timedelta(days=monthrange(year, month)[1],
            microseconds=-1)
        return start, end
    else:
        start = datetime(year, month, day, 0, 0, 0, tzinfo=utc)
        end = start + timedelta(days=1, microseconds=-1)
        return start, end