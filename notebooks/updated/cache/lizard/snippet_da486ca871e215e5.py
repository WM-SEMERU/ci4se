def provider_parser(subparser):
    identity_group = subparser.add_mutually_exclusive_group()
    identity_group.add_argument('--auth-id', help=
        'specify user id for authentication')
    identity_group.add_argument('--auth-subid', help=
        'specify subuser id for authentication')
    identity_group.add_argument('--auth-subuser', help=
        'specify subuser name for authentication')
    subparser.add_argument('--auth-password', help=
        'specify password for authentication')
    subparser.add_argument('--weight', help='specify the SRV record weight')
    subparser.add_argument('--port', help='specify the SRV record port')