def open(filename, mode='r', **kwargs):
    if six.PY3 or 'x' not in mode:
        return sys_open(filename, mode, **kwargs)
    flags = os.O_EXCL | os.O_CREAT | os.O_WRONLY
    if 'b' in mode and hasattr(os, 'O_BINARY'):
        flags |= os.O_BINARY
    fd = os.open(filename, flags)
    mode = mode.replace('x', 'w')
    return os.fdopen(fd, mode, 1636)