def np_to_datetime(intime):
    nptime = np.atleast_1d(intime)
    np_corr = (nptime - np.datetime64('1970-01-01T00:00:00')) / np.timedelta64(
        1, 's')
    return [datetime.utcfromtimestamp(t) for t in np_corr]