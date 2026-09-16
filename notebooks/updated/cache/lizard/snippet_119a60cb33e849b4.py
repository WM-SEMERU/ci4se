def close_open_fds(keep_files=[]):
    keep_fds = set()
    for file in keep_files:
        if isinstance(file, int):
            keep_fds.add(file)
        else:
            try:
                keep_fds.add(file.fileno())
            except Exception:
                pass
    for fd in os.listdir('/proc/self/fd'):
        fd = int(fd)
        if fd not in keep_fds:
            try:
                os.close(fd)
            except OSError:
                pass