def asfreq_actual(series, freq, method='ffill', how='end', normalize=False):
    orig = series
    is_series = False
    if isinstance(series, pd.Series):
        is_series = True
        name = series.name if series.name else 'data'
        orig = pd.DataFrame({name: series})
    t = pd.concat([orig, pd.DataFrame({'dt': orig.index.values}, index=orig
        .index.values)], axis=1)
    dts = t.asfreq(freq=freq, method=method, how=how, normalize=normalize)['dt'
        ]
    res = orig.loc[dts.values]
    if is_series:
        return res[name]
    else:
        return res