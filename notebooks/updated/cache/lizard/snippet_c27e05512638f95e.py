def setup_logger(logger, stream, filename=None, fmt=None):
    if len(logger.handlers) < 1:
        console = logging.StreamHandler(stream)
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter(fmt))
        logger.addHandler(console)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        if filename:
            outfile = logging.FileHandler(filename)
            outfile.setLevel(logging.INFO)
            outfile.setFormatter(logging.Formatter('%(asctime)s ' + (fmt if
                fmt else '%(message)s')))
            logger.addHandler(outfile)