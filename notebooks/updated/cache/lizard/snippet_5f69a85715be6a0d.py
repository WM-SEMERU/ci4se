def parse_options(self, prog_name, arguments):
    if '--version' in arguments:
        self.exit_status(self.version, fh=sys.stdout)
    parser = self.create_parser(prog_name)
    options, args = parser.parse_args(arguments)
    return options, args