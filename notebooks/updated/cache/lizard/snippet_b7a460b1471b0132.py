def time2fname(tstamp, full=False):
    result = tstamp.strftime(FILENAME_FORMAT)
    result = result if not full else join(time2dir(tstamp), result)
    return result