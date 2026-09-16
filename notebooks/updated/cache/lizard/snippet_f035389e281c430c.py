def plot_time_series(sdat, lovs):
    sovs = misc.set_of_vars(lovs)
    tseries = {}
    times = {}
    metas = {}
    for tvar in sovs:
        series, time, meta = get_time_series(sdat, tvar, conf.time.tstart,
            conf.time.tend)
        tseries[tvar] = series
        metas[tvar] = meta
        if time is not None:
            times[tvar] = time
    tseries['t'] = get_time_series(sdat, 't', conf.time.tstart, conf.time.tend
        )[0]
    _plot_time_list(sdat, lovs, tseries, metas, times)