def _get_formatter(fmt):
    fmt = _replace_and_pad(fmt, '%(timezone)s', LogManager.spec.timezone)
    return logging.Formatter(fmt)