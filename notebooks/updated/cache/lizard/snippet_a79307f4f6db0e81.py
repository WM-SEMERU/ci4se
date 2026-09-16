def do_directives(self, line):
    for name, cmd in self.adapter.directives.items():
        with colorize('blue'):
            print('bot %s:' % name)
            if cmd.__doc__:
                for line in cmd.__doc__.split('\n'):
                    print('  %s' % line)
            else:
                print()