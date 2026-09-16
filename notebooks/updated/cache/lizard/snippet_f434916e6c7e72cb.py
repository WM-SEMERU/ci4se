def aroon(arg, n, up_col='close', dn_col='close'):
    if isinstance(arg, pd.DataFrame):
        tmp = arg[[up_col, dn_col]].dropna()
        idx = tmp.index
        upvals = tmp[up_col].values
        dnvals = tmp[dn_col].values
    else:
        tmp = arg.dropna()
        idx = tmp.index
        upvals = tmp.values
        dnvals = upvals
    n = int(n)
    up, dn = np.empty(len(upvals), 'd'), np.empty(len(upvals), 'd')
    up[:n] = np.nan
    dn[:n] = np.nan
    for i in range(n, len(upvals)):
        up[i] = 100.0 * (n - upvals[i - n:i + 1][::-1].argmax()) / n
        dn[i] = 100.0 * (n - dnvals[i - n:i + 1][::-1].argmin()) / n
    osc = up - dn
    data = [('UP', pd.Series(up, index=idx)), ('DOWN', pd.Series(dn, index=
        idx)), ('OSC', pd.Series(osc, index=idx))]
    return pd.DataFrame.from_items(data).reindex(arg.index)