def _log(self, level, msg, args, exc_info=None, extra=None):
    if exc_info and not isinstance(exc_info, tuple):
        exc_info = sys.exc_info()
    self.append(HistoryRecord(level, 'unknown filename', 0, msg, args,
        exc_info, func='unknown func'))