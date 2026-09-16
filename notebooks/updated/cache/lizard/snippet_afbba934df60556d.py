def _get_time_utc(time_utc_str):
    dt = datetime.strptime(time_utc_str, TIME_FORMAT)
    return int(calendar.timegm(dt.utctimetuple()))