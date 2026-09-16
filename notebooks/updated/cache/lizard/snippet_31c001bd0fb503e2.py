def apply(cls, args, run):
    try:
        lvl = int(args)
    except ValueError:
        lvl = args
    run.root_logger.setLevel(lvl)