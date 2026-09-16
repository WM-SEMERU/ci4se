def log(_self, _level, _message, *args, **kwargs):
    r
    logger = _self.opt(exception=_self._exception, record=_self._record,
        lazy=_self._lazy, ansi=_self._ansi, raw=_self._raw, depth=_self.
        _depth + 1)
    logger._make_log_function(_level)(logger, _message, *args, **kwargs)