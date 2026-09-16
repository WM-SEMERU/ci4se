def __add_options(parser):
    parser.add_option('--upx-dir', default=None, help=
        'Directory containing UPX.')
    parser.add_option('-C', '--configfile', default=DEFAULT_CONFIGFILE,
        dest='configfilename', help=
        'Name of generated configfile (default: %default)')