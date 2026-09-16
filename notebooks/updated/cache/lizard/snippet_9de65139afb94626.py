def get_reporting_data(data, start=None, end=None, max_days=365,
    allow_billing_period_overshoot=False,
    ignore_billing_period_gap_for_day_count=False):
    if max_days is not None:
        if end is not None:
            raise ValueError(
                'If max_days is set, end cannot be set: end={}, max_days={}.'
                .format(end, max_days))
    start_inf = False
    if start is None:
        start_limit = pytz.UTC.localize(pd.Timestamp.min)
        start_inf = True
    else:
        start_limit = start
    end_inf = False
    if end is None:
        end_target = pytz.UTC.localize(pd.Timestamp.max)
        end_inf = True
    else:
        end_target = end
    data_after_start_limit = data[start_limit:].copy()
    if ignore_billing_period_gap_for_day_count:
        start_limit = data_after_start_limit.index.min()
    if not start_inf and max_days is not None:
        end_target = start_limit + timedelta(days=max_days)
    if allow_billing_period_overshoot:
        try:
            loc = data_after_start_limit.index.get_loc(end_target, method=
                'nearest')
        except (KeyError, IndexError):
            reporting_data = data_after_start_limit
            end_limit = end_target
        else:
            end_limit = data_after_start_limit.index[loc]
            reporting_data = data_after_start_limit[:end_limit].copy()
    else:
        end_limit = end_target
        reporting_data = data_after_start_limit[:end_limit].copy()
    if reporting_data.dropna().empty:
        raise NoReportingDataError()
    reporting_data.iloc[-1] = np.nan
    data_end = data.index.max()
    data_start = data.index.min()
    return reporting_data, _make_reporting_warnings(end_inf, start_inf,
        data_start, data_end, start_limit, end_limit)