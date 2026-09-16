def _is_dst(dt):
    localtime = time.localtime(time.mktime((dt.year, dt.month, dt.day, dt.
        hour, dt.minute, dt.second, dt.weekday(), 0, -1)))
    return localtime.tm_isdst > 0