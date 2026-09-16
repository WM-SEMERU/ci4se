def connectivity(measure_names, b, c=None, nfft=512):
    con = Connectivity(b, c, nfft)
    try:
        return getattr(con, measure_names)()
    except TypeError:
        return dict((m, getattr(con, m)()) for m in measure_names)