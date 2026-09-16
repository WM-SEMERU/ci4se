def set_loglevel(loggers, level):
    if not loggers:
        return
    if 'all' in loggers:
        loggers = lognames.keys()
    for key in loggers:
        logging.getLogger(lognames[key]).setLevel(level)