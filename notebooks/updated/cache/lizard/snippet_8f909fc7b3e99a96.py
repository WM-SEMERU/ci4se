def is_datetime_like(dtype):
    return np.issubdtype(dtype, np.datetime64) or np.issubdtype(dtype, np.
        timedelta64)