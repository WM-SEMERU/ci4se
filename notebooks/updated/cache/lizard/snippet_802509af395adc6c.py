def get_file_logger(name, formatter=None):
    if name is None or name == '':
        raise ValueError("Can't make a logger without name")
    logger = logging.getLogger(name)
    remove_handlers(logger)
    logger.setLevel(logging.INFO)
    if formatter is None:
        config = LOGGING_CONFIG.get(name, {}).get('file',
            DEFAULT_LOGGING_CONFIG.get('file'))
        formatter = BenchFormatter(config.get('level', 'DEBUG'), config.get
            ('dateformat'))
    func = get_testcase_logfilename(name + '.log')
    handler = _get_filehandler_with_formatter(func, formatter)
    logger.addHandler(handler)
    return logger