def log_to_console(status=True, level=None):
    if status:
        if level is not None:
            logger.setLevel(level)
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(levelname)s-%(name)s: %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        logger.info('GSSHApy {0}'.format(version()))
    else:
        for h in logger.handlers:
            if type(h).__name__ == 'StreamHandler':
                logger.removeHandler(h)