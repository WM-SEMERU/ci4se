def logging_on(level=logging.WARNING):
    global _is_logging_on
    if not _is_logging_on:
        console = logging.StreamHandler()
        console.setFormatter(logging.Formatter(
            '[%(levelname)s: %(asctime)s : %(name)s] %(message)s',
            '%Y-%m-%d %H:%M:%S'))
        console.setLevel(level)
        logging.getLogger('').addHandler(console)
        _is_logging_on = True
    log = logging.getLogger('')
    log.setLevel(level)
    for h in log.handlers:
        h.setLevel(level)