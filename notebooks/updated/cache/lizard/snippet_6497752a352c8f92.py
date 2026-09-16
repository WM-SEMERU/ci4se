def parse_args(self, argv=None):
    parser = optparse.OptionParser(version='%prog version: ' + __version__)
    for option in self.options:
        for args, kwargs in option.cli_options:
            cli_option = parser.add_option(*args, **kwargs)
            option.cli_names.append(cli_option.dest)
    parsed_options, args = parser.parse_args(argv)
    if args:
        raise errors.InvalidConfiguration(
            'The following command line arguments are not recognized: ' +
            ', '.join(args))
    if parsed_options.config_file:
        try:
            with open(parsed_options.config_file) as f:
                self.load_json(f.read())
        except (OSError, IOError, ValueError) as exc:
            tb = sys.exc_info()[2]
            raise errors.InvalidConfiguration(str(exc)).with_traceback(tb)
    values = parsed_options.__dict__
    for option in self.options:
        option.apply_function(option, dict((k, values.get(k)) for k in
            option.cli_names))