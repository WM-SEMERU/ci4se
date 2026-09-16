def ping(self, message=_NOTSET, *, encoding=_NOTSET):
    if message is not _NOTSET:
        args = message,
    else:
        args = ()
    return self.execute('PING', *args, encoding=encoding)