def do_library(self, args):
    func = getattr(args, 'func', None)
    if func is not None:
        func(self, args)
    else:
        self.do_help('library')