def log_to_stream(level=None, fmt=None, datefmt=None):
    _add_log_handler(logging.StreamHandler(), fmt=fmt, datefmt=datefmt,
        propagate=False)