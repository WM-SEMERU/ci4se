def do_quit(self, arg):
    if self.cmdprefix:
        raise CmdError('prefix not allowed')
    if arg:
        raise CmdError('too many arguments')
    if self.confirm_quit:
        count = self.debug.get_debugee_count()
        if count > 0:
            if count == 1:
                msg = "There's a program still running."
            else:
                msg = 'There are %s programs still running.' % count
            if not self.ask_user(msg):
                return False
    self.debuggerExit = True
    return True