def local_time_to_online(dt=None):
    is_dst = None
    utc_offset = None
    try:
        if dt is None:
            dt = datetime.datetime.now()
        is_dst = time.daylight > 0 and time.localtime().tm_isdst > 0
        utc_offset = time.altzone if is_dst else time.timezone
        return time.mktime(dt.timetuple()) * 1000 + utc_offset * 1000
    except:
        line, filename, synerror = trace()
        raise ArcRestHelperError({'function': 'local_time_to_online',
            'line': line, 'filename': filename, 'synerror': synerror})
    finally:
        is_dst = None
        utc_offset = None
        del is_dst
        del utc_offset