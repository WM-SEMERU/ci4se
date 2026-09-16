def na_value_for_dtype(dtype, compat=True):
    dtype = pandas_dtype(dtype)
    if is_extension_array_dtype(dtype):
        return dtype.na_value
    if is_datetime64_dtype(dtype) or is_datetime64tz_dtype(dtype
        ) or is_timedelta64_dtype(dtype) or is_period_dtype(dtype):
        return NaT
    elif is_float_dtype(dtype):
        return np.nan
    elif is_integer_dtype(dtype):
        if compat:
            return 0
        return np.nan
    elif is_bool_dtype(dtype):
        return False
    return np.nan