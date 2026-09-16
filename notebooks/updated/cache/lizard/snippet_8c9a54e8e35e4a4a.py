def readLipd(usr_path=''):
    global cwd, settings, files
    if settings['verbose']:
        __disclaimer(opt='update')
    start = clock()
    files['.lpd'] = []
    __read(usr_path, '.lpd')
    _d = __read_lipd_contents()
    end = clock()
    logger_benchmark.info(log_benchmark('readLipd', start, end))
    return _d