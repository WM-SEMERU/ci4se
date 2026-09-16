def group_callback(self, iocb):
    if _debug:
        IOGroup._debug('group_callback %r', iocb)
    for iocb in self.ioMembers:
        if not iocb.ioComplete.isSet():
            if _debug:
                IOGroup._debug('    - waiting for child: %r', iocb)
            break
    else:
        if _debug:
            IOGroup._debug('    - all children complete')
        self.ioState = COMPLETED
        self.trigger()