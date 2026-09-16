def set_log_level(self, level):
    if level == 'info':
        level = logging.INFO
    if level == 'debug':
        level = logging.DEBUG
    if level == 'error':
        level = logging.ERROR
    self._log.setLevel(level)