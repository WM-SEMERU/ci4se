def init_logging(stream=sys.stderr, filepath=None, format=
    '%(asctime).19s [%(levelname)s] %(name)s: %(message)s'):
    if not (len(logger.handlers) == 1 and isinstance(logger.handlers[0],
        logging.NullHandler)):
        logger.warn(
            'logging has already been initialized, refusing to do it again')
        return
    formatter = logging.Formatter(format)
    if stream is not None:
        handler = logging.StreamHandler(stream=stream)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    if filepath is not None:
        handler = logging.FileHandler(filename=filepath)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.info('successfully initialized logger')