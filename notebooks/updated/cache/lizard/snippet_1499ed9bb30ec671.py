def _close(self):
    callback = self.__callback
    self.__callback = None
    try:
        if callback:
            callback(None, InterfaceError('connection closed'))
    finally:
        self.__job_queue = []
        self.__alive = False
        self.__stream.close()