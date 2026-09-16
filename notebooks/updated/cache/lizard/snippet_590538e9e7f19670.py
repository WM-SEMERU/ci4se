def _parse_args(argv):
    parser = make_parser()
    args = parser.parse_args(argv)
    LOGGER.setLevel(to_log_level(args.loglevel))
    if args.inputs:
        if '-' in args.inputs:
            args.inputs = sys.stdin
    elif args.list:
        _show_psrs()
    elif args.env:
        cnf = os.environ.copy()
        _output_result(cnf, args.output, args.otype or 'json', None, None)
        sys.exit(0)
    else:
        parser.print_usage()
        sys.exit(1)
    if args.validate and args.schema is None:
        _exit_with_output('--validate option requires --scheme option', 1)
    return args