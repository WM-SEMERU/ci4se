def set_lock(fname):
    global fh
    fh = open(fname, 'w')
    if os.name == 'nt':
        import win32con
        import win32file
        import pywintypes
        LOCK_EX = win32con.LOCKFILE_EXCLUSIVE_LOCK
        LOCK_SH = 0
        LOCK_NB = win32con.LOCKFILE_FAIL_IMMEDIATELY
        __overlapped = pywintypes.OVERLAPPED()
        hfile = win32file._get_osfhandle(fh.fileno())
        try:
            win32file.LockFileEx(hfile, LOCK_EX | LOCK_NB, 0, -65536,
                __overlapped)
        except pywintypes.error as exc_value:
            if exc_value[0] == 33:
                return False
    else:
        from fcntl import flock, LOCK_EX, LOCK_NB
        try:
            flock(fh.fileno(), LOCK_EX | LOCK_NB)
        except Exception as ex:
            return False
    fh.write(str(os.getpid()))
    fh.flush()
    return True