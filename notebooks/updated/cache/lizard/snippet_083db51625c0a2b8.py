def do_continue(self, arg):
    if self.cmdprefix:
        raise CmdError('prefix not allowed')
    if arg:
        raise CmdError('too many arguments')
    if self.debug.get_debugee_count() > 0:
        return True