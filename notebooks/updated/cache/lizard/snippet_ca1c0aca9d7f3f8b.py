def set(self, key, value, *, expire=0, pexpire=0, exist=None):
    if expire and not isinstance(expire, int):
        raise TypeError('expire argument must be int')
    if pexpire and not isinstance(pexpire, int):
        raise TypeError('pexpire argument must be int')
    args = []
    if expire:
        args[:] = [b'EX', expire]
    if pexpire:
        args[:] = [b'PX', pexpire]
    if exist is self.SET_IF_EXIST:
        args.append(b'XX')
    elif exist is self.SET_IF_NOT_EXIST:
        args.append(b'NX')
    fut = self.execute(b'SET', key, value, *args)
    return wait_ok(fut)