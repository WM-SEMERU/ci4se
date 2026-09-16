def dispatch(self, args):
    if not args.list and not args.group:
        if not args.font and not args.char and not args.block:
            self.info()
            return
        else:
            args.list = args.group = True
    self._display = {k: args.__dict__[k] for k in ('list', 'group',
        'omit_summary')}
    if args.char:
        char = self._getChar(args.char)
        if args.font:
            self.fontChar(args.font, char)
        else:
            self.char(char)
    else:
        block = self._getBlock(args.block)
        self.chars(args.font, block)