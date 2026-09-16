def select_fds(read_fds, timeout, selector=AutoSelector):
    fd_map = dict((fd_to_int(fd), fd) for fd in read_fds)
    sel = selector()
    try:
        for fd in read_fds:
            sel.register(fd)
        result = sel.select(timeout)
        if result is not None:
            return [fd_map[fd_to_int(fd)] for fd in result]
    finally:
        sel.close()