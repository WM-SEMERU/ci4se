def password_args(subparsers):
    password_parser = subparsers.add_parser('set_password')
    password_parser.add_argument('vault_path', help=
        'Path which contains passwordsecret to be udpated')
    base_args(password_parser)