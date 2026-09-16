def get_argument_parser():
    desc = 'Generate a sample sheet based on a GEO series matrix.'
    parser = cli.get_argument_parser(desc=desc)
    g = parser.add_argument_group('Input and output files')
    g.add_argument('-s', '--series-matrix-file', type=cli.str_type,
        required=True, metavar=cli.file_mv, help='The GEO series matrix file.')
    g.add_argument('-o', '--output-file', type=cli.str_type, required=True,
        metavar=cli.file_mv, help='The output file.')
    g.add_argument('-e', '--encoding', type=cli.str_type, metavar=cli.
        str_mv, default='UTF-8', help=
        'The encoding of the series matrix file. [UTF-8]')
    cli.add_reporting_args(parser)
    return parser