def create_logger(level=logging.NOTSET):
    _test = os.path.join(os.path.join(os.getcwd(), 'pretty_bad_protocol'),
        'test')
    _now = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    _fn = os.path.join(_test, '%s_test_gnupg.log' % _now)
    _fmt = (
        '%(relativeCreated)-4d L%(lineno)-4d:%(funcName)-18.18s %(levelname)-7.7s %(message)s'
        )
    logging.addLevelName(GNUPG_STATUS_LEVEL, 'GNUPG')
    logging.Logger.status = status
    if level > logging.NOTSET:
        logging.basicConfig(level=level, filename=_fn, filemode='a', format
            =_fmt)
        logging.logThreads = True
        if hasattr(logging, 'captureWarnings'):
            logging.captureWarnings(True)
        colouriser = _ansistrm.ColorizingStreamHandler
        colouriser.level_map[9] = None, 'blue', False
        colouriser.level_map[10] = None, 'cyan', False
        handler = colouriser(sys.stderr)
        handler.setLevel(level)
        formatr = logging.Formatter(_fmt)
        handler.setFormatter(formatr)
    else:
        handler = NullHandler()
    log = logging.getLogger('gnupg')
    log.addHandler(handler)
    log.setLevel(level)
    log.info('Log opened: %s UTC' % datetime.ctime(datetime.utcnow()))
    return log