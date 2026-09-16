def encode_cf_datetime(dates, units=None, calendar=None):
    dates = np.asarray(dates)
    if units is None:
        units = infer_datetime_units(dates)
    else:
        units = _cleanup_netcdf_time_units(units)
    if calendar is None:
        calendar = infer_calendar_name(dates)
    delta, ref_date = _unpack_netcdf_time_units(units)
    try:
        if calendar not in _STANDARD_CALENDARS or dates.dtype.kind == 'O':
            raise OutOfBoundsDatetime
        assert dates.dtype == 'datetime64[ns]'
        delta_units = _netcdf_to_numpy_timeunit(delta)
        time_delta = np.timedelta64(1, delta_units).astype('timedelta64[ns]')
        ref_date = pd.Timestamp(ref_date)
        if ref_date.tz is not None:
            ref_date = ref_date.tz_convert(None)
        num = (pd.DatetimeIndex(dates.ravel()) - ref_date) / time_delta
        num = num.values.reshape(dates.shape)
    except (OutOfBoundsDatetime, OverflowError):
        num = _encode_datetime_with_cftime(dates, units, calendar)
    num = cast_to_int_if_safe(num)
    return num, units, calendar