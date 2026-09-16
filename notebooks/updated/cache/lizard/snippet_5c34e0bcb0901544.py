def get_stats_daily(start=None, end=None, last=None, **kwargs):
    import warnings
    warnings.warn(WNG_MSG % ('get_stats_daily', 'iexdata.get_stats_daily'))
    start, end = _sanitize_dates(start, end)
    return DailySummaryReader(start=start, end=end, last=last, **kwargs).fetch(
        )