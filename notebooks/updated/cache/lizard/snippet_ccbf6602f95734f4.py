def get_logger(name, level=None, fmt=':%(lineno)d: %(message)s'):
    if name not in Logger.loggers:
        if Logger.level is None and level is None:
            Logger.level = level = logging.ERROR
        elif Logger.level is None:
            Logger.level = level
        elif level is None:
            level = Logger.level
        logger = logging.getLogger(name)
        logger_handler = logging.StreamHandler()
        logger_handler.setFormatter(LoggingFormatter(fmt=name + fmt))
        logger.addHandler(logger_handler)
        logger.setLevel(level)
        Logger.loggers[name] = logger
    return Logger.loggers[name]