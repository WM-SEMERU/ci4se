def _attach_subcommands(self):
    if self.subcommands:
        self.subparsers = self.parser.add_subparsers()
        for subcommand in self.subcommands:
            subparser = self.subparsers.add_parser(subcommand.name, help=
                subcommand.title)
            if subcommand.handler:
                self._register_handler(subparser, subcommand.handler)
            subcommand._init(subparser)