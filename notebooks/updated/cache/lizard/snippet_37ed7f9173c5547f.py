def get_logger(name, verbosity, stream):
    logger = logging.getLogger(name)
    logger.setLevel({(0): DEFAULT_LOGGING_LEVEL, (1): logging.INFO, (2):
        logging.DEBUG}.get(min(2, verbosity), DEFAULT_LOGGING_LEVEL))
    logger.handlers = []
    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    logger.addHandler(handler)
    return logger