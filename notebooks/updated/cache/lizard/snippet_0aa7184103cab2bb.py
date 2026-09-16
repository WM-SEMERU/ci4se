def raise_or_lock(self, key, timeout):
    lock_path = self._get_lock_path(key)
    try:
        fd = os.open(lock_path, os.O_CREAT | os.O_EXCL)
    except OSError as error:
        if error.errno == errno.EEXIST:
            mtime = os.path.getmtime(lock_path)
            ttl = mtime + timeout - time.time()
            if ttl > 0:
                raise AlreadyQueued(ttl)
            else:
                os.utime(lock_path, None)
                return
        else:
            raise
    else:
        os.close(fd)