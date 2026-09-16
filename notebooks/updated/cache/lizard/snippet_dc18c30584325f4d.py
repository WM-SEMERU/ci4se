def validate_long(datum, **kwargs):
    return isinstance(datum, (int, long, numbers.Integral)
        ) and LONG_MIN_VALUE <= datum <= LONG_MAX_VALUE and not isinstance(
        datum, bool) or isinstance(datum, (datetime.time, datetime.datetime,
        datetime.date))