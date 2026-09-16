def add_env(parser):
    parser.add_argument('-e', '--env', choices=ENVS, default=os.getenv(
        'ENV', default='dev'), help='Deploy environment, overrides $ENV')