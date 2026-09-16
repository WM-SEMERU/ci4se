def add_timed_rotating_file_handler(logger=None, file_path='out.log', level
    =logging.INFO, log_format=log_formats.easy_read, when='w0', interval=1,
    backup_count=5, **handler_kwargs):
    if not isinstance(logger, logging.Logger):
        logger = logging.getLogger(logger)
    logger.addHandler(get_file_handler(file_path, level, log_format,
        handler=TimedRotatingFileHandler, when=when, interval=interval,
        backupCount=backup_count, **handler_kwargs))