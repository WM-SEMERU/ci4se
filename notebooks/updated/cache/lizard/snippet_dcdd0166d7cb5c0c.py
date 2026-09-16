def open_umanager(self):
    if self.umanager_opened:
        return
    self.ser.write(self.cmd_umanager_invocation)
    if self.read_loop(lambda x: x.endswith(self.umanager_prompt), self.
        timeout * self.umanager_waitcoeff):
        self.umanager_opened = True
    else:
        self.ser.write(self.cr)
        if self.read_loop(lambda x: x.endswith(self.umanager_prompt), self.
            timeout):
            self.umanager_opened = True
    if self.umanager_opened:
        log.debug('uManager opened')
    else:
        raise Dam1021Error(1, 'Failed to open uManager')