def seconds2str(seconds):
    if seconds < 0:
        return '{0:.3g}s'.format(seconds)
    elif math.isnan(seconds):
        return 'NaN'
    elif math.isinf(seconds):
        return 'Inf'
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h >= 1:
        return '{0:g}h {1:02g}m {2:.3g}s'.format(h, m, s)
    elif m >= 1:
        return '{0:02g}m {1:.3g}s'.format(m, s)
    else:
        return '{0:.3g}s'.format(s)