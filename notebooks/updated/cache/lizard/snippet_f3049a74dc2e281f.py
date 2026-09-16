def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging_config['loggers']['gcdt']['level'])
    return logger