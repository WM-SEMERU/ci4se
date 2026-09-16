def datetime2unix(T):
    T = atleast_1d(T)
    ut1_unix = empty(T.shape, dtype=float)
    for i, t in enumerate(T):
        if isinstance(t, (datetime, datetime64)):
            pass
        elif isinstance(t, str):
            try:
                ut1_unix[i] = float(t)
                continue
            except ValueError:
                t = parse(t)
        elif isinstance(t, (float, int)):
            return T
        else:
            raise TypeError('I only accept datetime or parseable date string')
        ut1_unix[i] = forceutc(t).timestamp()
    return ut1_unix