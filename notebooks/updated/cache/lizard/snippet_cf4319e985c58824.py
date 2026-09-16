def init_logging(verbose=False, format='%(asctime)s %(message)s'):

    def sig_handler(signum, frame):
        logger = logging.getLogger()
        log_level = logger.level
        if log_level == logging.DEBUG:
            log_level = logging.WARN
        else:
            log_level = logging.DEBUG
        logging.warn('Got signal %d, setting log level to %d', signum,
            log_level)
        logger.setLevel(log_level)
    signal.signal(signal.SIGUSR1, sig_handler)
    if verbose:
        initial_level = logging.DEBUG
    else:
        initial_level = logging.WARN
    logging.getLogger().setLevel(initial_level)
    logging.basicConfig(format=format, level=initial_level)