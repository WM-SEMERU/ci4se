def positions(weights, period, freq=None):
    weights = weights.unstack()
    if not isinstance(period, pd.Timedelta):
        period = pd.Timedelta(period)
    if freq is None:
        freq = weights.index.freq
    if freq is None:
        freq = BDay()
        warnings.warn("'freq' not set, using business day calendar",
            UserWarning)
    trades_idx = weights.index.copy()
    returns_idx = utils.add_custom_calendar_timedelta(trades_idx, period, freq)
    weights_idx = trades_idx.union(returns_idx)
    portfolio_weights = pd.DataFrame(index=weights_idx, columns=weights.columns
        )
    active_weights = []
    for curr_time in weights_idx:
        if curr_time in weights.index:
            assets_weights = weights.loc[curr_time]
            expire_ts = utils.add_custom_calendar_timedelta(curr_time,
                period, freq)
            active_weights.append((expire_ts, assets_weights))
        if active_weights:
            expire_ts, assets_weights = active_weights[0]
            if expire_ts <= curr_time:
                active_weights.pop(0)
        if not active_weights:
            continue
        tot_weights = [w for ts, w in active_weights]
        tot_weights = pd.concat(tot_weights, axis=1)
        tot_weights = tot_weights.sum(axis=1)
        tot_weights /= tot_weights.abs().sum()
        portfolio_weights.loc[curr_time] = tot_weights
    return portfolio_weights.fillna(0)