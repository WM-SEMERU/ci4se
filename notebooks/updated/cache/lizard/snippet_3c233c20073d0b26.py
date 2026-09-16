def configure_logging(info=False, debug=False):
    if info:
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urrlib3').setLevel(logging.WARNING)
        logging.getLogger('elasticsearch').setLevel(logging.WARNING)
    elif debug:
        logging.basicConfig(level=logging.DEBUG, format=DEBUG_LOG_FORMAT)
    else:
        logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT)
        logging.getLogger('requests').setLevel(logging.WARNING)
        logging.getLogger('urrlib3').setLevel(logging.WARNING)
        logging.getLogger('elasticsearch').setLevel(logging.WARNING)