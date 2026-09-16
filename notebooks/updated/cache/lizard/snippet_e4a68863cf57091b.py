def get_basic_logger(level=logging.WARN, scope='reliure'):
    logger = logging.getLogger(scope)
    logger.setLevel(level)
    ch = logging.StreamHandler()
    ch.setLevel(level)
    formatter = ColorFormatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'
        )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger