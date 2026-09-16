def register_special_log_handler(name_or_logger, callback):
    if isinstance(name_or_logger, string_types):
        name = name_or_logger
    else:
        name = name_or_logger.name
    special_logger_handlers[name] = callback