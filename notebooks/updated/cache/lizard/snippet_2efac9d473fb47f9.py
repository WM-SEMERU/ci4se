def setup_log(name):
    _log = logging.getLogger(name)
    _log.setLevel(GLOBAL_LOG_LEVEL)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - [%(name)s] %(message)s')
    handler.setFormatter(formatter)
    _log.addHandler(handler)
    _log.addFilter(XBMCFilter('[%s] ' % name))
    return _log