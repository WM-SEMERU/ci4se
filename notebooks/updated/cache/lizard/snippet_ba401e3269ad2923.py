def get_config_argparse(suppress=None):
    if suppress is None:
        suppress = []
    config_parser = ArgumentParser(description='Looking for config',
        add_help=not 'help' in suppress)
    if not 'config' in suppress:
        config_parser.add_argument('--config', metavar='CFG', type=str,
            help='Config file to load')
    if 'help' in suppress:
        config_parser.add_argument('--help', action='store_true', default=
            False, help='Display usage information and exit')
    if not 'quiet' in suppress:
        config_parser.add_argument('--quiet', action='store_true', default=
            False, help="Don't print messages to stdout")
    if not 'verbose' in suppress:
        config_parser.add_argument('--verbose', action='store_true',
            default=False, help='Output debug messages')
    if not 'version' in suppress:
        config_parser.add_argument('--version', action='store_true',
            default=False, help='Display version information and exit')
    return config_parser