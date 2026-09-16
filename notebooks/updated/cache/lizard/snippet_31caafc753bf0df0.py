def do_refresh(self, arg):
    if arg:
        raise CmdError('too many arguments')
    if self.cmdprefix:
        process = self.get_process_from_prefix()
        process.scan()
    else:
        self.debug.system.scan()