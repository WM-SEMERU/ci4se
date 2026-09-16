def get_parser(self, prog_name, subcommand):
    parser = OptionParser(prog=prog_name, usage=self.usage(subcommand),
        version=self.get_version(), option_list=sorted(self.get_option_list()))
    return parser