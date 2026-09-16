def Lock(fd, path, blocking):
    operation = fcntl.LOCK_EX if blocking else fcntl.LOCK_EX | fcntl.LOCK_NB
    try:
        fcntl.flock(fd, operation)
    except IOError as e:
        if e.errno == errno.EWOULDBLOCK:
            raise IOError('Exception locking %s. File already locked.' % path)
        else:
            raise IOError('Exception locking %s. %s.' % (path, str(e)))