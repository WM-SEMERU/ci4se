def add_infra(subparsers):
    infra_parser = subparsers.add_parser('infra', help=runner.
        prepare_infrastructure.__doc__)
    infra_parser.set_defaults(func=runner.prepare_infrastructure)