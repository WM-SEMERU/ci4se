def stop(self):
    self.__end.set()
    if self.__recv_thread:
        self.__recv_thread.join()
        self.__recv_thread = None
    if self.__send_thread:
        self.__send_thread.join()
        self.__send_thread = None