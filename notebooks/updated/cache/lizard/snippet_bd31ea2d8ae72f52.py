def get(self, block=True, timeout=None, method='pop'):
    if method not in ('pop', 'popleft'):
        raise ValueError('method must be "pop" or "popleft": {0!r}'.format(
            method))
    t_start = time.clock()
    while not self:
        if not block:
            raise self.Empty
        if timeout is None:
            wait(self)
        else:
            t_delta = time.clock() - t_start
            if t_delta > timeout:
                raise Timeout
            wait(self, timeout - t_delta)
    return getattr(self, method)()