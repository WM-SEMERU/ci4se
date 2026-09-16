def writeLipd(dat, path=''):
    global settings
    start = clock()
    __write_lipd(dat, path)
    end = clock()
    logger_benchmark.info(log_benchmark('writeLipd', start, end))
    return