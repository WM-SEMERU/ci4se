def wait(self, timeout=None):
    us = -1 if timeout is None else int(timeout * 1000000)
    return super(Reader, self).wait(us)