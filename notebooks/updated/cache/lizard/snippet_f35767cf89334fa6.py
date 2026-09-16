def log_warn(message, args):
    get_logger(DEFAULT_LOGGER, log_creation=False).log(logging.WARNING,
        message, *args)