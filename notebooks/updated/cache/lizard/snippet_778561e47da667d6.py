def add_arguments(self, parser):
    parser.add_argument('-p', '--product', action='store_true', help=
        'print the production information')
    parser.add_argument('-j', '--jtag', action='store_true', help=
        'print the JTAG pin status')
    return self.add_common_arguments(parser, False)