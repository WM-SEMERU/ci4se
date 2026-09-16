def init_logging(to_file=False, logfile=None, default_logfile=
    '/tmp/resync.log', human=True, verbose=False, eval_mode=False,
    default_logger='client', extra_loggers=None):
    fmt = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    formatter = UTCFormatter(fmt)
    if human:
        hh = logging.StreamHandler()
        hh.setLevel(logging.INFO if verbose else logging.WARNING)
        hh.setFormatter(logging.Formatter(fmt='%(message)s'))
    if to_file:
        if logfile is None:
            logfile = default_logfile
        fh = logging.FileHandler(filename=logfile, mode='a')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG if eval_mode else logging.INFO)
    loggers = [default_logger, 'resync']
    if extra_loggers is not None:
        for logger in extra_loggers:
            loggers.append(logger)
    for logger in loggers:
        log = logging.getLogger(logger)
        log.setLevel(logging.DEBUG)
        if human:
            log.addHandler(hh)
        if to_file:
            log.addHandler(fh)
    log = logging.getLogger(default_logger)
    if to_file:
        log.info('Writing detailed log to %s' % logfile)