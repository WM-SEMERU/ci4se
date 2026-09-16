def _times_to_hours_after_local_midnight(times):
    times = times.tz_localize(None)
    hrs = 1 / NS_PER_HR * (times.astype(np.int64) - times.normalize().
        astype(np.int64))
    return np.array(hrs)