def do_attach(self, arg):
    if self.cmdprefix:
        raise CmdError('prefix not allowed')
    targets = self.input_process_list(self.split_tokens(arg, 1))
    if not targets:
        print('Error: missing parameters')
    else:
        debug = self.debug
        for pid in targets:
            try:
                debug.attach(pid)
                print('Attached to process (%d)' % pid)
            except Exception:
                print("Error: can't attach to process (%d)" % pid)