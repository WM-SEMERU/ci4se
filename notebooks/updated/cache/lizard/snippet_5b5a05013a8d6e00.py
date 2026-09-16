def get_modernrpc_logger(name):
    logger = logging.getLogger(name)
    if not logger_has_handlers(logger):
        logger.addHandler(logging.NullHandler())
    return logger