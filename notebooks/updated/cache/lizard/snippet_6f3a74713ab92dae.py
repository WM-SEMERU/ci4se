def detect_proc():
    pid = os.getpid()
    for name in ('stat', 'status'):
        if os.path.exists(os.path.join('/proc', str(pid), name)):
            return name
    raise ProcFormatError('unsupported proc format')