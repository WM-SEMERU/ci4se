def initialise_loggers(names, log_level=_builtin_logging.WARNING,
    handler_class=SplitStreamHandler):
    frmttr = get_formatter()
    for name in names:
        logr = _builtin_logging.getLogger(name)
        handler = handler_class()
        handler.setFormatter(frmttr)
        logr.addHandler(handler)
        logr.setLevel(log_level)