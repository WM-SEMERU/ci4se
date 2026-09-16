def cmd_help(self, args):
    if len(args) < 1:
        self.print_usage()
        return
    if args[0] == 'about':
        print('MAVProxy Version ' + self.version + '\nOS: ' + self.host +
            '\nPython ' + self.pythonversion)
    elif args[0] == 'site':
        print('See http://dronecode.github.io/MAVProxy/ for documentation')
    else:
        self.print_usage()