def make(parser):
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--install', metavar='PKG(s)', help=
        'Comma-separated package(s) to install')
    action.add_argument('--remove', metavar='PKG(s)', help=
        'Comma-separated package(s) to remove')
    parser.add_argument('hosts', nargs='+')
    parser.set_defaults(func=pkg)