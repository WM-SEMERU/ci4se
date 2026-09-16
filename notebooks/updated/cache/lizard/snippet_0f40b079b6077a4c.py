def is_known_scalar(value):

    def _is_datetime_or_timedelta(value):
        return pd.Series(value).dtype.kind in ('M', 'm')
    return not np.iterable(value) and (isinstance(value, numbers.Number) or
        _is_datetime_or_timedelta(value))