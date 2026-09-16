def set_cloexec(fd):
    flags = fcntl.fcntl(fd, fcntl.F_GETFD)
    assert fd > 2
    fcntl.fcntl(fd, fcntl.F_SETFD, flags | fcntl.FD_CLOEXEC)