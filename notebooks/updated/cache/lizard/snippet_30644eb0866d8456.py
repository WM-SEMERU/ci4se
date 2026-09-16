def mainloop(self):
    if len(self.args) < 2:
        self.parser.error('No event type and info hash given!')
    if sys.stdin.isatty():
        self.options.no_fork = True