def set_min_level_to_save(self, level):
    self.min_log_level_to_save = level
    handler_class = logging.handlers.TimedRotatingFileHandler
    self._set_min_level(handler_class, level)