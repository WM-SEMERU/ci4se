def pack_command(self, *args):
    command = args[0]
    if ' ' in command:
        args = tuple([Token(s) for s in command.split(' ')]) + args[1:]
    else:
        args = (Token(command),) + args[1:]
    args_output = SYM_EMPTY.join([SYM_EMPTY.join((b(str(len(k))), SYM_LF, k,
        SYM_LF)) for k in imap(self.encode, args)])
    output = '%s%s' % (args_output, SYM_LF)
    return output