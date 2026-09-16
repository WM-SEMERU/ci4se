def join(self, timeout=None):
    if timeout is None:
        for thread in self.__threads:
            thread.join()
    else:
        deadline = _time() + timeout
        for thread in self.__threads:
            delay = deadline - _time()
            if delay <= 0:
                return False
            if not thread.join(delay):
                return False
    return True