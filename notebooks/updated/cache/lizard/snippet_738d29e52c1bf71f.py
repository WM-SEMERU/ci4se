def handle_command_def(self, line):
    cmd, arg, line = self.parseline(line)
    if not cmd:
        return
    if cmd == 'silent':
        self.commands_silent[self.commands_bnum] = True
        return
    elif cmd == 'end':
        self.cmdqueue = []
        return 1
    cmdlist = self.commands[self.commands_bnum]
    if arg:
        cmdlist.append(cmd + ' ' + arg)
    else:
        cmdlist.append(cmd)
    try:
        func = getattr(self, 'do_' + cmd)
    except AttributeError:
        func = self.default
    if func.__name__ in self.commands_resuming:
        self.commands_doprompt[self.commands_bnum] = False
        self.cmdqueue = []
        return 1
    return