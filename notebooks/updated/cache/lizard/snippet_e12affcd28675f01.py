def _init_logging(verbose):
    hdlr = logging.StreamHandler()
    hdlr.setFormatter(logging.Formatter(
        '%(asctime)s [%(levelname)s] [%(module)s] %(message)s'))
    LOG.addHandler(hdlr)
    if verbose:
        LOG.setLevel(logging.DEBUG)
        LOG.debug('Verbose output enabled.')
    else:
        LOG.setLevel(logging.INFO)