def wait(self, dwMilliseconds=None):
    if self.value is None:
        raise ValueError('Handle is already closed!')
    if dwMilliseconds is None:
        dwMilliseconds = INFINITE
    r = WaitForSingleObject(self.value, dwMilliseconds)
    if r != WAIT_OBJECT_0:
        raise ctypes.WinError(r)