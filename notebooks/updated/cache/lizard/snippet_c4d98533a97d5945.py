def get_stats_dict(a_in, full=True):
    d = {}
    a = checkma(a_in)
    d['count'] = a.count()
    thresh = 4000000.0
    if not full and d['count'] > thresh:
        a = a.compressed()
        stride = int(np.around(a.size / thresh))
        a = a[::stride]
    d['min'] = a.min()
    d['max'] = a.max()
    d['ptp'] = d['max'] - d['min']
    d['mean'] = a.mean(dtype='float64')
    d['std'] = a.std(dtype='float64')
    d['nmad'], d['med'] = mad(a, return_med=True)
    d['median'] = d['med']
    d['p16'], d['p84'], d['spread'] = robust_spread(a)
    from scipy.stats.mstats import mode
    d['mode'] = mode(a, axis=None)[0]
    for i in d:
        d[i] = float(d[i])
    d['count'] = int(d['count'])
    return d