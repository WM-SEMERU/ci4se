def readline(self, timeout=1):
    data = None
    if self.read_thread:
        data = self.read_thread.readline()
        if data and self.__print_io:
            self.logger.info(data, extra={'type': '<--'})
    return data