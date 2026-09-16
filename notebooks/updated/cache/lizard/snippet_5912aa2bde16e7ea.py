def day_counts(index):
    index = index.copy()
    if len(index) == 0:
        return pd.Series([], index=index)
    timedeltas = (index[1:] - index[:-1]).append(pd.TimedeltaIndex([pd.NaT]))
    timedelta_days = timedeltas.total_seconds() / (60 * 60 * 24)
    return pd.Series(timedelta_days, index=index)