def add_argparser(self, root, parents):
    parser = root.add_parser('diff', parents=parents)
    parser.set_defaults(func=self)
    parser.add_argument('--secrets', dest='secrets', action='store', help=
        'Path to the authorization secrets file (client_secrets.json).')
    parser.add_argument('-d', '--data', dest='data_path', action='store',
        default=None, help='Path to a existing JSON diff file.')
    parser.add_argument('report_a_path', action='store', help=
        'Path to a JSON file containing the initial report data.')
    parser.add_argument('report_b_path', action='store', help=
        'Path to a JSON file containing the report data to compare.')
    parser.add_argument('output_path', action='store', help=
        'Path to output either an HTML report or a JSON data file.')
    return parser