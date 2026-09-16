def _hash_scalar(val, encoding='utf8', hash_key=None):
    if isna(val):
        return np.array([np.iinfo(np.uint64).max], dtype='u8')
    if getattr(val, 'tzinfo', None) is not None:
        if not isinstance(val, tslibs.Timestamp):
            val = tslibs.Timestamp(val)
        val = val.tz_convert(None)
    dtype, val = infer_dtype_from_scalar(val)
    vals = np.array([val], dtype=dtype)
    return hash_array(vals, hash_key=hash_key, encoding=encoding,
        categorize=False)