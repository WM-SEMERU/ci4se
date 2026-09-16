def cmd(args, interact=False):
    if isinstance(args, (str, bytes)):
        args = args.split()
    return CLI.cmd(args=args, interact=interact)