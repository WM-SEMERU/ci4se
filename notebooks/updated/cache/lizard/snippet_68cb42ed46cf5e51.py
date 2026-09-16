def logger_format(self, value):
    self.__logger_format = value
    self.logger_formatter = logging.Formatter(self.__logger_format)