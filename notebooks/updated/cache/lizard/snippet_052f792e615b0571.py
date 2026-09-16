def _calculate_offset(date, local_tz):
    if local_tz:
        if date.year < 1970:
            t = time.mktime(date.replace(year=1972).timetuple)
        else:
            t = time.mktime(date.timetuple())
        if time.localtime(t).tm_isdst:
            return -time.altzone
        else:
            return -time.timezone
    else:
        return 0