def end_of_month(val):
    if type(val) == date:
        val = datetime.fromordinal(val.toordinal())
    if val.month == 12:
        return start_of_month(val).replace(year=val.year + 1, month=1
            ) - timedelta(microseconds=1)
    else:
        return start_of_month(val).replace(month=val.month + 1) - timedelta(
            microseconds=1)