def init_logger(log_requests=False):
    logger = logging.getLogger(__name__.split('.')[0])
    for handler in logger.handlers:
        logger.removeHandler(handler)
    formatter = coloredlogs.ColoredFormatter(fmt='%(asctime)s: %(message)s')
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    if log_requests:
        requests.packages.urllib3.add_stderr_logger()