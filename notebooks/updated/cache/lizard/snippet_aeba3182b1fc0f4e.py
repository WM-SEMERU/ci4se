def month_interval(year, month, return_str=False):
    if month == 12:
        start, end = datetime(year, month, 1), datetime(year + 1, 1, 1
            ) - timedelta(seconds=1)
    else:
        start, end = datetime(year, month, 1), datetime(year, month + 1, 1
            ) - timedelta(seconds=1)
    if not return_str:
        return start, end
    else:
        return str(start), str(end)