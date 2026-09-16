def _default(cls, opts):
    logging.basicConfig(level=logging.INFO, format=cls._log_format)
    return True