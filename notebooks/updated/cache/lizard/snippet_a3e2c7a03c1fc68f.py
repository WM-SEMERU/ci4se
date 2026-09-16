def parse_args(args=None):
    parser = argparse.ArgumentParser(description=ds.ARGPARSER['description'])
    parser.add_argument('input', help=ds.ARGPARSE_INPUT['help'])
    parser.add_argument('output', nargs='?', help=ds.ARGPARSE_OUTPUT['help'
        ], default=ds.ARGPARSE_OUTPUT['default'])
    parser.add_argument('-X', '--overwrite', help=ds.ARGPARSE_OVERWRITE[
        'help'], action='store_true')
    parser.add_argument('-e', '--extensions', nargs='+', default=ds.
        ARGPARSE_EXTENSION['default'], help=ds.ARGPARSE_EXTENSION['help'])
    parser.add_argument('-w', '--wrapper', help=ds.ARGPARSE_WRAPPER['help'],
        default=ds.ARGPARSE_WRAPPER['default'])
    parser.add_argument('-v', '--verbose', help=ds.ARGPARSE_VERBOSE['help'],
        action='store_true')
    parser.add_argument('-r', '-R', help=ds.ARGPARSE_RECURSIVE['help'],
        action='store_true', dest='recursive')
    parser.add_argument('--version', action='version', version=ah.__version__)
    if args is not None:
        return parser.parse_args(args)
    else:
        return parser.parse_args()