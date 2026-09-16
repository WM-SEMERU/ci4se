def _parse_args(args):
    parser = argparse.ArgumentParser(prog='nibble', description=
        'Speed, distance and time calculations around quantities of digital information.'
        )
    parser.add_argument('-V', '--version', action='version', version=
        '%(prog)s ' + nibble.__version__)
    parser.add_argument('-v', '--verbosity', help=
        'increase output verbosity', action='count', default=0)
    parser.add_argument('expression', type=util.decode_cli_arg, nargs='+',
        help='the calculation to execute')
    return parser.parse_args(args[1:])