def use_loggly(self, enabled=True, loggly_token=None, loggly_tag=None,
    level=logging.WARNING, log_format=None, date_format=None):
    if enabled:
        if not self.__loggly_handler:
            assert loggly_token, 'Loggly token is missing!'
            if not loggly_tag:
                loggly_tag = self.name
            self.__loggly_handler = LogglyHandler(token=loggly_token, tag=
                loggly_tag)
            if not log_format:
                log_format = (
                    '{"name":"%(name)s","process":"%(process)d","levelname":"%(levelname)s","time":"%(asctime)s","filename":"%(filename)s","programname":"%(programname)s","module":"%(module)s","funcName":"%(funcName)s","lineno":"%(lineno)d","message":"%(message)s"}'
                    )
            formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
            self.__loggly_handler.setFormatter(fmt=formatter)
            self.__loggly_handler.setLevel(level=level)
            self.add_handler(hdlr=self.__loggly_handler)
    elif self.__loggly_handler:
        self.remove_handler(hdlr=self.__loggly_handler)
        self.__loggly_handler = None