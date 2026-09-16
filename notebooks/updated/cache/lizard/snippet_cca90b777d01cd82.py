def error(self, message):
    if all(len(x) == 0 for x in self._reparse_args.values()):
        self.print_usage(sys.stderr)
        self.exit(2, gt('%s: error: %s\n') % (self.prog, message))