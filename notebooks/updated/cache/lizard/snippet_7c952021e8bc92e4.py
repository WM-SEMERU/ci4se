def aws_env_args(subparsers):
    env_parser = subparsers.add_parser('aws_environment')
    env_parser.add_argument('vault_path', help='Full path(s) to the AWS secret'
        )
    export_arg(env_parser)
    base_args(env_parser)