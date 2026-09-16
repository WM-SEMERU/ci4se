def _dt_to_float_ordinal(dt):
    if isinstance(dt, (np.ndarray, Index, ABCSeries)
        ) and is_datetime64_ns_dtype(dt):
        base = dates.epoch2num(dt.asi8 / 1000000000.0)
    else:
        base = dates.date2num(dt)
    return base