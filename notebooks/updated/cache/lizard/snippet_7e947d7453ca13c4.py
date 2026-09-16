def acquire(self, blocking=True, timeout=None):
    if timeout is None:
        return self.__lock.acquire(blocking)
    else:
        endtime = _time() + timeout
        delay = 0.0005
        while not self.__lock.acquire(False):
            remaining = endtime - _time()
            if remaining <= 0:
                return False
            delay = min(delay * 2, remaining, 0.05)
            _sleep(delay)
        return True