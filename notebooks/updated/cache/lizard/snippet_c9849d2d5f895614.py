def wait(self, timeout=None):
    result = self.__event.wait(timeout)
    if self.__exception is None:
        return result
    else:
        raise self.__exception