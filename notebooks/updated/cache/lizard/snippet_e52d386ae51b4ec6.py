def AddArguments(cls, argument_group):
    argument_group.add_argument('--user', dest='username', type=str, action
        ='store', default=cls._DEFAULT_USERNAME, metavar='USERNAME',
        required=False, help='The username used to connect to the database.')
    argument_group.add_argument('--password', dest='password', type=str,
        action='store', default=cls._DEFAULT_PASSWORD, metavar='PASSWORD',
        help='The password for the database user.')
    argument_group.add_argument('--db_name', '--db-name', dest='db_name',
        action='store', type=str, default=cls._DEFAULT_NAME, required=False,
        help='The name of the database to connect to.')
    server_config.ServerArgumentsHelper.AddArguments(argument_group)