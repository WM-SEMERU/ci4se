def start_msstitch(exec_drivers, sysargs):
    parser = populate_parser(exec_drivers)
    args = parser.parse_args(sysargs[1:])
    args.func(**vars(args))