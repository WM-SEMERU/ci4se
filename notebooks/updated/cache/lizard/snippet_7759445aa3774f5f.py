def log_to_file(status=True, filename=default_log_file, level=None):
    if status:
        if level is not None:
            logger.setLevel(level)
        try:
            os.mkdir(os.path.dirname(filename))
        except OSError:
            pass
        file_handler = logging.FileHandler(filename)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s-%(name)s: %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info('GSSHApy {0}'.format(version()))
    else:
        for h in logger.handlers:
            if type(h).__name__ == 'FileHandler':
                logger.removeHandler(h)