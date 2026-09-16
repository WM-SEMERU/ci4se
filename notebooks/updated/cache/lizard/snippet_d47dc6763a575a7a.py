def brpop(self, key, *keys, timeout=0, encoding=_NOTSET):
    if not isinstance(timeout, int):
        raise TypeError('timeout argument must be int')
    if timeout < 0:
        raise ValueError('timeout must be greater equal 0')
    args = keys + (timeout,)
    return self.execute(b'BRPOP', key, *args, encoding=encoding)