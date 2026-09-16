def cftime_to_nptime(times):
    times = np.asarray(times)
    new = np.empty(times.shape, dtype='M8[ns]')
    for i, t in np.ndenumerate(times):
        try:
            dt = pd.Timestamp(t.year, t.month, t.day, t.hour, t.minute, t.
                second, t.microsecond)
        except ValueError as e:
            raise ValueError(
                'Cannot convert date {} to a date in the standard calendar.  Reason: {}.'
                .format(t, e))
        new[i] = np.datetime64(dt)
    return new