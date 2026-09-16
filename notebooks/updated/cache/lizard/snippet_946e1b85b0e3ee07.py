def get_logger(logger_name):
    if logger_name is None:
        return __instance
    assert isinstance(logger_name, str), 'Logger name must be a string!'
    with __lock:
        if logger_name in __loggers:
            return __loggers[logger_name]
        logger_instance = LogOne(logger_name=logger_name)
        __loggers[logger_name] = logger_instance
        return logger_instance