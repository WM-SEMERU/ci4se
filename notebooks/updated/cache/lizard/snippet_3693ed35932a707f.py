def set_level(self, level=1):
    if level is True or level == 1:
        level = logging.INFO
        level_name = 'INFO'
    elif level is False or level <= 0:
        level = logging.WARNING
        level_name = 'WARNING'
    elif level >= 2:
        level = logging.DEBUG
        level_name = 'DEBUG'
    if not self.logger.handlers:
        self.logger.tasklogger = self
        self.logger.propagate = False
        handler = logging.StreamHandler(stream=stream.RSafeStream(stream=
            self.stream))
        handler.setFormatter(logging.Formatter(fmt='%(message)s'))
        self.logger.addHandler(handler)
    if level != self.logger.level:
        self.level = level
        self.logger.setLevel(level)
        self.debug('Set {} logging to {}'.format(self.name, level_name))