def log(message: str, *args: str, category: str='info', logger_name: str=
    'pgevents'):
    global _DEBUG_ENABLED
    if _DEBUG_ENABLED:
        level = logging.INFO
    else:
        level = logging.CRITICAL + 1
    with _create_logger(logger_name, level) as logger:
        log_fn = getattr(logger, category, None)
        if log_fn is None:
            raise ValueError('Invalid log category "{}"'.format(category))
        log_fn(message, *args)