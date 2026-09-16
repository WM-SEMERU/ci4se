def logger_file(self, value):
    self.__logger_file = value
    if self.__logger_file:
        self.logger_file_handler = logging.FileHandler(self.__logger_file)
        self.logger_file_handler.setFormatter(self.logger_formatter)
        for _, logger in six.iteritems(self.logger):
            logger.addHandler(self.logger_file_handler)