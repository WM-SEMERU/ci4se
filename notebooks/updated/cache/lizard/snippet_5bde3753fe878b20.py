def start(self, run=False):
    if run:
        args, argv = [], []
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]
            args.append(arg)
            if not arg.startswith('-') and canparse(arguments, args[:-1]):
                argv = sys.argv[i + 1:]
                break
        if '--verbose' in args:
            args = list(coconut_run_verbose_args) + args
        else:
            args = list(coconut_run_args) + args
        args += ['--argv'] + argv
    else:
        args = None
    self.cmd(args)