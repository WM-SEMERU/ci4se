def LOGGER(filename):
    pwd = os.getcwd()
    name = filename.replace(pwd, '$PWD')
    try:
        first, name = name.split('site-packages')
        name += '... site'
    except:
        pass
    loglevel = logging.CRITICAL
    try:
        level = grep('loglevel:', config_file('/cloudmesh_debug.yaml')).strip(
            ).split(':')[1].strip().lower()
        if level.upper() == 'DEBUG':
            loglevel = logging.DEBUG
        elif level.upper() == 'INFO':
            loglevel = logging.INFO
        elif level.upper() == 'WARNING':
            loglevel = logging.WARNING
        elif level.upper() == 'ERROR':
            loglevel = logging.ERROR
        else:
            level = logging.CRITICAL
    except:
        loglevel = logging.DEBUG
    log = logging.getLogger(name)
    log.setLevel(loglevel)
    formatter = logging.Formatter(
        'CM {0:>50}:%(lineno)s: %(levelname)6s - %(message)s'.format(name))
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log