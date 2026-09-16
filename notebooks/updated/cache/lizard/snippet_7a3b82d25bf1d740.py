def log_every_n(n, level, message, *args):
    return _log_every_n_to_logger(n, None, level, message, *args)