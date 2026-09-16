def do_verbose(self, args, arguments):
    if args == '':
        self.echo = not self.echo
    else:
        self.echo = arguments['True']