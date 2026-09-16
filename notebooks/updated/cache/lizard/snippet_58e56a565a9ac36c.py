def thaw_args(subparsers):
    thaw_parser = subparsers.add_parser('thaw')
    thaw_parser.add_argument('--gpg-password-path', dest='gpg_pass_path',
        help='Vault path of GPG passphrase location')
    thaw_parser.add_argument('--ignore-missing', dest='ignore_missing',
        help=
        'Warn when secrets are missing from icefilesinstead of exiting',
        action='store_true', default=False)
    secretfile_args(thaw_parser)
    archive_args(thaw_parser)
    vars_args(thaw_parser)
    base_args(thaw_parser)