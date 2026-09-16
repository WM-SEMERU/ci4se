def http_time(time):
    return formatdate(timeval=mktime(time.timetuple()), localtime=False,
        usegmt=True)