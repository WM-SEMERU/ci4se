def select_windows(rlist, wlist, xlist, timeout, retry=True):
    from ctypes import windll, byref, c_ulong, c_void_p, WinError, GetLastError
    PIPE_ENDED = 109
    read_ready = []
    rlist = [item for item in rlist]
    for i in range(2):
        for fd in rlist:
            bytes_available = c_ulong(0)
            handle = _get_named_pipe_from_fileno(fd.fileno())
            result = windll.kernel32.PeekNamedPipe(c_void_p(handle), None,
                c_ulong(0), None, byref(bytes_available), None)
            if not result:
                last_error = GetLastError()
                if last_error != PIPE_ENDED:
                    raise WinError(last_error)
                continue
            if bytes_available.value:
                read_ready.append((fd, bytes_available.value))
                rlist.remove(fd)
        sleep(timeout)
    return read_ready, wlist, xlist