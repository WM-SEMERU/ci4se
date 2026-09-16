def parse_args_and_run():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help=
        'Docker-tag-naming sub-commands', dest='subparser_name')
    parser_forge = subparsers.add_parser('forge', help=
        'Create a new version tag')
    parser_forge.add_argument('--version', type=int, default=1, help=
        'Version number')
    parser_forge.add_argument('--commit-id', required=True, help=
        'Git commit id')
    parser_forge.add_argument('--branch', required=True, help=
        'The branch name (ie. master)')
    parser_latest = subparsers.add_parser('latest', help=
        'Query the latest tag in the registry')
    parser_latest.add_argument('image', help=
        'The image to query (ie. username/image)')
    parser_latest.add_argument('branch', help='The branch name (ie. master)')
    parser_bump = subparsers.add_parser('bump', help=
        'Query the latest tag in the registry and return a +1')
    parser_bump.add_argument('image', help=
        'The image to bump (ie. username/image)')
    parser_bump.add_argument('branch', help='The branch name (ie. master)')
    parser_bump.add_argument('--commit-id', required=True, help=
        'Git commit id for the newly created tag')
    parser_latest = subparsers.add_parser('refresh', help=
        'Loop until the latest tag in the registry changes')
    parser_latest.add_argument('image', help=
        'The image to query (ie. username/image)')
    parser_latest.add_argument('branch', help='The branch name (ie. master)')
    args = parser.parse_args()
    {'bump': run_bump, 'latest': run_latest, 'forge': run_forge, 'refresh':
        run_refresh}.get(args.subparser_name)(args)