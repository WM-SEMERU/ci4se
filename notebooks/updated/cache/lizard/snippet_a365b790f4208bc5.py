def __recv_exc_clear(self, log_if_exc_set=None):
    if not (log_if_exc_set is None or self.__recv_exc is None):
        logger.info(log_if_exc_set)
    self.__recv_exc = None