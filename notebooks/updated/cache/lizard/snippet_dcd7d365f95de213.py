def start_logging(out=_stdout, level='info'):
    global _loggers, _observer, _log_level, _started_logging
    if level not in log_levels:
        raise RuntimeError("Invalid log level '{0}'; valid are: {1}".format
            (level, ', '.join(log_levels)))
    if _started_logging:
        return
    _started_logging = True
    _log_level = level
    set_global_log_level(_log_level)
    if out:
        _observer = _LogObserver(out)
    if _NEW_LOGGER:
        _observers = []
        if _observer:
            _observers.append(_observer)
        globalLogBeginner.beginLoggingTo(_observers)
    else:
        assert out, 'out needs to be given a value if using Twisteds before 15.2'
        from twisted.python import log
        log.startLogging(out)