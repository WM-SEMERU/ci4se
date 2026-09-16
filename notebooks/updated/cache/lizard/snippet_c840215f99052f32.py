def time2slurm(timeval, unit='s'):
    d, h, m, s = 24 * 3600, 3600, 60, 1
    timeval = Time(timeval, unit).to('s')
    days, hours = divmod(timeval, d)
    hours, minutes = divmod(hours, h)
    minutes, secs = divmod(minutes, m)
    return '%d-%d:%d:%d' % (days, hours, minutes, secs)