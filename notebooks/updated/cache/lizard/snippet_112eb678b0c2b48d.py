def _configure_logging(self):
    self.log_level = ComponentCore.LOG_LEVEL_MAP.get(self.log_level,
        logging.ERROR)
    self.log = logging.getLogger(self.service_name)
    self.log.setLevel(self.log_level)
    if self.log_path:
        file_path = self.log_path
        if not self.log_path.endswith('.log'):
            file_path = os.path.join(self.log_path, self.service_name + '.log')
        file_handler = WatchedFileHandler(file_path)
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(self._log_formatter())
        self.log.addHandler(file_handler)
    if self.verbose:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(self._log_formatter())
        self.log.addHandler(console_handler)
    self.log.info('Logging configured for: %s', self.service_name)