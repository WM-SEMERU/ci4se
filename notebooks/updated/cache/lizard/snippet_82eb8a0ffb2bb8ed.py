def set_log_level(cls, log_level):
    log = logging.getLogger(cls.cls_logger + '.set_log_level')
    log.info('Attempting to set the log level...')
    if log_level is None:
        log.info('Arg loglevel was None, log level will not be updated.')
        return False
    if not isinstance(log_level, basestring):
        log.error('Passed arg loglevel must be a string')
        return False
    log_level = log_level.upper()
    log.info('Attempting to set log level to: %s...', log_level)
    if log_level == 'DEBUG':
        cls._logger.setLevel(logging.DEBUG)
    elif log_level == 'INFO':
        cls._logger.setLevel(logging.INFO)
    elif log_level == 'WARN':
        cls._logger.setLevel(logging.WARN)
    elif log_level == 'WARNING':
        cls._logger.setLevel(logging.WARN)
    elif log_level == 'ERROR':
        cls._logger.setLevel(logging.ERROR)
    else:
        log.error('Could not set log level, this is not a valid log level: %s',
            log_level)
        return False
    log.info('pycons3rt loglevel set to: %s', log_level)
    return True