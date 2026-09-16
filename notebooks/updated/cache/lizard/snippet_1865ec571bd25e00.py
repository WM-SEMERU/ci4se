def do_trace(self, arg):
    if arg:
        raise CmdError('too many arguments')
    if self.lastEvent is None:
        raise CmdError('no current thread set')
    self.lastEvent.get_thread().set_tf()
    return True