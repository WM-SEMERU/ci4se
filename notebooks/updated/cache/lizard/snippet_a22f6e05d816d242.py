def clear_lock(self, lock_type='update'):
    lock_file = self._get_lock_file(lock_type=lock_type)

    def _add_error(errlist, exc):
        msg = 'Unable to remove update lock for {0} ({1}): {2} '.format(self
            .url, lock_file, exc)
        log.debug(msg)
        errlist.append(msg)
    success = []
    failed = []
    try:
        os.remove(lock_file)
    except OSError as exc:
        if exc.errno == errno.ENOENT:
            pass
        elif exc.errno == errno.EISDIR:
            try:
                shutil.rmtree(lock_file)
            except OSError as exc:
                _add_error(failed, exc)
        else:
            _add_error(failed, exc)
    else:
        msg = "Removed {0} lock for {1} remote '{2}'".format(lock_type,
            self.role, self.id)
        log.debug(msg)
        success.append(msg)
    return success, failed