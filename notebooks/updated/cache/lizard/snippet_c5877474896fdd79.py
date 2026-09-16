def zpopmin(self, key, count=None, *, encoding=_NOTSET):
    if count is not None and not isinstance(count, int):
        raise TypeError('count argument must be int')
    args = []
    if count is not None:
        args.extend([count])
    fut = self.execute(b'ZPOPMIN', key, *args, encoding=encoding)
    return fut