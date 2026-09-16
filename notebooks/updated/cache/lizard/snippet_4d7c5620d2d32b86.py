def get_external_logger(name=None, short_name=' ', log_to_file=True):
    global LOGGERS
    loggername = name
    logger = _check_existing_logger(loggername, short_name)
    if logger is not None:
        return logger
    logging_config = LOGGING_CONFIG.get(name, LOGGING_CONFIG.get('external'))
    filename = logging_config.get('file', {}).get('name', loggername)
    if not filename.endswith('.log'):
        filename = str(filename) + '.log'
    logger = _get_basic_logger(loggername, log_to_file,
        get_base_logfilename(filename))
    cbh = logging.StreamHandler()
    cbh.formatter = BenchFormatterWithType(COLOR_ON)
    if VERBOSE_LEVEL == 1 and not SILENT_ON:
        cbh.setLevel(logging.INFO)
    elif VERBOSE_LEVEL >= 2 and not SILENT_ON:
        cbh.setLevel(logging.DEBUG)
    elif SILENT_ON:
        cbh.setLevel(logging.ERROR)
    else:
        cbh.setLevel(getattr(logging, logging_config.get('level')))
    logger.addHandler(cbh)
    LOGGERS[loggername] = BenchLoggerAdapter(logger, {'source': short_name})
    return LOGGERS[loggername]