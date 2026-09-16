def is_dead(self, proc, name):
    LOGGER.debug('Checking %s (%r)', name, proc)
    try:
        status = proc.status()
    except psutil.NoSuchProcess:
        LOGGER.debug('NoSuchProcess: %s (%r)', name, proc)
        return True
    LOGGER.debug('Process %s (%s) status: %r (Unresponsive Count: %s)',
        name, proc.pid, status, self.unresponsive[name])
    if status in _PROCESS_RUNNING:
        return False
    elif status == psutil.STATUS_ZOMBIE:
        try:
            proc.wait(0.1)
        except psutil.TimeoutExpired:
            pass
        try:
            proc.terminate()
            status = proc.status()
        except psutil.NoSuchProcess:
            LOGGER.debug('NoSuchProcess: %s (%r)', name, proc)
            return True
    return status in _PROCESS_STOPPED_OR_DEAD