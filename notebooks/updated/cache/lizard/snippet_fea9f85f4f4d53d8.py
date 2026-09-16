def set_log_level(level):
    lLevel = level.lower()
    unrecognized = False
    if lLevel == 'debug-all':
        loglevel = logging.DEBUG
    elif lLevel == 'debug':
        loglevel = logging.DEBUG
    elif lLevel == 'info':
        loglevel = logging.INFO
    elif lLevel == 'warning':
        loglevel = logging.WARNING
    elif lLevel == 'error':
        loglevel = logging.ERROR
    elif lLevel == 'critical':
        loglevel = logging.CRITICAL
    else:
        loglevel = logging.DEBUG
        unrecognized = True
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s:%(lineno)d/%(funcName)s: %(message)s'
        )
    console = logging.StreamHandler()
    console.setLevel(loglevel)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.getLogger('').setLevel(loglevel)
    if lLevel != 'debug-all':
        packagesWarning = ['requests.packages.urllib3', 'urllib3',
            'requests_kerberos', 'jenkinsapi']
        for package in packagesWarning:
            logging.debug('Setting loglevel for %s to WARNING.', package)
            logger = logging.getLogger(package)
            logger.setLevel(logging.WARNING)
    if unrecognized:
        logging.warning('Unrecognized log level: %s  Log level set to debug',
            level)
    fh = logging.FileHandler('builder.log')
    fh.setLevel(loglevel)
    fh.setFormatter(formatter)
    logging.getLogger('').addHandler(fh)