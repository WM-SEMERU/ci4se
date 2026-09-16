def get_behave_args(self, argv=sys.argv):
    parser = BehaveArgsHelper().create_parser('manage.py', 'behave')
    args, unknown = parser.parse_known_args(argv[2:])
    behave_args = []
    for option in unknown:
        if option.startswith('--behave-'):
            option = option.replace('--behave-', '', 1)
            prefix = '-' if len(option) == 1 else '--'
            option = prefix + option
        behave_args.append(option)
    return behave_args