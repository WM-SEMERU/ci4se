def redirect_stdout(self, enabled=True, log_level=logging.INFO):
    if enabled:
        if self.__stdout_wrapper:
            self.__stdout_wrapper.update_log_level(log_level=log_level)
        else:
            self.__stdout_wrapper = StdOutWrapper(logger=self, log_level=
                log_level)
        self.__stdout_stream = self.__stdout_wrapper
    else:
        self.__stdout_stream = _original_stdout
    sys.stdout = self.__stdout_stream