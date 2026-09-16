def build(self):
    self._cmd_parser.add_argument('install', type=str, default=None, nargs=
        '+', help='')
    self._cmd_parser.add_argument('-l', '--location', default=None, help=
        'Specify the installation location. ')
    return super(Cmd, self).build()