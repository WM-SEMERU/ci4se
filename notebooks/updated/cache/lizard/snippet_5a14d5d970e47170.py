def setLoggerLevel(self, logger, level):
    if level == logging.NOTSET:
        self.removeLogger(logger)
        self.handler().setLoggerLevel(logger, level)
        return
    if isinstance(logger, logging.Logger):
        logger = logger.name
    if not logger in self._loggers:
        self.addLogger(logger, level)
    else:
        self.handler().setLoggerLevel(logger, level)