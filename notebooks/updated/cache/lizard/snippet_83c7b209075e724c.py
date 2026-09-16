def cli_parse(parser):
    parser.add_argument('-n', '--samples', type=int, required=True, help=
        'Number of Samples')
    return parser