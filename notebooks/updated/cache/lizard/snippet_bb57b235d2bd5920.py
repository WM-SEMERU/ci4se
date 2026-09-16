def run(self, args=None):
    raw_args = self.__parser.parse_args(args=args)
    args = vars(raw_args)
    cmd = args.pop('cmd')
    if hasattr(cmd, '__call__'):
        cmd(**args)