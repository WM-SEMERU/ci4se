def add_general_optgroup(parser):
    g = parser.add_argument_group('General Options')
    g.add_argument('-q', '--quiet', dest='silent', action='store_true',
        default=False)
    g.add_argument('-v', '--verbose', nargs=0, action=_opt_cb_verbose)
    g.add_argument('-o', '--output', dest='output', default=None)
    g.add_argument('-j', '--json', dest='json', action='store_true',
        default=False)
    g.add_argument('--show-ignored', action='store_true', default=False)
    g.add_argument('--show-unchanged', action='store_true', default=False)
    g.add_argument('--ignore', action=_opt_cb_ignore, help=
        'comma-separated list of ignores')