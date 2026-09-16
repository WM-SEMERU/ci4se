def parse_global_args(argv):
    parser = create_parser()
    args = parser.parse_args(argv)
    should_log = args.include or args.exclude or args.verbose > 0
    verbosity = args.verbose
    root = logging.getLogger()
    if should_log:
        formatter = logging.Formatter(
            '%(asctime)s.%(msecs)03d %(levelname).3s %(name)s %(message)s',
            '%y-%m-%d %H:%M:%S')
        if args.logfile:
            handler = logging.FileHandler(args.logfile)
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        if args.include and args.exclude:
            print(
                'You cannot combine whitelisted (-i) and blacklisted (-e) loggers, you must use one or the other.'
                )
            sys.exit(1)
        loglevels = [logging.ERROR, logging.WARNING, logging.INFO, logging.
            DEBUG]
        if verbosity >= len(loglevels):
            verbosity = len(loglevels) - 1
        level = loglevels[verbosity]
        if args.include:
            for name in args.include:
                logger = logging.getLogger(name)
                logger.setLevel(level)
                logger.addHandler(handler)
            root.addHandler(logging.NullHandler())
        else:
            for name in args.exclude:
                logger = logging.getLogger(name)
                logger.disabled = True
            root.setLevel(level)
            root.addHandler(handler)
    else:
        root.addHandler(logging.NullHandler())
    return args