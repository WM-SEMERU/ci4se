def _get_vm_status(self):
    result = yield from self._control_vm('info status', [b'debug',
        b'inmigrate', b'internal-error', b'io-error', b'paused',
        b'postmigrate', b'prelaunch', b'finish-migrate', b'restore-vm',
        b'running', b'save-vm', b'shutdown', b'suspended', b'watchdog',
        b'guest-panicked'])
    if result is None:
        return result
    status = result.rsplit(' ', 1)[1]
    if status == 'running' or status == 'prelaunch':
        self.status = 'started'
    elif status == 'suspended':
        self.status = 'suspended'
    elif status == 'shutdown':
        self.status = 'stopped'
    return status