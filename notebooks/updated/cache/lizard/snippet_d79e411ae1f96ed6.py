def _check_series_convert_timestamps_internal(s, timezone):
    from pyspark.sql.utils import require_minimum_pandas_version
    require_minimum_pandas_version()
    from pandas.api.types import is_datetime64_dtype, is_datetime64tz_dtype
    if is_datetime64_dtype(s.dtype):
        tz = timezone or _get_local_timezone()
        return s.dt.tz_localize(tz, ambiguous=False).dt.tz_convert('UTC')
    elif is_datetime64tz_dtype(s.dtype):
        return s.dt.tz_convert('UTC')
    else:
        return s