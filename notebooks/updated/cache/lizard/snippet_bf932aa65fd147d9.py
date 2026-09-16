def add_loghandler(handler):
    format = '%(levelname)s %(name)s %(asctime)s %(threadName)s %(message)s'
    handler.setFormatter(logging.Formatter(format))
    logging.getLogger(LOG_ROOT).addHandler(handler)
    logging.getLogger().addHandler(handler)