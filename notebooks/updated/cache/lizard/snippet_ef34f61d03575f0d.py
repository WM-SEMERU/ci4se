def add_reporting_args(parser):
    g = parser.add_argument_group('Reporting options')
    g.add_argument('-l', '--log-file', default=None, type=str, metavar=
        file_mv, help=
        'Path of log file (if specified, report to stdout AND file.')
    g.add_argument('-q', '--quiet', action='store_true', help=
        'Only output errors and warnings.')
    g.add_argument('-v', '--verbose', action='store_true', help=
        'Enable verbose output. Ignored if --quiet is specified.')
    return g