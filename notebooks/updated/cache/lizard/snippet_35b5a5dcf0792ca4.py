def set_system_time(newtime, utc_offset=None):
    fmts = ['%I:%M:%S %p', '%I:%M %p', '%H:%M:%S', '%H:%M']
    dt_obj = _try_parse_datetime(newtime, fmts)
    if dt_obj is None:
        return False
    return set_system_date_time(hours=dt_obj.hour, minutes=dt_obj.minute,
        seconds=dt_obj.second, utc_offset=utc_offset)