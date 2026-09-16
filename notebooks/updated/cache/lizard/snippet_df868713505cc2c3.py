def setup_logging(verbose=False, logger=None):
    if not verbose:
        logging.getLogger('requests').setLevel(logging.WARNING)
    format_ = ('%(asctime)s %(levelname)-8s %(name)-40s %(message)s' if
        verbose else '%(message)s')
    level = logging.DEBUG if verbose else logging.INFO
    handler_stdout = logging.StreamHandler(sys.stdout)
    handler_stdout.setFormatter(logging.Formatter(format_))
    handler_stdout.setLevel(logging.DEBUG)
    handler_stdout.addFilter(InfoFilter())
    handler_stderr = logging.StreamHandler(sys.stderr)
    handler_stderr.setFormatter(logging.Formatter(format_))
    handler_stderr.setLevel(logging.WARNING)
    root_logger = logging.getLogger(logger)
    root_logger.setLevel(level)
    root_logger.addHandler(handler_stdout)
    root_logger.addHandler(handler_stderr)